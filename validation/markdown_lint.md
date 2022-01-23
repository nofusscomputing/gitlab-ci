# Markdown File Linting
This job lints markdown files as part of the validation CI stage. It is designated to run on all branches. If any errors are found, the generated JUnit test report will let you know what errors were found.

This job provides the following badge:

- _None_

## Dependencies

- **Optional** file `.markdownlint.json` in repository root with any rules you wish to specify

- **Mandatory** file `.markdownlint-cli2.jsonc` in the repository root so that a Junit test report is created.

## your .gitlab-ci.yml changes
To use this job add the following to your `.gitlab-ci.yml` file

``` yaml

stages:
    - validation

include:
    - local: CI/validation/.gitlab-ci.yml

Markdown Linting:
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
