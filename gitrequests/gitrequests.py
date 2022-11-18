import requests
import json
import sys

url = "https://api.github.com/users/octocat/repos"
repo_key = "html_url"

def main():
    if len(sys.argv) != 2:
        print("usage: python %s <token>" % sys.argv[0])
        sys.exit(0)
    token = sys.argv[1]
    header = { "Accept" : "application/vnd.github+json",
               "Authorization" : "Bearer {}".format(token)  
    }   
    try:
        r  = requests.get(url,header)
        result = r.json()
        #print(result)
        for repo in range(len(result)):
            print(result[repo][repo_key]) 
    except Exception as e:
        print("Failed to get repo list", e)
        sys.exit() 

if __name__ == '__main__':
    main()