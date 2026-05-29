#!/usr/bin/env python3
import argparse
import json
import re
from collections import Counter
VERSION = "1.0.0"

def analyze_text(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return {
        'word_count': len(words),
        'unique_words': len(set(words)),
        'sentences': len(re.split(r'[.!?]+', text)),
        'avg_word_length': round(sum(len(w) for w in words) / len(words), 2) if words else 0
    }

def main():
    parser = argparse.ArgumentParser(description='Text Analyzer Pro')
    parser.add_argument('input', nargs='?', help='Text to analyze')
    parser.add_argument('-f', '--file', help='Read from file')
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args()
    if args.file:
        with open(args.file, 'r') as f:
            text = f.read()
    else:
        text = args.input or ''
    result = analyze_text(text)
    print(json.dumps(result, indent=2) if args.json else f"Words: {result['word_count']}, Unique: {result['unique_words']}")
if __name__ == '__main__':
    main()
