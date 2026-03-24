# Project Documentation – Grammar Correction API

---

## 1. Introduction

The Grammar Correction API is a backend service built using FastAPI that processes user input text and returns a grammatically corrected version using the LanguageTool library.

---

## 2. Objectives

* Build a scalable backend API
* Implement grammar correction logic
* Apply input validation
* Maintain modular architecture
* Ensure production-level code quality

---

## 3. System Architecture

```
Client Request
     ↓
FastAPI Route
     ↓
Pydantic Validation
     ↓
Custom Validation Logic
     ↓
Grammar Service (LanguageTool)
     ↓
Response Returned
```

---

## 4. Modules Description

### 4.1 main.py

* Entry point of the application
* Initializes FastAPI app
* Includes routes

---

### 4.2 routes/grammar.py

* Handles API endpoints
* Connects request → service → response

---

### 4.3 services/grammar_service.py

* Core logic for grammar correction
* Uses language-tool-python

---

### 4.4 schemas/grammar_schema.py

* Defines request and response models
* Uses Pydantic for validation

---

### 4.5 core/validator.py

* Custom validations:

  * Empty input
  * Length check
  * Invalid characters

---

### 4.6 app/cli.py
* Multi-mode terminal interface:
  * --interactive: Real-time user prompt.
  * --text: Single-line CLI argument.
  * --file: Batch processing for text files.


## 5. Grammar Correction Engine

### Library: language-tool-python

#### Features:

* Grammar correction
* Spell checking
* Offline support
* Multiple language support

#### Working:

* Input text → analyzed → corrected output returned

---

## 6. Validations Implemented

| Validation      | Description              |
| --------------- | ------------------------ |
| Empty Input     | Prevent blank input      |
| Max Length      | Limit to 1000 chars      |
| Character Check | Restrict invalid symbols |

---

## 7. API Design

### Endpoints:

#### 7.1 POST /api/correct
* Correct single sentence via JSON

#### 7.2 POST /api/correct-file
* Upload `.txt` file for batch correction
* Returns a list of all line results

### Request (7.1):

```
{
  "text": "Incorrect sentence"
}
```

### Response:

```
{
  "original": "Incorrect sentence",
  "corrected": "Correct sentence"
}
```

---

## 8. Execution Flow

1. User sends request (API/CLI/Prompt)
2. Core services receive input
3. Validator checks rules
4. Grammar service processes text line(s)
5. Results returned to user

---

## 9. Error Handling

* 400 → Validation errors
* 500 → Internal server errors

---

## 10. Advantages

* Lightweight (no database)
* Fast processing
* Clean architecture
* Easy to scale

---

## 11. Future Scope

* Add database logging
* Multi-language support
* File upload API
* AI-based correction (advanced NLP)

---

## 12. Testing Strategy

* Unit testing for validation
* API testing via Swagger/Postman
* Edge case testing

---

## 13. Conclusion

This project demonstrates backend development skills using FastAPI, input validation, and integration of a third-party grammar correction library. It is suitable for real-world applications and technical interviews.
