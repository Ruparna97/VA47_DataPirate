import pickle

patients={
	1:{
		"digit_glucose":[],
		"digit_creatinine":[],
		"digit_blood":[],
		"age":3,
		"gender":'m'

	},
	2:{
		"digit_glucose":[],
		"digit_creatinine":[],
		"digit_blood":[],
		"age":5,
		"gender":'f'
	},

}
output = open('patient.pkl', 'wb')
pickle.dump(patients, output)
output.close()