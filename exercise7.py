#! /usr/bin/python3

import requests
import passwords

user= passwords.user
passwd = passwords.passwd

# GitHub API 
url = f"https://api.github.com/user/repos"

# Make a GET request to the GitHub API with basic authentication
response = requests.get(url, auth=(user, passwd))

# Check if the request was successful
if response.status_code == 200:
    repos = response.json()
    print(f"Repositories for {user}:")
    for repo in repos:
        print(f"- {repo['name']}: {repo['html_url']}")
else:
    print(f"Failed to fetch repositories: {response.status_code} - {response.text}")
