import collections

class ARC:
	def __init__(self, size):
		self.cache = set()
		self.c = size
		self.p = 0
		self.T1 = collections.deque()
		self.B1 = collections.deque()
		self.T2 = collections.deque()
		self.B2 = collections.deque()
		self.hits=0
		self.misses=0

	def clean(self,size):
		self.cache = set()
		self.c = size
		self.p = 0
		self.T1 = collections.deque()
		self.B1 = collections.deque()
		self.T2 = collections.deque()
		self.B2 = collections.deque()
		self.hits=0
		self.misses=0

	def replace(self, item):
		#print ("in function replace")
		if len(self.T1) >= 1 and ((item in self.B2 and len(self.T1) == self.p) or len(self.T1) > self.p):
			old = self.T1.pop()
			self.B1.appendleft(old)
		else:
			old = self.T2.pop()
			self.B2.appendleft(old)
		self.cache.remove(old)

	def re(self, item):
    # Case I
		if (item in self.T1) or (item in self.T2):
			#print ("in Case I")
			if item in self.T1:
				self.T1.remove(item)
			elif item in self.T2:
				self.T2.remove(item)
			self.T2.appendleft(item)
			self.hits+=1
		elif (item in self.B1):
			#print ("in Case II")
			self.p = min(self.c, self.p + max(len(self.B2) / len(self.B1) * 1. , 1))
			self.replace(item)
			self.B1.remove(item)
			self.T2.appendleft(item)
			self.cache.add(item)
			self.misses+=1
		elif (item in self.B2):
			#print ("in Case III")
			self.p = max(0, self.p - max(len(self.B1)/len(self.B2) * 1. , 1))
			self.replace(item)
			self.B2.remove(item)
			self.T2.appendleft(item)
			self.cache.add(item)
			self.misses+=1
		elif (item not in self.T1) or (item not in self.B1) or (item not in self.T2) or (item not in self.B2):
			if len(self.T1) + len(self.B1) == self.c:
				#print ("in Case IV(i)")
				if len(self.T1) < self.c:
					self.B1.pop()
					self.replace(item)
				else:
					old = self.T1.pop()
					self.cache.remove(old) 
			elif len(self.T1) + len(self.B1) < self.c and (len(self.T1) + len(self.B1) + len(self.T2) + len(self.B2)) >= self.c:
				#print ("in Case IV(ii)")
				if (len(self.T1) + len(self.B1) + len(self.T2) + len(self.B2)) == 2 * self.c:
					self.B2.pop()
				self.replace(item)

			self.T1.appendleft(item)
			self.cache.add(item)
			self.misses+=1
		else:
			"There is an error."
		
		# Printing the current status of all lists
		# #print ("item: ", item)
		# #print ("Cache: ", self.cache)
		# #print ("p = ", self.p)
		# #print ("T1: ", self.T1)
		# #print ("B1: ", self.B1)
		# #print ("T2: ", self.T2)
		# #print ("B2: ", self.B2)
		# #print (" ")
	def hit_ratio(self,hit, length):
		ratio = round(((hit/length)*100))
    	#print('Hit ratio: ', ratio, '%')
		return ratio

	def run(self,_cache,size):
		self.cache=set(_cache)
		self.c=size
		for item in _cache:
			self.re(item)
		#print(len(_cache),self.hits+self.misses)
		return self.hit_ratio(self.hits,self.hits+self.misses)



	
# ref1 = [1,2,1,1,2,3,1,1,3,5,6,1,2,4,2,3,5,2,2,5,2,2,5,6,1,3,4]
# cachesize=3
# arc=ARC(cachesize)
# print("cache size:",5,', Hit ratio: ',arc.run(ref1,cachesize),"%")
