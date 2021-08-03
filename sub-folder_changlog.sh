#!/bin/bash





for D in *; do
    if [ -d "${D}" ]; then
        echo "[DEBUG] Creating changelog for sub-folder: ${D}"

        CHANGELOG_DATA=$(git log --pretty="format:%ci [%h](https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/commit/%H) - %s  " --follow -- "${D}")

        echo "# Changelog" > ${D}/CHANGELOG.md

        echo "" >> ${D}/CHANGELOG.md
        echo "$CHANGELOG_DATA" >> ${D}/CHANGELOG.md

    fi
done
