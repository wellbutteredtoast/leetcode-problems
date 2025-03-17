#!/bin/bash

# LeetCode Problem #193 -- Valid Phone Numbers (Shell)
# Language: Bash
# Runtime: 62ms
# Memory: 3.55mb
# Date: 17 March, 2025

# Regex testing: https://regexr.com/

FILE_TO_READ=file.txt
REGEX_PATTERN_1="^\([0-9]{3}\)\s[0-9]{3}-[0-9]{4}$" # FORMAT: (123) 123-4567
REGEX_PATTERN_2="^[0-9]{3}-[0-9]{3}-[0-9]{4}$"      # FORMAT: 123-456-7890
grep -E "$REGEX_PATTERN_1|$REGEX_PATTERN_2" "$FILE_TO_READ"

# Dense but usable, the regex is a little weird for me but I can tolerate it.
# It's about the average runtime for most of the community so it can probably be improved.