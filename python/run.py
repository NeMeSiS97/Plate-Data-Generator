import time
import openalpr_api
import os
from os import walk
from openalpr_api.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = openalpr_api.DefaultApi()
#with open("7.png", "rb") as f:
    #data = f.read()
    #image_bytes = data.encode("base64")
import base64
import glob
SIZE=[]
txtfiles = []
cls_id=0
for file1 in glob.glob1(os.getcwd()+'/Images', "*.png"):
    	print (file1)
    	with open('Images/'+file1, "rb") as image_file:
        	image_bytes = base64.b64encode(image_file.read())
	#image_bytes = '7.png' # str | The image file that you wish to analyze encoded in base64 
	secret_key ='sk_DEMODEMODEMODEMODEMODEMO'
	country = 'in' 
	recognize_vehicle = 0 
	state = '' 
	return_image = 1 
	topn = 1 
	prewarp = '' 
	try:
    		api_response = api_instance.recognize_bytes(image_bytes, secret_key, country, recognize_vehicle=recognize_vehicle, state=state, return_image=return_image, topn=topn, prewarp=prewarp)
    		#pprint(api_response.results)
    		SIZE=[api_response.img_height,api_response.img_width]
    		cord=openalpr_api.models.plate_details.res
		plate=openalpr_api.models.plate_details.plat
    		pprint(plate)
	except ApiException as e:
   		print "Exception when calling DefaultApi->recognize_bytes: %s\n" % e
