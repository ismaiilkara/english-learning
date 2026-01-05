---
description: IELTS test JSON dosyası oluşturma prompt'u
---

# IELTS Test JSON Generator Prompt

Bu prompt'u AI'a vererek IELTS test JSON dosyaları oluşturabilirsin.

---

## 🎯 PROMPT (Kopyala ve Yapıştır)

```
Sen bir IELTS test JSON dosyası oluşturucususun. Aşağıdaki formata uygun JSON dosyaları üretmelisin.

## GENEL YAPI

Her test dosyası şu yapıda olmalı:

{
    "id": [sayı],
    "name": "[Test adı]",
    "subtitle": "[Açıklama]",
    "type": "[academic veya general]",
    "reading": {
        "title": "[Reading Test başlığı]",
        "sections": [...]  // General Training için
        // VEYA
        "passages": [...]  // Academic için
    },
    "listening": {...}  // Opsiyonel
}

---

## GENERAL TRAINING FORMAT

General Training testleri 3 section içerir ve her section birden fazla passage içerebilir:

{
    "reading": {
        "title": "General Training Reading Test X",
        "sections": [
            {
                "id": 1,
                "title": "Section 1",
                "questionRange": "Questions 1-14",
                "passages": [
                    {
                        "id": "1a",
                        "title": "[Passage başlığı]",
                        "content": "<p>HTML formatında metin...</p>",
                        "questions": [...]
                    }
                ]
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

---

## ACADEMIC FORMAT

Academic testler doğrudan passages array'i kullanır:

{
    "reading": {
        "title": "Academic Reading Test X",
        "passages": [
            {
                "id": 1,
                "title": "[Passage başlığı]",
                "content": "<p>HTML formatında metin...</p>",
                "questions": [...]
            },
            {
                "id": 2,
                "title": "[Passage başlığı]",
                "content": "...",
                "questions": [...]
            },
            {
                "id": 3,
                "title": "[Passage başlığı]",
                "content": "...",
                "questions": [...]
            }
        ]
    }
}

---

## SORU TİPLERİ

### 1. TRUE/FALSE/NOT GIVEN (trueFalseNotGiven)
{
    "type": "trueFalseNotGiven",
    "instructions": "Do the following statements agree with the information given in the text?",
    "items": [
        {"number": 1, "statement": "[İfade metni]", "answer": "TRUE"},
        {"number": 2, "statement": "[İfade metni]", "answer": "FALSE"},
        {"number": 3, "statement": "[İfade metni]", "answer": "NOT GIVEN"}
    ]
}

### 2. YES/NO/NOT GIVEN (yesNoNotGiven)
{
    "type": "yesNoNotGiven",
    "instructions": "Do the following statements agree with the views of the writer?",
    "items": [
        {"number": 1, "statement": "[İfade metni]", "answer": "YES"},
        {"number": 2, "statement": "[İfade metni]", "answer": "NO"}
    ]
}

### 3. MATCHING (matching)
{
    "type": "matching",
    "instructions": "Look at the descriptions A-E. For which description are the following statements true?",
    "options": ["A", "B", "C", "D", "E"],
    "items": [
        {"number": 1, "statement": "[İfade metni]", "answer": "D"},
        {"number": 2, "statement": "[İfade metni]", "answer": "A"}
    ]
}

### 4. MATCH PEOPLE (matchPeople)
ÖNEMLİ: "text" alanı kullan, "statement" değil!

{
    "type": "matchPeople",
    "instructions": "Match each statement with the correct person, A-D.",
    "people": [
        {"letter": "A", "name": "Susan Jebb"},
        {"letter": "B", "name": "Kim Roberts"},
        {"letter": "C", "name": "Janice Burberry"},
        {"letter": "D", "name": "Seema Kennedy"}
    ],
    "items": [
        {"number": 32, "text": "[İfade metni]", "answer": "C"},
        {"number": 33, "text": "[İfade metni]", "answer": "A"}
    ]
}

### 5. MATCHING HEADINGS (matchingHeadings)
{
    "type": "matchingHeadings",
    "instructions": "Choose the correct heading for each section from the list of headings below.",
    "headings": [
        {"number": "i", "text": "[Başlık 1]"},
        {"number": "ii", "text": "[Başlık 2]"},
        {"number": "iii", "text": "[Başlık 3]"}
    ],
    "items": [
        {"number": 28, "section": "A", "answer": "vi"},
        {"number": 29, "section": "B", "answer": "iii"}
    ]
}

### 6. MULTIPLE CHOICE (multipleChoice)
{
    "type": "multipleChoice",
    "items": [
        {
            "number": 28,
            "question": "[Soru metni]",
            "options": [
                {"letter": "A", "text": "[Seçenek A]"},
                {"letter": "B", "text": "[Seçenek B]"},
                {"letter": "C", "text": "[Seçenek C]"},
                {"letter": "D", "text": "[Seçenek D]"}
            ],
            "answer": "D"
        }
    ]
}

### 7. SENTENCE COMPLETION - Fill in Blank (sentenceCompletion)
Endings OLMADAN kullan:

{
    "type": "sentenceCompletion",
    "instructions": "Complete the sentences below. Choose ONE WORD ONLY from the text for each answer.",
    "items": [
        {"number": 15, "sentence": "You may have to help the client if they have a .................... that makes this challenging.", "answer": "condition"},
        {"number": 16, "sentence": "The next task may be cooking breakfast and it's nice to have some ....................", "answer": "conversation"}
    ]
}

### 8. SENTENCE COMPLETION - With Endings (sentenceCompletion + endings)
{
    "type": "sentenceCompletion",
    "instructions": "Complete each sentence with the correct ending, A-G, below.",
    "endings": [
        {"letter": "A", "text": "is funded__(continued)__"},
        {"letter": "B", "text": "another ending text"}
    ],
    "items": [
        {"number": 1, "text": "The start of sentence...", "answer": "A"}
    ]
}

### 9. NOTE COMPLETION (noteCompletion)
{
    "type": "noteCompletion",
    "instructions": "Complete the notes below. Choose ONE WORD ONLY from the text for each answer.",
    "title": "The best way to resign",
    "items": [
        {"number": 22, "note": "Avoid all .................... to resign in an angry way.", "answer": "temptations"},
        {"number": 23, "note": "request information on the type of .................... you will receive.", "answer": "reference"}
    ]
}

### 10. SUMMARY COMPLETION (summaryCompletion)
{
    "type": "summaryCompletion",
    "instructions": "Complete the summary below. Choose ONE WORD ONLY from the text for each answer.",
    "title": "The importance of the 'face with tears of joy'",
    "summary": "It is probable that before long, an emoji such as the 'face with tears of joy' will seem {33}. This is of interest as it tells us about developments in {34}.",
    "items": [
        {"number": 33, "answer": "dated"},
        {"number": 34, "answer": "society"}
    ]
}

---

## ÖNEMLİ KURALLAR

1. Content alanı HTML formatında olmalı: <p>, <strong>, <ul>, <li> kullan
2. matchPeople için "text" kullan, "statement" DEĞİL
3. Soru numaraları 1'den 40'a kadar sıralı olmalı
4. General Training: Section 1 (1-14), Section 2 (15-27), Section 3 (28-40)
5. JSON syntax hatası olmamalı - virgüllere dikkat!
6. Tüm cevaplar doğru olmalı

---

## ÖRNEK KULLANIM

"Cambridge IELTS 19 General Training Test 3'ü JSON formatına çevir. Test içeriği şöyle:

[Buraya test içeriğini yapıştır]

Yukarıdaki formata uygun JSON üret."
```

---

## 📝 Notlar

- Bu prompt'u ChatGPT, Claude veya başka bir AI'a verebilirsin
- Test içeriğini prompt'a ekle
- Üretilen JSON'u `ielts-tests/general/testX.json` veya `ielts-tests/testX.json` olarak kaydet
- Dosya adı sıralı olmalı (test1, test2, test3...)
