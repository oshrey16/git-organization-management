from github import Github
import time
import sys

def main(key,organization_name, number_of_groups, visibility, template_repo_name):
    print("Creating {} groups..".format(number_of_groups))
    time.sleep(0.5)

    # Setup git key, organization and number of groups
    g = Github(key)
    org = g.get_organization(organization_name)

    visibility = convert_visibility(visibility)

    for i in range(1,number_of_groups+1):
        time.sleep(0.5)
        # Create the repo
        org.create_repo(template_repo_name + str(i),private=visibility)
        print("Repo " + template_repo_name + str(i) + " has been created!")

def convert_visibility(visibility):
    if visibility=="private":
        return True
    elif visibility=="public":
        return False

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python3 create_repos.py <key> <organization_name> <number_of_groups> <visibility> <template_repo_name>")
    else:
        key = sys.argv[1]
        organization_name = sys.argv[2]
        number_of_groups = int(sys.argv[3])
        visibility = sys.argv[4]
        template_repo_name = sys.argv[5]
        main(key,organization_name, number_of_groups, visibility, template_repo_name)