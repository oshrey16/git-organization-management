from github import Github
import time
import sys
import json

# arg1 - number of groups
print("Creating {} groups..".format(sys.argv[1]))

# Opening JSON file
f = open('data.json')
# returns JSON object as a dictionary
data = json.load(f)
# Setup git key, organization and number of groups
g = Github(data["key"])
org = g.get_organization(data["organization"])
groups = data["number_of_groups"]


for i in range(1,groups+1):
    time.sleep(0.5)
    # Create the repo
    org.create_repo(data["template_repo_name"] + str(i),private=True)
    print("Created " + data["template_repo_name"] + str(i) + "Repo")