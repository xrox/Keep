class Foo():
	def __init__(self,message):
		self.message = message
	def function(self):
		print (self.message)
obj = Foo("HelloPython!")
obj.function()
print(obj.message)

print('==========================')
class Foo1:
	def function1(self, message):
		print ('%s' %message)
obj1 = Foo1()
obj1.function1("HelloPython!")
