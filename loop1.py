import cloud
import map1
import os
import pdftimg



def looping(id):
	open('static/outpu1.txt', 'w').close()
	directory = r'images'
	for filename in os.listdir(directory):
		ext = os.path.splitext(filename)[-1].lower()
		if(ext!=".pdf"):
			print(filename)
			cloud.get_table_csv_results(os.path.join(directory, filename))
			#print("loop id",id)
			map1.mapping(id)
		else:
			pdftimg.convert(os.path.join(directory, filename))
			directory=r'pdf'
			for filename in os.listdir(directory):
		# ext = os.path.splitext(filename)[-1].lower()
		# if(ext!=".pdf")
				print(filename)
				cloud.get_table_csv_results(os.path.join(directory, filename))



