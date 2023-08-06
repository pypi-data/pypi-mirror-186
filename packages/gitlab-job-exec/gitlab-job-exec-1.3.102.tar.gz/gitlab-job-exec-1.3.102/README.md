## GitLab-CI Job Executor

This is a simple tool to parse and expand a `.gitlab-ci.yml` file to then execute GitLab-CI jobs in a docker container. 
It can be used either as a library or an command line executable.

#### Note
This tool was made to fit the needs of the authors first. Suggestions on what should be implemented next are welcomed.

#### Requirements
* Python 3

### Main features
* No need to commit before running a job since it mounts the working directory in the job's container.
* `extends` support for jobs templates.
* `include` support to import jobs and templates from other files. 
   Its behavior is as close as possible to how GitLab does it (https://docs.gitlab.com/ee/ci/yaml/README.html#include).
    * Supports `local`, `remote`, `project` and `template` includes.
* For `include:project` type includes:
    * The included file needs to be accessible by a HTTP GET request made using the URL pattern.
    * The pattern (which can be passed as an argument) has 2 variables possible to place in it: 'group' and 'project'
        * The values will correspond to the 'project' key of the include ({group}/{project})
        * This will follow defaults GitLab Pages URL with subgroup being part of {project}. 
    * Supported schemes are http://, https:// and file://
    * You can look at the setup used by our projects in https://gitlab.com/uncrns for a setup that is compatible 
      with `gitlab-job-exec`.
* Possibility for extra volumes to mount to the container running the job.
* Possibility to pass extra/overrides environment variables to the job.
* Configuration file for the command line interface.

### Command line interface
For the command line executable, we suggest using `gitlab-job-exec --help` to get detailed usage information.

### Library
```
class GitlabCI(filename, include_pattern, template_url)
```
The constructor will do the parsing and expansion of the `.gitlab-ci.yml` file.
* `filename`: the path to the `.gitlab-ci.yml` file to read and parse.
* `include_pattern`: The pattern to use for `include:project` file includes. 
   Defaults to `https://{group}.gitlab.io/{project}` which is the default URL for GitLab Pages.
* `template_url`: Base URL to use to fetch GitLab templates for `include:template`.

`GitlabCI.defaults`: Contains the details of the `default` job (if defined) to define global defaults.

`GitlabCI.include_pattern`: The include pattern passed to the constructor.

`GitlabCI.jobs`: Dictionary representing the different jobs available to execute, excluding jobs starting with `.` or global attributes 
not representing a complete job. Keys are the jobs' names and the values are instances of `gitlab_job_exec.GitlabJobs`.

`GitlabCI.stages`: The list of stages defined in the pipeline definition.

`GitlabCI.template_url`: The template base URL passed to the constructor.

`GitlabCI.variables`: Dictionary containing the global variables defined by the `variables` keyword in the pipeline definition.

```
class GitlabJob(name, parameters, defaults, global_variables)
```
* `name`: Name of the job.
* `parameters`: Other job parameters.
* `defaults`: Values in the `GitlabCI.defaults` dict.
* `global_variables`: Values in the `GitlabCI.variables` dict.

The keys `before_script`, `image`, `name`, `script`, `services`, `stage` and `variables` are available members with 
values equal to the job's definition.

`classmethod GitlabJobs.run(extra_variables, extra_volumes, pull_image, user)`:
Runs a job in a docker container and returns the exit code of the script.

* `extra_variables`: Environment variables to pass to the job. They will override existing values defined in the job.
* `extra_volumes`: Extra volumes to mount in the job's container. The format is the one used by 
`docker.DockerClient.containers.run()` for volumes.
* `pull_image`: Boolean indicating if the docker image should be pulled or not before starting the job.
* `user`: The user to use in the container. The format used is the same as the `docker.DockerClient.containers.run()`.

### Predefined GitLab environment variables
GitLab-CI is defining a lot of environment variables that can be used in a pipeline. We have implemented the following 
variables that will be passed to the jobs:

| Variable          | Value                                         |
|-------------------|-----------------------------------------------|
| CI_PIPELINE_ID    | Current date and time (ex:202102190830)       |
| CI_PIPELINE_IID   | Current date and time (ex:202102190830)       |
| CI_PIPELINE_SOURCE| "local"                                       |
| CI_PROJECT_DIR    | The current working directory                 |
| CI_PROJECT_NAME   | The base name of the current working directory|
| CI_PROJECT_NAMESPACE | The directory in which the cwd is located (dirname of ../). Prefixed with `${CI_PROJECT_ROOT_NAMESPACE}/` if defined |
| CI_PROJECT_PATH   | "local/${CI_PROJECT_NAME}"                    |
| CI_PROJECT_ROOT_NAMESPACE | Empty by defaults |
| CI_PROJECT_URL    | "https://localhost/${CI_PROJECT_NAME}"        |
| CI_REGISTRY       | "registry.gitlab.com"                         |
| CI_REGISTRY_IMAGE | "registry.gitlab.com/local/${CI_PROJECT_NAME}"|
| CI_SERVER_URL     | "https://gitlab.com"                          |

---
### Main unsupported features/current limitation
* `after_script` is not being read. (See #8)
* Override of Docker entrypoint and command for `services` containers.
* Health check on services/wait for services to be ready before starting the job.
* Have an array of `extends` in a job. (See #23)
* Envrionment variables regarding the namespace of a project only supports 1 level of dynamic value. (See #27)
