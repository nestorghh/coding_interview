import requests

def get_points():
	u = "http://api.flutrack.org/?time=7"
	return requests.get(u)




