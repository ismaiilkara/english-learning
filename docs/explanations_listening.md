# IELTS Listening Answer Explanation Writing Guide

## Purpose
Write clear, educational explanations for Listening test answers that help students understand:
1. **What was said** - The exact words/phrases spoken that give the answer
2. **Why the correct answer is correct** - Direct quote from the transcript
3. **Why wrong answers are wrong** - Whether they were distractors, not mentioned, or contradicted

---

## Key Difference from Reading Explanations

In Listening tests, **distractors** are common - wrong answers are often MENTIONED in the audio but are incorrect because:
- They refer to something else
- They are corrected or changed by the speaker
- They describe a different person/place/time
- The speaker rejects or negates them

Always explain WHY wrong options are wrong when they appear in the audio.

---

## General Principles

1. **Quote the transcript** - Use the exact words spoken
2. **Include speaker context** - Note WHO said it (Speaker A, the woman, etc.)
3. **Explain distractors** - Why tempting wrong answers are incorrect
4. **Note corrections** - Speakers often change their mind or correct themselves
5. **Be concise** - Keep explanations to 2-4 sentences

---

## Question Type-Specific Instructions

### MULTIPLE CHOICE

**Format:**
```json
{
    "number": 1,
    "question": "What time does the library close on Saturdays?",
    "options": [
        {"letter": "A", "text": "5pm"},
        {"letter": "B", "text": "6pm"},
        {"letter": "C", "text": "7pm"}
    ],
    "answer": "B",
    "explanation": "The speaker says 'We close at 6pm on Saturdays.' Option A (5pm) is mentioned as the weekday closing time. Option C (7pm) is not mentioned at all."
}
```

**Instructions:**
- Quote the sentence that gives the answer
- Explain why EACH wrong option is wrong:
  - Was it mentioned in a different context?
  - Was it not mentioned at all?
  - Was it corrected/changed?

---

### FORM/NOTE COMPLETION (Fill-in-the-blank)

**Format:**
```json
{
    "number": 15,
    "answer": "parking",
    "explanation": "The speaker says 'The main problem is parking - there's nowhere to leave your car.' The word 'parking' directly fills the blank asking about the main problem."
}
```

**Instructions:**
- Quote the exact phrase containing the answer word
- Note any spelling variations if relevant
- Mention if the speaker spells out the word

---

### MATCHING

**Format:**
```json
{
    "number": 21,
    "statement": "is concerned about the cost",
    "answer": "B",
    "explanation": "Speaker B (the man) says 'I'm worried it might be too expensive for us.' Option A (the woman) mentions cost but says 'the price seems reasonable.' The concern belongs to Speaker B."
}
```

**Instructions:**
- Identify which speaker/option matches
- Quote what that speaker said
- Explain why other options don't match (especially if they mention similar topics)

---

### MAP/PLAN LABELLING

**Format:**
```json
{
    "number": 11,
    "location": "Reception",
    "answer": "G",
    "explanation": "The guide says 'When you enter through the main door, the reception desk is directly in front of you' - this corresponds to position G on the map. Position F is mentioned as the café, which is 'to your left as you enter.'"
}
```

**Instructions:**
- Quote directional language (left, right, opposite, next to, behind)
- Reference landmarks mentioned (main entrance, stairs, etc.)
- Explain why nearby positions are wrong

---

### TRUE/FALSE/NOT GIVEN (Listening variant)

**Format:**
```json
{
    "number": 31,
    "statement": "The museum was opened in 1985.",
    "answer": "FALSE",
    "explanation": "The speaker says 'The museum was established in 1975, not 1985 as many people think.' The speaker directly contradicts the date and even acknowledges the common misconception."
}
```

**TRUE:** Quote confirms the statement
**FALSE:** Quote contradicts the statement
**NOT GIVEN:** Explain what IS said about the topic, note what's missing

---

## Handling Common Listening Traps

### 1. Self-Correction
Speakers often change their answer:
```
"The meeting is on Tuesday... sorry, I mean Wednesday."
→ Answer: Wednesday (NOT Tuesday)
→ Explanation: "The speaker initially says 'Tuesday' but immediately corrects to 'Wednesday.' Always listen for corrections - the FINAL answer given is correct."
```

