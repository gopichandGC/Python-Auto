# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://gopichand-vadlamudi.atlassian.net/rest/api/3/project"
api_token="ATATT3xFfGF0I4onq9THyaZQdfG-kGm_xeUId2MyuJE6UlTqlrVCABPuFbOUBxa7ORbCLauDdET0sYYT9b0GkZWEbhT1NOBkQzc0WOl5a_faI6k3_jDM0aMaaBkgXT8hrRBQO0jyspagfKh7pVrOFjj6iutRtXGa4c0hA-m66psp3j5Kbyxuqm4=3C0528D2"
 

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