#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
	req = request.get_json(silent=True, force=True)

	print("Request:")
	print(json.dumps(req, indent=4))

	res = makeWebhookResult(req)

	res = json.dumps(res, indent=4)
	print(res)
	r = make_response(res)
	r.headers['Content-Type'] = 'application/json'
	return r

def makeWebhookResult(req):
	try:
		if req.get("result").get("action") == 'get_action':
			flag=0
			speech="At the very beginning\n"+req.get("result").get("action")+"\n"
			print("Speech:"+'\t'+speech+'\t'+"flag:"+'\t'+str(flag))
			result=req.get("result")
			parameters=result.get("parameters")
			try:
				contact_id=parameters.get("contact_types")
				speech=speech+contact_id+"\n"
			except:
				contact_id=""
				speech=speech+"1\n"
			try:		
				need_id=parameters.get("no_need")
				speech=speech+need_id+"\n"
			except:
				need_id=""
				speech=speech+"2\n"
			try:		
				contact_id2=parameters.get("contact_types1")
				speech=speech+contact_id2+"\n"
			except:
				contact_id2=""
				speech=speech+"3\n"	

			flag+=1	
			print("Speech:"+'\t'+speech+'\t'+"flag:"+'\t'+str(flag))


			speech="speech\n"	
			if contact_id=="mail":
				speech="Sure Stay connected.\n"
				speech=speech+"Here you go. My mail id is : mailme@anirbansaha.com\n"	
			elif contact_id=="number":
				speech="Sure Stay connected.\n"
				speech=speech+"My contact number is: +91 9903055542\n"
			elif contact_id=="contact":
				speech="Sure Stay connected.\n"
				speech=speech+"My email is mailme@anirbansaha.com and my phone number is +91 9903055542\n"
			else:
				speech=""

			flag+=1	
			print("Speech:"+'\t'+speech+'\t'+"flag:"+'\t'+str(flag))

			
			if contact_id2=="mail":

				speech=speech+"Here you go. My mail id is : mailme@anirbansaha.com\n"	
			elif contact_id2=="number":
				speech=speech+"My contact number is: +91 9903055542\n"
			elif contact_id2=="contact":
				speech=speech+"My email is mailme@anirbansaha.com and my phone number is +91 9903055542\n"
			else:	
				speech=speech+""

			flag+=1	
			print("Speech:"+'\t'+speech+'\t'+"flag:"+'\t'+str(flag))	

			if "mail" in need_id:
				speech="Have a nice day\n"
			elif "number" in need_id:
				speech="Have a nice day\n"
			elif "contact" in need_id:
				speech="Have a nice day\n"
			else:
				speech="Have a nice day\n"

			flag+=1	
			print("Speech:"+'\t'+speech+'\t'+"flag:"+'\t'+str(flag))

			return {
				"speech": speech,
				"displayText": speech,
				"data": {},
				"contextOut": [],
				"source": "apiai-onlinestore-shipping"
			}
		else:
			return{}
			# speech="I am flag one in get_action module\n"+str(req.get("result").get("action"))
			# return {
			# 	"speech": speech,
			# 	"displayText": speech,
			# 	#"data": {},
			# 	# "contextOut": [],
			# 	"source": "apiai-onlinestore-shipping"
			# }

				
	except Exception as error:
		#speech=str(error)
		speech="I am inside error module \n"
		print("Speech:"+'\t'+speech+'\t'+"flag:"+'\t'+str(flag))
		return {
			"speech": speech,
			"displayText": speech,
			#"data": {},
			# "contextOut": [],
			"source": "apiai-onlinestore-shipping"
		}

if __name__ == '__main__':
	port = int(os.getenv('PORT', 5000))

	print("Starting app on port %d" % port)

	app.run(debug=True, port=port, host='0.0.0.0')

