from github import Github
import csv
import json

# add_to_members
# Opening JSON file
f = open('data.json')
# returns JSON object as a dictionary
data = json.load(f)

g = Github(data["key"])
org = g.get_organization(data["organization"])
template_team_name = data["template_team_name"]

# load report file to write if users not found
report_file = open("git_users_addto_team_report.txt",'w')

# read csv file
# column0 - username on github
# column4 - teamName
with open('outputgit.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, dialect='excel',delimiter=',')
    for row in csv_reader:
        team_num =  row[4].partition("_TEAM_")[2]   # get number of team
        team = org.get_team_by_slug(template_team_name + str(team_num)) # get team from github
        user =  row[0]  # username
        try:
            user = g.get_user(user)
            print("Invite sent to {} team {}".format(user,team))
            team.add_membership(user)
        except:
            report_file.write("Group: " + team_num +", Email: " + row[2] + " Not Found!\n")
f.close()