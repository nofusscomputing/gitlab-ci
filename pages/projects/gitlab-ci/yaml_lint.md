---
title: YAML Linting
description: How to use No Fuss Computings gitlab-ci job for YAML Linting
date: 2021-08-11
template: manual.html
about: https://gitlab.com/nofusscomputing/projects/gitlab-ci
---

This job does yaml linting when any commit is pushed to any branch.


This job provides the following badge:

- None

## Dependencies

- None

## your .gitlab-ci.yml changes
To use this job add the following to your `.gitlab-ci.yml` file

``` yaml
stages:
    - validation

include:
    - remote: https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/raw/master/yaml_lint/.gitlab-ci.yml

Yaml Lint (python 3.6):
    variables:
        YAML_LINT_PATH: "roles/"
        YAML_LINT_CONFIG: ".yamllint.yaml"
    extends:
        - .yaml_linter_defaults
    image: python:3.6-slim
```
> You can use any python version you wish.

## CI/CD Variables required

| var name | Description |
|:----:|:----|
| YAML_LINT_PATH | *The path you wish the linter to search for yaml files* |
| YAML_LINT_CONFOG | *The path you have stored the yaml config file in* |


## Job Workflow

 - This job will lint any yaml file in the specified directory using the specified rules.

## Artifacts

 - `$CI_PROJECT_DIR/artifacts` - Root artifact directory
 - `$CI_PROJECT_DIR/artifacts/$CI_JOB_STAGE/tests/$PYTHON_VERSION-yaml-lint.junit.xml` - JUnit Test report
 - `$CI_PROJECT_DIR/artifacts/$CI_JOB_STAGE/$CI_JOB_NAME/$PYTHON_VERSION-yaml-lint.log` - Linter log

## License
To view the license for this folder and any sub-folders, refer [here](https://gitlab.com/nofusscomputing/projects/gitlab-ci)
