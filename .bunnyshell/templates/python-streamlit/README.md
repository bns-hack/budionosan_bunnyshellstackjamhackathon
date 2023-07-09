## Environment Overview

- **kind: Environment** are is user-defined group that brings together applications and all of the services and databases those applications require, running within a namespace.
- **name: firstbunnyshell** are is Bunnyshell environment name.
- **type: primary** are is manually-created environments and are not destroyed automatically. primary type must use Docker Compose (docker-compose.yml).
- **components** are is a Contains the definitions of the Applications / Services / Databases composing the Environment.
  - **kind: Application** are is used for git-stored code that needs to be built
  - **name: streamlit** are is application name.
  - **gitRepo** are is Github repository
  - **gitBranch** are is Github repository branch.
  - **gitApplicationPath** are is application path.
  - **dockerCompose** are is method used for create components, build use Dockerfile and setting port 8080
  - **hosts** are is URL that after deploy in Bunnyshell cluster.

## Template Overview

- **name: Python (Streamlit)** are is template name.
- **description** are is information about this template.
- **tags and icons** are is programming language or database such as Python, MySQL.
- **stack have package** are is define tags and icons with version.
- **discoverable** are is can this template is discover (true) or not (false).

## How to use it

## Any other information about this template
