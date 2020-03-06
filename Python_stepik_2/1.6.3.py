class LoggableList(list, Loggable):
	def append(self, object):
		super().append(object)
		self.log(object)

