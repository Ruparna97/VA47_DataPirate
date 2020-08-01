import matplotlib.pyplot as plt
import numpy as np
import pickle
import os



def graphing(id):

	pkl_file = open('patient.pkl', 'rb')
	mydict = pickle.load(pkl_file)
	pkl_file.close()
	x=[]
	y = mydict[id]["digit_creatinine"]
	for i in range(len(mydict[id]["digit_creatinine"])):
		x.append(i+1)

	plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='blue', markersize=12)
	plt.ylim(0,5)
	plt.xlabel('time')
	plt.ylabel('creatinine')

	plt.title('Line graph!')
	plt.savefig("static/chart1.png")
	plt.close()

	x1=[]
	y1 = mydict[id]["digit_glucose"]
	for i in range(len(mydict[id]["digit_glucose"])):
		x1.append(i+1)

	plt.plot(x1, y1, color='green', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='blue', markersize=12)
	plt.ylim(0,5)
	plt.xlabel('time')
	plt.ylabel('glucose')

	plt.title('Line graph!')

	plt.savefig("static/chart2.png")
	plt.close()

	x1=[]
	y1 = mydict[id]["digit_blood"]
	for i in range(len(mydict[id]["digit_blood"])):
		x1.append(i+1)

	plt.plot(x1, y1, color='green', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='blue', markersize=12)
	plt.ylim(0,5)
	plt.xlabel('time')
	plt.ylabel('glucose')

	plt.title('Line graph!')

	plt.savefig("static/chart2.png")
	plt.close()
	