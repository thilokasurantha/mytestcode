class MessageBox :
	def __init__(self, c_width, c_height, c_msg) :
			self.width = c_width
			self.height = c_height
			self.msg = c_msg

	def message_box_drawing(self) :

			left_align = ((self.width-2)-len(self.msg))//2
			right_align =  self.width-2 - len(self.msg) - left_align  #(((self.width-2)-len(self.msg))//2)

			print("#" * self.width)

			for self.down in range(1,self.height) :
				print("#" + " "*(width-2) + "#")

				if (self.down == self.height//2) :
						print("#" + " "*left_align + self.msg + " "*right_align + "#")

			print("#" * self.width)


if __name__ == '__main__':
    	
	repeat = 'yes'	
	while (repeat == 'yes' or  repeat=='y') :
		width = int(input("Enter the box width ? "))
		height = int(input("Enter the box height ? "))
		msg = input("Enter your message ? ")

		myObj = MessageBox(width,height,msg)
		myObj.message_box_drawing()
		repeat = input("Do you want to repeat this prgramme ? ")

	print("Bye")
