## Environment Overview

This template have **Bunnyshell** environment file - bunnyshell.yaml.
- **name: firstbunnyshell** are is **Bunnyshell** environment name.
- **components** are is a definition of the application in the Environment.
  - **kind: Application** are is used for git-stored code that needs to be built.
  - **name: streamlit** are is application name.
  - **gitRepo** are is Github repository.
  - **gitBranch** are is Github repository branch.
  - **gitApplicationPath** are is Github repository application path.
  - **dockerCompose** are is from docker-compose.yaml definition, build use Dockerfile and setting port 8080.
  - **hosts** are is URL that after deploy in **Bunnyshell** cluster.

## Template Overview

This template also have **Bunnyshell** template file - template.yaml.
- **name: Python (Streamlit)** are is **Bunnyshell** template name.
- **description** are is information about this template.
- **tags and icons** are is programming language or database such as Python, MySQL.
- **stack have package** are is define tags and icons with version.
- **discoverable** are is can this template is discover (true) or not (false).

## How to use it

1. Click "Templates" then click "Add custom templates". Fill the templates source name, choose your Github account, also your Github repository that already has `bunnyshell.yaml` and `template.yaml` file and fill the branch name.  Click "Add custom templates".
2. Click your template source name and click "Create environment". Fill the environment name and choose Project then click "Create environment".
3. Click "Deploy", choose "Bunnyshell cluster" for Kubernetes cluster and click "Deploy" then wait for several minutes. You also can click "Pipeline" to see progress. (You can see the screenshot in the project media)
4. After the pipeline is finished, you can click "URLs" and click your URL to a new tab. 
