#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import os
import git
import re

class Commits:


    def __init__(self):

        self._repository = git.Repo(os.getcwd())
        
        self._failed = []
        merge_base = self._repository.merge_base('development', 'changelog-footer-toggle')
        self._merge_base = str(merge_base[0])

        self.fetch_all()


    def fetch_all(self) -> bool: # get the commits and filter to only the current branch
        
        commits = list(self._repository.iter_commits(self._repository.active_branch))

        clean = True
        Branch_commits = []
        for remove in commits:

            if str(remove).lower() == self._merge_base.lower():
                
                clean = False

            if clean:

                Branch_commits.append(remove)

        self._commits = Branch_commits


    def fetch(self, sha1:str) -> str: # fetch a single git message

        for commit in self._commits:

            if str(commit).lower() == sha1.lower():

                return commit.message

        return ''


    def footer(self, git_message:str) -> list: # Get the last line of the commit message if has more than 2 lines

        if git_message.count("\n") > 2:

            footer_line = git_message.split("\n")
            footer_line = footer_line[(len(footer_line)-1)]

            footer = re.findall(r"([\!|\#][0-9]+)", str(git_message))

            if len(footer) > 0:
                return footer
            else:
                return False

        return None


    def junit(self) -> bool:
        junit = False

        junit_testsuites = '<testsuites id="Commits Messages Check" name="commit footer references" errors="{0}" tests="{1}" time="0">'.format(len(self._failed), len(self._commits))
        junit_testsuite = '<testsuite errors="{0}" name="commit footer references" tests="{1}">'.format(len(self._failed), len(self._commits))

        junit_testcase = ''
        for commit in self._failed:
            for key in commit:
                junit_testcase += '''
                <testcase classname="{0}" file="https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/blob/development/gitlab_release/README.md" line="0" name="No commit footer references found" time="0" timestamp="date">
                    <failure message="No References in the commit footer" type="validation">{1}</failure>
                    <system-out>
                        <![CDATA[ {1} ]]>
                    </system-out>
                    <system-err>
                    <![CDATA[ {1} ]]>
                </system-err>
            </testcase>'''.format(key, str(commit[key]))


        if junit_testcase == '':
           junit_testcase = '<testcase classname="nil" file="https://gitlab.com/nofusscomputing/projects/gitlab-ci/-/blob/development/gitlab_release/README.md" name="commit footer references"/>'

        junit_close = '</testsuite></testsuites>'
        print(str(junit_testsuites))
        print(str(junit_testsuite))
        print(str(junit_testcase))
        print(str(junit_close))
        

    def check(self) -> bool:
        check = True

        start_check = False

        for commit in self._commits:

            if commit.message.count('\n') < 3:
               continue
            footer = self.footer(commit.message)

            if footer is False:
                failed = {str(commit): str(commit.message)}
                self._failed.append(failed)
                continue

        self.junit()

        if len(self._failed) > 0:
            check = False

        return check


