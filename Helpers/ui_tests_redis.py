from helpers.redis.redis_connection import RedisConnection

class UITestsRedis(RedisConnection):
	"""update results to Redis"""
	
	def __init__(self):
		super(UITestsRedis, self).__init__("REDIS_STATS")
		self.get_redis_connection()
		self.key = "h:uitests"
	
	def update_result(self, url, result):
		return self.redis.hset(self.key, url, result)

	def get_redis_connection(self):
		self.redis = super(UITestsRedis, self).get_redis_connection()
