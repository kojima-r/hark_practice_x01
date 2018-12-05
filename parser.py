import json

while True:
	line=input()
	try:
		line=line.replace("'","\"")
		obj=json.loads(line)
		print(obj)
	except:
		pass

