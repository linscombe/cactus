from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from github import Github
import os

# Create your views here.
def index_view(request):
    print('GitHub')

    # using an access token
    g = Github(os.environ.get('ACCESS_TOKEN'))
    # Then play with your Github objects:

    # access single repo
    # repo = g.get_repo("linscombe/cactus")

    list = []
    for repo in g.get_user().get_repos():
        print(repo.name)


        open_issues = repo.get_issues(state='open')
        for issue in open_issues:
            print(issue)
            item = {
                "repo": repo.name,
                "title": issue.title,
                "number": issue.number
            }
            list.append(item)

    context ={
        "list":list,
    }
      
    return render(request, "index.html", context)
