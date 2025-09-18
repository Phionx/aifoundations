# Curriculum Design Crew

Welcome to the Curriculum Design Crew project, powered by [crewAI](https://crewai.com). This multi-agent crew creates comprehensive course materials for any topic, designed to serve both business and technical students with industry-relevant content.

## Overview

The Curriculum Design Crew consists of 8 specialized AI agents that collaborate to create a complete educational curriculum:

- **Professor**: Leads course design and creates the comprehensive syllabus
- **Business TA**: Develops business-focused assignments and materials
- **Technical TA**: Creates hands-on technical assignments and projects
- **Business Student**: Provides student perspective and feedback on business track
- **Technical Student**: Provides student perspective and feedback on technical track
- **Business Industry Expert**: Contributes real-world business insights and guest lectures
- **Technical Industry Expert**: Provides industry technical expertise and best practices
- **Critic**: Reviews all materials and provides improvement recommendations

## What Gets Created

The crew generates comprehensive course materials organized in structured directories:

- **Research Reports**: Business and technical research on the chosen topic
- **Course Syllabus**: Complete fall semester curriculum with learning objectives
- **Guest Lectures**: Industry expert materials for both business and technical tracks
- **Weekly Assignments**: Progressive assignments for both student tracks
- **Student Feedback**: Simulation reports from both student perspectives
- **Final Project**: Business use case and technical solution specifications
- **Assessment**: Grading rubrics and evaluation criteria
- **Course Review**: Comprehensive analysis and improvement recommendations

## Example Output

Check out the `generated_courses/` folder to see example course materials created by this crew, including a complete curriculum for "Quantum Error Correction" that demonstrates the comprehensive materials generated.

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

This command initializes the Curriculum Design Crew, assembling the agents and assigning them tasks needed to create comprehensive course materials for a topic of your choice. The topic is entered via user prompt after the above command is run.

## Understanding the Crew

The Curriculum Design Crew follows a structured workflow across 6 phases:

1. **Research Phase**: Business and technical research on the topic
2. **Curriculum Design**: Syllabus creation and guest lecture development
3. **Assignment Creation**: Weekly assignments for both tracks
4. **Student Simulation**: Feedback from both student perspectives
5. **Final Project**: Business use case and technical solution design
6. **Assessment & Review**: Grading criteria and comprehensive course review

Each agent has specialized expertise and works collaboratively to ensure the curriculum serves both business and technical students effectively while maintaining industry relevance.

## Reflections

This project successfully demonstrated the power of multi-agent collaboration in educational content creation. The structured workflow with 8 specialized agents proved effective at generating comprehensive, industry-relevant curriculum materials that serve both business and technical students. The dependency-based task system ensured each phase built logically on previous work, while the organized output structure made the generated materials easy to navigate and use. However, the sequential process could be slow for large topics, and some agents occasionally produced redundant content. The most valuable learning was how different agent perspectives (student, industry expert, critic) created a more robust curriculum than any single agent could produce alone. The example "Quantum Error Correction" course in the generated_courses folder showcases the crew's ability to handle complex, specialized topics effectively.

## Acknowledgements

This crew was created by Shantanu R. Jha during the Fall 2025 iteration of the [AI Studio Course](https://aiforimpact.github.io/) at MIT, taught by Prof. Ramesh Raskar and team.


---

Name: Shantanu R. Jha
Track: Technical