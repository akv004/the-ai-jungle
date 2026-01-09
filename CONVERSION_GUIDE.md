# QMD to MD Conversion for Google Notebook ML

## Overview
This document describes the conversion process for converting Quarto (.qmd) chapter files to standard Markdown (.md) format for Google Notebook ML compatibility.

## Problem Statement
Google Notebook ML only accepts `.md` format files, not `.qmd` (Quarto Markdown) files. The goal was to convert all chapter files while preserving:
- All content and structure
- Image references
- Formatting and organization

## Solution

### Created Resources

1. **`markdown-chapters/` directory** - Contains all converted files
   - 22 markdown (.md) files (chapters, intro, index, summary, references)
   - Complete `images/` subdirectory with all 27 images
   - `README.md` with usage instructions

2. **`convert_qmd_to_md.py`** - Python conversion script that:
   - Removes Quarto YAML frontmatter
   - Converts Quarto callout blocks to standard markdown blockquotes with emojis
   - Removes Quarto-specific image attributes (e.g., `{width=100% height=auto}`)
   - Preserves all image references with correct relative paths
   - Copies the entire images directory to the output folder

### Conversion Details

#### Quarto Features Converted

1. **YAML Frontmatter** - Removed (not needed in standard markdown)
   ```yaml
   ---
   title: "Chapter Title"
   ---
   ```

2. **Callout Blocks** - Converted to blockquotes with emojis
   ```markdown
   # Before (Quarto)
   ::: {.callout-tip}
   This is a tip
   :::
   
   # After (Standard MD)
   > **💡 Tip**
   > This is a tip
   ```

3. **Image Attributes** - Simplified to standard markdown
   ```markdown
   # Before (Quarto)
   ![Alt text](path/to/image.png){width=100% height=auto}
   
   # After (Standard MD)
   ![Alt text](path/to/image.png)
   ```

#### Callout Type Mappings
- `tip` → 💡 Tip
- `note` → 📝 Note
- `warning` → ⚠️ Warning
- `caution` → ⚠️ Caution
- `important` → ❗ Important
- `info` → ℹ️ Info

### Files Converted

All book content files were successfully converted:
- `index.qmd` → `index.md`
- `intro.qmd` → `intro.md`
- `chapter1.qmd` through `chapter18.qmd` → `chapter1.md` through `chapter18.md`
- `summary.qmd` → `summary.md`
- `references.qmd` → `references.md`

### Original Files
**Important**: All original `.qmd` files remain **unchanged** in the repository root. The conversion creates new files in a separate directory without modifying the source files.

## Usage

### For Users
To upload to Google Notebook ML:
1. Navigate to the `markdown-chapters/` directory
2. Upload the desired `.md` files to Google Notebook ML
3. The images are included in the `images/` subdirectory with the same structure

### For Regeneration
To regenerate the markdown files after changes to the .qmd source files:
```bash
python3 convert_qmd_to_md.py
```

## Directory Structure
```
the-ai-jungle/
├── chapter*.qmd                    # Original Quarto files (unchanged)
├── images/                         # Original images (unchanged)
├── convert_qmd_to_md.py           # Conversion script
└── markdown-chapters/              # NEW - Converted files
    ├── README.md                   # Usage instructions
    ├── chapter*.md                 # Converted markdown files
    ├── index.md
    ├── intro.md
    ├── summary.md
    ├── references.md
    └── images/                     # Copy of all images
        ├── chapter1_images/
        ├── chapter2_images/
        └── ... (all image subdirectories)
```

## Verification

✅ 22 files converted successfully  
✅ 27 images copied to markdown-chapters/images  
✅ All image references preserved with correct paths  
✅ Quarto callout blocks converted to blockquotes with emojis  
✅ Original .qmd files unchanged  
✅ README.md created with usage instructions  

## Technical Notes

- The conversion script is written in Python 3
- Uses regular expressions for pattern matching and conversion
- Handles both styled callouts (`::: {.callout-type}`) and simple callouts (`::: type`)
- Preserves all markdown formatting, tables, code blocks, and other elements
- Image paths are relative and work correctly from the markdown-chapters directory

## Future Maintenance

To update the markdown files after editing the original .qmd files:
1. Make changes to the `.qmd` files in the repository root
2. Run: `python3 convert_qmd_to_md.py`
3. Commit the updated files in `markdown-chapters/`

The script will overwrite existing files in the markdown-chapters directory with fresh conversions.
