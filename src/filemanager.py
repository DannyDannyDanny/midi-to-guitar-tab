import json

def put(data, filename):
	try:
		jsondata = json.dumps(data, indent=4, skipkeys=True, sort_keys=True)
		fd = open(filename, 'w')
		fd.write(jsondata)
		fd.close()
	except:
		print('ERROR writing', filename)
		pass

def get(filename):
	returndata = {}
	try:
        # filename = 'dink.json'
		fd = open('./'+filename, 'r')
		text = fd.read()
		fd.close()
		returndata = json.loads(text)
		# Hm.  this returns unicode keys...
		#returndata = simplejson.loads(text)
	except:
		print('COULD NOT LOAD:', filename)
	return returndata
