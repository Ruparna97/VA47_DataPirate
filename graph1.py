import matplotlib.pyplot as plt
import numpy as np
import pickle
import os



def graphing(id):

	pkl_file = open('patient.pkl', 'rb')
	mydict = pickle.load(pkl_file)
	pkl_file.close()
	x=[]
	y = mydict[id]["digit"]
	for i in range(len(mydict[id]["digit"])):
		x.append(i+1)

	plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='blue', markersize=12)
	plt.ylim(0,5)
	plt.xlabel('time')
	plt.ylabel('health')

	plt.title('Line graph!')

	plt.savefig("static/chart.png")
	