---
title: Ansible Playbook
description: How to use No Fuss Computings gitlab-ci job for running Ansible Playbooks
date: 2023-05-29
template: project.html
about: https://gitlab.com/nofusscomputing/projects/gitlab-ci
---

This job enables you to run an Ansible playbook within the Gitlab CI/CD environment.


This job provides the following badge:

- None


## Dependencies

- **Mandatory** file `.nfc_automation.yaml` see [Documentation](../git_configuration/submodule/) for file details. 


## your .gitlab-ci.yml changes

To use this job add the following to your `.gitlab-ci.yml` file

``` yaml

stages:
    - chores

include:
  - project: nofusscomputing/projects/gitlab-ci
    ref: master
    file:
      - automation/.gitlab-ci-ansible.yaml

Ansible Job:
  extends: .ansible_playbook
  variables:
    ansible_playbook: 'git_configuration.yaml'
    ansible_tags: 'submodule'
    PIPELINE_RUN_TRIGGER: 'false'
    PIPELINE_RUN_SCHEDULE: 'false'

```

!!! Tip
    You can optionally override the stage by specifying the job you define


## CI/CD Variables required

| var name | Description |
|:----:|:----|
| ansible_playbook | ***Mandatory** The ansible playbook to run.* |
| ansible_tags | ***Optional** Tags to limit task scope* |
| PIPELINE_RUN_TRIGGER | ***Optional** if the job can be triggered by pipeline.* |
| PIPELINE_RUN_SCHEDULE | ***Optional** if the job can be triggered by schedule.* |

!!! Tip
    In addition to the variables above, you can also specify any additional Environment variables for use by Ansible. Refer to the [Ansible configuration documentation](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#common-options) for further details


## Job Workflow

This job will run the specified Ansible playbook using our [Ansible Execution Environment](../execution_environment) container. This container contains all of our playbooks and roles.


## Artifacts

- None


## gitlab-ci.yml definition

``` yaml title=".gitlab-ci.yml" linenums="1"

--8<-- "automation/.gitlab-ci-ansible.yaml"

```
