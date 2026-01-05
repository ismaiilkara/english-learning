# AGENTS.md

This file provides guidance for AI agents working with this codebase.

## Project Overview

This is an **English Learning Platform** - an interactive web application for language learners, featuring vocabulary practice, grammar lessons, test preparation (ITU PROF, IELTS), and various study tools.

**Live URL:** [yourenglishapp.com](https://yourenglishapp.com)

## Tech Stack

- **HTML5** - Page structure
- **CSS3** - Custom styling with modern design patterns
- **JavaScript** - Core logic and interactivity
- **Alpine.js** - Lightweight reactive framework for UI state
- **Tailwind CSS** - Utility-first CSS framework
- **JSON** - Data storage for vocabulary, tests, and content

## Project Structure

```
english-learning/
├── index.html                 # Main landing page
├── vocabulary.html            # Vocabulary practice module
├── vocabulary-data.json       # Vocabulary sets and questions
├── grammar.html               # Grammar lessons and exercises
├── ielts.html                 # IELTS test preparation
├── itu-prof.html              # ITU PROF test preparation
├── itu-prof-data.json         # ITU PROF test metadata
├── sentence-builder.html      # Sentence construction practice
├── data.json                  # General app data
│
├── itu_prof_samples/          # ITU PROF test JSON files
│   └── itu-prof-test*.json    # Individual test data
│
├── ielts-tests/               # IELTS test resources
│
├── tools/                     # Utility tools
│   ├── essay-writing-screen.html   # Essay writing practice
│   ├── habit-tracker.html          # Study habit tracker
│   ├── ielts-body-paragraph.html   # IELTS paragraph builder
│   ├── mp3_to_mp4.py               # Audio conversion utility
│   └── pdf_to_png.py               # PDF conversion utility
│
└── social-media-tools/        # Content creation tools
    ├── ad-creator.html             # Ad creative generator
    ├── vocab-card-creator.html     # Vocabulary card generator
    ├── vocab-sentence-post-generator.html
    ├── program-cards.html          # Program info cards
    ├── score-share.html            # Score sharing graphics
    └── toefl-ad-downloader.html    # TOEFL ad generator
```

## Development Guidelines

### HTML Pages

- Each `.html` file is a standalone page
- Pages use inline `<script>` and `<style>` tags for Alpine.js logic and custom CSS
- Tailwind CSS is loaded via CDN
- Alpine.js is loaded via CDN

### Data Management

- All content data is stored in JSON files
- Vocabulary data: `vocabulary-data.json`
- ITU PROF tests: `itu-prof-data.json` (metadata) + `itu_prof_samples/*.json` (test content)
- General data: `data.json`

### Styling Conventions

- Use **Tailwind CSS** classes for layout and common utilities
- Use custom CSS for complex animations, gradients, and specialized effects
- Dark/modern aesthetic with glassmorphism effects
- Responsive design is required for all pages

### JavaScript/Alpine.js Patterns

- Use Alpine.js `x-data` for component state
- Use `x-init` for initialization logic
- Use `@click`, `@change` for event handling
- Use `fetch()` for loading JSON data
- Use `localStorage` for persisting user data (scores, progress, preferences)

### Test Data Format (ITU PROF)

ITU PROF tests have three sections:
1. **Cloze Test** - Fill-in-the-blank passages
2. **Reading Comprehension** - Passage-based questions
3. **Restatement** - Sentence paraphrase questions

### Social Media Tools

Tools in `social-media-tools/` generate downloadable images (PNG/JPEG) for Instagram and other platforms:
- Use `html2canvas` library for rendering HTML to images
- Maintain Instagram-safe zones for text placement
- Support Turkish language content

## Common Tasks

### Adding New Vocabulary Sets
1. Edit `vocabulary-data.json`
2. Follow existing set structure with `id`, `name`, `words` array

### Adding New ITU PROF Tests
1. Create new JSON file in `itu_prof_samples/`
2. Register in `itu-prof-data.json`
3. Follow existing test structure

### Creating New Pages
1. Use existing pages as templates
2. Include Alpine.js and Tailwind CDN links
3. Maintain consistent navigation and styling

## Important Notes

- **Language:** UI content is primarily in **Turkish**
- **Deployment:** Static site hosted via GitHub Pages with custom domain
- **No Build Step:** All files are served directly without compilation
- **Browser Testing:** Test in modern browsers (Chrome, Safari, Firefox)
