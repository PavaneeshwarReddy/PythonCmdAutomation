

from statistics import mean


class operation:


	def __init__(self, query_field, data = []):

		self.query_field = query_field

		self.data = [self.__type_converter(value[query_field]) for value in data if 'NIL' not in 
					value[query_field]]


	def __type_converter(self, value):

		type_func_map = {
			"Year of release" : lambda value : int(value),
			"Rating" : lambda value : float(value),
			"Ratedby" : lambda value : int(value.split('K')[0]),
			"Box office collection" : lambda value : float(value.replace('$','').replace(',','')),
			"User reviews" : lambda value : int(value),
		}

		formatted_value = type_func_map[self.query_field](value) 

		return formatted_value

	def query(self,operation_type):

		query_func_map = {
			"total" : self.__total,
			"average" : self.__average,
			"max" : self.__max,
			"min" : self.__min
		}

		return query_func_map[operation_type]()


	def __max(self):

		return max(self.data)


	def __min(self):

		return min(self.data)


	def __average(self):

		return mean(self.data)


	def __total(self):

		return sum(self.data)