### 2. Distractors (Wrong Options Mentioned)
```
"Some people prefer the 9am class, but the 11am session is actually better for beginners."
→ Answer: 11am
→ Explanation: "Both times are mentioned. 9am is what 'some people prefer' but 11am is recommended 'for beginners' - which matches what the question asks about."
```

### 3. Negation
```
"We don't offer refunds, but exchanges are possible."
→ If question asks about refunds: Answer is NO/FALSE
→ Explanation: "The speaker explicitly says 'We don't offer refunds.' The mention of exchanges is a distractor."
```

### 4. Different Speakers
```
Woman: "I think we should take the train."
Man: "Actually, the bus is cheaper and faster."
→ Answer depends on WHO the question asks about
→ Explanation: "The woman suggests the train, but the man prefers the bus. The question asks about the man's preference, so 'bus' is correct."
```

### 5. Similar-Sounding Words
```
"The price is fifty pounds" (not "fifteen")
→ Explanation: "The speaker clearly says 'fifty' (5-0) not 'fifteen' (1-5). Listen carefully to distinguish similar numbers."
```

---

## Explanation Structure Template

### For Multiple Choice:
```
"[QUOTE FROM AUDIO]."

Correct answer: [X] because [reason].

Why other options are wrong:
- Option [A]: [mentioned as X / not mentioned / contradicted by Y]
- Option [B]: [mentioned as X / not mentioned / contradicted by Y]
```

### For Fill-in-the-blank:
```
"The speaker says '[QUOTE containing answer word].'

The answer '[WORD]' fits because [grammatical/contextual reason]."
```

### For Matching:
```
"[Speaker/Option X] says '[QUOTE].'

This matches the statement about [topic] because [reason].
[Other speaker] discusses [topic] differently: '[their quote].'"
```

---

## JSON Structure Examples

### Multiple Choice with Distractors:
```json
{
    "number": 5,
    "question": "What does the woman decide to buy?",
    "options": [
        {"letter": "A", "text": "a laptop"},
        {"letter": "B", "text": "a tablet"},
        {"letter": "C", "text": "a desktop computer"}
    ],
    "answer": "B",
    "explanation": "The woman says 'I was thinking about a laptop, but actually a tablet would be more portable. I'll go with that.' Option A (laptop) is initially considered but rejected. Option C (desktop) is not mentioned."
}
```

### Form Completion with Spelling:
```json
{
    "number": 8,
    "answer": "Fitzgerald",
    "explanation": "The caller spells out their name: 'It's Fitzgerald - F-I-T-Z-G-E-R-A-L-D.' When names are spelled, write exactly what is spelled."
}
```

### Matching with Multiple Speakers:
```json
{
    "number": 23,
    "statement": "wants to improve their speaking skills",
    "answer": "A",
    "optionLabels": {"A": "Student 1", "B": "Student 2", "C": "Both students"},
    "explanation": "Student 1 says 'My main goal is to become more fluent in conversation.' Student 2 focuses on 'writing better essays.' Only Student 1 mentions speaking/conversation skills."
}
```

---

## Checklist Before Finalizing

- [ ] Did I quote the exact words from the transcript?
- [ ] Did I explain why the correct answer is correct?
- [ ] Did I address why wrong options are wrong (especially if mentioned)?
- [ ] Did I note any speaker corrections or changes?
- [ ] Did I identify which speaker said what (if multiple speakers)?
- [ ] Is my explanation under 4 sentences?
- [ ] Did I highlight any tricky distractors?

---

## Important Notes for Agents

1. **You need the transcript** - Without the listening transcript, you cannot write accurate explanations. Request or locate the transcript first.

2. **Mark unclear audio** - If transcript is unavailable, note: "Explanation requires transcript. The answer is [X] based on [general reasoning]."

3. **Use timestamps if available** - Help students know WHERE to listen: "At approximately 2:30, the speaker says..."

4. **Explain spelling** - For names, places, or unusual words, note if they are spelled out in the audio.

5. **Note accents/speed** - If relevant, mention that a section is spoken quickly or with a particular accent that might cause confusion.
