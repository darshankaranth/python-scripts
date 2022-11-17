import requests
import argparse
import json
import re


def main():
    ### Get arguments from the CLI ###
    my_parser = argparse.ArgumentParser(prog='config', description='Upgrade app')
    my_parser.add_argument('env', action='store', type=str, help='URL')
    my_parser.add_argument('-u', action='store', type=str,required=True, help='username')
    my_parser.add_argument('-p', action='store', type=str,required=True, help='password')
    my_parser.add_argument('-name', action='store',type=str, required=True, help='Enterprise name')
    my_parser.add_argument('-version', action='store',type=str, required=True, help='upgrade version')                           
    args = my_parser.parse_args()
    env = args.env
    user = args.u
    pwd = args.p
    org = args.name
    version = args.version


    ### Set url ###
    url = "https://{}.sdxcloud.in".format(env)
    
    ### Call appstack class in module.py ###
    client = appstack(url)

    ### Login and retrieve bearer token ###
    auth = client.appauth(user, pwd)

    ### Check Enterprise name syntax ###
    org_check = False
    try:
        if(org):
            if re.search('[a-zA-Z]{3,4}', org):
                org_check = True
                if(org_check == True):
                     client.appupgrade(auth, org, version)
            else:
                print("Enter a 3 aplhabet Enterprise name. Eg AAA,BBB,CCC.DDD")
    except OSError as e:
        print("OS error:", e)
 
class appstack(object):

    def __init__(self, hostname ):
        self._session = requests.Session()
        self._rooturl = self._root_url(hostname)
    
    def _root_url(self, hostname):
        return hostname

    ### Login and retrieve bearer token ###

    def appauth(self, user, pwd):
        path = "/v2/auth"
        endpoint = self._rooturl + path
        headers = {
            'Content-Type': 'application/json'
        }
        data = {"username": user, "password": pwd}
        try:
            r = self._session.post(endpoint, headers=headers,
                               data=json.dumps(data))
        
            res = r.json()
            if(r.status_code==200):
                token = (res['auth_token'])
                if(token):
                    print("Login token is \n\n%s" % token)
                    print('\n')
                else:
                    print(user, "Login failed")
                    print('\n\n')

                return token    
            else:
                print ("Incorrect credentials")
                
        except OSError as e:
            print("OS error:", e)

    ### Upgrade ###

    def appupgrade(self, auth, org, version):
        putupgrade_path = "/v2/orgs/{}/upgrade".format(org)
        putupgrade_endpoint = self._rooturl + putupgrade_path
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(auth)
        }
        data = {

			"version": version
			
        }
        r = self._session.put(putupgrade_endpoint, headers=headers, data=json.dumps(data))
        res_upgrade = r.json()
        print('{}\n\n'.format(res_upgrade))
    

if __name__ == '__main__':
    main()