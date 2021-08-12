# Conventional Commits User Manual
Commitizen is used to validate the format of commit messages. we use [Conventional Commit Messages](https://www.conventionalcommits.org/en/v1.0.0/) format for our validation jobs.

This repository may have two CI jobs to do with commitizen:
- **MR Title** *Checks the Merge Request Title*
- **Commit Messages** *Checks all commit messages*

These CI Jobs output a test report that can be viewed inside of the merge request and contain the error(s), if any.

To fix an error please refer to the titled sections below.

## MR Title
Ensure that the merge request title is in the [conventional message](https://www.conventionalcommits.org/en/v1.0.0/) format. NOTE: the title is case sensitive.


## Commit Messages
All commit messages that form part of your merge request must be in [conventional message](https://www.conventionalcommits.org/en/v1.0.0/) format. 

To fix them go back and edit your commit messages.


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


# Conventional Commits Admin Manual Manual
This job checks commit messages on a branch and the merge request title for validity against the [conventional commit format](https://www.conventionalcommits.org/en/v1.0.0/)

This job provides the following badge:

- None

## Dependencies

- None

## your .gitlab-ci.yml changes
To use this job add the following to your `.gitlab-ci.yml` file

``` yaml
variables:
    GIT_SUBMODULE_STRATEGY: recursive
    MY_PROJECT_ID: "{yourproject id number}"

stages:
    - validation

include:
    - remote: https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/raw/development/conventional_commits/.gitlab-ci.yml
```

## CI/CD Variables required

| var name | Description |
|:----:|:----|
| MR_ACCESS_TOKEN | *only required if you are accessing a private repository.* <br>This token is a user access token that as a minimum requires read-only access to the api to fetch the projects merg requests. |


## Job Workflow


## Artifacts


## License
To view the license for this folder and any sub-folders, refer [here](https://gitlab.com/nofusscomputing/projects/gitlab-ci)
