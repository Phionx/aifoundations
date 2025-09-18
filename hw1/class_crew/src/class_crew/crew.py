from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import SerperDevTool

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class ClassCrew():
    """Curriculum Design Crew - Creates comprehensive course materials for both business and technical students"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    
    # Core Leadership Agent
    @agent
    def professor(self) -> Agent:
        return Agent(
            config=self.agents_config['professor'], # type: ignore[index]
            verbose=True
        )

    # Track-Specific Content Creators
    @agent
    def business_ta(self) -> Agent:
        return Agent(
            config=self.agents_config['business_ta'], # type: ignore[index]
            verbose=True
        )

    @agent
    def technical_ta(self) -> Agent:
        return Agent(
            config=self.agents_config['technical_ta'], # type: ignore[index]
            verbose=True
        )

    # Student Perspectives
    @agent
    def business_student(self) -> Agent:
        return Agent(
            config=self.agents_config['business_student'], # type: ignore[index]
            verbose=True
        )

    @agent
    def technical_student(self) -> Agent:
        return Agent(
            config=self.agents_config['technical_student'], # type: ignore[index]
            verbose=True
        )

    # Industry Expertise
    @agent
    def business_industry_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['business_industry_expert'], # type: ignore[index]
            verbose=True
        )

    @agent
    def technical_industry_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['technical_industry_expert'], # type: ignore[index]
            verbose=True
        )

    # Quality & Review
    @agent
    def critic(self) -> Agent:
        return Agent(
            config=self.agents_config['critic'], # type: ignore[index]
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    
    # Phase 1: Research Tasks (Independent)
    @task
    def business_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['business_research_task'], # type: ignore[index]
            output_file='course_materials/research/business_research_report.md',
            verbose=True,
            tools=[SerperDevTool()]

        )

    @task
    def technical_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['technical_research_task'], # type: ignore[index]
            output_file='course_materials/research/technical_research_report.md',
            verbose=True,
            tools=[SerperDevTool()]
        )

    # Phase 2: Curriculum Design Tasks
    @task
    def syllabus_creation_task(self) -> Task:
        return Task(
            config=self.tasks_config['syllabus_creation_task'], # type: ignore[index]
            output_file='course_materials/curriculum/course_syllabus.md'
        )

    @task
    def business_guest_lecture_task(self) -> Task:
        return Task(
            config=self.tasks_config['business_guest_lecture_task'], # type: ignore[index]
            output_file='course_materials/lectures/business_guest_lecture.md',
            verbose=True,
            tools=[SerperDevTool()]
        )

    @task
    def technical_guest_lecture_task(self) -> Task:
        return Task(
            config=self.tasks_config['technical_guest_lecture_task'], # type: ignore[index]
            output_file='course_materials/lectures/technical_guest_lecture.md',
            verbose=True,
            tools=[SerperDevTool()]
        )

    # Phase 3: Assignment Creation Tasks
    @task
    def business_assignments_task(self) -> Task:
        return Task(
            config=self.tasks_config['business_assignments_task'], # type: ignore[index]
            output_file='course_materials/assignments/business_assignments.md'
        )

    @task
    def technical_assignments_task(self) -> Task:
        return Task(
            config=self.tasks_config['technical_assignments_task'], # type: ignore[index]
            output_file='course_materials/assignments/technical_assignments.md'
        )

    # Phase 4: Student Simulation Tasks
    @task
    def business_student_simulation_task(self) -> Task:
        return Task(
            config=self.tasks_config['business_student_simulation_task'], # type: ignore[index]
            output_file='course_materials/feedback/business_student_simulation.md'
        )

    @task
    def technical_student_simulation_task(self) -> Task:
        return Task(
            config=self.tasks_config['technical_student_simulation_task'], # type: ignore[index]
            output_file='course_materials/feedback/technical_student_simulation.md'
        )

    # Phase 5: Final Project Tasks
    @task
    def business_use_case_task(self) -> Task:
        return Task(
            config=self.tasks_config['business_use_case_task'], # type: ignore[index]
            output_file='course_materials/projects/business_use_case.md',
            verbose=True,
            tools=[SerperDevTool()]
        )

    @task
    def technical_solution_task(self) -> Task:
        return Task(
            config=self.tasks_config['technical_solution_task'], # type: ignore[index]
            output_file='course_materials/projects/technical_solution.md',
            verbose=True,
            tools=[SerperDevTool()]
        )

    # Phase 6: Assessment & Review Tasks
    @task
    def final_project_grading_task(self) -> Task:
        return Task(
            config=self.tasks_config['final_project_grading_task'], # type: ignore[index]
            output_file='course_materials/assessment/final_project_grading.md'
        )

    @task
    def course_review_task(self) -> Task:
        return Task(
            config=self.tasks_config['course_review_task'], # type: ignore[index]
            output_file='course_materials/review/course_review_report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Curriculum Design Crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
