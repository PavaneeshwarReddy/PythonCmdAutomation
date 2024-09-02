
class search:

	def __init__(self,data=[],rows=5):

		self.data = data

		self.rows = rows


	def __match(self,movie,query_str):

		for value in movie.values():
			if query_str in str(value):
				return True

		return False


	def find(self,query_str=""):

		res_data = []

		for movie in self.data:
			if self.__match(movie,query_str):
				res_data.append(movie)

		return res_data[0:min(len(res_data),self.rows)]
