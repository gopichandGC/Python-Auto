# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os


url = "https://gopichand-vadlamudi.atlassian.net/rest/api/3/project"
os.getenv("api_token")
auth = HTTPBasicAuth("vadlamudigchand@gmail.com",api_token)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
output=json.loads(response.text)
#print(output)
name=output[0]["name"]
print(name)
# for i in output:
#   name=i[i]["name"]
#   print(name)
# nested_list=output
# flattened_list = [item for sublist in nested_list for item in sublist] 
# print(flattened_list["name"])