# IELTS Answer Explanation Writing Guide

## Purpose
Write clear, educational explanations that help students understand WHY each answer is correct by referencing specific evidence from the passage.

---

## General Principles

1. **Always quote the text** - Include the exact words/phrases from the passage that support the answer
2. **Explain the logic** - Show how the quoted text leads to the correct answer
3. **Be concise** - Keep explanations to 1-3 sentences
4. **Use simple language** - Avoid complex vocabulary; students are learning English
5. **Highlight key synonyms** - Point out when question words are paraphrased in the passage

---

## Question Type-Specific Instructions

### TRUE/FALSE/NOT GIVEN

**TRUE:**
- Quote the sentence that confirms the statement
- Show how it matches the statement's meaning
- Format: `The text states '[QUOTE]'. This confirms/supports the statement that [RESTATE].`

**FALSE:**
- Quote the sentence that contradicts the statement
- Explain the contradiction clearly
- Format: `The text states '[QUOTE]', which contradicts the statement. The passage says [X], not [Y].`

**NOT GIVEN:**
- Explain what the text DOES say about the topic
- Clarify what information is MISSING
- Format: `The text mentions [RELATED INFO] but does not state whether [STATEMENT CLAIM]. This information is not provided.`

**Example:**
```json
{
    "statement": "The museum is open on weekends.",
    "answer": "TRUE",
    "explanation": "The text states 'Visitors can explore the museum every Saturday and Sunday from 10am to 6pm.' This confirms the museum is open on weekends."
}
```

---

### MATCHING (Activities, People, Locations, etc.)

- Identify the KEY WORD in the question
- Quote the matching phrase from the correct option
- Show the connection between question and answer

**Format:** `In [Option Letter] ([Option Name]), the text states '[QUOTE]'. [KEY WORD] matches [QUOTED PHRASE].`

**Example:**
```json
{
    "statement": "You may get minor injuries",
    "answer": "H",
    "explanation": "In Mountain boarding (H), the text mentions 'a few bruises' after practice. Bruises are minor injuries."
}
```

---

### MULTIPLE CHOICE

- Explain why the correct answer is right
- Optionally explain why ONE wrong answer is wrong (most tempting distractor)
- Reference specific text evidence

**Format:** `The text states '[QUOTE]', which matches option [LETTER]. Option [WRONG] is incorrect because [REASON].`

**Example:**
```json
{
    "question": "What does the writer say about scribes?",
    "answer": "B",
    "explanation": "The text states scribes 'wrote about everything from grain stocks to tax records.' The phrase 'everything from...to' indicates varied topics (Option B). Option C is wrong because 'most scribes were men from privileged backgrounds.'"
}
```

---

### SENTENCE/SUMMARY COMPLETION (Fill-in-the-blank)

- Quote the relevant sentence from the passage
- Show the grammatical fit if relevant
- Highlight paraphrasing between question and text

**Format:** `The text states '[QUOTE containing the answer]'. The word '[ANSWER]' fits the blank because [REASON].`

**Example:**
```json
{
    "sentence": "Managers do not have enough relevant ________",
    "answer": "knowledge",
    "explanation": "The text states 'managers of small businesses have an inadequate knowledge of health and safety issues.' Inadequate = not enough."
}
```

---

### NOTES COMPLETION

- Same as sentence completion
- Reference the specific paragraph or section
- Explanations are stored in a separate `explanations` object keyed by question number

**Format for explanations object:**
```json
"explanations": {
    "15": "The text states 'events including festivals bringing together choirs.' Festivals is the type of event mentioned.",
    "16": "The text states 'ensuring it does not exceed its budget.' Keeping to = not exceeding."
}
```

---

## Key Vocabulary for Explanations

| To express agreement | To express contradiction | To express absence |
|---------------------|-------------------------|-------------------|
| confirms | contradicts | does not mention |
| supports | differs from | no information about |
| matches | the opposite of | not stated |
| aligns with | conflicts with | not addressed |

---

## Checklist Before Finalizing

- [ ] Did I quote the exact text from the passage?
- [ ] Did I explain the connection between quote and answer?
- [ ] Is my explanation under 3 sentences?
- [ ] Did I use simple, clear language?
- [ ] Did I highlight any synonyms/paraphrasing?

---

## JSON Structure Examples

### For items with individual explanations:
```json
{
    "number": 1,
    "statement": "The company was founded in 1990.",
    "answer": "FALSE",
    "explanation": "The text states 'established in 1985', not 1990. This contradicts the statement."
}
```

### For notes/summary with shared explanations object:
```json
{
    "type": "notes",
    "answers": {
        "15": "festivals",
        "16": "budget"
    },
    "explanations": {
        "15": "The text mentions 'events, including festivals' as activities organized by the service.",
        "16": "The manager must ensure the service 'does not exceed its budget' - keeping to = not exceeding."
    }
}
```
