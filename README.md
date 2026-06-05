# College Enquiry Chatbot

## Overview

The College Enquiry Chatbot is a web-based application designed to automate responses to common student queries regarding admissions, courses, departments, fees, facilities, and other college-related information. The chatbot interacts with users through a simple interface and retrieves relevant information from a MySQL database.

To improve the user experience, the system incorporates fuzzy string matching, allowing it to understand queries even when users make spelling mistakes or use slightly different wording.

---

## Features

* Interactive chatbot interface
* College information retrieval
* Admission-related query support
* Course and department information
* Fee structure enquiries
* Fuzzy query matching
* Database-driven responses
* Fast and accurate information retrieval
* User-friendly web interface

---

## Technology Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask

### Database

* MySQL
* mysql-connector-python

### NLP & Query Matching

* FuzzyWuzzy
* Python-Levenshtein

---

## System Architecture

```text
User
 │
 ▼
Web Interface
 │
 ▼
Flask Application
 │
 ├──────────────► MySQL Database
 │
 ▼
Fuzzy Query Matching Engine
 │
 ▼
Relevant Response
```

---

## Project Structure

```text
College_Enquiry_Chatbot/
│
├── app.py
├── requirements.txt
├── database.sql
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── index.html
│   └── chat.html
│
├── chatbot/
│   ├── query_processor.py
│   ├── fuzzy_matcher.py
│   └── database_handler.py
│
└── README.md
```

---

## How It Works

1. User enters a question through the chatbot interface.
2. The query is processed by the Flask backend.
3. FuzzyWuzzy compares the query against stored keywords and patterns.
4. Relevant information is retrieved from the MySQL database.
5. The chatbot returns the most appropriate response.

---

## Database Functionality

The MySQL database stores information such as:

* Courses offered
* Department details
* Admission information
* Fee structure
* Faculty details
* Campus facilities
* Contact information

The chatbot dynamically retrieves and displays information based on user requests.

---

## Fuzzy Matching

The project uses:

* FuzzyWuzzy
* Python-Levenshtein

Benefits:

* Handles spelling mistakes
* Supports similar word matching
* Improves chatbot accuracy
* Enhances user experience

Example:

```text
User Input: "admision fee"

Matched Query: "admission fee"

Response: Admission fee details retrieved successfully.
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/College_Enquiry_Chatbot.git
cd College_Enquiry_Chatbot
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure MySQL Database

Create a database and import the SQL file:

```sql
CREATE DATABASE college_chatbot;
```

Import:

```bash
mysql -u root -p college_chatbot < database.sql
```

### Run Application

```bash
python app.py
```

Open your browser:

```text
http://localhost:5000
```

---

## Requirements

```text
Flask
mysql-connector-python
fuzzywuzzy
python-Levenshtein
```

---

## Future Enhancements

* AI-powered conversational responses
* Voice-based interaction
* Multi-language support
* Integration with college ERP systems
* Student authentication portal
* Generative AI chatbot integration

---

## Learning Outcomes

* Database Management Systems (DBMS)
* Flask Web Development
* MySQL Integration
* Query Processing
* Fuzzy String Matching
* Backend Development

---

## Author

**Avinash**

**Rohit**

College Enquiry Chatbot – DBMS & Flask-Based Web Application

---


