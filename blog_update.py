import os
import openai
openai.api_key = os.getenv('OPENAI_API_KEY')

from git import Repo
from pathlib import Path

PATH_TO_BLOG_REPO = Path('/Users/knetterville/python/ai_courses/ai_github_blog/.git')
PATH_TO_BLOG = PATH_TO_BLOG_REPO.parent
PATH_TO_CONTENT = PATH_TO_BLOG/"content"
PATH_TO_CONTENT.mkdir(exist_ok=True, parents=True)


def update_blog(commit_msg='Update blog'):
    # GitPython repo set
    repo = Repo(PATH_TO_BLOG_REPO)
    repo.git.add(all=True)
    repo.index.commit(commit_msg)
    origin = repo.remote(name='origin')
    origin.push()

# Add new content to Index.html
with open(PATH_TO_BLOG/"index.html", 'w') as f:
    f.write("Update text aaa")

update_blog()