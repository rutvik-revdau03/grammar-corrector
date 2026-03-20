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

### 4. Run the Server

```
uvicorn app.main:app --reload
```

---

## API Documentation

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoint

### POST /api/correct

#### Request Body

```
{
  "text": "I has a apple"
}
```

#### Response

```
{
  "original": "I has a apple",
  "corrected": "I have an apple"
}
```

---

## Validations

* Input cannot be empty
* Maximum length: 1000 characters
* Only valid characters allowed

---

## Future Enhancements

* File upload support
* Batch correction
* Authentication
* Frontend integration

