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
