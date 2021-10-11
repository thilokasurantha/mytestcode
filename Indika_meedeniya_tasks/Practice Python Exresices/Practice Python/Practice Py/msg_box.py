class MessageBox :
	def __init__(self, name, width, height) :
		self.name = name
		self.width = width
		self.height = height

	def create_box(self) :
		print("#"*self.width)

		for x in self.width :
			print("#"*x, " "*(self.width-2), "#"*x)

		print("#"*self.width)
if __name__ == '__main__':
	myObj = MessageBox("Thlioka",12,12)
	myObj.create_box()