import re

# --- Regular Expressions ---
REGEX_PATTERNS = {
    "email": r"[a-zA-Z0-9!#$%&'*+\-/=?^_`{|}~.]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "url": r"(https?:\/\/)?(www\.)?[-a-zA-Z0-9]+(\.[a-zA-Z0-9-]+)+(\:[0-9]+)?([\/\?][-a-zA-Z0-9:%_\+.~#?&//=]*)?|\b[a-zA-Z0-9][-a-zA-Z0-9]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?\b",
    "credit_card": r"\b(?:\d{4} \d{4} \d{4} \d{4}|\d{4}-\d{4}-\d{4}-\d{4})\b",
    "hashtag": r"#[A-Za-z0-9_]+"
}

# Pre-compile patterns for better performance
COMPILED_PATTERNS = {key: re.compile(pattern) for key, pattern in REGEX_PATTERNS.items()}

# --- Example Data ---
EXAMPLES = {
    "email": ["user@example.com", "firstname.lastname@company.co.uk"],
    "url": ["https://www.example.com", "www.example.com", "regex-examples.com"],
    "credit_card": ["1234 5678 9012 3456", "1234-5678-9012-3456"],
    "hashtag": ["#example", "#ThisIsAHashtag"],
    "mixed": ["Contact us at support@example.com or visit https://help.example.com.",
              "Check out #pythonregex and #coding on our site regex-examples.com."]
}

def validate_string(input_string):
    """Validates a string against all patterns."""
    if not input_string or not input_string.strip():
        return {}, []

    results = {}
    valid_types = []

    for data_type, pattern in COMPILED_PATTERNS.items():
        try:
            is_valid = bool(pattern.fullmatch(input_string))
            results[data_type] = is_valid
            if is_valid:
                valid_types.append(data_type)
        except Exception:
            results[data_type] = False

    return results, valid_types

def extract_data_from_text(text):
    """Extracts all pattern matches from text."""
    if not text or not text.strip():
        return {key: [] for key in COMPILED_PATTERNS}

    extracted_data = {key: [] for key in COMPILED_PATTERNS}

    for data_type, pattern in COMPILED_PATTERNS.items():
        try:
            full_matches = [match.group(0) for match in pattern.finditer(text)]
            if full_matches:
                extracted_data[data_type].extend(full_matches)
        except Exception:
            pass
            
    return extracted_data

def print_header(text):
    """Print a simple header."""
    print(f"\n=== {text} ===")

def display_results(text, extraction=False):
    """Display validation or extraction results."""
    if extraction:
        # Extract and display patterns from text
        extracted = extract_data_from_text(text)
        print_header(f"Data Extracted from: \"{text}\"")

        # Display found patterns
        has_matches = False
        for data_type, items in extracted.items():
            if items:
                has_matches = True
                print(f"\n• {data_type.replace('_', ' ').capitalize()}s ({len(items)}):")
                for i, item in enumerate(items, 1):
                    print(f"  {i}. {item}")

        if not has_matches:
            print("No patterns matched in this text.")
    else:
        # Validate string against all patterns
        results, valid_types = validate_string(text)
        print_header(f"Validating: \"{text}\"")

        if valid_types:
            print(f"✓ Valid as: {', '.join(valid_types)}")
        else:
            print("✗ Not valid for any pattern")

            # Show partial matches
            extracted = extract_data_from_text(text)
            has_partial = False
            for data_type, items in extracted.items():
                if items:
                    has_partial = True
                    print(f"  • {data_type}: {', '.join(items)}")

            if not has_partial:
                print("  • No partial matches found")

def run_examples():
    """Run tests using the example data."""
    print_header("TESTING EXAMPLES")

    # Test individual examples
    for data_type, examples in EXAMPLES.items():
        if data_type != "mixed":
            print(f"\nTesting {data_type} examples:")
            for example in examples:
                display_results(example)

    # Test mixed examples
    print_header("EXTRACTING FROM MIXED TEXT")
    for text in EXAMPLES["mixed"]:
        display_results(text, extraction=True)

def interactive_mode():
    """Run a simple interactive mode."""
    print_header("INTERACTIVE MODE")
    print("Enter text to validate or extract data from (quit to exit)")
    print("Prefix with 'extract:' to switch to extraction mode")

    while True:
        user_input = input("\n> ")
        if user_input.lower() == 'quit':
            break

        if user_input.lower().startswith('extract:'):
            # Extract mode
            text = user_input[8:].strip()
            if text:
                display_results(text, extraction=True)
        else:
            # Validate mode
            display_results(user_input)

if __name__ == "__main__":
    print("\nREGEX DATA EXTRACTION TOOL")
    print("Supports: emails, URLs, credit cards, and hashtags.\n")

    try:
        run_examples()
        interactive_mode()
        print("\nThank you, stay safe")
    except KeyboardInterrupt:
        print("\n\nProgram terminated.")
