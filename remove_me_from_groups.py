from github import Github
import json
import sys
####
# arg1 - your username on Github
####
# Opening JSON file
f = open('data.json')
# returns JSON object as a dictionary
data = json.load(f)

# Setup numberGroups, key, org, templates and visibility.
total_groups = data["number_of_groups"]
g = Github(data["key"])
org = g.get_organization(data["organization"])
template_team_name = data["template_team_name"]

my_user = g.get_user(sys.argv[1])
for i in range(1,total_groups+1):
    team = org.get_team_by_slug(template_team_name + str(i))
    team.remove_membership(my_user)
    print("Removed from " + str(team))