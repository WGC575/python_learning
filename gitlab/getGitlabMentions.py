'''
Required CLI parameters:
-   project_id = args[1]
-   issue_set_file = arg[2]
This script use project id to get all issue mentions/notes (as seen under the issue pages).
'''

import gitlab
import numpy as np
import json
import sys
import time

# CLI arguments, an array
args = sys.argv

# print the arguments
print("Number of arguments:", len(args))
print("The arguments are:", str(args))

# traverse arguments
if args[1]:
    project_id = args[1]
else:
    exit("Missing project ID.")

if args[2]:
    issue_set_file = args[2]
else:
    exit("Missing issue ID.")

# directories   
dirctory_name = "../../data/"
output_directory = "./results/"

# open token file (token file is ignored, and a local token file is required)
with open("gitlabToken.token", "rb") as f:
    token = f.read()
#print(token)

# open issue list file
with open(issue_set_file, "rb") as f:
    issue_ids = json.load(f)
print(issue_ids)

# Specify your GitLab server URL and access token
gitlab_url = 'https://gitlab.com'
access_token = token

# Create a GitLab API client
gl = gitlab.Gitlab(gitlab_url, private_token=access_token)

def get_issue_mentions(project_id, issue_id):
    project = gl.projects.get(project_id)
    issue = project.issues.get(issue_id)

    # Retrieve the mentions from the issue description and notes
    mentions = {}

    # Check mentions in the issue description
    #print(issue)
    #mentions.extend(issue.description['mention'])

    # Fetch notes from the issue and check mentions in each note
    
    notes = issue.notes.list(all=True)
    print(len(notes))
    
    for note in notes:
        note = issue.notes.get(note.get_id())
        #print(note.to_json())
        mentions[issue_id] = note.to_json()
    
    time.sleep(3)
    return mentions

'''
Example:
project_id = 4207231
issue_id = 1242
'''
mentions = list()

for issue_id in issue_ids:
    mention = get_issue_mentions(project_id, issue_id)
    mentions.append(mention)
    print("Writting issue " + issue_id + " to output...")

output_json = "project_" + project_id +"_decision_mentions_result.json"
'''
with open("output_json", "w") as f:
    f.write(mentions)
print("Search result successfully dumped to " + output_json)
'''
#print(mentions)
with open(output_json, "w") as f:
    json.dump(mentions, f)
print("Search result successfully dumped to " + output_json)
