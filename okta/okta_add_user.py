import requests
import json
import sys
import os



def main():
  if len(sys.argv) != 4:
    print("usage: python %s <account> <groupid> <token>" % sys.argv[0])
    sys.exit(0)
  
  accountid = sys.argv[1]
  groupid = [sys.argv[2]]
  token = sys.argv[3]

  headers = { 'Content-Type': 'application/json', 
            'Accept' : 'application/json',
            'Authorization': 'SSWS {}'.format(token)
          }
  print(headers)
  url = "https://dev-{}-admin.okta.com/api/v1/users?activate=true&nextLogin=changePassword".format(accountid)
  print(url)
  try:
      base_path = os.path.dirname(os.path.abspath(__file__))
      user_file = os.path.join(base_path, 'okta_user_list.json')
      with open(user_file) as userlist:
         user_list = json.load(userlist)
         for item in user_list:
            data = {
            "profile": {
            "firstName": item['firstName'],
            "lastName": item['lastName'],
            "email": item['email'],
            "login": item['login']
            },
            "credentials" : {
            "password" : "Welcome123!"
            },
  
          "groupIds": groupid
          }
            r = requests.post(url, headers=headers, data=json.dumps(data))
            res = r.json()
            print('{}\n\n'.format(res))
  except Exception as e:
    print("Failed to read org_data file:", e)
    sys.exit() 

if __name__ == '__main__':
    main()

