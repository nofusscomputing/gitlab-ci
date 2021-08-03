# git push mirror Admin Manual Manual
This job does a git push to a remote git repo.

This job provides the following badge:

- None

## Dependencies

- None

## your .gitlab-ci.yml changes
To use this job add the following to your `.gitlab-ci.yml` file

``` yaml
stages:
    - sync

include:
    - remote: https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/raw/development/git_push_mirror/.gitlab-ci.yml

Github (Push --mirror):
    variables:
        GIT_SYNC_URL: "https://$GITHUB_USERNAME_ROBOT:$GITHUB_TOKEN_ROBOT@github.com/NoFussComputing/gitlab-ci.git"
    extends:
        - .git_push_mirror

```

## CI/CD Variables required

| var name | Description |
|:----:|:----|
| GIT_SYNC_URL | this is the remote git repositories https clone address. <br>***Note:** if the remote repository requires authentication, you will need to build the url. like above.* |


## Job Workflow


## Artifacts

 - 

## License
To view the license for this folder and any sub-folders, refer [here](https://gitlab.com/nofusscomputing/projects/gitlab-ci)
