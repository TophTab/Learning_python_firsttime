import requests

url='https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
print('Status code:',r.status_code)

response_dict=r.json()
print("Total repositories;",response_dict['total_count'])

repo_dicts=response_dict['items']
print("Repositories returned:",len(repo_dicts))

print("\nSome information about each repository")
for repo_dict in repo_dicts:
    print("Name:",repo_dict['name'])
    print('Owner:',repo_dict['owner']['login'])
    print("Stars:",repo_dict['stargazers_count'])
    print('Repository',repo_dict['html_url'])
    print("Description:",repo_dict['description'])