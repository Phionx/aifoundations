#!/usr/bin/env python3
"""
MIT AI Studio - Crew AI Example Agent
A simple example of a Crew AI agent system that represents an AI Studio student.

This example demonstrates:
- Creating multiple specialized agents
- Defining tasks for each agent
- Orchestrating agents in a crew
- Running the crew from the terminal

Author: MIT AI Studio
"""

from dotenv import load_dotenv

load_dotenv()  

import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, FileWriterTool
from crewai import LLM

# Set up environment variables (you would need to set these with your actual API keys)
# For this example, we'll use placeholder values
# os.environ["OPENAI_API_KEY"] = "your-openai-api-key-here"
# os.environ["SERPER_API_KEY"] = "your-serper-api-key-here"  # Optional: for web search

gemini_llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.0
)

def create_research_agent():
    """Create a research agent that specializes in gathering information."""
    return Agent(
        role='Research Assistant',
        goal='To find and compile accurate, up-to-date information on given topics',
        backstory="""You are a diligent research assistant with expertise in academic 
        research and information synthesis. You have a keen eye for credible sources 
        and can quickly identify the most relevant information for any given topic.""",
        verbose=True,
        allow_delegation=False,
        llm=gemini_llm
    )

def create_writer_agent():
    """Create a writer agent that specializes in content creation."""
    return Agent(
        role='Content Writer',
        goal='To create clear, engaging, and well-structured written content',
        backstory="""You are a skilled writer with experience in academic and 
        technical writing. You excel at taking complex information and presenting 
        it in a clear, accessible manner that engages readers.""",
        verbose=True,
        allow_delegation=False,
        tools=[FileWriterTool()],  # Tool to write files,
        llm=gemini_llm
    )

def create_research_task(agent, topic):
    """Create a research task for the research agent."""
    return Task(
        description=f"""Research the topic: {topic}
        
        Your task is to:
        1. Gather information about the key concepts and recent developments
        2. Identify the main benefits and challenges
        3. Find relevant examples or case studies
        4. Summarize your findings in a structured format
        
        Focus on credible sources and current information.""",
        expected_output="""A comprehensive research summary containing:
        - Key concepts and definitions
        - Recent developments and trends
        - Benefits and challenges
        - Relevant examples
        - List of sources used""",
        agent=agent
    )

def create_writing_task(agent, research_output):
    """Create a writing task for the writer agent."""
    return Task(
        description=f"""Based on the research findings, create a well-structured article.
        
        Research findings to use: {research_output}
        
        Your task is to:
        1. Write an engaging introduction
        2. Organize the content into clear sections
        3. Include examples and explanations
        4. Write a conclusion that summarizes key points
        5. Save the article to a file called 'ai_studio_article.md'
        
        The article should be approximately 800-1000 words.""",
        expected_output="""A well-written article saved as 'ai_studio_article.md' containing:
        - Engaging introduction
        - Well-organized body sections
        - Clear explanations and examples
        - Thoughtful conclusion
        - Proper formatting in Markdown""",
        agent=agent
    )

def main():
    """Main function to run the Crew AI example."""
    print("🚀 Starting MIT AI Studio Crew AI Example")
    print("=" * 50)
    
    # Get topic from user input
    topic = input("Enter a topic you'd like to research and write about: ")
    if not topic.strip():
        topic = "Artificial Intelligence in Education"  # Default topic
        print(f"Using default topic: {topic}")
    
    print(f"\n📚 Topic: {topic}")
    print("=" * 50)
    
    # Create agents
    print("\n🤖 Creating AI agents...")
    researcher = create_research_agent()
    writer = create_writer_agent()
    
    # Create tasks
    print("📋 Setting up tasks...")
    research_task = create_research_task(researcher, topic)
    
    # Note: In a real implementation, you'd pass the research output to the writing task
    # For this example, we'll create a simplified version
    writing_task = Task(
        description=f"""Write a comprehensive article about: {topic}
        
        Your task is to:
        1. Write an engaging introduction to the topic
        2. Explain key concepts and their importance
        3. Discuss current trends and developments
        4. Include practical examples or applications
        5. Conclude with insights about the future
        6. Save the article to 'ai_studio_article.md'
        
        Make the article informative yet accessible, around 800-1000 words.""",
        expected_output="""A well-written article saved as 'ai_studio_article.md' with:
        - Engaging introduction
        - Clear explanations of key concepts
        - Current trends and developments
        - Practical examples
        - Future insights
        - Proper Markdown formatting""",
        agent=writer
    )
    
    # Create crew
    print("👥 Assembling the crew...")
    crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, writing_task],
        process=Process.sequential,  # Tasks will be executed in sequence
        verbose=True
    )
    
    # Execute the crew
    print("\n🎯 Starting crew execution...")
    print("=" * 50)
    
    try:
        result = crew.kickoff()
        
        print("\n✅ Crew execution completed!")
        print("=" * 50)
        print("📄 Final Result:")
        print(result)
        
        # Check if the article file was created
        if os.path.exists('ai_studio_article.md'):
            print("\n📝 Article successfully saved to 'ai_studio_article.md'")
            with open('ai_studio_article.md', 'r') as f:
                content = f.read()
                print(f"📊 Article length: {len(content)} characters")
        else:
            print("\n⚠️  Article file not found. The writer agent may not have used the file tool.")
            
    except Exception as e:
        print(f"\n❌ An error occurred: {str(e)}")
        print("\n💡 Note: This example requires valid API keys to function properly.")
        print("Please set your OPENAI_API_KEY environment variable.")
