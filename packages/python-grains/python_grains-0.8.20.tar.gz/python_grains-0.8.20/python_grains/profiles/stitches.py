import json
import datetime
import pytz
import time
import random
from python_grains.locks import Lock

DEFAULT_DOMAIN = None
DEFAULT_REDIS_CLIENT = None
DEFAULT_DJANGO_STITCH_POOL_MODEL = None
DEFAULT_DJANGO_STITCH_MODEL = None
DEFAULT_DJANGO_CONNECTION_TUPLE = (None, None)
DEFAULT_USER_TTL = 6 * 24 * 60 * 60
DEFAULT_USER_DATA_TTL_MARGIN = 2
DEFAULT_MAX_STITCH_KEYS = 50

class StitchPool(object):

    recently_checked_db_postfix = ':rc'
    domain = DEFAULT_DOMAIN
    redis_client = DEFAULT_REDIS_CLIENT
    django_stitch_pool_model = DEFAULT_DJANGO_STITCH_POOL_MODEL
    user_ttl = DEFAULT_USER_TTL
    user_data_ttl_margin = DEFAULT_USER_DATA_TTL_MARGIN
    django_connection_tuple = DEFAULT_DJANGO_CONNECTION_TUPLE

    def __init__(self,
                 user_id,
                 stitch_keys=None,
                 timestamps=None,
                 recently_checked_db=None):

        self.user_id = user_id
        self.stitch_keys = set()
        self.stitch_keys_with_ts = {}
        self._recently_checked_db = recently_checked_db

        if stitch_keys:
            self.add_stitch_keys(stitch_keys, timestamps=timestamps)

        if self.domain is None:
            raise ValueError('domain should not be None')

        if self.redis_client is None:
            raise ValueError('redis_client should not be None')

    def add_stitch_keys(self,
                        stitch_keys,
                        timestamps=None):

        assert isinstance(stitch_keys, (list, set)), 'stitch_keys needs to be a list or set'

        if timestamps:
            assert isinstance(timestamps, list), 'timestamps should be a list'
            assert len(timestamps) == len(stitch_keys), 'length of timestamps should be equal to length of stitch_keys'
            assert all(isinstance(ts, (float, int)) for ts in timestamps), 'all timestamps should be floats or integers'
        else:
            now = pytz.utc.localize(datetime.datetime.utcnow()).timestamp()
            timestamps = [now for _ in stitch_keys]

        self.stitch_keys_with_ts.update({stitch_key: max(ts, self.stitch_keys_with_ts.get(stitch_key, 0)) for stitch_key, ts in
                                      dict(zip(stitch_keys, timestamps)).items()})
        self.stitch_keys = self.stitch_keys.union(set(stitch_keys))

    def offload(self):
        self.get(force_db=True)
        self.to_db()
        self.redis_client.remove_stitch_keys_from_pool(
            keys=[
                self.key,
                self.all_stitchpools_key,
                self.recently_checked_db_key
            ],
            args=self.stitch_keys
        )


    def to_cache(self):

        pipe = self.redis_client.pipeline()
        pipe.zadd(self.key, self.stitch_keys_with_ts)
        pipe.expire(self.key, self.user_ttl + self.user_data_ttl_margin)
        pipe.execute()

    def get(self, force_db=False):

        result = self.redis_client.zrangebyscore(self.key, min='-inf', max='+inf', withscores=True)
        stitch_keys = [s[0].decode() for s in result]
        timestamps = [s[1] for s in result]
        self.add_stitch_keys(stitch_keys, timestamps=timestamps)
        if not self.recently_checked_db or force_db:
            self.complement_from_db()

    def complement_from_db(self):

        model = self.usable_django_model()
        try:
            stitch_pool_model = model.objects.get(user_id=self.user_id)
            stitches_keys = [str(s) for s in stitch_pool_model.stitch_keys]
            timestamps = [float(ts) for ts in stitch_pool_model.timestamps]
            self.add_stitch_keys(stitches_keys, timestamps=timestamps)
            if len(stitches_keys) > 0:
                self.to_cache()
            self.set_recent_db_check()
        except model.DoesNotExist:
            self.set_recent_db_check()
            return []

    @classmethod
    def get_expired(cls,
                    num=300,
                    start=0,
                    dev=False):

        now = pytz.utc.localize(datetime.datetime.utcnow()).timestamp()
        expired_stitchpools = cls.redis_client.zrangebyscore(cls._all_stitchpools_key(),
                                                             min='-inf',
                                                             max='+inf' if dev else (now - cls.user_ttl + 2 * cls.user_data_ttl_margin),
                                                             start=start,
                                                             num=num,
                                                             withscores=True)

        return [cls.from_key(stitchpool_key.decode()) for stitchpool_key, timestamp in expired_stitchpools]

    def lock(self, ttl):
        return Lock('sp' + str(self.user_id), self.redis_client, ttl=ttl * 1000)

    def delete_from_cache(self):
        self.redis_client.delete(self.key)
        self.redis_client.zrem(self.all_stitchpools_key, self.key)


    def to_db(self):

        # first call complement_from_db!

        if len(self.stitch_keys_with_ts) == 0:
            raise Exception('Cannot store empty stitch_keys')
        max_tries = 3
        _tmp = list(self.stitch_keys_with_ts.items())
        stitch_keys = [s[0] for s in _tmp]
        timestamps = [s[1] for s in _tmp]

        for i in range(max_tries):
            try:
                self.usable_django_model().objects.update_or_create(
                    user_id=self.user_id,
                    defaults={'stitch_keys': stitch_keys, 'timestamps': timestamps})
                return
            except Exception as e:
                if 'OperationalError' in e.__class__.__name__:
                    error = e
                    time.sleep(1 + random.random() / 10)
        raise error

    def remove_stitch_keys(self,
                           stitch_keys,
                           remove_from_stitches=False):

        assert isinstance(stitch_keys, (list, set)), 'stitch_keys needs to be a list or set'
        pipe = self.redis_client.pipeline()
        pipe.zrem(self.key, *stitch_keys)
        if remove_from_stitches:
            for stitch_key in stitch_keys:
                pipe.zrem(stitch_key, self.user_id)
        pipe.execute()
        self.stitch_keys = self.stitch_keys - set(stitch_keys)
        self.stitch_keys_with_ts = {k: v for k, v in self.stitch_keys_with_ts if not k in stitch_keys}

    @classmethod
    def usable_django_model(cls):
        if cls.django_stitch_pool_model:
            if all(cls.django_connection_tuple):
                if cls.django_connection_tuple[0].connection and not cls.django_connection_tuple[0].is_usable():
                    del cls.django_connection_tuple[1]._connections.default
                return cls.django_stitch_pool_model
            else:
                return cls.django_stitch_pool_model

    @property
    def recently_checked_db(self):
        if self._recently_checked_db is None:
            self._recently_checked_db = bool(self.redis_client.get(self.recently_checked_db_key))
        return self._recently_checked_db

    @property
    def key(self):
        return self._key(user_id=self.user_id)

    @classmethod
    def _key(cls,
             user_id):
        # this is also defined on the profile class in python-grains!
        return f'st:u:p:{cls.domain}:{user_id}'

    @classmethod
    def parse_key(cls, key):
        split_str = key.split(':')
        user_id = split_str[-1]
        domain = ':'.join(split_str[3:-1])
        return domain, user_id

    @classmethod
    def from_key(cls, key):
        domain, user_id = cls.parse_key(key)
        return cls(user_id=user_id)

    @property
    def recently_checked_db_key(self):
        return self._recently_checked_db_key(user_id=self.user_id)

    @classmethod
    def _recently_checked_db_key(cls,
                                 user_id):
        return cls._key(user_id=user_id) + cls.recently_checked_db_postfix

    def set_recent_db_check(self):
        self.redis_client.set(self.recently_checked_db_key, "1", ex=self.user_ttl)

    @property
    def all_stitchpools_key(self):
        return self._all_stitchpools_key()

    @classmethod
    def _all_stitchpools_key(cls):
        return f'st:u:p:all:{cls.domain}'

