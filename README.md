# 💰 ExpenseAI — AI-Powered Personal Expense Tracker

> **Track smarter. Understand spending better. Manage your finances with AI.**

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-000000?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-black?style=flat&logo=ollama&logoColor=white)](https://ollama.ai/)
[![Tesseract OCR](https://img.shields.io/badge/OCR-Tesseract-blue?style=flat)](https://github.com/tesseract-ocr/tesseract)

**ExpenseAI** is a comprehensive personal expense management and financial assistant web application built with Python and Flask. It pairs core budget tracking with **machine learning categorization, OCR-based receipt extraction, automated SMS/UPI transaction parsing, predictive spending analysis, and an offline local AI conversational assistant**.

---

## 📌 Overview

Manual expense tracking is tedious and makes spotting spending patterns difficult. **ExpenseAI** consolidates multiple expense ingestion pipelines into a single platform:

- Ingest data via manual inputs, receipt images (OCR), or SMS/UPI notifications.
- Automatically classify transaction descriptions using a trained ML pipeline.
- Chat with an offline, privacy-first local financial assistant powered by **Ollama**.

---

## ✨ Key Features

### 💸 Core Expense & Bill Management
- **Transaction Tracking:** Record, modify, categorize, and delete daily income and expenses.
- **Bill Management:** Track recurring and upcoming bills with dedicated views.
- **Visual Analytics:** Interactive dashboards displaying category distributions, monthly totals, and spending history.

### 🤖 Local AI Financial Assistant
- Offline conversational queries powered by local LLMs via **Ollama**.
- Natural language queries such as *"How much did I spend on food this month?"* or *"Where can I optimize expenses?"*
- Privacy-first architecture: no financial records are transmitted to third-party cloud APIs.

### 🧠 Machine Learning Expense Categorization
- Supervised classification model trained on `expense_data.csv`.
- Automatically maps items to categories: 🍔 **Food**, 🚗 **Travel**, 💡 **Utilities**, 🧴 **Personal Care**, and 🛍️ **Shopping**.
- Serialized pipeline stored as `expense_category_model.pkl`.

### 📷 OCR Receipt Scanner
- Uses **Tesseract OCR** to extract transaction items, dates, and amounts directly from uploaded paper or digital receipts.

### 📱 SMS & UPI Transaction Parser
- Converts unformatted bank SMS messages and UPI payment confirmations into structured expense records automatically.

### 🔮 Predictive Insights
- Evaluates historical spending data to project future expenses and prevent budget overruns.

---

## 🏗️ System Architecture

```text
                        ┌─────────────────────┐
                        │        USER         │
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │   Flask Web App     │
                        │      (app.py)       │
                        └──────────┬──────────┘
                                   │
             ┌─────────────────────┼─────────────────────┐
             │                     │                     │
             ▼                     ▼                     ▼
     ┌───────────────┐     ┌───────────────┐     ┌───────────────┐
     │ Expense Input │     │  OCR / Bills  │     │   SMS / UPI   │
     └───────┬───────┘     └───────┬───────┘     └───────┬───────┘
             │                     │                     │
             └─────────────────────┼─────────────────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │  Data Processing &  │
                        │ Expense Management  │
                        └──────────┬──────────┘
                                   │
                   ┌───────────────┴───────────────┐
                   │                               │
                   ▼                               ▼
         ┌──────────────────┐             ┌──────────────────┐
         │ ML Categorization│             │ Expense Database │
         │      Model       │             │   (SQLite / DB)  │
         └────────┬─────────┘             └────────┬─────────┘
                  │                                │
                  └───────────────┬────────────────┘
                                  │
                                  ▼
                        ┌─────────────────────┐
                        │ Analytics & Insights│
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │ AI Finance Assistant│
                        │  (Ollama Local LLM) │
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │   User Dashboard    │
                        └─────────────────────┘
