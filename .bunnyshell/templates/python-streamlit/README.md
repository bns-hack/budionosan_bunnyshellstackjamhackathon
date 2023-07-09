## Environment Overview

This template have **Bunnyshell** environment file - bunnyshell.yaml. This nvironment Template is a working Magento 2.4 instance
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


## Any other information about this template

Because this template use Google Cloud, you must 
