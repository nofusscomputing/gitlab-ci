---
title: Automatic Gitlab CI/CD jobs Template
description: How to use No Fuss Computings gitlab-ci template for auto creation of CI/CD joobs.
date: 2023-05-22
template: project.html
about: https://gitlab.com/nofusscomputing/projects/gitlab-ci
---

This template is designed to autodetect which jobs should be created. By including it within your project, the jobs will be automagically created for the pipeline.


## Docs ToDo

- document variables `PIPELINE_RUN_TRIGGER: 'false'` and `PIPELINE_RUN_SCHEDULE: 'false'` as being used as a gate to enable the jobs to run by the specified source.


!!! Note
    Docs Still under development


# GitLab CI/CD YAML Template Documentation

This documentation provides an overview and explanation of the GitLab CI/CD YAML template. The template is designed to run Ansible jobs using the `nofusscomputing/ansible-ee:dev` Docker image.


## Job: `.ansible_playbook`

This job runs an Ansible playbook using the `nofusscomputing/ansible-ee:dev` Docker image.


### Stage: Chores

This job is responsible for executing an Ansible playbook. It can be customized by setting the following variables:


#### Variables

- `ansible_inventory`: The Ansible inventory file.

- `ansible_playbook`: The name of the Ansible playbook file.

- `ansible_tags`: The tags to be applied during playbook execution.


### Rules

- Rule 1: If the `NFC_AUTO_JOBS` variable is set to `"false"`, the job will never run.

- Rule 2: If the pipeline is triggered by a schedule and `PIPELINE_RUN_SCHEDULE` is set to `"true"`, the job will run only if the `.nfc_automation.yaml` file exists.

- Rule 3: If the pipeline is triggered by an API call, another pipeline, a trigger, or a parent pipeline, and `PIPELINE_RUN_TRIGGER` is set to `"true"`, the job will run only if the `.nfc_automation.yaml` file exists.

- Rule 4: If the pipeline is triggered by a push to the `development` branch, the job will run only if the `.nfc_automation.yaml` file exists.

- Rule 5: This rule prevents the job from running under any circumstances.


## Job: `.ansible_playbook_git_submodule`

This job extends the `.ansible_playbook` job and is specifically used for running the `git_configuration.yaml` playbook with the `submodule` tags.


### Stage: Chores

This job is responsible for executing the `git_configuration.yaml` playbook with the `submodule` tags.


#### Variables

- `ansible_playbook`: The name of the Ansible playbook file (`git_configuration.yaml`).

- `ansible_tags`: The tags to be applied during playbook execution (`submodule`).

### Rules

- Rule 1: If the `NFC_AUTO_JOBS` variable is set to `"false"`, the job will never run.

- Rule 2: If the pipeline is triggered by a schedule and `PIPELINE_RUN_SCHEDULE` is set to `"true"`, the job will run only if the `.nfc_automation.yaml` file exists.

- Rule 3: If the pipeline is triggered by an API call, another pipeline, a trigger, or a parent pipeline, and `PIPELINE_RUN_TRIGGER` is set to `"true"`, the job will run only if the `.nfc_automation.yaml` file exists.

- Rule 4: If the pipeline is triggered by a push to the `development` branch, the job will run only if the `.nfc_automation.yaml` file exists.

- Rule 5: This rule prevents the job from running under any circumstances.


## Job: `.submodule_update_trigger`

This job triggers a pipeline in another project.


### Stage: Publish

This job is responsible for triggering a pipeline in another project.


#### Variables

- `PIPELINE_RUN_TRIGGER`: The flag to indicate if the triggered pipeline should run (`true`).


### Rules

- Rule 1: If the pipeline is triggered by a push to the `master` or `development` branch, and there is no associated tag, the job will run on successful completion.

- Rule 2: This rule prevents the job from running under any other circumstances.


## gitlab-ci.yml definition

``` yaml title=".gitlab-ci.yml" linenums="1"

--8<-- "template/automagic.gitlab-ci.yaml"

```
