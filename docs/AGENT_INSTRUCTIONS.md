# IELTS Test Creation Instructions for Agents

## CRITICAL: Read this file completely before creating any test content!

---

## ABSOLUTE RULES - NO EXCEPTIONS

### 1. NEVER SKIP ANYTHING THE USER PROVIDES
- If the user gives you content, you MUST include ALL of it
- You have NO authority to decide what is "important" or "unimportant"
- Every single word, sentence, paragraph the user provides MUST be in the output
- If unsure whether to include something: INCLUDE IT

### 2. NEVER SUMMARIZE
- Do NOT summarize passages - include FULL TEXT word for word
- Do NOT shorten explanations
- Do NOT skip examples
- Do NOT remove "obvious" or "repetitive" content

### 3. NEVER MAKE DECISIONS ON YOUR OWN
- You are a transcription agent, not an editor
- Your job is to FORMAT the content into JSON, not to MODIFY it
- If something seems wrong or missing, ASK the user - don't assume

### 4. ALWAYS INCLUDE
- Every paragraph of every passage
- Every question (1-40 for reading, 1-40 for listening)
- Every answer option (A, B, C, D, E, F, G, H)
- Every transcript for listening tests
- Every instruction text
- Every title and subtitle

### 5. WRITE EXACTLY IN THE FORMAT GIVEN TO YOU
- Do NOT change the structure the user provides
- Do NOT "improve" or "optimize" the format
- Do NOT rearrange content
- Do NOT add your own formatting ideas
- If user gives you a specific format, use EXACTLY that format
- Copy the style from example files (general-test1.json, test1.json) EXACTLY
- Same field names, same nesting, same order

### 6. NO TYPOS OR SPELLING ERRORS - ZERO TOLERANCE
- You MUST copy text EXACTLY as provided - character by character
- Double-check every word you write before submitting
- If you make a typo, the entire test becomes UNUSABLE
- Common mistakes to avoid:
  - Missing letters (e.g., "th" instead of "the")
  - Swapped letters (e.g., "teh" instead of "the")
  - Extra spaces or missing spaces
  - Wrong punctuation
- This is an ENGLISH LEARNING platform - spelling errors are UNACCEPTABLE
- If you're unsure about a word's spelling, copy it DIRECTLY from the source
- Re-read your output before finishing to catch any errors

---

## General Rules

1. **NEVER skip any content** - Include ALL information from the source material
2. **Include full passage text** - Not summaries, the COMPLETE original text
3. **Preserve formatting** - Use `<p>`, `<strong>`, `<em>` tags appropriately
4. **Include ALL questions** - Every question number from 1-40 must be present

---

## JSON Structure Requirements

### Reading Tests (General Training)

```json
{
    "id": [number],
    "name": "IELTS General Training - Test [X]",
    "subtitle": "Cambridge IELTS [X] General Training Test [Y]",
    "type": "general",
    "reading": {
        "title": "General Training Reading Test [X]",
        "sections": [
            {
                "id": 1,
                "title": "Section 1",
                "questionRange": "Questions 1-14",
                "passages": [...]
            },
            {
                "id": 2,
                "title": "Section 2",
                "questionRange": "Questions 15-27",
                "passages": [...]
            },
            {
                "id": 3,
                "title": "Section 3",
                "questionRange": "Questions 28-40",
                "passages": [...]
            }
        ]
    }
}
```

---

## Question Types and Their Structure

### 1. Matching Questions
```json
{
    "type": "matching",
    "title": "Questions X-Y",
    "instructions": "Which paragraph contains the following information?",
    "options": ["A", "B", "C", "D", "E", "F"],
    "optionLabels": {
        "A": "Label for A",
        "B": "Label for B"
    },
    "items": [
        {"number": 1, "statement": "...", "answer": "A"}
    ]
}
```

### 2. True/False/Not Given
```json
{
    "type": "trueFalseNotGiven",
    "title": "Questions X-Y",
    "instructions": "Do the following statements agree with the information given in the text?",
    "items": [
        {"number": 1, "statement": "...", "answer": "TRUE"}
    ]
}
```

### 3. Sentence Completion (Fill in blank)
```json
{
    "type": "sentenceCompletion",
    "title": "Questions X-Y",
    "instructions": "Complete the sentences below. Choose ONE WORD ONLY from the text.",
    "items": [
        {"number": 15, "textBefore": "The text before blank", "textAfter": "text after blank.", "answer": "word"}
    ]
}
```

### 4. Note Completion
```json
{
    "type": "noteCompletion",
    "title": "Questions X-Y",
    "instructions": "Complete the notes below.",
    "noteTitle": "Title of the notes section",
    "items": [
        {"number": 15, "textBefore": "Text before", "textAfter": "text after", "answer": "answer"}
    ]
}
```

### 5. Table Completion
```json
{
    "type": "tableCompletion",
    "title": "Questions X-Y",
    "instructions": "Complete the table below.",
    "tableTitle": "Table Title",
    "headers": ["Column 1", "Column 2", "Column 3"],
    "rows": [
        {
            "cells": ["Cell content", "Cell with 15 ___ blank", "More content"],
            "answers": {"15": "answer"}
        }
    ]
}
```

### 6. Multiple Choice
```json
{
    "type": "multipleChoice",
    "title": "Questions X-Y",
    "instructions": "Choose the correct letter, A, B, C or D.",
    "items": [
        {
            "number": 28,
            "text": "Question text here?",
            "options": [
                {"letter": "A", "text": "Option A text"},
                {"letter": "B", "text": "Option B text"},
                {"letter": "C", "text": "Option C text"},
                {"letter": "D", "text": "Option D text"}
            ],
            "answer": "B"
        }
    ]
}
```

