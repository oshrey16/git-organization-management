from github import Github
import json

# Opening JSON file
f = open('data.json')
# returns JSON object as a dictionary
data = json.load(f)

# Setup numberGroups, key, org, templates.
total_groups = data["number_of_groups"]
g = Github(data["key"])
org = g.get_organization(data["organization"])
template_team_name = data["template_team_name"]
template_repo_name = data["template_repo_name"]
# Load log file
f = open("log_permission.txt", 'w')
select = input(
    "Please select option\n1- Admin\n2- Maintain\n3- Write\n4- Triage\n5- Read\ninput: ")
# permission options
options = {"1": "admin", "2": "maintain",
           "3": "write", "4": "triage", "5": "read"}

for i in range(1, total_groups+1):
    team = org.get_team_by_slug(template_team_name + str(i))    # get team
    repo = org.get_repo(template_repo_name + str(i))    # get repo
    try:
        team.update_team_repository(repo, options[select])  # update repo permission
        print("repository {} updated to {}".format(template_repo_name + str(i),options[select]))
    except:
        f.write("Group: " + i + " Faild")
f.close()
