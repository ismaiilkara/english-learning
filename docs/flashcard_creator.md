# Flashcard Vocabulary Creator Guide

This guide explains how to add new vocabulary words to the flashcard system.

## File Location

All vocabulary data is stored in: `data/vocabulary/awl-vocabulary.json`

## JSON Structure

```json
{
  "title": "Academic Word List (AWL)",
  "description": "Essential academic vocabulary for university-level English",
  "totalWords": 570,
  "categories": [
    {
      "id": 1,
      "name": "Category Name",
      "words": [
        {
          "word": "example",
          "type": "noun",
          "definition": "A thing characteristic of its kind",
          "turkish": "ornek",
          "example": "This is an ---- of how to use the word."
        }
      ]
    }
  ]
}
```

## Word Entry Fields

| Field | Required | Description |
|-------|----------|-------------|
| `word` | Yes | The English word |
| `type` | Yes | Part of speech: `noun`, `verb`, `adjective`, `adverb` |
| `definition` | Yes | English definition of the word |
| `turkish` | Yes | Turkish translation(s), comma-separated if multiple |
| `example` | Yes | Example sentence with `----` as placeholder for the word |

## Example Sentence Format

Use `----` (four dashes) as a placeholder where the word should appear:

```json
"example": "Scientists ---- the data to find patterns."
```

The flashcard system will automatically highlight the word in the example sentence.

## Adding a New Word

### To an existing category:

1. Open `data/vocabulary/awl-vocabulary.json`
2. Find the category by `id` or `name`
3. Add a new word object to the `words` array:

```json
{
  "word": "collaborate",
  "type": "verb",
  "definition": "To work jointly with others",
  "turkish": "isbirligi yapmak, beraber calismak",
  "example": "The teams ---- to complete the project on time."
}
```

### Creating a new category:

Add a new category object to the `categories` array:

```json
{
  "id": 19,
  "name": "New Category Name",
  "words": [
    {
      "word": "firstword",
      "type": "noun",
      "definition": "Definition here",
      "turkish": "Turkce karsiligi",
      "example": "Example sentence with ----."
    }
  ]
}
```

## Existing Categories

| ID | Category Name |
|----|---------------|
| 1 | Analysis & Research |
| 2 | Communication & Expression |
| 3 | Change & Development |
| 4 | Structure & Organization |
| 5 | Relationships & Connections |
| 6 | Quantity & Measurement |
| 7 | Process & Method |
| 8 | Cause & Effect |
| 9 | Economy & Resources |
| 10 | Society & People |
| 11 | Environment & Nature |
| 12 | Government & Politics |
| 13 | Time & Frequency |
| 14 | Importance & Significance |
| 15 | Possibility & Certainty |
| 16 | Achievement & Success |
| 17 | Agreement & Opposition |
| 18 | Limits & Restrictions |

## Word Types Reference

| Type | Description | Example |
|------|-------------|---------|
| `noun` | Person, place, thing, idea | analysis, environment |
| `verb` | Action or state | analyse, evaluate |
| `adjective` | Describes a noun | analytical, significant |
| `adverb` | Describes a verb/adjective | theoretically, significantly |

## Tips for Good Entries

1. **Definitions**: Keep them clear and concise (1 sentence)
2. **Turkish**: Include common synonyms separated by commas
3. **Examples**: Use realistic sentences that show the word in context
4. **Word families**: Group related words (analyse, analysis, analyst, analytical)

## Validation Checklist

Before saving, verify:

- [ ] JSON syntax is valid (no missing commas, brackets)
- [ ] All required fields are present
- [ ] `----` placeholder is in the example sentence
- [ ] Word type is one of: noun, verb, adjective, adverb
- [ ] Category ID is unique (if creating new category)
- [ ] Update `totalWords` count in the root object

## Testing

After adding words:

1. Open `flashcards.html` in browser
2. Select the category from the filter
3. Verify the new word appears
4. Check that the example sentence displays correctly
