# AI Coding Assistant Guide for The AI Jungle

This document provides formatting guidelines for AI assistants working on this Quarto book project. Follow these rules to ensure consistent and properly rendered documents.

---

## Project Overview

- **Project Type:** Quarto Book
- **File Format:** `.qmd` (Quarto Markdown)
- **Build Command:** `quarto render` or `quarto preview`
- **Output:** HTML book in `docs/` folder

---

## Quarto Markdown Formatting Rules

### 1. Text Formatting

| Style | Syntax | Example |
|-------|--------|---------|
| Bold | `**text**` | **bold text** |
| Italics | `*text*` | *italic text* |
| Bold Italics | `***text***` | ***bold italic*** |
| Subscript | `text~2~` | H~2~O |
| Superscript | `text^2^` | E=mc^2^ |
| Strikethrough | `~~text~~` | ~~deleted~~ |
| Inline Code | `` `code` `` | `variable` |

---

### 2. Headings

Use hash symbols `#` followed by a space. **CRITICAL: Always add a blank line after every heading.**

```markdown
# Chapter Title (Level 1)

Content starts here after blank line.

## Section (Level 2)

Content starts here after blank line.

### Subsection (Level 3)

Content starts here after blank line.

#### Sub-subsection (Level 4)

Content starts here after blank line.
```

⚠️ **Common Mistake to Avoid:**
```markdown
## Heading
Content immediately after (WRONG!)
```

✅ **Correct:**
```markdown
## Heading

Content after blank line (CORRECT!)
```

---

### 3. Lists

**CRITICAL: Always leave a blank line before starting any list.**

#### Unordered Lists
```markdown
Here is some text.

- Item 1
- Item 2
  - Sub-item (indent 2-4 spaces)
  - Another sub-item
- Item 3
```

#### Ordered Lists
```markdown
Here is some text.

1. First item
2. Second item
3. Third item
```

#### Ordered Lists with Bold Labels
```markdown
1. **Label:** Description of the item.
2. **Another Label:** Another description.
```

#### Nested Lists in Bullet Points
```markdown
- **Main Point:**
    - Sub-point one
    - Sub-point two
```

#### Definition Lists
```markdown
Term
: Definition of the term
```

#### Task Lists
```markdown
- [ ] Incomplete task
- [x] Completed task
```

---

### 4. Links & Images

```markdown
<!-- Hyperlinks -->
[Link Text](https://example.com)

<!-- Direct URLs -->
<https://example.com>

<!-- Images -->
![Caption](path/to/image.png)

<!-- Images with Quarto attributes -->
![Caption](path/to/image.png){fig-align="center" width="80%"}

<!-- Images with Alt Text -->
![Caption](path/to/image.png){fig-alt="Alternative text description"}

<!-- Linked Images -->
[![Caption](image.png)](https://link-url.com)
```

---

### 5. Tables

```markdown
| Column 1 | Column 2 | Column 3 |
|----------|:--------:|---------:|
| Left     | Center   | Right    |
| aligned  | aligned  | aligned  |
```

Alignment in separator row:
- Left: `:-----`
- Center: `:----:`
- Right: `-----:`

---

### 6. Code Blocks

````markdown
```python
# Python code with syntax highlighting
def hello():
    print("Hello, World!")
```

```{.python filename="script.py"}
# Code block with filename attribute
import pandas as pd
```
````

---

### 7. Math & Equations

```markdown
<!-- Inline Math -->
The formula $E = mc^{2}$ shows energy-mass equivalence.

<!-- Display Math Block -->
$$
E = mc^{2}
$$
```

---

### 8. Quarto-Specific Elements

#### Callout Blocks
```markdown
::: {.callout-note}
This is a note callout.
:::

::: {.callout-warning}
This is a warning callout.
:::

::: {.callout-tip}
This is a tip callout.
:::

::: {.callout-important}
This is an important callout.
:::
```

