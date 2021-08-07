# Gitlab Release
This job bumps the version, updates the changelog, creates a git tag and creates a gitlab release. The git tag and release title use [semantic versioning](https://semver.org/). for this job to function correctly a `.cz.yaml` is required in the root of the repository. this file contains the [commitizen](https://github.com/commitizen-tools/commitizen) config and the version details. 

This job has the following workflow:

- `master` Branch
     > Automatically increment the version

- `development` Branch
     > Manual CI job made available to increment the version. (release-candidate increment only)

|  :octagonal_sign: Danger  |
|:----|
|  *If prior to merging to the master branch you do a version increment, and there are no commits prior to merging. the job will not increment the version and the job will fail. it is recommended that you only do a version increment on the `development` branch if you are going to commit further changes to the `development` branch*  |


This job provides the following badge:

- None

## Dependencies

- None

## your .gitlab-ci.yml changes
To use this job add the following to your `.gitlab-ci.yml` file

``` yaml
stages:
    - release

include:
    - remote: https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/raw/development/gitlab_release/.gitlab-ci.yml

Gitlab Release:
    variables:
        MY_COMMAND: "{your command here}"
    extends:
        - .gitlab_release
```
> if you wish to run any commands you can add them to variable `MY_COMMAND`. The custom command will run under shell `/bin/sh`. This command is set to run before the version bump commit is conducted so any changes you wish to add as part of the version bump, you can do here as long as you `git add {changed file name}`.


## CI/CD Variables required

| var name | Description |
|:----:|:----|
| GIT_COMMIT_TOKEN | *this must be a personal token that has write access to the repository* |


## Job Workflow

This CI job's workflow is:

1. updates the changelog from the commits
1. commit the changelog to git
1. adds a `git tag` to the changelog commit. 
1. pushes the change back to the repo
1. creates a git release from the `git tag`


## Artifacts

 - None

## License
To view the license for this folder and any sub-folders, refer [here](https://gitlab.com/nofusscomputing/projects/gitlab-ci)

