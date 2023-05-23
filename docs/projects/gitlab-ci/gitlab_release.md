---
title: Gitlab Release / Commit Footer References
description: How to use No Fuss Computings gitlab-ci job for Gitlab Releases and commit footer messages
date: 2021-08-03
template: project.html
about: https://gitlab.com/nofusscomputing/projects/gitlab-ci
---


## User Manual

All commit messages must be in [conventional commit format](https://www.conventionalcommits.org/en/v1.0.0/) and have a footer with a gitlab reference. The reference **must** be either a merge request or a gitlab issue. (format i.e. `!1` or `#2` *using the correct reference number*).


### fixing commit messages (suggestion)

If only the last commit is the commit with an error just use `git commit --amend` and edit your commit message to be in the correct format and save. now push your changes.


You will require the following information if the commit message with the error is further down the commit tree:

- Commit message SHA1 of your first commit message to the branch `{original_commit}`

- Commit message SHA1 prior to your first commit `{source_commit}`

Run these commands once you have the information above.

``` bash

git format-patch {original_commit}..HEAD -o diff-patches

git reset {source_commit} --hard

```

Now, navigate to the `diff-patches` folder, open up the offending patch (commit) and edit the `subject` or message body as appropriate and save. Once all the edits have been done, re-apply the patches to your tree with:

``` bash

git am diff-patches/*.patch

```

Now push your changes upstream.

| :notebook_with_decorative_cover: Note  |
|:-----:|
|  *As you have changed the commit SHA1(s), when you next push your changes upstream, you must force push. `git push --force`*  |

| :octagonal_sign: **WARNING**  |
|:-----:|
|  *Ensure that all of your commits were exported prior to reseting the branch and when re-applying, that all of your commits were applied correctly*  |


## Gitlab Release - Developer Manual

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


### Dependencies

- None


### your .gitlab-ci.yml changes

To use this job add the following to your `.gitlab-ci.yml` file

CI Job `ci commit footer` is automatically set to run on all branches except `development` and `master`. This job checks the commits on the users branch that they contain a footer with gitlab references. i.e. `#1` for issue one or `!1` for merge request one.

``` yaml

stages:
    - validate
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


### CI/CD Variables required

| var name | Description |
|:----:|:----|
| GIT_COMMIT_TOKEN | *this must be a personal token that has write access to the repository* |
| CHANGELOG_FOOTER_REFERENCES |  ***Optional** If set to `False` the changelog will not output gitlab references for each entry of the changelog. If this variable is set globally, it will also prevent the creation of the CI job to validate a users commits as having gitlab references.*  |


### Job Workflow

This CI job's workflow is:

1. updates the changelog from the commits

1. commit the changelog to git

1. adds a `git tag` to the changelog commit.

1. pushes the change back to the repo

1. creates a git release from the `git tag`

| :octagonal_sign: **NOTE** |
|:----|
| *If the user has forked the branch, they must keep the development brnach synced with the main repo. If they **don't** the CI job 'commit footer refs' will fail as it will not be able to fetch the parent (`development`) hash of the branch.* |


### Artifacts

- `ci commit footer`
    > $CI_PROJECT_DIR/artifacts/$CI_JOB_STAGE/tests/$CI_JOB_NAME.junit.xml

- `Gitlab Release`
    > None


## Gitlab job Definition

When you include this definition the following makes up the job definition

``` yaml title=".gitlab-ci.yml" linenums="1"

--8<-- "gitlab_release/.gitlab-ci.yml"

```

!!! Note
    Docs Still under development
