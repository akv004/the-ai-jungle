# Markdown Chapters for Google Notebook ML

This directory contains all the chapters from "The AI Jungle" book converted from Quarto (.qmd) format to standard Markdown (.md) format, specifically for use with Google Notebook ML.

## What's Inside

- **22 Markdown files**: All book chapters, intro, index, references, and summary
- **Images directory**: Complete copy of all images with the same structure as the original

## Conversion Details

The conversion script has:
- ✅ Removed Quarto YAML frontmatter
- ✅ Converted Quarto callout blocks to standard markdown blockquotes with emojis
- ✅ Preserved all image references (paths are relative to this directory)
- ✅ Removed Quarto-specific image attributes while keeping standard markdown syntax
- ✅ Maintained all original content and formatting

## How to Use with Google Notebook ML

1. **Upload the .md files**: You can upload individual chapter files or multiple files at once to Google Notebook ML
2. **Images are included**: The images directory contains all referenced images, organized in subdirectories by chapter
3. **Recommended order**: 
   - Start with `index.md` (book introduction)
   - Then `intro.md` (preface)
   - Follow with `chapter1.md` through `chapter18.md` in sequence
   - Optionally include `summary.md` and `references.md`

## File List

### Main Content
- `index.md` - Book introduction and overview
- `intro.md` - Author's introduction
- `chapter1.md` through `chapter18.md` - Main chapters
- `summary.md` - Book summary
- `references.md` - References and citations

### Supporting Files
- `images/` - All images referenced in the chapters, organized by chapter subdirectories

## Notes

- **Original .qmd files remain unchanged** in the parent directory
- All image paths use relative references: `images/chapterX_images/imagename.png`
- Callout blocks are converted to blockquotes with appropriate emojis:
  - 💡 Tip
  - 📝 Note
  - ⚠️ Warning/Caution
  - ℹ️ Info
  - ❗ Important

## Regenerating the Markdown Files

If you need to regenerate these files from the source .qmd files, run:

```bash
python3 convert_qmd_to_md.py
```

The script is located in the repository root directory.

---

**Book Title**: The AI Jungle: Learn AI & ML with Nature's Wisdom  
**Author**: Amit Kumar Verma  
**Format**: Standard Markdown (.md)  
**Compatible with**: Google Notebook ML and other markdown-based tools
