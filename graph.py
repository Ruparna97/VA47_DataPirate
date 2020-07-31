import matplotlib.pyplot as plt
import numpy as np
import pickle
import os



'''

plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='blue', markersize=12)
plt.ylim(0,4)
plt.xlabel('time')
plt.ylabel('health')

plt.title('Line graph!')

plt.show()
'''

'''
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.set_ylim(0,6)
ax.set_xlim(0,10)
ax.set_ylabel('Health Status')
ax.set_title('TrendChart')

ax.bar(x,y)
plt.show()
'''
def graphing(id):

	pkl_file = open('patient.pkl', 'rb')
	mydict = pickle.load(pkl_file)
	pkl_file.close()
	x=[]
	y = mydict[id]["digit"]
	for i in range(len(mydict[id]["digit"])):
		x.append(i+1)

	print(mydict)
	width = 0.8 # width of the bars

	fig, ax = plt.subplots()
	rects1 = ax.bar(x, y, width, color='b')

	ax.set_ylim(0,5)
	ax.set_ylabel('Health')
	ax.set_xlabel('Time')
	ax.set_title('TrendChart')
	#ax.set_xticks(np.add(x,(width/2))) # set the position of the x ticks


	def autolabel(rects):
	    # attach some text labels
	    for rect in rects:
	        height = rect.get_height()
	        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
	                '%d' % int(height),
	                ha='center', va='bottom')

	autolabel(rects1)
	
	plt.savefig("static/chart.png")
	plt.close(fig)