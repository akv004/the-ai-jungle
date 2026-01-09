#!/usr/bin/env python3
"""
Convert Quarto (.qmd) files to standard Markdown (.md) for Google Notebook ML.
This script:
- Removes YAML frontmatter
- Converts Quarto callout blocks to standard markdown
- Preserves image references
- Copies images to the markdown-chapters directory
"""

import os
import re
import shutil
from pathlib import Path

def remove_figure_placeholders(content):
    """Remove Quarto figure placeholder divs."""
    # Remove :::{.figure-placeholder} and ::::
    content = re.sub(r':::+\s*\{\.figure-placeholder\}\s*\n', '', content)
    content = re.sub(r':::+\s*\n', '', content)
    return content

def convert_callout_to_markdown(content):
    """
    Convert Quarto callout blocks to standard markdown.
    
    Quarto callouts:
    ::: {.callout-tip}
    Content
    :::
    
    Convert to:
    > **💡 Tip**
    > Content
    """
    
    # Pattern for callout blocks with class
    pattern = r':::\s*\{\.callout-(\w+)(?:\s+[^}]*)?\}(.*?):::'
    
    def replace_callout(match):
        callout_type = match.group(1)
        content = match.group(2).strip()
        
        # Map callout types to emojis and labels
        type_map = {
            'note': ('📝', 'Note'),
            'tip': ('💡', 'Tip'),
            'warning': ('⚠️', 'Warning'),
            'caution': ('⚠️', 'Caution'),
            'important': ('❗', 'Important'),
            'info': ('ℹ️', 'Info')
        }
        
        emoji, label = type_map.get(callout_type, ('📌', callout_type.title()))
        
        # Convert content to blockquote format
        lines = content.split('\n')
        quoted_lines = [f"> **{emoji} {label}**"]
        for line in lines:
            if line.strip():
                quoted_lines.append(f"> {line}")
            else:
                quoted_lines.append(">")
        
        return '\n'.join(quoted_lines)
    
    # Replace callouts with class
    content = re.sub(pattern, replace_callout, content, flags=re.DOTALL)
    
    # Pattern for simple callout blocks without class (e.g., ::: warning)
    simple_pattern = r':::\s*(\w+)(.*?):::'
    
    def replace_simple_callout(match):
        callout_type = match.group(1)
        content = match.group(2).strip()
        
        # Check if this is a known callout type
        known_types = ['note', 'tip', 'warning', 'caution', 'important', 'info']
        if callout_type.lower() not in known_types:
            # Not a callout, return as is
            return match.group(0)
        
        type_map = {
            'note': ('📝', 'Note'),
            'tip': ('💡', 'Tip'),
            'warning': ('⚠️', 'Warning'),
            'caution': ('⚠️', 'Caution'),
            'important': ('❗', 'Important'),
            'info': ('ℹ️', 'Info')
        }
        
        emoji, label = type_map.get(callout_type.lower(), ('📌', callout_type.title()))
        
        lines = content.split('\n')
        quoted_lines = [f"> **{emoji} {label}**"]
        for line in lines:
            if line.strip():
                quoted_lines.append(f"> {line}")
            else:
                quoted_lines.append(">")
        
        return '\n'.join(quoted_lines)
    
    content = re.sub(simple_pattern, replace_simple_callout, content, flags=re.DOTALL)
    
    return content

def remove_yaml_frontmatter(content):
    """Remove YAML frontmatter from anywhere in the file."""
    # Match YAML frontmatter between --- delimiters, anywhere in the file
    pattern = r'---\s*\n.*?\n---\s*\n'
    content = re.sub(pattern, '', content, flags=re.DOTALL)
    return content

def remove_quarto_divs(content):
    """Remove Quarto-specific div blocks and attributes."""
    # Remove divs like :::{.no-number}
    content = re.sub(r':::+\s*\{[^}]+\}\s*\n', '', content)
    # Remove inline attributes like {.unnumbered}
    content = re.sub(r'\s*\{\.[\w-]+\}', '', content)
    return content

def convert_image_attributes(content):
    """
    Convert Quarto image attributes to standard markdown.
    
    ![alt](path){width=100% height=auto}
    becomes:
    ![alt](path)
    """
    pattern = r'(!\[.*?\]\([^)]+\))\{[^}]+\}'
    content = re.sub(pattern, r'\1', content)
    return content

def convert_qmd_to_md(qmd_file, output_dir):
    """Convert a single .qmd file to .md format."""
    
    print(f"Converting {qmd_file}...")
    
    # Read the .qmd file
    with open(qmd_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Apply conversions
    content = remove_yaml_frontmatter(content)
    content = remove_quarto_divs(content)
    content = convert_callout_to_markdown(content)
    content = convert_image_attributes(content)
    content = remove_figure_placeholders(content)
    
    # Generate output filename
    input_path = Path(qmd_file)
    output_file = output_dir / f"{input_path.stem}.md"
    
    # Write the .md file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  → Created {output_file}")
    return output_file

def main():
    """Main conversion function."""
    
    # Setup paths
    repo_root = Path(__file__).parent
    output_dir = repo_root / "markdown-chapters"
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(exist_ok=True)
    
    # Copy images directory to markdown-chapters
    images_src = repo_root / "images"
    images_dst = output_dir / "images"
    
    if images_src.exists():
        if images_dst.exists():
            shutil.rmtree(images_dst)
        shutil.copytree(images_src, images_dst)
        print(f"Copied images directory to {images_dst}")
    
    # Find all .qmd files (chapters only, not config files)
    qmd_files = [
        "index.qmd",
        "intro.qmd",
        "chapter1.qmd",
        "chapter2.qmd",
        "chapter3.qmd",
        "chapter4.qmd",
        "chapter5.qmd",
        "chapter6.qmd",
        "chapter7.qmd",
        "chapter8.qmd",
        "chapter9.qmd",
        "chapter10.qmd",
        "chapter11.qmd",
        "chapter12.qmd",
        "chapter13.qmd",
        "chapter14.qmd",
        "chapter15.qmd",
        "chapter16.qmd",
        "chapter17.qmd",
        "chapter18.qmd",
        "references.qmd",
        "summary.qmd"
    ]
    
    print(f"\nConverting {len(qmd_files)} chapter files...\n")
    
    # Convert each file
    converted_files = []
    for qmd_file in qmd_files:
        qmd_path = repo_root / qmd_file
        if qmd_path.exists():
            output_file = convert_qmd_to_md(qmd_path, output_dir)
            converted_files.append(output_file)
        else:
            print(f"Warning: {qmd_file} not found, skipping...")
    
    print(f"\n✅ Conversion complete!")
    print(f"   Converted {len(converted_files)} files")
    print(f"   Output directory: {output_dir}")
    print(f"\nYou can now upload the .md files from '{output_dir}' to Google Notebook ML.")

if __name__ == "__main__":
    main()
