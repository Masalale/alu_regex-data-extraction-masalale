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
