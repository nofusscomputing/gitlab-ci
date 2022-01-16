<div align="center" width="100%">

# No Fuss Computing - Gitlab-CI

<br>

![Project Status - Active](https://img.shields.io/badge/Project%20Status-Active-green?logo=gitlab&style=plastic) 

<br>

![Gitlab forks count](https://img.shields.io/badge/dynamic/json?label=Forks&query=%24.forks_count&url=https%3A%2F%2Fgitlab.com%2Fapi%2Fv4%2Fprojects%2F28543717%2F&color=ff782e&logo=gitlab&style=plastic) ![Gitlab stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.star_count&url=https%3A%2F%2Fgitlab.com%2Fapi%2Fv4%2Fprojects%2F28543717%2F&color=ff782e&logo=gitlab&style=plastic) [![Open Issues](https://img.shields.io/badge/dynamic/json?color=ff782e&logo=gitlab&style=plastic&label=Open%20Issues&query=%24.statistics.counts.opened&url=https%3A%2F%2Fgitlab.com%2Fapi%2Fv4%2Fprojects%2F28543717%2Fissues_statistics)](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues)

![GitHub forks](https://img.shields.io/github/forks/NoFussComputing/gitlab-ci?logo=github&style=plastic&color=000000&labell=Forks) ![GitHub stars](https://img.shields.io/github/stars/NoFussComputing/gitlab-ci?color=000000&logo=github&style=plastic) ![Github Watchers](https://img.shields.io/github/watchers/NoFussComputing/gitlab-ci?color=000000&label=Watchers&logo=github&style=plastic)

<br>

This project is hosted on [Gitlab](https://gitlab.com/nofusscomputing/projects/gitlab-ci) and has a read-only copy hosted on [Github](https://github.com/NoFussComputing/gitlab-ci).


----

**Stable Branch**

![Gitlab build status - stable](https://img.shields.io/badge/dynamic/json?color=ff782e&label=Build&query=0.status&url=https%3A%2F%2Fgitlab.com%2Fapi%2Fv4%2Fprojects%2F28543717%2Fpipelines%3Fref%3Dmaster&logo=gitlab&style=plastic) ![branch release version](https://img.shields.io/badge/dynamic/yaml?color=ff782e&logo=gitlab&style=plastic&label=Release&query=%24.commitizen.version&url=https%3A%2F%2Fgitlab.com%2Fnofusscomputing%2Fprojects%2Fgitlab-ci%2F-%2Fraw%2Fmaster%2F.cz.yaml) [![PyLint Score](https://img.shields.io/badge/dynamic/json?&style=plastic&logo=python&label=PyLint%20Score&query=%24.PyLintScore&url=https%3A%2F%2Fgitlab.com%2Fnofusscomputing%2Fprojects%2Fgitlab-ci%2F-%2Fjobs%2Fartifacts%2Fmaster%2Fraw%2Fartifacts%2Fvalidation%2FPyLint%2Fbadge_pylint.json%3Fjob%3DPyLint)](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/jobs/artifacts/master/file/artifacts/validation/tests/gl-code-quality-report.html?job=PyLint)

----

**Development Branch** 

![Gitlab build status - development](https://img.shields.io/badge/dynamic/json?color=ff782e&label=Build&query=0.status&url=https%3A%2F%2Fgitlab.com%2Fapi%2Fv4%2Fprojects%2F28543717%2Fpipelines%3Fref%3Ddevelopment&logo=gitlab&style=plastic) ![branch release version](https://img.shields.io/badge/dynamic/yaml?color=ff782e&logo=gitlab&style=plastic&label=Release&query=%24.commitizen.version&url=https%3A%2F%2Fgitlab.com%2Fnofusscomputing%2Fprojects%2Fgitlab-ci%2F-%2Fraw%2Fdevelopment%2F.cz.yaml) [![PyLint Score](https://img.shields.io/badge/dynamic/json?&style=plastic&logo=python&label=PyLint%20Score&query=%24.PyLintScore&url=https%3A%2F%2Fgitlab.com%2Fnofusscomputing%2Fprojects%2Fgitlab-ci%2F-%2Fjobs%2Fartifacts%2Fdevelopment%2Fraw%2Fartifacts%2Fvalidation%2FPyLint%2Fbadge_pylint.json%3Fjob%3DPyLint)](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/jobs/artifacts/development/file/artifacts/validation/tests/gl-code-quality-report.html?job=PyLint)

----

<br>

</div>

links:

- [Issues](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues)

- [Merge Requests (Pull Requests)](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests)


## Using this repository for your Gitlab CI/CD Jobs.
This repository has been designed as a central point for your repositories CI/CD jobs. By simply linking this repository to your repository and configuring, your CI/CD jobs will run as part of the build process, whilst keeping any CI/CD commits limited within your git history.

Each CI/CD job is contained within its own sub-folder. Each sub-folder has a readme specific to the job, which includes the details on how to implement, use etc.


### gitlab-ci layout

We use the following branches *(these jobs assume you do as well)*:
 - `master` - Considered as the stable branch
 - `development` considered as unstable

We also tag each branch to denote the version of release. We use our own repo to do the version increment automagically in line with [semantic versioning](https://semver.org/).



### CI Stages
The CI stages for these jobs are as follows, and in the order expected by the jobs:

- validation
    > validation of files, commits,  Merge Request titles, code quality, license checks.

- build
    > build any binaries or files that would be used in the later stages .

- prepare
    > any jobs that must run after build but before testing. for example a docker image build that includes artifacts from the build job

- test
    > unit, functional, integration and any other tests.

- release
    > git tagging and creating a gitlab release. Also includes adding build artifacts to gitlab registry.

- sync
    > repository synchronization, i.e. push mirror to github.

- publish
    > placement of build objects to external sources

### .gitlab-ci.yml example

example:
``` yaml
stages:
    - validation
    - build
    - prepare
    - test
    - release
    - sync
    - publish

variables:
    GIT_SUBMODULE_STRATEGY: recursive
    MY_PROJECT_ID: "{your_project_id}"

include:
  - project: nofusscomputing/projects/gitlab-ci
    ref: 68b6bc3bfacf0770e10d2e10a5c57952070d44fe
    file:
      - conventional_commits/.gitlab-ci.yml
      - gitlab_release/.gitlab-ci.yml
      - git_push_mirror/.gitlab-ci.yml
      - ansible/.gitlab-ci.yml

```
| :bulb: Tip |
|:----|
|  *Use a project import in your `.gitlab-ci.yml` file that is tied to a specific `ref`. for example a commit or tag. Also ensure that the `gitlab-ci` `git sub-module` and the `ref` as part of the includes matches.*  |


### Artifacts
Any artifacts by jobs will be created in folders named after the stage.

preference is placed on jobs to output JUnit.xml test reports. This is because they are visible in merge requests.


## Git Sub-Module setup

It is recommended that you set-up this repo as a git sub-module to your repo and that you configure it to a set commit/tag. This ensures that any change to `gitlab-ci` repo, does not effect your CI/CD jobs.

run the following commands:
``` bash
git submodule add -b {ref} https://gitlab.com/nofusscomputing/projects/gitlab-ci.git gitlab-ci
git submodule update --remote

```

|  :bulb: Tip  |
|:-----|
|  NOTE: `{ref}` should be replaced with the branch name, `master` is the stable branch and recommended. by default the sub-module will be created in folder `gitlab-ci`, it is recommended that you **don't** change this folder name.  
You can also substitute the gitlab url with the github url `https://github.com/NoFussComputing/gitlab-ci.git` for the submodule if you desire. this repo is auto-synced with github on each change to the repo.  |

After each `git submodule update --remote` you will have to commit the sub-module update to your repo. Suggested commands as follows:
``` bash
git add .gitmodules 

git add gitlab-ci

git commit -m "ci(gitlab-ci): updated to use version x

{your reason here or explain what is provided/changed}"
```
Then push the changes to your source.


## Contributing
All contributions for this project must conducted from [Gitlab](https://gitlab.com/nofusscomputing/projects/gitlab-ci).

For further details on contributing please refer to the [contribution guide](CONTRIBUTING.md).


## Other

This repo is release under this [license](LICENSE)

