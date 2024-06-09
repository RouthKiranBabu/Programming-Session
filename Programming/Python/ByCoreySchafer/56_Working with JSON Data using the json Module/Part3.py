import json
from urllib.request import urlopen

with urlopen("https://google.com") as response:
    source = response.read()
print(source)
#Output
#b'<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" 
#lang="en-IN"><head><meta content="text/html; charset=UTF-8" 
#http-equiv="Content-Type"><meta content="/logos/doodles/2024/2024-indian-
#premier-league-final-6753651837110502-l.png" itemprop="image"><meta 
#content="Indian Premier League Final 2024" property="twitter:tit
#...

#link: https://cran.r-project.org/web/packages/jsonlite/vignettes/json-apis.html
with urlopen("https://api.github.com/users/hadley/orgs") as response:
    source = response.read()
try:
    data = json.loads(source)
    print(json.dumps(data, indent = 2))
except Exception as e:
    print(e)
#Output
#[
#  {
#    "login": "ggobi",
#    "id": 423638,
#    "node_id": "MDEyOk9yZ2FuaXphdGlvbjQyMzYzOA==",
#    "url": "https://api.github.com/orgs/ggobi",
#    "repos_url": "https://api.github.com/orgs/ggobi/repos",
#    "events_url": "https://api.github.com/orgs/ggobi/events",
#    "hooks_url": "https://api.github.com/orgs/ggobi/hooks",
#    "issues_url": "https://api.github.com/orgs/ggobi/issues",
#    "members_url": "https://api.github.com/orgs/ggobi/members{/member}",
#    "public_members_url": "https://api.github.com/orgs/ggobi/public_members{/member}",
#    "avatar_url": "https://avatars.githubusercontent.com/u/423638?v=4",
#    "description": ""
#  },
#  {
#    "login": "rstudio",
#    "id": 513560,
#    "node_id": "MDEyOk9yZ2FuaXphdGlvbjUxMzU2MA==",
#    "url": "https://api.github.com/orgs/rstudio",
#    "repos_url": "https://api.github.com/orgs/rstudio/repos",
#    "events_url": "https://api.github.com/orgs/rstudio/events",
#    "hooks_url": "https://api.github.com/orgs/rstudio/hooks",
#    "issues_url": "https://api.github.com/orgs/rstudio/issues",
#    "members_url": "https://api.github.com/orgs/rstudio/members{/member}",
#    "public_members_url": "https://api.github.com/orgs/rstudio/public_members{/member}",
#    "avatar_url": "https://avatars.githubusercontent.com/u/513560?v=4",
#    "description": ""
#  },
#  {
#    "login": "rstats",
#    "id": 722735,
#    "node_id": "MDEyOk9yZ2FuaXphdGlvbjcyMjczNQ==",
#    "url": "https://api.github.com/orgs/rstats",
#    "repos_url": "https://api.github.com/orgs/rstats/repos",
#    "events_url": "https://api.github.com/orgs/rstats/events",
#    "hooks_url": "https://api.github.com/orgs/rstats/hooks",
#    "issues_url": "https://api.github.com/orgs/rstats/issues",
#    "members_url": "https://api.github.com/orgs/rstats/members{/member}",
#    "public_members_url": "https://api.github.com/orgs/rstats/public_members{/member}",
#    "avatar_url": "https://avatars.githubusercontent.com/u/722735?v=4",
#    "description": null
#  },
#...

with urlopen("https://api.github.com/users/hadley/orgs") as response:
    source = response.read()
try:
    data = json.loads(source)
    #print(json.dumps(data, indent = 2))
    print(len(data[0]["login"]))
except Exception as e:
    print(e)
#Output
#5

with urlopen("https://api.github.com/users/hadley/orgs") as response:
    source = response.read()
try:
    data = json.loads(source)
except Exception as e:
    print(e)
for item in data[0]["login"]: print(item)
#Output
#g
#g
#o
#b
#i