### 7. Heading Matching (i, ii, iii style)
```json
{
    "type": "headingMatching",
    "title": "Questions X-Y",
    "instructions": "Choose the correct heading for each paragraph.",
    "headings": [
        {"number": "i", "text": "Heading text 1"},
        {"number": "ii", "text": "Heading text 2"}
    ],
    "items": [
        {"number": 28, "statement": "Paragraph A", "answer": "vi"}
    ]
}
```

### 8. Summary Completion
```json
{
    "type": "summaryCompletion",
    "title": "Questions X-Y",
    "instructions": "Complete the summary below.",
    "summary": "Summary text with {37} blanks {38} indicated by numbers.",
    "items": [
        {"number": 37, "textBefore": "context before", "textAfter": "context after", "answer": "word"}
    ]
}
```

---

## Passage Content Guidelines

### DO Include:
- Full paragraph text with proper HTML formatting
- Bold headings: `<strong>A Perry Forest</strong>`
- Paragraph breaks: `<p>...</p>`
- Italic text: `<em>...</em>`
- All details, examples, and explanations from source

### DO NOT:
- Summarize or shorten passages
- Skip "unimportant" details
- Remove examples or quotes
- Change the original wording

---

## Listening Tests Structure

```json
{
    "id": [number],
    "name": "IELTS Listening Test [X]",
    "listening": {
        "title": "Cambridge IELTS [X] Test [Y] - Listening",
        "parts": [
            {
                "part": 1,
                "title": "Part 1 Title",
                "audioUrl": "https://pub-abcdc34fb0d6469f97657d9a699d2e28.r2.dev/ELT_IELTS[X]_t[Y]_audio1.mp3",
                "type": "notes",
                "instructions": "Write ONE WORD AND/OR A NUMBER for each answer.",
                "items": [...],
                "answers": {"1": "answer1", "2": "answer2"},
                "transcript": "Full transcript text..."
            },
            {
                "part": 2,
                "title": "Part 2 Title",
                "audioUrl": "https://pub-abcdc34fb0d6469f97657d9a699d2e28.r2.dev/ELT_IELTS[X]_t[Y]_audio2.mp3",
                "type": "...",
                ...
            },
            {
                "part": 3,
                "title": "Part 3 Title",
                "audioUrl": "https://pub-abcdc34fb0d6469f97657d9a699d2e28.r2.dev/ELT_IELTS[X]_t[Y]_audio3.mp3",
                "type": "...",
                ...
            },
            {
                "part": 4,
                "title": "Part 4 Title",
                "audioUrl": "https://pub-abcdc34fb0d6469f97657d9a699d2e28.r2.dev/ELT_IELTS[X]_t[Y]_audio4.mp3",
                "type": "...",
                ...
            }
        ]
    }
}
```

### IMPORTANT: Audio URL Format
- We use Cloudflare R2 for hosting audio files
- EACH PART has its own separate audio file (audio1.mp3, audio2.mp3, audio3.mp3, audio4.mp3)
- Use `audioUrl` field inside EACH part object, NOT at the listening level
- Format: `https://pub-abcdc34fb0d6469f97657d9a699d2e28.r2.dev/ELT_IELTS[BOOK]_t[TEST]_audio[PART].mp3`
- Example: `https://pub-abcdc34fb0d6469f97657d9a699d2e28.r2.dev/ELT_IELTS17_t4_audio1.mp3` for IELTS 17 Test 4 Part 1
- The audio changes automatically when user switches between parts

---

## Checklist Before Submitting

- [ ] All 40 questions present (Reading) or all questions for the part (Listening)
- [ ] Full passage text included, not summarized
- [ ] All answers verified against answer key
- [ ] JSON syntax validated (no trailing commas, proper quotes)
- [ ] Question numbers are sequential and correct
- [ ] Instructions match the original test format
- [ ] Transcript included for listening tests

---

## Common Mistakes to Avoid

1. **Missing questions** - Always count to ensure all questions are present
2. **Wrong answer format** - TRUE not True, A not a
3. **Incomplete passages** - Include EVERY paragraph
4. **Missing options** - All A-F or A-H options must be listed
5. **Forgetting transcript** - Listening tests MUST have transcripts
6. **Wrong question type** - Match the exact type from the source

---

## Example Reference Files

- General Test: `general/general-test1.json`
- Listening Test: `listening/test1.json`

Always check these files for correct structure before creating new tests.

---

## WARNINGS

### If you skip content:
- The test will be INCOMPLETE and UNUSABLE
- The user will have to REDO your work
- You are wasting the user's time

### If you summarize:
- Students cannot practice with incomplete passages
- The test loses its value
- You are FAILING at your task

### Remember:
- You are NOT smarter than the source material
- You do NOT know better than the user
- Your job is to CONVERT, not to EDIT
- When in doubt: INCLUDE EVERYTHING

---

## Before You Start Any Test

1. Read this ENTIRE file
2. Look at example files (general-test1.json, test1.json)
3. Confirm you understand the JSON structure
4. Ask the user if anything is unclear
5. Only then start creating the test

## After You Finish

1. Count all questions - are there 40? (or correct number for the section)
2. Check all passages - is the FULL text included?
3. Verify all answers are present
4. Validate JSON syntax
5. Report what you created to the user
