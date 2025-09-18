# ClassCrew Crew

Welcome to the ClassCrew Crew project, powered by [crewAI](https://crewai.com). This multi-agent crew allows users to create a course on a topic of their choice. 



## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `SERPER_API_KEY` and `GEMINI_API_KEY` into the `.env` file**

- Modify `src/class_crew/config/agents.yaml` to define your agents
- Modify `src/class_crew/config/tasks.yaml` to define your tasks
- Modify `src/class_crew/crew.py` to add your own logic, tools and specific args
- Modify `src/class_crew/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the class_crew Crew, assembling the agents and assigning them tasks needed to create the course materials for a topic of your choice. The topic is entered via user prompt after the above command is run. 

## Understanding the Crew

The class_crew Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Acknowledgements

This crew was created by Shantanu R. Jha during the Fall 2025 iteration of the [AI Studio Course](https://aiforimpact.github.io/) at MIT, taught by Prof. Ramesh Raskar and team.

