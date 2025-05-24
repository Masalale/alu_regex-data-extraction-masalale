#!/usr/bin/env python3
"""
Simple Regex Pattern Tool
"""

import re

# Patterns for validation and extraction
PATTERNS = {
    "email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "time": r"(?:1[0-2]|0?[1-9]):[0-5][0-9]\s*(?:AM|PM|am|pm)|(?:[01]?[0-9]|2[0-3]):[0-5][0-9](?!\s*(?:AM|PM|am|pm))",
    "credit_card": r"\b\d{4}[-\s]\d{4}[-\s]\d{4}[-\s]\d{4}\b",
    "hashtag": r"#[A-Za-z0-9_]{1,50}"
}

# Demo text for validation and extraction
DEMO_TEXT_SAMPLES = [
    "Contact us at user@example.com. Meeting is at 14:30 today. My card is 1234-5678-9012-3456.",
    "Check out #example and #ThisIsAHashtag. The event starts at 2:30 PM. Another email is firstname.lastname@company.co.uk.",
    "Invalid: c.chomba@alustudent. Meeting time: 0915 or 1145AM. Card: 9876543210987654. # FunTime"
]

# Function to validate input against all patterns
def find_patterns(text):
    """Find all defined patterns from text."""
    found_all = {}
    for pattern_type, pattern_regex in PATTERNS.items():
        try:
            matches = re.findall(pattern_regex, text)
            if matches:
                # Remove duplicates while preserving order for display
                unique_matches = []
                for match in matches:
                    if match not in unique_matches:
                        unique_matches.append(match)
                found_all[pattern_type] = unique_matches
        except re.error as e:
            print(f"Error with regex for {pattern_type}: {e}")
            found_all[pattern_type] = []
    return found_all

# Function to display data from text
def display_data(text_source_description, text_to_process):
    """Displays data from the given text."""
    print(f"\n--- {text_source_description} ---")
    print(f"\"{text_to_process}\"")

    found_data = find_patterns(text_to_process)

    if not any(found_data.values()):
        print("- No patterns found.")
        return

    for pattern_type, matches in found_data.items():
        print(f"\n{pattern_type.replace('_', ' ').capitalize()}:")
        if matches:
            for item in matches:
                print(f"- {item}")
        else:
            print("- None found")

# Function to run demo examples
def run_demo():
    """Show pattern examples."""
    print("=== DEMO ===")
    for i, sample_text in enumerate(DEMO_TEXT_SAMPLES):
        display_data(f"Demo Sample {i+1}", sample_text)

# Function for interactive mode
def interactive_mode():
    """Interactive mode for finding patterns."""
    print("\n=== INTERACTIVE MODE ===")
    print("Enter text to find patterns or 'quit' to exit.")

    while True:
        user_input = input("\n> ").strip()

        if user_input.lower() in ['quit', 'exit']:
            break
        elif user_input:
            display_data("Your Input", user_input)
        else:
            print("Please enter some text or 'quit'.")

def main():
    """Main program."""
    print("REGEX PATTERN TOOL")
    print("Patterns: Email, Time, Credit Card, Hashtag\n")

    run_demo()
    interactive_mode()

    print("\nProgram completed!")

if __name__ == "__main__":
    main()
