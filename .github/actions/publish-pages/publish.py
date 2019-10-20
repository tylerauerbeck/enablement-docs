import requests, re, jmespath, json

PR = os.getenv('GITHUB_EVENT_PATH')

with open(PR) as json_file:
    data = json.load(json_file)
    PR_ENDPOINT = jmespath.search('pull_request._links.self.href',data)
    print(PR_ENDPOINT)

r = requests.get(url = PR_ENDPOINT)

files = jmespath.search('[].filename',r.json())

for file in files:
    if re.search("^exercises\/.*",file):
        print("Exercises have been modified")
        break
