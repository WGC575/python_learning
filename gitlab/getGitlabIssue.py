'''
Required CLI parameters:
-   project_id = args[1]
-   issue_id = args[2]
This script use project id to get all issue merges (as seen under the issue pages).
Example:
project_id = 4207231
issue_id = 1242
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
    issue_id = args[2]
else:
    exit("Missing issue ID.")

# directories   
dirctory_name = "../../data/"
output_directory = "./results/"

# open token file (token file is ignored, and a local token file is required)
with open("gitlabToken.token", "rb") as f:
    token = f.read()
#print(token)

# Specify your GitLab server URL and access token
gitlab_url = 'https://gitlab.com'
access_token = token

# Create a GitLab API client
gl = gitlab.Gitlab(gitlab_url, private_token=access_token)

def get_issue_merges(project_id, issue_id):
    project = gl.projects.get(project_id)
    issue = project.issues.get(issue_id)

    # Retrieve the merges from the issue description and notes
    merges = {}
    print(issue_id)
    print(issue.references)

    # Check merges in the issue description
    print(issue.notes.list)

    '''
    # Fetch merge request details and add them to the result list
    merge_request_info = []
    print("Merges: ")
    print(merges)
    for mr_iid in merges:
        merge_request = project.mergerequests.get(mr_iid)
        print("Merge Request: ")
        print(merge_request)
        merge_request_info.append({
            'id': merge_request.id,
            'title': merge_request.title,
            'url': merge_request.web_url
        })
    time.sleep(3)
    return merge_request_info
    '''

merges = list()

mention = get_issue_merges(project_id, issue_id)
merges.append(mention)
print("Writting issue " + issue_id + " to output...")

output_json = "project_" + project_id +"_decision_merges_result.json"
'''
with open("output_json", "w") as f:
    f.write(merges)
print("Search result successfully dumped to " + output_json)
'''
#print(merges)
with open(output_json, "w") as f:
    json.dump(merges, f)
print("Search result successfully dumped to " + output_json)

