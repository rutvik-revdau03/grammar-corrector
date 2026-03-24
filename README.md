# Grammar Correction API

## Overview

This project is a backend API built using FastAPI that corrects grammatical errors in text input using the LanguageTool library.

---

## Features

* Grammar and spelling correction
* FastAPI-based REST API
* Input validation (empty, length, invalid characters)
* Modular project structure
* No database (lightweight and fast)

---

## Tech Stack

* Python 3.x
* FastAPI
* Uvicorn
* language-tool-python
* Pydantic

---

## Project Structure

```
grammar-corrector/
│
├── app/
│   ├── main.py
│   ├── routes/
│   │   └── grammar.py
│   ├── services/
│   │   └── grammar_service.py
│   ├── schemas/
│   │   └── grammar_schema.py
│   ├── core/
│   │   └── validator.py
│
├── requirements.txt
├── README.md
└── PROJECT-DOCS.md
```

---

## Setup Instructions

### 1. Clone the Repository

```
git clone <your-repo-url>
cd grammar-corrector
```

### 2. Create Virtual Environment

```
python -m venv venv
```

Activate:

* Windows:

```
venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Run the Server (API)

```bash
uvicorn app.main:app --reload
```

---

## Usage (Terminal/CLI)

You can also use the tool directly from your terminal:

*   **Interactive Mode:**
    ```bash
    python -m app.cli
    ```
*   **File Processing:**
    ```bash
    python -m app.cli --file test_sentences.txt
    ```
*   **Direct Argument:**
    ```bash
    python -m app.cli --text "I has a apple"
    ```

---

## API Documentation

Open in browser: `http://127.0.0.1:8000/docs`

### Endpoints

#### POST /api/correct
*   Input: `{"text": "string"}`
*   Output: Corrected text

#### POST /api/correct-file
*   Input: `.txt` file upload
*   Output: JSON list of all corrected lines from the file

---

## Validations

* Input cannot be empty
* Maximum length: 1000 characters
* Only valid characters allowed

---

## Future Enhancements

* Multiple language support
* AI-powered deep correction
* User authentication
