#!/usr/bin/python3

import json
import argparse
from modules.data.extract import extract
from modules.query.search import search
from modules.query.operation import operation
from modules.output.terminal import terminal 
from modules.output.file import file


def parse_arguments(parser):

	parser.add_argument("-v","--version",action='version',version='%(prog)s 1.0')
	
	parser.add_argument("-s","--search",help="for searching with a input text")
	
	parser.add_argument("-op","--operation",choices=["total","average","max","min"],help="perform an \
		 				operation on choosen field")	
	
	parser.add_argument("-f","--field",choices=["Year of release", "Rating", "Watch  hour ",
                        "Box office collection","User reviews", "Awards"],
                        default = 'Rating',help="to display all above the input rating")
	
	subparser = parser.add_subparsers(help="type of output",required=True)

	parser_terminal = subparser.add_parser('print') 

	parser_email = subparser.add_parser('email')
	parser_email.add_argument('email',help="receiver email address")

	parser_file = subparser.add_parser('file')
	parser_file.add_argument('path',help="location of processed output")

	parser.add_argument("-r","--rows",type=int,default=5,help="no of rows the output should be limited")

	return parser.parse_args()
	

def process_arguments(arguments,data):

	search_res_data = []

	if arguments.search:
		s = search(data,arguments.rows)
		search_res_data = s.find(arguments.search)

	operation_res_data = None

	if arguments.field:
		op = operation(arguments.field,data)
		operation_res_data = op.query(arguments.operation)

	if search_res_data or operation_res_data :
		data_str =("Search Query Results" + '\n' +'##########' + '\n' +
				   json.dumps(search_res_data) + '\n' + '\n' +
				   'Operation Query Results' + "\n" +'##########' + '\n' +
				   arguments.operation + " " + json.dumps(operation_res_data))
		if "path" in arguments :
			f = file(arguments.path,data_str)
		else:
			t = terminal(data_str)
			t.print()


			

	



def main():

	parser = argparse.ArgumentParser(prog='mda', 
                                     description='below are the available options, \
                                     for processing movie data',
                                     prefix_chars='-')
	
	arguments = parse_arguments(parser)
	
	data = extract('./assets/data.csv').data()

	process_arguments(arguments,data)




if __name__== "__main__":
	main()

