#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from class_crew.crew import ClassCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def get_topic_from_user():
    """
    Get the course topic from user input.
    """
    print("=" * 60)
    print("🎓 CURRICULUM DESIGN CREW")
    print("=" * 60)
    print("This crew will create comprehensive course materials for both")
    print("business and technical students on your chosen topic.")
    print()
    
    while True:
        topic = input("Enter the course topic (e.g., 'Machine Learning', 'Blockchain', 'Data Science'): ").strip()
        if topic:
            return topic
        print("Please enter a valid topic.")

def run():
    """
    Run the curriculum design crew.
    """
    topic = get_topic_from_user()
    
    print(f"\n🚀 Starting curriculum design for: {topic}")
    print("This will create comprehensive course materials including:")
    print("  • Research reports (business & technical)")
    print("  • Course syllabus")
    print("  • Guest lecture materials")
    print("  • Weekly assignments")
    print("  • Student simulation feedback")
    print("  • Final project specifications")
    print("  • Assessment criteria")
    print("  • Course review and recommendations")
    print("\n⏳ This may take several minutes to complete...\n")
    
    inputs = {
        'topic': topic,
        'current_year': str(datetime.now().year)
    }
    
    try:
        result = ClassCrew().crew().kickoff(inputs=inputs)
        print("\n✅ Curriculum design completed successfully!")
        print(f"📁 Course materials have been saved to organized directories.")
        print(f"📋 Check the output files for your comprehensive {topic} curriculum.")
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    topic = get_topic_from_user()
    
    inputs = {
        "topic": topic,
        'current_year': str(datetime.now().year)
    }
    try:
        ClassCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        ClassCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    topic = get_topic_from_user()
    
    inputs = {
        "topic": topic,
        "current_year": str(datetime.now().year)
    }
    
    try:
        ClassCrew().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


if __name__ == "__main__":
    run()