class Stitch(object):

    default_type = 'default'
    recently_checked_db_postfix = ':rc'
    domain = DEFAULT_DOMAIN
    redis_client = DEFAULT_REDIS_CLIENT
    user_ttl = DEFAULT_USER_TTL
    user_data_ttl_margin = DEFAULT_USER_DATA_TTL_MARGIN
    django_stitch_model = DEFAULT_DJANGO_STITCH_MODEL
    django_connection_tuple = DEFAULT_DJANGO_CONNECTION_TUPLE
    max_stitch_keys = DEFAULT_MAX_STITCH_KEYS

    def __init__(self,
                 value,
                 type,
                 user_ids=None,
                 timestamps=None,
                 recently_checked_db=None):

        self.type = (type or self.default_type).lower()
        self.value = value
        self.user_ids_with_ts = {}
        self.user_ids = set()
        self._recently_checked_db = recently_checked_db

        if user_ids:
            self.add_user_ids(user_ids, timestamps=timestamps)

        if self.domain is None:
            raise ValueError('domain should not be None')

        if self.redis_client is None:
            raise ValueError('redis_client should not be None')

    def add_user_ids(self,
                     user_ids,
                     timestamps=None):

        assert isinstance(user_ids, (list, set)), 'user_ids needs to be a list or set'
        if timestamps:
            assert isinstance(timestamps, list), 'timestamps should be a list'
            assert len(timestamps) == len(user_ids), 'length of timestamps should be equal to length of user_ids'
            assert all(isinstance(ts, (float, int)) for ts in timestamps), 'all timestamps should be floats or integers'
        else:
            now = pytz.utc.localize(datetime.datetime.utcnow()).timestamp()
            timestamps = [now for _ in user_ids]

        self.user_ids_with_ts.update({user_id: max(ts, self.user_ids_with_ts.get(user_id, 0)) for user_id, ts in dict(zip(user_ids, timestamps)).items()})
        self.user_ids = self.user_ids.union(set(user_ids))

    def delete_from_cache(self):
        self.redis_client.delete(self.key)
        self.redis_client.zrem(self.all_stitches_key, self.key)

    def offload(self):
        self.get(force_db=True)
        self.to_db()
        self.redis_client.remove_user_ids_from_stitch(
            keys=[
                self.key,
                self.all_stitches_key,
                self.recently_checked_db_key
            ],
            args=self.user_ids
        )

    def lock(self, ttl):
        return Lock('st' + str(self.value), self.redis_client, ttl=ttl * 1000)

    def to_cache(self):
        pipe = self.redis_client.pipeline()
        pipe.zadd(self.key, self.user_ids_with_ts)
        pipe.expire(self.key, self.user_ttl + self.user_data_ttl_margin)
        pipe.execute()

    def get(self, force_db=False):
        result = self.redis_client.zrangebyscore(self.key, min='-inf', max='+inf', withscores=True)
        user_ids = [u[0].decode() for u in result]
        timestamps = [u[1] for u in result]
        self.add_user_ids(user_ids, timestamps=timestamps)
        if not self.recently_checked_db or force_db:
            self.complement_from_db()

    @classmethod
    def get_expired(cls,
                    num=300,
                    start=0,
                    dev=False):

        now = pytz.utc.localize(datetime.datetime.utcnow()).timestamp()
        expired_stitches = cls.redis_client.zrangebyscore(cls._all_stitches_key(),
                                                          min='-inf',
                                                          max='+inf' if dev else (now - cls.user_ttl + 2 * cls.user_data_ttl_margin),
                                                          start=start,
                                                          num=num,
                                                          withscores=True)

        return [cls.from_key(stitch_key.decode()) for stitch_key, timestamp in expired_stitches]

    def remove_user_ids(self,
                        user_ids,
                        remove_from_pools=False):

        assert isinstance(user_ids, (list, set)), 'user_ids needs to be a list or set'
        pipe = self.redis_client.pipeline()
        pipe.zrem(self.key, *user_ids)
        if remove_from_pools:
            for user_id in user_ids:
                pipe.zrem(self.stitch_pool_key(user_id=user_id), self.key)
        pipe.execute()
        self.user_ids = self.user_ids - set(user_ids)
        self.user_ids_with_ts = {k: v for k, v in self.user_ids_with_ts.items() if not k in user_ids}

    def set_recent_db_check(self):

        self.redis_client.set(self.recently_checked_db_key, "1", ex=self.user_ttl)

    @property
    def recently_checked_db(self):

        if self._recently_checked_db is None:
            self._recently_checked_db = bool(self.redis_client.get(self.recently_checked_db_key))
        return self._recently_checked_db

    @classmethod
    def get_multiple(cls,
                     keys):

        data = cls.redis_client.get_multiple_stitches(
            keys=[],
            args=[
                json.dumps(list(set(keys))),
                cls.recently_checked_db_postfix
            ]
        )
        data_dict = {k.decode(): cls.from_redis_data(key=k, data=dict(zip(v[::2], v[1::2])))
                     for k, v in dict(zip(data[::2], data[1::2])).items()}
        should_check_db = {k: v for k, v in data_dict.items() if not v.recently_checked_db}
        checked_in_db = cls.complement_multiple_from_db(should_check_db)
        data_dict.update(checked_in_db)

        return list(data_dict.values())


    @classmethod
    def complement_multiple_from_db(cls, should_check_dict):

        model = cls.usable_django_model()
        stitch_models = list(model.objects.filter(key__in=list(should_check_dict.keys())))
        for stitch_model in stitch_models:
            should_check_dict[stitch_model.key].add_user_ids(
                [str(u) for u in stitch_model.user_ids],
                [float(t) for t in stitch_model.timestamps]
            )
            should_check_dict[stitch_model.key].to_cache()
            should_check_dict[stitch_model.key].set_recent_db_check()

        return should_check_dict

    def complement_from_db(self):
        model = self.usable_django_model()
        try:
            stitch_model = model.objects.get(key=self.key)
            user_ids = [str(u) for u in stitch_model.user_ids]
            timestamps = [float(ts) for ts in stitch_model.timestamps]
            self.add_user_ids(user_ids, timestamps=timestamps)
            if len(user_ids) > 0:
                self.to_cache()
            self.set_recent_db_check()
        except model.DoesNotExist:
            self.set_recent_db_check()
            return []

    def as_dict(self):
        return {
            'value': self.value,
            'type': self.type
        }

    def to_db(self):

        # first call complement_from_db!

        if len(self.user_ids_with_ts) == 0:
            raise Exception('Cannot store empty user_ids')
        max_tries = 3
        _tmp = list(self.user_ids_with_ts.items())
        user_ids = [u[0] for u in _tmp]
        timestamps = [u[1] for u in _tmp]

        for i in range(max_tries):
            try:
                self.usable_django_model().objects.update_or_create(
                    key=self.key,
                    defaults={'user_ids': user_ids, 'timestamps': timestamps})
                return
            except Exception as e:
                if 'OperationalError' in e.__class__.__name__:
                    error = e
                    time.sleep(1 + random.random() / 10)
        raise error


    @classmethod
    def from_redis_data(cls,
                        key,
                        data):

        type, value, domain = cls.parse_key(key)
        user_data_with_ts = (data[b'user_ids'] or [])
        user_ids_with_timestamps = [(k.decode(), float(v)) for k,v in dict(zip(user_data_with_ts[::2], user_data_with_ts[1::2])).items()]
        # user_ids_with_timestamps = [u.decode() for u in (data[b'user_ids'] or [])]
        checked_db = bool(data[b'recent_check'])
        user_ids = [o[0] for o in user_ids_with_timestamps]
        timestamps = [o[1] for o in user_ids_with_timestamps]
        return cls(value=value, type=type, user_ids=user_ids, timestamps=timestamps, recently_checked_db=checked_db)

    @classmethod
    def usable_django_model(cls):
        if cls.django_stitch_model:
            if all(cls.django_connection_tuple):
                if cls.django_connection_tuple[0].connection and not cls.django_connection_tuple[0].is_usable():
                    del cls.django_connection_tuple[1]._connections.default
                return cls.django_stitch_model
            else:
                return cls.django_stitch_model

    @classmethod
    def from_key(cls, key):
        type, value, domain = cls.parse_key(key)
        return cls(value=value, type=type)

    @classmethod
    def parse_key(cls, key):

        key = key.decode() if isinstance(key, bytes) else key
        split_key = key.split(':')
        type, value, domain = split_key[2], ':'.join(split_key[3:-1]), split_key[-1]
        return type, value, domain

    @classmethod
    def stitch_pool_key(cls,
                        user_id):
        # this is also defined on the stitch pool class in python-grains!
        return f'st:u:p:{cls.domain}:{user_id}'

    @classmethod
    def all_stitchpools_key(cls):
        # this is also defined on the stitch pool class in python-grains!
        return f'st:u:p:all:{cls.domain}'

    @property
    def key(self):
        return self._key(type=self.type, value=self.value)

    @classmethod
    def _key(cls, type, value):
        return f'st:u:{type}:{value}:{cls.domain}'

    @property
    def recently_checked_db_key(self):
        return self._recently_checked_db_key(type=self.type, value=self.value)

    @classmethod
    def _recently_checked_db_key(cls, type, value):
        return cls._key(type=type, value=value) + cls.recently_checked_db_postfix

    @property
    def all_stitches_key(self):
        return self._all_stitches_key()

    @classmethod
    def _all_stitches_key(cls):
        return f'st:u:all:{cls.domain}'
