# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://gopichand-vadlamudi.atlassian.net/rest/api/3/issue"
api_token="ATATT3xFfGF0I4onq9THyaZQdfG-kGm_xeUId2MyuJE6UlTqlrVCABPuFbOUBxa7ORbCLauDdET0sYYT9b0GkZWEbhT1NOBkQzc0WOl5a_faI6k3_jDM0aMaaBkgXT8hrRBQO0jyspagfKh7pVrOFjj6iutRtXGa4c0hA-m66psp3j5Kbyxuqm4=3C0528D2"
 

auth = HTTPBasicAuth("vadlamudigchand@gmail.com",api_token)


headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}
payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "project": {
      "key": "AUT"
    },
    "issuetype": {
      "id": "10008"
    },
    "summary": "First JIRA Ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))