import getpass
import requests
import json
import os

from pathlib import Path

class GitLab:
    def filecheck(self):
        file = ["RepoUrls.txt", "HTTPSUrls.txt", "SSHUrls.txt", "repodetails.json"]
        for i in file:
            my_file = Path(i)
            if my_file.is_file():
                open(my_file, 'w').close()

    def gitlabdomain(self):
        global gitlabdomain
        gitlabdomain = input('Enter the GitLab domain name : ')
        return gitlabdomain

    def groupname(self):
        global groupname
        groupname = input('Enter the project group name : ')
        return groupname

    def privatetoken(self):
        global privatetoken
        privatetoken = getpass.getpass('Please enter private token : ')
        return privatetoken
    
    def tokenverification(self):
        while True:
            try:
                self.gitlabdomain()
                self.groupname()
                self.privatetoken()
                r = requests.get('https://'+gitlabdomain+'/api/v4/groups/'+groupname+'/projects?private_token='+privatetoken)
                r.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('Incorrect Token...Please try again...')
                continue
            break
        print('Token Succesfull...')
        return r.status_code

    def headerrequest(self):
        req = requests.get('https://'+gitlabdomain+'/api/v4/groups/'+groupname+'/projects?private_token='+privatetoken+'&include_subgroups=true')
        return req.headers['X-Total-Pages']

    def repodetails(self):
        page = self.headerrequest()
        for i in range(1, int(page)+1):
            print('On page '+str(i))
            req = requests.get('https://'+gitlabdomain+'/api/v4/groups/'+groupname+'/projects?private_token='+privatetoken+'&page='+str(i)+'&include_subgroups=true')
            repodetails = req.json()
            with open('repodetails.json', 'a') as f:
                json.dump(repodetails, f, indent=2)

class RepoFiltering:
    def weburllist(self):
        os.system("jq -r '.[] | select(.archived==false).web_url' repodetails.json >> RepoUrls.txt")
        os.system("sort -o RepoUrls.txt RepoUrls.txt")
        print("RepoUrls.txt is populated with repo web url\n")

    def httpurllist(self):
        os.system("jq -r '.[] | select(.archived==false).http_url_to_repo' repodetails.json >> HTTPSUrls.txt")
        os.system("sort -o HTTPSUrls.txt HTTPSUrls.txt")
        print("HTTPSUrls.txt is populated with repo web url\n")

    def sshurllist(self):
        os.system("jq -r '.[] | select(.archived==false).ssh_url_to_repo' repodetails.json >> SSHUrls.txt")
        os.system("sort -o SSHUrls.txt SSHUrls.txt")
        print("SSHUrls.txt is populated with repo web url\n")

GitLab().filecheck()
GitLab().tokenverification()
GitLab().repodetails()
RepoFiltering().weburllist()
RepoFiltering().httpurllist()
RepoFiltering().sshurllist()