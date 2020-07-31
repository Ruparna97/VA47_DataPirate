import pickle

patients={
	1:{
		"digit":[],
		"age":3,
		"gender":'m'

	},
	2:{
		"digit":[],
		"age":5,
		"gender":'f'
	},

}
output = open('patient.pkl', 'wb')
pickle.dump(patients, output)
output.close()