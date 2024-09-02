

import csv


class extract:


	def __init__(self,csv_path):

		self.csv_path = csv_path


	def data(self):

		data = []
			
		with open(self.csv_path,'r') as file:
			reader = csv.DictReader(file)
			for row in reader:
				data.append(row)

		return data

