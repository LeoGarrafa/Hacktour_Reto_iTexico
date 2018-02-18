class Edge():
	def __init__(self, value = None):
		self.current = value
		
	# Return TRUE if there is any change
	def any(self, value):
		if self.current != value:
			self.current = value
			return True
		else:
			return False
	
	# Return TRUE if there is an increment in the signal		
	def rise(self, value):
		rtn = None
		
		if self.current < value:
			rtn = True
		else:
			rtn = False
			
		self.current = value		
		return rtn
