from github import Github
import sys

# Replace these values with your own
access_token = sys.argv[1]
repository_name = 'Blazemeter/sdubey-testing'
release_version = sys.argv[2]  # Replace with your desired release version
release_name = f"Release {release_version}"  # Replace with your desired release name
release_body = f"Release {release_version}"  # Replace with your desired release description

# Authenticate with your GitHub account using the access token
g = Github(access_token)

# Get the repository
repo = g.get_repo(repository_name)

# Create the release
release = repo.create_git_release(
    tag=release_version,
    name=release_name,
    message=release_body,
    draft=False,  # Set to True if you want to create a draft release
    prerelease=False  # Set to True if this is a prerelease
)

print(f"Created release {release.tag_name}: {release.title}")
