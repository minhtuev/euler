from heapq import heappush, heappop, heapify

def heapsort(iterable):
	h = []
	for value in iterable:
		heappush(h, value)
	return [heappop(h) for i in range(len(h))]

class PriorityQueue(object):
	def __init__(self):
		self.h = []
		self.dic = {}

	def push(self, key, value):
		heappush(self.h, (value, key))
		self.dic[key] = True

	def put(self, data):
		heappush(self.h, data)
		self.dic[data(1)] = True

	def get(self):
		return self.pop()

	def pop(self):
		(value, key) = heappop(self.h)
		del self.dic[key]
		return (value, key)

	def update(self, key, value):
		for index, data in enumerate(self.h):
			(item_value, item_key) = data
			if item_key == key:
				self.h[index] = (value, key)
		heapify(self.h)

	def update_min(self, key, value):
		for index, data in enumerate(self.h):
			(item_value, item_key) = data
			if item_key == key:
				self.h[index] = (min(value, item_value), key)
		heapify(self.h)


	def push_or_update(self, key, value):
		if key in self.dic:
			self.update(key, value)
		else:
			self.push(key, value)

	def push_or_update_min(self, key, value):
		if key in self.dic:
			self.update_min(key, value)
		else:
			self.push(key, value)