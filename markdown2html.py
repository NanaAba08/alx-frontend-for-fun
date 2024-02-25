#!/usr/bin/python3
"""
This is a script to convert a Markdown file to HTML.

Usage:
    ./markdown2html.py [input_file] [output_file]

Arguments:
    input_file: the name of the Markdown file to be converted
    output_file: the name of the output HTML file

Example:
    ./markdown2html.py README.md README.html
"""

import sys
import os
import markdown


import sys
import os
import markdown

def convert_markdown_to_html(markdown_file, output_file):
    try:
        # Check if Markdown file exists
        if not os.path.exists(markdown_file):
            print(f"Missing {markdown_file}", file=sys.stderr)
            sys.exit(1)
        
        # Read Markdown content
        with open(markdown_file, 'r') as md_file:
            markdown_content = md_file.read()
        
        # Convert Markdown to HTML
        html_content = markdown.markdown(markdown_content)
        
        # Write HTML content to output file
        with open(output_file, 'w') as html_file:
            html_file.write(html_content)
        
        # Print nothing and exit 0
        sys.exit(0)
    
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    # Check if arguments are provided correctly
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    
    # Extract arguments
    markdown_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # Convert Markdown to HTML
    convert_markdown_to_html(markdown_file, output_file)
