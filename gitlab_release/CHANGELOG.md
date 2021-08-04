# Changelog

2021-08-04 11:50:41 +0930 [287b4c9](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/287b4c954dddfaaf0a66af387676ea438cc80e61) - feat(gitlab_release): Include code refactor as part of the changelog  
2021-08-04 11:48:28 +0930 [eebe8e3](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/eebe8e30dcb11cd239f35fcb98216b2ae4d20ece) - docs(gitlab_release): Include custom command instructions  
2021-08-04 11:29:22 +0930 [7a69685](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/7a69685b53cbe5bd7341a176bf63fd17d36bc7f0) - refactor(gitlab_release): Dont conduct any release, git push or tag delete if the version was not bumped  
2021-08-04 11:16:44 +0930 [72e8b6c](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/72e8b6c84defdb903c5741e3469651987769713f) - refactor(gitlab_release): build gitlab commit url for changelog so that there is a weblink to the changes  
2021-08-04 01:33:47 +0000 [6d34977](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/6d349774269bcd7c6e406cfe72c78b99f246df7b) - build(version): bump version 0.0.1 → 0.1.0  
2021-08-04 11:00:19 +0930 [80ca361](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/80ca3618ee56d0f2a2c012416cb6206599a4f3f6) - fix(gitlab_release): A 'feat' commit must do a MINOR bump to version  
2021-08-04 10:46:25 +0930 [ed5be7f](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/ed5be7fd3c16e86d48e179a2cded53a38f79e1d9) - fix(gitlab_release): ci image is alpine, use '/bin/sh' and add the changlogs to git cache for commiting  
2021-08-04 10:44:57 +0930 [2035ed2](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/2035ed27af7fc1f3f5b2c42aa5874219fc5fe323) - refactor(gitlab_release): use 'git log' to get current commit hash  
2021-08-04 10:43:25 +0930 [7706085](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/7706085b09f3cd9b7c09f7f93b182fd425f6525a) - fix(gitlab_release): All tasks run as part of script including user custom script  
2021-08-04 10:40:46 +0930 [1446c28](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/1446c28ed2bfe2efec99bc2fc83b111717bcb2af) - fix(gitlab_release): Use a user token to access the git repo for pushing commits back  
2021-08-03 15:48:35 +0930 [6678a3d](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/6678a3dbab2763addc185e766cbaffbc074a6e98) - feat(git_release): Migrated from ansible-roles  
