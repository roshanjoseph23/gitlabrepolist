# gitlabrepolist
To get the RepoDetails, SSH URLs, HTTPS Urls, Repo Web URLs under a group

## Prerequisites

* Gitlab profile which has access to the group/projects that you need to get the list of.
* Create an Access Token from your gitlab profile to access the group/repo details using api

## Usage

1. Execute the python script

```bash
python gitlab_repo_list.py
```

2. Provide the Gitlab Domain
```
Enter the GitLab domain name :
```

3. Provide the group name of all the repo's that you need the list of
```
Enter the project group name :
```

4. Provide the Access token that you have
```
Please enter private token :
```

***
***

Once the token provided is successful, you will receive an output

```
Token Succesfull...
```

After successful verification, script will get the Total number of pages of repo details from the Group name you have provided in step 3.
Then it will get all the Repository details going through all the pages and add this in `repodetails.json` file.

Then it will filter out the Repo Web URL List, HTTPS URL List, SSH URL List to respective `RepoUrls.txt, HTTPSUrls.txt, SSHUrls.txt` file.