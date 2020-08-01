import webbrowser, os
import json
import boto3
import io
from io import BytesIO
import sys
from pprint import pprint
import test_param
from cdifflib import CSequenceMatcher

 
def get_table_csv_results(file_name):
	with open(file_name, 'rb') as file:
		img_test = file.read()
		bytes_test = bytearray(img_test)
		print('Image loaded', file_name)


	client = boto3.client('textract')

	response = client.analyze_document(Document={'Bytes': bytes_test}, FeatureTypes=['TABLES'])
	output_file = 'outpu1.txt'
	f=open('outpu1.txt','w+')

	for item in response["Blocks"]:
		if item["BlockType"] == "WORD":
			for i in test_param.param:
				if i in item['Text'].lower():
				if(CSequenceMatcher(lambda x: x == " ",i,item['Text'].lower()).ratio()>0.7):
					f.write("\n")
			f.write(item['Text'].lower() +" ")





