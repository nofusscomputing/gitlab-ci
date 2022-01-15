## v0.4.0 (2022-01-15)

### Bug Fixes

- **commit.py**: [99bdc2a0](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/99bdc2a0929d4e7036e50e8ce22ce9b0f90f0736) - fix typo that caused exception [ [#6](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/6) [!12](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/12) ]
- **conventional_commits**: [d03d9fef](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/d03d9fefc916dd6730d9ffa778c11d48d621318e) - fetch all branches prior to check for parent branch [ [#6](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/6) [!12](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/12) ]
- **ci**: [d5782d95](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/d5782d95e825d406ea805c425cfefd6752fb6e35) - added variable 'GIT_SUBMODULE_STRATEGY' to be 'recursive' [ [#10](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/10) [!12](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/12) ]
- **conventional_commits**: [42ad02ee](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/42ad02ee5db65c3c6c33ad14fe0371c9916897bf) - use git show-branch to find origin branch [ [#6](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/6) [!11](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/11) ]

### Features

- **commit.py**: [e5531fc7](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/e5531fc77b5bdb1ccc0741e388df2d8d25ba6ade) - throw an error if no token was supplied. i.e. empty variable. [ [#11](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/11) [!12](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/12) ]
- **commit.py**: [6b7ad95f](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/6b7ad95fc0ccccf79ff645bad3f86660f5096a4e) - confirm a merge request was found, if not output 'ci: No Merge Request found' [ [#11](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/11) [!12](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/12) ]
- **commit.py**: [c543c47a](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/c543c47af8c7c386ae57f5a7a50904d396758c3a) - try to us `CI_JOB_TOKEN` before the specified token, if any. [ [#11](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/11) [!12](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/12) ]
- **commit.py**: [b01550e0](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/b01550e09f273edc8a57f4ad4b41ee2d67705d41) - removed ability to fetch first commit or target branch [ [#6](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/6) [#6](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/6) [!12](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/12) ]

## v0.3.1 (2022-01-11)

### Bug Fixes

- **pylint**: [4b6cc317](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/4b6cc3176fc4acc3b7dbb954162802af9cbb4c68) - install the required packages for files being checked [ [#7](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/7) ]
- **pylint**: [936299ae](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/936299aefc6eadf9cbfec3152b352b321969cfab) - fix bug introduced in code quality commit [ [#7](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/7) ]
- **commit_footer**: [2ac22c0e](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/2ac22c0e914016a8944ff9b94640f3e87f409069) - fix bug introduced in code quality commit [ [#7](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/7) ]

### Documentaton / Guides

- **readme**: [8ac36de8](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/8ac36de8e0f113ce17d54dfce1345a0adab41bc8) - Updated with an example .gitlab-ci.yml example [ [#2](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/2) [!10](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/10) ]

## v0.3.0 (2021-08-12)

### BREAKING CHANGE

- !2

### Bug Fixes

- **commit_message**: [3360a15f](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/3360a15fde12682edfd9044d2541dc819615b838) - fixed commit message check if there is only one commit to the branch [ [!7](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/7) ]
- **commit_footer_refs**: [63af1efb](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/63af1efb4fd92a9f8755f766728a18d8f390b805) - Use the current git branch for comparison. [ [!5](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/5) [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]
- **gitlab_release**: [f76cabee](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/f76cabeeb04b028a231dc1c232862db5fcad4345) - Adjust release workflow [ [!2](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/2) ]

### Code Refactor

- **gitlab_release**: [eb0bf4c1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/eb0bf4c1740dbd7a47ceb031c0d1c854899a1e40) - file link to be in local repository for helping fix commit footer ref check failures [ [#4](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/4) ]
- **gitlab_release**: [81776223](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/81776223c5cb392c12c7ca63488a1df10290e9d1) - use a name for failed test to denote the issue [ [#4](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/4) ]

### Continious Integration

- **gitlab_release**: [7cb676eb](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/7cb676eb98a7de30d47a6b49a87067116684cfd2) - Add a validation job to check if commit messages contain a gitlab reference in the footer [ [#4](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/4) ]

### Documentaton / Guides

- **readme**: [0653766c](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/0653766c935cb117082bfe1481ae83e4a1b2bb5c) - Updated badges and intro [ [!5](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/5) ]
- **gitlab_templates**: [9f7a24c1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/9f7a24c1ebc0bdb5a153977dcb1c53d7ec2fb140) - added issue and merge request templates [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]
- **template**: [da8eb5c3](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/da8eb5c3381379f6e405c3ebe14d9a883c52f41a) - added template readme for CI job folders [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]
- **readme**: [ace7a034](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/ace7a03456861d59e2f904405f45409c53e831ab) - explain sync and using github to link gitlab-ci [ [!5](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/5) [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]
- **readme**: [8790917e](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/8790917e7d959aa7b8305912bb443ba6b72200c6) - explain repo layout and versioning [ [!5](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/5) ]
- **readme**: [19900945](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/19900945e763249b6ef7a9e2e2cbcf11748b1eea) - added how to update gitlab-ci [ [!5](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/5) ]
- **readme**: [8a988ebf](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/8a988ebf09015211f8f6566acc0ba71c1f00bee1) - Added how to use this repository [ [!5](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/5) ]
- **gitlab_release**: [dc13d4f2](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/dc13d4f2841038c085dcf29dfb0b0c5d2f00f099) - Added user docs to fix errors from ci job 'commit footer refs' [ [#3](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/3) [#4](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/4) ]
- **changelog**: [35edb7cf](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/35edb7cfc59e2d147bdb5cb5d03710ec747073ae) - Updated changelog to new layout [ [!3](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/3) [#3](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/3) ]
- **gitlab_release**: [5f273ce2](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/5f273ce23a331eaf11623207ec4aba8b856c14f0) - Updated docs with new instructions on version incrementing [ [!2](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/2) ]

### Features

- **python_linting**: [d6105624](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/d61056243804728e059b99fce1644a8cc37230bb) - added ci job, python linting, code quality and scoring [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]
- **yaml_lint**: [d20a56fa](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/d20a56fa0ca492e3fc2ad7c548fc891cc8ffc8ec) - Added job yaml lint for checking yaml files [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]
- **gitlab_release**: [22136f7d](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/22136f7dd22b9487d362a7ed63ca1b76e52b9cc7) - Toggle var added to enable switching changelog references. [ [#3](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/3) ]
- **gitlab_release**: [756b9406](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/756b9406dde8cf0bf0030ac72855a054ece3a883) - be able to toggle commit footer check job [ [#4](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/4) ]
- **gitlab_release**: [11e15661](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/11e156619d0d820e534897bafd5f39e6f9defcbf) - python module to check if a commit message has gitlab references in the footer [ [#4](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/4) ]
- **gitlab_release**: [8699c412](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/8699c41219d70e6f41f42dc7f2c1bcf542b3f723) - Add commit footer to changelog [ [!1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/merge_requests/1) [#3](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/3) ]

## v0.3.0rc1 (2021-08-04)

### Documentaton / Guides

- **changelog**: [cb78ab82](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/cb78ab82182a9edcd568a8b4c315490041539149) - regenerated so that all entries use the new url format [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]

## v0.3.0rc0 (2021-08-04)

### Code Refactor

- **gitlab_release**: [cc3fabda](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/cc3fabdaa28f97c3e1600e4a0d95a05bb547e772) - Use Short commit SHA1 in main changelog link to gitlab [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]

### Features

- **gitlab_release**: [3e8c3ce7](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/3e8c3ce7cd64a6e9110818d32c15c3602fefb76c) - On the development brnach, releases to be 'rc' to denote considered non-stable [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]

## v0.2.1 (2021-08-04)

### Bug Fixes

- **gitlab_release**: [588698df](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/588698df2668853a97fe60901ab324310f34f279) - Correctly fetch the CI_PROJECT_URL for the environment

## v0.2.0 (2021-08-04)

### Code Refactor

- **gitlab_release**: [7a69685b](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/7a69685b53cbe5bd7341a176bf63fd17d36bc7f0) - Dont conduct any release, git push or tag delete if the version was not bumped
- **gitlab_release**: [72e8b6c8](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/72e8b6c84defdb903c5741e3469651987769713f) - build gitlab commit url for changelog so that there is a weblink to the changes [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]

### Documentaton / Guides

- **gitlab_release**: [eebe8e30](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/eebe8e30dcb11cd239f35fcb98216b2ae4d20ece) - Include custom command instructions [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]

### Features

- **gitlab_release**: [287b4c95](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/287b4c954dddfaaf0a66af387676ea438cc80e61) - Include code refactor as part of the changelog [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]

## v0.1.0 (2021-08-04)

### Bug Fixes

- **gitlab_release**: [80ca3618](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/80ca3618ee56d0f2a2c012416cb6206599a4f3f6) - A 'feat' commit must do a MINOR bump to version [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]
- **gitlab_release**: [ed5be7fd](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/ed5be7fd3c16e86d48e179a2cded53a38f79e1d9) - ci image is alpine, use '/bin/sh' and add the changlogs to git cache for commiting [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]
- **gitlab_release**: [7706085b](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/7706085b09f3cd9b7c09f7f93b182fd425f6525a) - All tasks run as part of script including user custom script [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]
- **gitlab_release**: [1446c28e](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/1446c28ed2bfe2efec99bc2fc83b111717bcb2af) - Use a user token to access the git repo for pushing commits back [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]
- **ansible**: [2a3266fb](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/2a3266fb537e22dddf47708d0af101945027128f) - Ensure the default ci directory is populated [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]

### Code Refactor

- **gitlab_release**: [2035ed27](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/2035ed27af7fc1f3f5b2c42aa5874219fc5fe323) - use 'git log' to get current commit hash [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]

### Continious Integration

- **git_push_mirror**: [b5935056](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/b593505698b3d3359569f29f97c90e17e211f304) - Push repo to github NoFussComputing/gitlab-gi [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]
- **conventional_commits**: [a2174104](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/a2174104d1eb05d329bacd44700bf81ac709dcac) - Add conventional commits job to check commits and MR titles [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]

### Documentaton / Guides

- **README.md**: [247264e3](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/247264e36bc0b6c86d2f06f8dae09ff7447fc156) - Added readme for the repo [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]
- **git_push_mirror**: [7ffb2041](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/7ffb20418cfa8e6fa20cca60e42155171961d1ce) - Update workflow and typos [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]

### Features

- **job_changelog**: [1ecd857c](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/1ecd857c0bf8ef009ad2482ad1d52604adadc0ed) - Create a changelog per job folder [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]
- **git_release**: [6678a3db](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/6678a3dbab2763addc185e766cbaffbc074a6e98) - Migrated from ansible-roles [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]
- **ansible**: [2413daef](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/2413daefb1e7e5a9e7a3cbb2d8cff2214f4a98ae) - Added ansible validation job for linting [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]
- **git_push_mirror**: [9b28ae59](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/9b28ae5952adfb3d61e660814074ad3c7b42ff61) - Added a job that syncs to a remote git repo [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]
- **conventional_commits**: [392a200f](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/392a200fd469c4161dbab5f2b59031a7a64f20a2) - Added conventional commit job [ [#1](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/issues/1) ]

## v0.0.1 (2021-08-03)
