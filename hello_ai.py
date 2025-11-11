# hello_ai.py
# Muhammad Burhan
# CSCI 130 - Week 1 Project
# Date: 11/11/2025

import random
import datetime


def greeting_agent():
    """
    A simple AI agent that provides personalized greetings

    This demonstrates a simple reflex agent from Chapter 2
    """

    # Get current time
    current_hour = datetime.datetime.now().hour

    # Determine time of day
    if current_hour < 12:
        time_period = "morning"
    elif current_hour < 17:
        time_period = "afternoon"
    else:
        time_period = "evening"

    # Get user's name
    name = input("What's your name? ")

    # Generate personalized greeting
    greetings = [
        f"Good {time_period}, {name}! Welcome to AI class!",
        f"Hello {name}! Hope you're having a great {time_period}!",
        f"Hi {name}! Ready to learn AI this {time_period}?",
    ]

    # Select and display random greeting
    print("\n" + random.choice(greetings))

    # Simple conversation
    mood = input("\nHow are you feeling about learning AI? ")

    # Simple response based on keywords (reflex agent behavior)
    mood_lower = mood.lower()

    if "excited" in mood_lower or "good" in mood_lower or "happy" in mood_lower:
        print("That's wonderful! Your enthusiasm will help you learn!")
    elif "nervous" in mood_lower or "worried" in mood_lower or "scared" in mood_lower:
        print("Don't worry! We'll take it step by step.")
    elif "tired" in mood_lower:
        print("Totally get that. Even small steps count toward progress!")
    else:
        print("Thanks for sharing! Let's make this a great learning experience!")

    # Display an AI fact
    ai_facts = [
        "Did you know? The term 'Artificial Intelligence' was coined in 1956!",
        "Fun fact: Your smartphone uses AI for face recognition!",
        "AI insight: Netflix uses AI to recommend shows you might like!",
        "Did you know? AI helps doctors detect diseases earlier!",
        "Cool fact: Self-driving cars use AI to understand their surroundings!",
        "AI tip: Spam filters use AI to decide which emails to block!",
    ]

    print(f"\n{random.choice(ai_facts)}")
    print("\nLet's start our AI journey together!")


# Run the program
if __name__ == "__main__":
    print("=" * 50)
    print("Welcome to CSCI 130: Introduction to AI")
    print("=" * 50)
    print()
    greeting_agent()