#### Custom Divs
```markdown
::: {.border}
Content with border styling
:::

::: {.figure-placeholder}
![Figure caption](image.png){fig-align="center" width="80%"}
:::
```

#### Inline Spans
```markdown
[Red text]{.red}
[Custom styled text]{.custom-class}
```

---

### 9. Special Elements

#### Footnotes
```markdown
Here is a sentence with a footnote.^[This is the footnote text.]

Or use references[^1] for longer footnotes.

[^1]: This is a referenced footnote with longer content.
```

#### Page Breaks
```markdown
{{< pagebreak >}}
```

#### Videos
```markdown
{{< video https://www.youtube.com/watch?v=VIDEO_ID >}}
```

#### Mermaid Diagrams
````markdown
```{mermaid}
flowchart LR
  A[Start] --> B[Process]
  B --> C[End]
```
````

---

## Project-Specific Conventions

### Chapter Structure

Each chapter follows this structure:

```markdown
# Chapter Title

- Character/Theme subtitle

## Introduction: Section Name

Opening paragraph...

:::{.figure-placeholder}
![Figure X.X — Description](images/chapterX_images/image.png){fig-align="center" width="80%"}
:::

## Main Section

### Subsection

#### Sub-subsection

## Key Takeaways

1. **Point One:** Description.
2. **Point Two:** Description.

## Story Finale & Next Steps

Closing narrative...

**Teaser:** Preview of next chapter...
```

### Formatting Patterns Used in This Book

#### Story Notes and Links
```markdown
**Story Note:** The narrative explanation...

**Story Link:** Connection to the story...

**Story Twist:** A narrative development...
```

#### Case Studies
```markdown
#### Case Study: Title

- **Context:** Background information.
- **Approach:**
    1. **Step One:** Description.
    2. **Step Two:** Description.
- **Outcome:** Results achieved.
```

#### Exercises and Projects
```markdown
#### Quick Exercise

1. First task instruction.
2. Second task instruction.

#### Hands-On Mini-Project

- Step one of the project.
- Step two of the project.
```

---

## Common Formatting Fixes

When reviewing or editing `.qmd` files, check for these issues:

| Issue | Problem | Fix |
|-------|---------|-----|
| Missing blank line after heading | `## Heading\nText` | Add `\n` after heading |
| Missing blank line before list | `Text\n- Item` | Add `\n` before list |
| Unformatted list labels | `1. Label:` | Use `1. **Label:**` |
| Trailing spaces on headings | `## Heading ` | Remove trailing space |
| Broken em-dashes | `word— word` | Use `word—word` |
| Plain text labels | `Story Note:` | Use `**Story Note:**` |

---

## Build & Preview Commands

```bash
# Preview single chapter
quarto preview chapter7.qmd

# Preview entire book
quarto preview

# Render entire book
quarto render

# Render single chapter
quarto render chapter7.qmd
```

---

## File Structure

```
TheAIJungle/
├── _quarto.yml          # Main Quarto config
├── _quarto-book.yml     # Book-specific config
├── index.qmd            # Book landing page
├── intro.qmd            # Introduction
├── chapter1.qmd         # Chapter files
├── chapter2.qmd
├── ...
├── references.qmd       # Bibliography
├── references.bib       # BibTeX references
├── styles.css           # Custom CSS
├── images/              # Image assets
│   ├── chapter1_images/
│   ├── chapter2_images/
│   └── ...
└── docs/                # Rendered output
```

---

## Summary for AI Assistants

When editing Quarto files in this project:

1. ✅ **Always add blank lines after headings**
2. ✅ **Always add blank lines before lists**
3. ✅ **Use `**bold**` for labels in lists**
4. ✅ **Use proper Quarto div syntax `:::{.class}`**
5. ✅ **Maintain consistent heading hierarchy**
6. ✅ **Use fig-align and width attributes for images**
7. ✅ **Follow the chapter structure template**
8. ❌ **Never remove blank lines between sections**
9. ❌ **Never use HTML tags when Quarto syntax exists**
10. ❌ **Never forget the space after `#` in headings**
