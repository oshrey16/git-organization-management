from github import Github
import json

# Opening JSON file
f = open('data.json')
# returns JSON object as a dictionary
data = json.load(f)

# Setup numberGroups, key, org, templates and visibility.
total_groups = data["number_of_groups"]
g = Github(data["key"])
org = g.get_organization(data["organization"])
template_team_name = data["template_team_name"]
template_repo_name = data["template_repo_name"]
vis = data["visibility"]
if vis=="private":
    visibility = True
elif vis=="public":
    visibility = False

# load report file to write if something faild
f = open("log_permission.txt",'w')

for i in range(1,total_groups+1):
        repo = org.get_repo(template_repo_name + str(i))
        try:
            repo.edit(private= visibility)
            print("Group " + str(i) + ": Changed To {}".format(vis))
        except:
            f.write("Group: " + str(i) + " Faild")
f.close()