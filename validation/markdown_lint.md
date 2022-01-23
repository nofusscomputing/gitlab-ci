# Markdown File Linting
Summary of job here

This job provides the following badge:

- _None_

## Dependencies

- _None_

## your .gitlab-ci.yml changes
To use this job add the following to your `.gitlab-ci.yml` file

``` yaml

stages:
    - validation

include:
    - local: CI/validation/.gitlab-ci.yml

Markdown:
  extends:
    - .Lint_Markdown

```

## CI/CD Variables required

| var name | Description |
|:----:|:----|
| MDLINT_PATH | **Optional** specifies the path to lint. defaults to `"**/*.md"` |
| MDLINT_EXCLUDE_PATHS | **optional** Specifies the paths to exclude from linting. Defaults to `"!gitlab-ci"` |

## Job Workflow

1. installs the required job dependencies

1. Lints any markdow file found in `$MDLINT_PATH`, excluding paths `$MDLINT_EXCLUDE_PATHS`

## Artifacts

- JUnit test report located at `$CI_PROJECT_DIR/artifacts/$CI_JOB_STAGE/tests/*.junit.xml`

## License
To view the license for this folder and any sub-folders, refer [here](https://gitlab.com/nofusscomputing/projects/gitlab-ci)
