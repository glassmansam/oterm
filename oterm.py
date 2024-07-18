#!/usr/bin/env python3
import argparse
import openai
import subprocess
import sys
import os

# Configuration for OpenAI
openai.api_key = 'your-openai-api-key'

# Memory to hold chat messages in interactive mode
interactive_session_memory = []


def generate_command(prompt):
    """Generate a command using OpenAI."""
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    command = response.choices[0].text.strip()
    return command


def explain_command(command):
    """Explain the given command."""
    explanation_prompt = f"Explain the following command:\n{command}"
    explanation = generate_command(explanation_prompt)
    return explanation


def execute_command(command):
    """Execute the given command and return the output and errors."""
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        output = result.stdout
        errors = result.stderr
        return output, errors
    except Exception as e:
        return "", str(e)


def correct_command(command, error_message):
    """Correct the given command based on the error message."""
    correction_prompt = f"The following command resulted in an error: {command}\nError: {error_message}\nPlease correct the command."
    corrected_command = generate_command(correction_prompt)
    return corrected_command


def interactive_session():
    """Start an interactive session for command generation and execution."""
    global interactive_session_memory
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        interactive_session_memory.append({"role": "user", "content": user_input})
        command = generate_command(user_input)
        print(f"Generated Command: {command}")
        user_response = input("Do you want to (e)xecute, (y)es, (n)o, (ex)plain, (q)uit: ").lower()
        if user_response == 'e' or user_response == 'y':
            if user_response == 'e':
                explanation = explain_command(command)
                print(f"Explanation: {explanation}")
            output, errors = execute_command(command)
            if errors:
                print(f"Error: {errors}")
                corrected_command = correct_command(command, errors)
                print(f"Corrected Command: {corrected_command}")
            else:
                print(f"Output: {output}")
        elif user_response == 'n':
            continue
        elif user_response == 'ex':
            explanation = explain_command(command)
            print(f"Explanation: {explanation}")
        elif user_response == 'q':
            break


def main():
    parser = argparse.ArgumentParser(description="Generate and execute Linux commands using OpenAI.")
    parser.add_argument("prompt", nargs='?', help="Prompt for the command to be generated.")
    parser.add_argument("-e", "--explain", action="store_true", help="Explain the generated command.")
    parser.add_argument("-y", "--yes", action="store_true", help="Automatically execute the generated command.")
    parser.add_argument("-i", "--interactive", action="store_true", help="Start an interactive session.")

    args = parser.parse_args()

    if args.interactive:
        interactive_session()
    else:
        if not args.prompt:
            print("Prompt is required unless using interactive mode.")
            sys.exit(1)

        command = generate_command(args.prompt)
        print(f"Generated Command: {command}")

        if args.explain:
            explanation = explain_command(command)
            print(f"Explanation: {explanation}")

        if args.yes:
            output, errors = execute_command(command)
            if errors:
                print(f"Error: {errors}")
                corrected_command = correct_command(command, errors)
                print(f"Corrected Command: {corrected_command}")
                output, errors = execute_command(corrected_command)
            if errors:
                print(f"Error: {errors}")
            else:
                print(f"Output: {output}")
        else:
            user_response = input("Do you want to (e)xecute, (y)es, (n)o, (ex)plain: ").lower()
            if user_response == 'e' or user_response == 'y':
                if user_response == 'e':
                    explanation = explain_command(command)
                    print(f"Explanation: {explanation}")
                output, errors = execute_command(command)
                if errors:
                    print(f"Error: {errors}")
                    corrected_command = correct_command(command, errors)
                    print(f"Corrected Command: {corrected_command}")
                    output, errors = execute_command(corrected_command)
                if errors:
                    print(f"Error: {errors}")
                else:
                    print(f"Output: {output}")
            elif user_response == 'ex':
                explanation = explain_command(command)
                print(f"Explanation: {explanation}")

if __name__ == "__main__":
    main()

