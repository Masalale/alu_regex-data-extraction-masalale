# Regex Data Extraction Tool

A lightweight Python tool for validating and extracting common data patterns from text using regular expressions.

## Author
Clarence Chomba

## Overview

This tool uses regex patterns to identify and extract common data types including:
- Email addresses
- URLs / Web addresses
- Credit card numbers
- Hashtags

It provides both validation (checking if a string fully matches a pattern) and extraction (finding all matches in longer text) functionality.

## Features

- **Pattern Validation**: Check if a string is a valid email, URL, credit card, or hashtag
- **Data Extraction**: Extract all instances of supported patterns from text
- **Interactive Testing**: User-friendly interface for testing strings and text
- **Pre-built Examples**: Includes sample data to demonstrate functionality

## Requirements

- Python 3.6 or higher

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/alu_regex-data-extraction-masalale.git
cd alu_regex-data-extraction-masalale
```

## Usage

Run the script:

```bash
python clarence_chomba_fromative_1_regex.py
```

### Interactive Mode

After running the examples, the tool enters interactive mode where you can:

1. **Validate a string**:
   ```
   > user@example.com
   ```

2. **Extract patterns from text**:
   ```
   > extract: Check out our website at example.com or email us at info@example.com
   ```

3. **Exit the tool**:
   ```
   > quit
   ```

## Examples

Here's how the validation works:
```
=== Validating: "user@example.com" ===
✓ Valid as: email
```

And here's an extraction example:
```
=== Data Extracted from: "Contact us at support@example.com or visit https://help.example.com." ===

• Emails (1):
  1. support@example.com

• Urls (1):
  1. https://help.example.com
```

## Supported Patterns

### Email Addresses
- Matches standard email format
- Example: `user@example.com`, `firstname.lastname@company.co.uk`

### URLs
- Matches URLs
- Handles subdomains and paths
- Example: `https://www.example.com`, `example.com`, `regex-examples.com`

### Credit Card Numbers
- Matches 16-digit numbers in common formats
- Supports space-separated format (1234 5678 9012 3456)
- Supports hyphen-separated format (1234-5678-9012-3456)

### Hashtags
- Matches standard hashtags starting with #
- Example: `#example`, `#ThisIsAHashtag`