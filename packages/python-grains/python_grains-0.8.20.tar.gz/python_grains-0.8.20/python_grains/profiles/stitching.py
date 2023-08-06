#
# DEFAULT_DOMAIN = None
# DEFAULT_STITCH_TYPE = 'default'
# DEFAULT_REDIS_CLIENT = None
#
# class Stitch(object):
#
#     default_type = DEFAULT_STITCH_TYPE
#     recently_checked_db_postfix = ':rc'
#     domain = DEFAULT_DOMAIN
#     redis_client = DEFAULT_REDIS_CLIENT
#
#     def __init__(self,
#                  value,
#                  type,
#                  user_ids=None,
#                  recently_checked_db=None):
#
#         self.type = (type or self.default_type).lower()
#         self.value = value
#         self.user_ids = set()
#         self._recently_checked_db = recently_checked_db
#
#         if user_ids:
#             self.add_user_ids(user_ids)
#
#         if self.domain is None:
#             raise ValueError('domain should not be None')
#
#     def add_user_ids(self,
#                      user_ids):
#
#         assert isinstance(user_ids, (list, set)), 'user_ids needs to be a list or set'
#         self.user_ids = self.user_ids.union(set(user_ids))
#
#     def get(self):
#         user_ids = [u.decode() for u in redis_client_sessions_users.zrangebyscore(self.key, min='-inf', max='+inf')]
#         self.add_user_ids(user_ids)
#         if not self.recently_checked_db:
#             self.complement_from_db()
