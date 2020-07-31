import data
import pickle


avg=0
t=0
low=high=0
count=0
pkl_file = open('patient.pkl', 'rb')
mydict = pickle.load(pkl_file)
pkl_file.close()


def digitize(line,tname,id):
	value=0
	print("digitize",id)
	for i in line.split():
		print(i)
		if(data.param[tname]["data"]):
			if(data.param[tname]["range"]):
				low=high=0
				count=0
				a=[]
				if(i=='-'):
					for x in line.split():
						if(x.replace('.','').isdigit()):
							if(count==0):
								low=float(x)
							if(count==1):
								high=float(x)
							count=count+1
					if(data.param[tname]["gender"]):
						a=data.param[tname][mydict[id]["gender"]] 
							#if result depends on age	
					elif(data.param[tname]["age"]):
						for k in data.param[tname]:
							if(k.isdigit()):
								if(k>=mydict[id]["age"]):
									a=data.param[tname][k]
					else:
						a=data.param[tname]["value"]
					
					a=a.split('-')
					low1,high1= float(a[0]),float(a[1])
					if(low>=low1 and high<=high1):
						value=1
					if((low1-low)>1 or (high-high1)>1):
						value=2
					if((low1-low)>3 or (high-high1)>3):
						value=3
					if((low1-low)>6 or (high-high1)>6):
						value=4
				

					print(value)
					break
				
				elif('-' in i):
						if((i.replace('-','')).replace('.','').isdigit()):
								b=i.split('-')
								count+=1
								if(count<2):
										low,high= float(b[0]),float(b[1])
								if(data.param[tname]["gender"]):
										a=data.param[tname][mydict[id]["gender"]] 
							#if result depends on age	
								elif(data.param[tname]["age"]):
									for k in data.param[tname]:
										if(k.isdigit()):
											if(k>=mydict[id]["age"]):
												a=data.param[tname][k]
								else:
									a=data.param[tname]["value"]
					
								a=a.split('-')
								low1,high1= float(a[0]),float(a[1])
								if(low>=low1 and high<=high1):
										value=1
								if((low1-low)>1 or (high-high1)>1):
										value=2
								if((low1-low)>3 or (high-high1)>3):
										value=3
								if((low1-low)>6 or (high-high1)>6):
										value=4

						print(value)
						break

			else:
				if(i.replace('.','').isdigit()):
					  #gender dependent
						if(data.param[tname]["gender"]):
							a=data.param[tname][mydict[id]["gender"]]
						#age dependent 
						elif(data.param[tname]["age"]):
							for k in data.param[tname]:
								if(type(k)==int):
									if(k>=mydict[id]["age"]):
										a=data.param[tname][k]
						#otherwise
						else:
							a=data.param[tname]["value"]
						a = a.split('-')
						low,high= float(a[0]),float(a[1])
						i=float(i)
						if(i<=high and i>=low):
								value=1
						if(i<=(low+(0.1*low)) or i>=(high +(0.1*high))):
								value=2
						if(i<=(low+(0.2*low)) or i>=(high +(0.2*high))):
								value=3
						if(i<=(low+(0.4*low)) or i>=(high +(0.4*high))):
								value=4

						print(value)
						break

		else:
			if(i=='absent' or i=='not'):
			
					if(data.param[tname]["value"]=='negative'):
						value=1
					elif(data.param[tname]["value"]=='positive'):
						value=4
					print(value)
					break
		

			elif(i=='present' or i=='found' or i=='none'):
			
					if(data.param[tname]["value"]=='negative'):
						value=4
					elif(data.param[tname]["value"]=='positive'):
						value=1
					print(value)
					break
									
	return value			

					



def mapping(id):
	print("map id",id)
	avg=0
	t=0
	with open("outpu1.txt") as openfile:
		for line in openfile:  
			for part in line.split():
				#for i in data.param:
					if "creatinine" in part:
						print(part)
						val=digitize(line,"creatinine",id)
						if(val>0):
							print(val)
							# if(val!=0):
							# 	avg=avg+val
							# 	t=t+1
							# 	print(avg)
							mydict[id]["digit_creatinine"].append(val)
							output = open('patient.pkl', 'wb')
							pickle.dump(mydict, output)
							output.close()

	with open("outpu1.txt") as openfile:
		for line in openfile:  
			for part in line.split():

				if "glucose" in part:
					print(part)
					val=digitize(line,"glucose",id)
					if(val>0):
						print(val)
						# if(val!=0):
						# 	avg=avg+val
						# 	t=t+1
						# 	print(avg)
						mydict[id]["digit_glucose"].append(val)
						output = open('patient.pkl', 'wb')
						pickle.dump(mydict, output)
						output.close()
	# avg1=avg/t
	# print(avg1)
	#mydict[id]["digit"].append(avg1)

	# output = open('patient.pkl', 'wb')
	# pickle.dump(mydict, output)
	# output.close()

	print(mydict)	

