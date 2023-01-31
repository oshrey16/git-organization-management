from github import Github
import json

# Opening JSON file
f = open('data.json')
# returns JSON object as a dictionary
data = json.load(f)

# Setup args and git connection
total_group = data["number_of_groups"]
team_name = data["template_team_name"]
repo_name = data["template_repo_name"]
g = Github(data["key"])
org = g.get_organization(data["organization"])

for i in range(1,total_group+1):
    # get the repo to connect
    repo = org.get_repo(repo_name+ str(i))
    # Create a team and connect the repo
    org.create_team(name = team_name+str(i), repo_names = [repo])
    print("Created team {}".format(team_name+str(i)))