## Unreleased

### Code Refactor

- **gitlab_release**: [cc3fabda](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/cc3fabdaa28f97c3e1600e4a0d95a05bb547e772) - Use Short commit SHA1 in main changelog link to gitlab

### Features

- **gitlab_release**: [3e8c3ce7](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/3e8c3ce7cd64a6e9110818d32c15c3602fefb76c) - On the development brnach, releases to be 'rc' to denote considered non-stable

## v0.2.1 (2021-08-04)

### Bug Fixes

- **gitlab_release**: [588698df](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/588698df2668853a97fe60901ab324310f34f279) - Correctly fetch the CI_PROJECT_URL for the environment

## v0.2.0 (2021-08-04)

### Code Refactor

- **gitlab_release**: [7a69685b](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/7a69685b53cbe5bd7341a176bf63fd17d36bc7f0) - Dont conduct any release, git push or tag delete if the version was not bumped
- **gitlab_release**: [72e8b6c8](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/72e8b6c84defdb903c5741e3469651987769713f) - build gitlab commit url for changelog so that there is a weblink to the changes

### Documentaton / Guides

- **gitlab_release**: [eebe8e30](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/eebe8e30dcb11cd239f35fcb98216b2ae4d20ece) - Include custom command instructions

### Features

- **gitlab_release**: [287b4c95](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/287b4c954dddfaaf0a66af387676ea438cc80e61) - Include code refactor as part of the changelog

## v0.1.0 (2021-08-04)

### Bug Fixes

- **gitlab_release**: [80ca3618](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/80ca3618ee56d0f2a2c012416cb6206599a4f3f6) - A 'feat' commit must do a MINOR bump to version
- **gitlab_release**: [ed5be7fd](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/ed5be7fd3c16e86d48e179a2cded53a38f79e1d9) - ci image is alpine, use '/bin/sh' and add the changlogs to git cache for commiting
- **gitlab_release**: [7706085b](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/7706085b09f3cd9b7c09f7f93b182fd425f6525a) - All tasks run as part of script including user custom script
- **gitlab_release**: [1446c28e](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/1446c28ed2bfe2efec99bc2fc83b111717bcb2af) - Use a user token to access the git repo for pushing commits back
- **ansible**: [2a3266fb](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/2a3266fb537e22dddf47708d0af101945027128f) - Ensure the default ci directory is populated

### Code Refactor

- **gitlab_release**: [2035ed27](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/2035ed27af7fc1f3f5b2c42aa5874219fc5fe323) - use 'git log' to get current commit hash

### Continious Integration

- **git_push_mirror**: [b5935056](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/b593505698b3d3359569f29f97c90e17e211f304) - Push repo to github NoFussComputing/gitlab-gi
- **conventional_commits**: [a2174104](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/a2174104d1eb05d329bacd44700bf81ac709dcac) - Add conventional commits job to check commits and MR titles

### Documentaton / Guides

- **README.md**: [247264e3](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/247264e36bc0b6c86d2f06f8dae09ff7447fc156) - Added readme for the repo
- **git_push_mirror**: [7ffb2041](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/7ffb20418cfa8e6fa20cca60e42155171961d1ce) - Update workflow and typos

### Features

- **job_changelog**: [1ecd857c](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/1ecd857c0bf8ef009ad2482ad1d52604adadc0ed) - Create a changelog per job folder
- **git_release**: [6678a3db](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/6678a3dbab2763addc185e766cbaffbc074a6e98) - Migrated from ansible-roles
- **ansible**: [2413daef](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/2413daefb1e7e5a9e7a3cbb2d8cff2214f4a98ae) - Added ansible validation job for linting
- **git_push_mirror**: [9b28ae59](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/9b28ae5952adfb3d61e660814074ad3c7b42ff61) - Added a job that syncs to a remote git repo
- **conventional_commits**: [392a200f](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/392a200fd469c4161dbab5f2b59031a7a64f20a2) - Added conventional commit job

## v0.0.1 (2021-08-03)
