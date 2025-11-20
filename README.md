# **Digital Doppelgänger Agent**

A multi-agent AI system that learns a user’s writing style from sample text and generates new content that matches their tone, vocabulary, and personality. Built as a capstone project for the Kaggle x Google Agents Intensive 2025 (Freestyle Track).

---

## **Overview**

People often struggle to maintain a consistent writing style across emails, posts, notes, and long-form content. This project builds a personalized “Digital Doppelgänger” that analyzes a user’s writing samples and creates a writing persona capable of generating new text in the same voice.

Unlike simple prompt-based style mimicry, this system uses coordinated agents, evaluation loops, and a memory-driven approach to produce highly personalized, consistent output.

---

## **Core Features**

### **1. Persona Builder Agent**

Extracts writing features such as:

* Tone and emotional signature
* Vocabulary patterns
* Sentence structure and rhythm
* Formality level
* Writing quirks and stylistic tendencies

Outputs a structured “persona profile.”

### **2. Task Executor Agent**

Generates new content using the persona profile.
Supports multiple tasks:

* Emails
* Social media posts
* Essays
* Summaries
* Creative writing

### **3. Evaluator Agent**

Scores the generated output based on:

* Style similarity
* Tone alignment
* Clarity
* Coherence

Improves final output using feedback.

### **Additional Components**

* **Memory Bank:** Stores persona profiles for reuse
* **Logging & Observability:** Tracks agent decisions for transparency
* **Notebook Interface:** The entire workflow is implemented in a Kaggle Notebook for reproducibility

---

## **Architecture**

```
User Text Samples
        ↓
Persona Builder Agent
        ↓
Persona Profile
        ↓
Task Executor Agent → Draft Output
        ↓
Evaluator Agent → Scored + Refined Output
        ↓
Final Output (User-style text)
```

---

## **Tech Stack**

* Python
* LangChain / Agents Framework (or custom agent logic)
* Text preprocessing & embeddings
* Kaggle Notebook environment
* GitHub for version control and documentation

---

## **Use Cases**

* Content creators maintaining tone consistency
* Professionals writing emails/posts in a uniform style
* Students generating long-form writing assistance
* Personalized AI assistants
* UX writing tools
* Resume or profile tone matching

---

## **Project Goals**

* Build a working multi-agent system
* Demonstrate style extraction and persona modeling
* Produce personalized writing generation
* Provide transparency through evaluation metrics
* Create a clean, reproducible Kaggle Notebook

---

## **Repository Structure**

```
digital-doppelganger-agent/
│
├── src/
│   └── placeholder.txt
├── data/
│   └── placeholder.txt
└── README.md
```

---

## **Status**

**In Progress**
The notebook and agent modules will be added during the development timeline (Nov 19–Dec 1).

---

## **License**

Open for learning and non-commercial use.

---
