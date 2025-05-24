# Regex Pattern Tool

A streamlined Python tool for finding and displaying common data patterns from text using regular expressions.

## Overview

This tool demonstrates regex pattern matching by identifying and displaying the following patterns.
- **Email addresses**
- **Time formats**
- **Credit card numbers**
- **Hashtags**

## Features

- **Pattern Finding**: Identifies all instances of supported patterns in text
- **Clean Display**: Organized presentation of found patterns by category
- **Interactive Mode**: User-friendly interface for testing with custom text
- **Demo Examples**: Built-in samples demonstrating pattern recognition
- **Edge Case Handling**: Properly excludes malformed data (e.g., incomplete emails, time without colons)

## Requirements

- Python 3.6 or higher

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/Masalale/alu_regex-data-extraction-masalale.git
cd alu_regex-data-extraction-masalale
```

## Usage

```bash
python3 clarence_chomba_fromative_1_regex.py
```

### Program Flow

1. **Demo Mode**: Displays three demo samples showing pattern recognition
2. **Interactive Mode**: Enter your own text to find patterns
3. **Exit**: Type 'quit' or 'exit' to end the program

## Examples

### Demo Output
```
--- Demo Sample 1 ---
"Contact us at user@example.com. Meeting is at 14:30 today. My card is 1234-5678-9012-3456."

Emails:
- user@example.com

Time:
- 14:30

Credit cards:
- 1234-5678-9012-3456
```

### Interactive Example
```
> Check out #Python and meet at 2:30 PM!

--- Your Input ---
"Check out #Python and meet at 2:30 PM!"

Time:
- 2:30 PM

Hashtags:
- #Python
```