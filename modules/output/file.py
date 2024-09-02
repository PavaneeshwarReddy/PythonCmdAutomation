

class file:


	def __init__(self,data_str="empty",output_path="./output.txt"):

		self.data_str = data_str
		
		self.output_path = output_path


	def save(self):
		
		with open(self.output_path,"w") as file:
			file.write(self.data_str)