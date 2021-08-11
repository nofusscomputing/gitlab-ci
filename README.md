# No Fuss Computing - Gitlab-CI

[![Gitlab build status - stable](https://img.shields.io/badge/dynamic/json?color=ff782e&label=Build%20%5B%20Stable%20%5D&query=0.status&url=https%3A%2F%2Fgitlab.com%2Fapi%2Fv4%2Fprojects%2F28543717%2Fpipelines%3Fref%3Dmaster&logo=gitlab&style=plastic)](https://gitlab.com/nofusscomputing/projects/gitlab-ci)


[![Gitlab build status - development](https://img.shields.io/badge/dynamic/json?color=ff782e&label=Build%20[%20Development%20]&query=0.status&url=https%3A%2F%2Fgitlab.com%2Fapi%2Fv4%2Fprojects%2F28543717%2Fpipelines%3Fref%3Ddevelopment&logo=gitlab&style=plastic)](https://gitlab.com/nofusscomputing/projects/gitlab-ci)


This repository is hosted on [gitlab.com](https://gitlab.com/nofusscomputing/projects/gitlab-ci) and has a read-only copy hosted on [github.com](https://github.com/NoFussComputing/gitlab-ci).

links:

- [![Open Issues](https://img.shields.io/badge/dynamic/json?color=ff782e&logo=gitlab&style=plastic&label=Open%20Issues&query=%24.statistics.counts.opened&url=https%3A%2F%2Fgitlab.com%2Fapi%2Fv4%2Fprojects%2F28543717%2Fissues_statistics) Issues](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues)

- [Merge Requests (Pull Requests)](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests)


## Using this repository for your Gitlab CI/CD Jobs.
This repository has been designed as a central point for your repositories CI/CD jobs. By simply linking this repository to your repository and configuring, your CI/CD jobs will run as part of the build process, whilst keeping any CI/CD commits limited within your git history.

Each CI/CD job is contained within its own sub-folder. Each sub-folder has a readme specific to the job, which includes the details on how to implement, use etc.



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

### Artifacts
Any artifacts by jobs will be created in folders named after the stage.

preference is placed on jobs to output JUnit.xml test reports. This is because they are visible in merge requests.


It is recommended that you set-up this repo as a git sub-module to your repo and that you configure it to a set commit/tag. This ensures that any change to `gitlab-ci` repo, does not effect your CI/CD jobs.

run the following commands:
``` bash
git submodule add -b {ref} https://gitlab.com/nofusscomputing/projects/gitlab-ci.git gitlab-ci
git submodule update --remote

```

|  :bulb: Tip  |
|:-----|
|  NOTE: `{ref}` should be replaced with the branch name, `master` is the stable branch and recommended. by default the sub-module will be created in folder `gitlab-ci`, it is recommended that you **don't** change this folder name.  |


## Contributing
All contributions for this project must conducted from [Gitlab](https://gitlab.com/nofusscomputing/projects/gitlab-ci).

For further details on contributing please refer to the [contribution guide](CONTRIBUTING.md).


## Other

This repo is release under this [license](LICENSE)

