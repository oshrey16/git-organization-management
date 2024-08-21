import json
import subprocess

def load_config():
    with open('configure.json') as f:
        return json.load(f)

def run_script_with_config():
    config = load_config()
    key = config.get("key")
    organization_name = config.get("organization_name")
    number_of_groups = config.get("number_of_groups")
    visibility = config.get("visibility")
    template_team_name = config.get("template_team_name")
    template_repo_name = config.get("template_repo_name")
    
    # Validate require config:
    key_Isvalid(key)
    organization_name_Isvalid(organization_name)
    number_of_groups_Isvalid(number_of_groups)
    visibility_Isvalid(visibility)
    template_repo_name_Isvalid(template_repo_name)
    def run_create_repos():
        # Call the create_repos.py script
        subprocess.run(['python3', 'create_repos.py', key, organization_name, number_of_groups, visibility, template_repo_name])
    
    def menu(choice):
        match choice:
            case '1':
                run_create_repos()
            case _:
                print("Error - not valid choice")
    
    while(True):
        choice = input("Enter action number: ")
        menu(choice)

def key_Isvalid(key):
    if len(key) == 0:
        print("Error: 'key' must be in configure.json.")
def organization_name_Isvalid(organization_name):
    if len(organization_name) == 0:
        print("Error: 'organization_name' must be in configure.json.")
def number_of_groups_Isvalid(number_of_groups):
    if not number_of_groups.isdigit():
        print("Error: 'number_of_groups' must be a digit in configure.json.")
        return
    if int(number_of_groups) <= 0:
        print("Error: 'number_of_groups' must be positive number.")
        return
def visibility_Isvalid(visibility):
    if visibility != "private" and visibility != "public":
        print("Error: 'visibility' must be in 'public' or 'private' in configure.json.")
def template_repo_name_Isvalid(template_repo_name):
    if len(template_repo_name) == 0:
        print("Error: 'template_repo_name' must be in configure.json.")
    
if __name__ == "__main__":
    run_script_with_config()
