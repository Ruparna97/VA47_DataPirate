import cloud
import map2
import os



def looping(id):
	open('static/outpu1.txt', 'w').close()
	directory = r'images'
	for filename in os.listdir(directory):
		print(filename)
		cloud.get_table_csv_results(os.path.join(directory, filename))
		#print("loop id",id)
		map2.mapping(id)

