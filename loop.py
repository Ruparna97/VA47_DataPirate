import cloud
import map1
import os



def looping(id):
	directory = r'images'
	for filename in os.listdir(directory):
		print(filename)
		cloud.get_table_csv_results(os.path.join(directory, filename))
		print("loop id",id)
		map1.mapping(id)

