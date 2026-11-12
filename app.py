import unittest
#app code
def add(a,b):
	return a+b
def subtract (a-b):
	return a-b
def multiply (a,b) : 
	return a*b
#automated test cases
calss Testcalculator (unittest Teestcase):
	def test_add(self):
		self.assestEqual(add(10,20),30)
	def test_subtract(self):
		self.assertEqual(subtract(20,10),10)
	def test_multiply(self):
		self.assertEqual(multiply(5,4),20)
#main application
if  --name-- == "__main__":
	print("Student calculator Application " ) 
	print("Addition:",add(10,20) ) 
	print("Subtraction:",subtract(20,10) ) 
	print("Multiplication: ",multiply(5,4) ) 
	print("\nExecuting Automated Tests...\n " )
	unittest.naib(argv=['first-arg-is-ignored'],exit=False) 
print("Extra line")
