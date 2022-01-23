# MKDocs Static Site Build
Build a MKDocs site from the config specified in `mkdocs.yml`. _Only runs if `mkdocs.yml` exists in the repository root directory._

This job provides the following badge:

- _None_

## Dependencies

- _None_

## your .gitlab-ci.yml changes
To use this job add the following to your `.gitlab-ci.yml` file

``` yaml
variables:
    VARNAME: "a var value"

stages:
    - build

include:
    - local: CI/build/.gitlab-ci.yml

MKDocs build:
  extends:
    - .MKDocs_Build

```

## CI/CD Variables required

| var name | Description |
|:----:|:----|
| MKDOCS_VERSION | **Optional** The MKDocs version to install. Defaults to `"==1.2.3"` |
| MKDOCS_BUILD_PATH | **Mandatory, if different from default** The path where MKDocs places the build files. Defaults to `build` |
| MKDOCS_INCLUDE_SOURCE | **Optional** Include the build source files in the artifacts. Default is Not set. Any value in this variable, will include the source files. |
| MKDOCS_SOURCE_PATH | **Optional, if source files are not to be included** Set to the path where mkdocs uses to build the static html. |

## Job Workflow

1. install mkdocs

    1. if file `requirements.txt` exists in the repository root directory, use this fill to also install additional dependencies.

    1. if no `requirements.txt` file exists, only install mkdocs.

1. run mkdocs to build the static pages

1. if variable `$MKDOCS_INCLUDE_SOURCE` is set, then copy `$MKDOCS_SOURCE_PATH` to the artifacts location.

1. copy directory `$MKDOCS_BUILD_PATH` to the artifacts location.


## Artifacts

- files in `"$CI_PROJECT_DIR/artifacts/$CI_JOB_STAGE/$CI_JOB_NAME"`

## License
To view the license for this folder and any sub-folders, refer [here](https://gitlab.com/nofusscomputing/projects/gitlab-ci)
