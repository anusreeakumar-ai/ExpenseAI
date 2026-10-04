\# 💰 ExpenseAI — AI-Powered Personal Expense Tracker



> \*\*Track smarter. Understand spending better. Manage your finances with AI.\*\*



ExpenseAI is an \*\*AI-powered personal expense management and financial assistant web application\*\* built with Python and Flask. It combines traditional expense tracking with \*\*machine learning, OCR-based data extraction, SMS/UPI transaction processing, spending analysis, and an AI-powered conversational assistant\*\* to provide users with a smarter way to manage their personal finances.



\---



\## 📌 Overview



Managing personal expenses manually can be time-consuming and makes it difficult to identify spending patterns.



\*\*ExpenseAI\*\* addresses this problem by bringing expense recording, categorization, bill management, transaction extraction, financial insights, and AI assistance into a single web application.



The system can accept expense information through multiple sources and process it into structured financial data. A machine-learning model helps categorize expenses, while the AI assistant provides conversational interaction and financial guidance.



\---



\## ✨ Key Features



\### 💸 Expense Management



\* Add and manage personal expenses

\* Edit and delete expenses

\* View expense history

\* Categorize expenses

\* Track spending across different categories

\* Dashboard-based expense visualization



\### 🤖 AI Financial Assistant



\* Conversational AI chatbot for financial queries

\* Natural-language interaction with the application

\* AI-assisted financial guidance and insights

\* Powered by a locally hosted LLM through \*\*Ollama\*\*



\### 🧠 Machine Learning Expense Categorization



ExpenseAI includes a trained machine-learning model for automatically classifying expenses into categories.



Example categories include:



\* 🍔 Food

\* 🚗 Travel

\* 💡 Utilities

\* 🧴 Personal Care

\* 🛍️ Shopping



The model is trained using the project's `expense\_data.csv` dataset and saved as:



```text

expense\_category\_model.pkl

```



\### 📷 OCR-Based Expense Extraction



The application supports extracting information from bills/receipts using \*\*Optical Character Recognition (OCR)\*\*, reducing the need for users to manually enter transaction information.



\### 📱 SMS / UPI Transaction Processing



ExpenseAI includes functionality for processing transaction information from SMS/UPI-related data and converting it into structured expense records.



This helps automate expense recording from transaction notifications.



\### 📊 Expense Dashboard



The dashboard provides users with an overview of their financial activity, helping them understand:



\* Total expenses

\* Spending categories

\* Recent transactions

\* Bills

\* Spending patterns



\### 🧾 Bill Management



Users can:



\* Add bills

\* View bills

\* Track bill information

\* Manage bill records



\### 🔮 Expense Prediction



The application includes a prediction interface for analyzing spending and providing future-oriented expense insights.



\### 👤 User Management



The application includes:



\* User registration

\* Login

\* Profile management

\* Settings

\* Personalized user experience



\---



\# 🏗️ System Architecture



```text

&#x20;                        ┌─────────────────────┐

&#x20;                        │        USER         │

&#x20;                        └──────────┬──────────┘

&#x20;                                   │

&#x20;                                   ▼

&#x20;                        ┌─────────────────────┐

&#x20;                        │   Flask Web App     │

&#x20;                        │      (app.py)       │

&#x20;                        └──────────┬──────────┘

&#x20;                                   │

&#x20;             ┌─────────────────────┼─────────────────────┐

&#x20;             │                     │                     │

&#x20;             ▼                     ▼                     ▼

&#x20;     ┌───────────────┐     ┌───────────────┐     ┌───────────────┐

&#x20;     │ Expense Input │     │  OCR / Bills  │     │ SMS / UPI    │

&#x20;     └───────┬───────┘     └───────┬───────┘     └───────┬───────┘

&#x20;             │                     │                     │

&#x20;             └─────────────────────┼─────────────────────┘

&#x20;                                   │

&#x20;                                   ▼

&#x20;                        ┌─────────────────────┐

&#x20;                        │ Data Processing \&   │

&#x20;                        │ Expense Management  │

&#x20;                        └──────────┬──────────┘

&#x20;                                   │

&#x20;                   ┌───────────────┴───────────────┐

&#x20;                   │                               │

&#x20;                   ▼                               ▼

&#x20;         ┌──────────────────┐             ┌──────────────────┐

&#x20;         │ ML Categorization│             │ Expense Database │

&#x20;         │      Model       │             │     Storage      │

&#x20;         └────────┬─────────┘             └────────┬─────────┘

&#x20;                  │                                │

&#x20;                  └───────────────┬────────────────┘

&#x20;                                  │

&#x20;                                  ▼

&#x20;                        ┌─────────────────────┐

&#x20;                        │ Analytics \&         │

&#x20;                        │ Financial Insights  │

&#x20;                        └──────────┬──────────┘

&#x20;                                   │

&#x20;                                   ▼

&#x20;                        ┌─────────────────────┐

&#x20;                        │ AI Finance Assistant│

&#x20;                        │       Ollama        │

&#x20;                        └──────────┬──────────┘

&#x20;                                   │

&#x20;                                   ▼

&#x20;                        ┌─────────────────────┐

&#x20;                        │ User Dashboard \&    │

&#x20;                        │ Recommendations    │

&#x20;                        └─────────────────────┘

```



\---



\# 🧠 Machine Learning Pipeline



The expense categorization component uses a supervised machine-learning approach.



```text

Expense Description

&#x20;       │

&#x20;       ▼

Text Preprocessing

&#x20;       │

&#x20;       ▼

Feature Representation

&#x20;       │

&#x20;       ▼

Trained ML Classifier

&#x20;       │

&#x20;       ▼

Predicted Category

&#x20;       │

&#x20;       ▼

Food / Travel / Utilities /

Personal Care / Shopping

```



The training data is stored in:



```text

expense\_data.csv

```



Example:



```csv

item,category

milk,Food

banana,Food

bus ticket,Travel

petrol,Travel

electricity bill,Utilities

soap,Personal Care

shirt,Shopping

```



The trained model is stored as:



```text

expense\_category\_model.pkl

```



The training script is:



```text

train\_model.py

```



\---



\# 🤖 AI Assistant



ExpenseAI also integrates a conversational AI assistant using \*\*Ollama\*\*, allowing users to interact with their financial information through natural language.



Example interactions:



```text

User:

How much did I spend on food?



AI:

Your food expenses for the selected period are ...



User:

Which category takes most of my spending?



AI:

Based on your recorded expenses, ...



User:

How can I reduce my monthly expenses?



AI:

Here are some areas where you could potentially reduce spending...

```



Using a locally hosted LLM allows the application to experiment with AI-assisted financial interaction without requiring every conversation to be sent to a cloud AI API.



\---



\# 📷 OCR Processing



ExpenseAI uses OCR technology to reduce manual data entry.



```text

Receipt / Bill

&#x20;     │

&#x20;     ▼

&#x20;  OCR Engine

&#x20;     │

&#x20;     ▼

Extracted Text

&#x20;     │

&#x20;     ▼

Information Processing

&#x20;     │

&#x20;     ▼

Structured Expense

&#x20;     │

&#x20;     ▼

Expense Database

```



This makes the system more convenient for users who receive expenses primarily through physical or digital bills.



\---



\# 📱 SMS / UPI Expense Processing



The application also includes an SMS-related workflow for extracting transaction information.



```text

Transaction SMS

&#x20;      │

&#x20;      ▼

Message Processing

&#x20;      │

&#x20;      ▼

Transaction Information

&#x20;      │

&#x20;      ▼

Expense Extraction

&#x20;      │

&#x20;      ▼

Category Assignment

&#x20;      │

&#x20;      ▼

Expense Record

```



This provides a pathway toward more automated personal expense tracking.



\---



\# 📊 Application Modules



| Module             | Purpose                                     |

| ------------------ | ------------------------------------------- |

| Authentication     | User registration and login                 |

| Dashboard          | Financial overview and spending information |

| Expense Management | Add, edit, view and manage expenses         |

| Bill Management    | Add and manage bills                        |

| OCR                | Extract information from bills/receipts     |

| SMS Processing     | Process transaction messages                |

| ML Categorization  | Automatically classify expenses             |

| AI Chatbot         | Conversational financial assistance         |

| Prediction         | Expense prediction/analysis                 |

| Profile            | User profile management                     |

| Settings           | Application/user configuration              |



\---



\# 🛠️ Technology Stack



\### Backend



\* \*\*Python\*\*

\* \*\*Flask\*\*



\### Machine Learning



\* \*\*Scikit-learn\*\*

\* \*\*Pandas\*\*

\* \*\*NumPy\*\*

\* Serialized ML model using \*\*Pickle\*\*



\### Generative AI



\* \*\*Ollama\*\*

\* Local Large Language Model



\### OCR



\* \*\*Tesseract OCR\*\*

\* Python OCR integration



\### Frontend



\* \*\*HTML5\*\*

\* \*\*CSS3\*\*

\* \*\*JavaScript\*\*

\* Jinja2 Templates



\### Database



\* SQLite



\### Development Tools



\* Visual Studio Code

\* Git

\* GitHub

\* Python Virtual Environment



\---



\# 📂 Project Structure



```text

ExpenseAI/

│

├── app.py

├── database.py

├── train\_model.py

├── expense\_data.csv

├── expense\_category\_model.pkl

├── .gitignore

│

├── static/

│   ├── style.css

│   └── js/

│       └── animation.js

│

└── templates/

&#x20;   ├── layout.html

&#x20;   ├── landing.html

&#x20;   ├── login.html

&#x20;   ├── register.html

&#x20;   ├── dashboard.html

&#x20;   ├── add\_expense.html

&#x20;   ├── edit\_expense.html

&#x20;   ├── view\_expenses.html

&#x20;   ├── add\_bill.html

&#x20;   ├── bills.html

&#x20;   ├── bill\_view.html

&#x20;   ├── chatbot.html

&#x20;   ├── prediction.html

&#x20;   ├── sms.html

&#x20;   ├── offers.html

&#x20;   ├── profile.html

&#x20;   └── settings.html

```



\---



\# ⚙️ Installation \& Setup



\## 1. Clone the repository



```bash

git clone https://github.com/Adonna222/ExpenseAI.git

cd ExpenseAI

```



\## 2. Create a virtual environment



Windows:



```bash

python -m venv .venv

```



Activate it:



```bash

.venv\\Scripts\\activate

```



\---



\## 3. Install dependencies



If `requirements.txt` is available:



```bash

pip install -r requirements.txt

```



If not, install the dependencies required by the project and generate it with:



```bash

pip freeze > requirements.txt

```



\---



\## 4. Install Tesseract OCR



Install \*\*Tesseract OCR\*\* on your system and ensure the executable is available to the application.



If your application specifies a Tesseract executable path in `app.py`, update it according to your local installation.



\---



\## 5. Install Ollama



Install Ollama and download a compatible local language model.



Example:



```bash

ollama pull qwen2.5:3b

```



Start Ollama if it is not already running:



```bash

ollama serve

```



\---



\## 6. Train the expense categorization model



The repository includes the training script:



```bash

python train\_model.py

```



This uses:



```text

expense\_data.csv

```



to train the expense categorization model.



The generated model is saved as:



```text

expense\_category\_model.pkl

```



\---



\## 7. Run ExpenseAI



Start the Flask application:



```bash

python app.py

```



Then open the local URL displayed by Flask in your browser.



\---



\# 🔐 Security



Sensitive information should \*\*never be committed to GitHub\*\*.



The repository excludes:



```text

.env

\*.db

\*.sqlite

uploads/

\_\_pycache\_\_/

```



API keys, passwords, tokens, and other credentials should be stored using environment variables rather than directly inside source code.



\---



\# 🎯 Project Objectives



ExpenseAI was developed with the following objectives:



\* Automate personal expense tracking

\* Reduce manual expense entry

\* Automatically categorize transactions

\* Extract expense information from bills

\* Process transaction messages

\* Provide visual spending insights

\* Integrate Generative AI into personal finance

\* Explore local LLM-based financial assistance

\* Build a unified personal finance management platform



\---



\# 🔮 Future Enhancements



Potential future improvements include:



\* 📈 Advanced spending forecasting

\* 🧠 More accurate ML-based categorization

\* 💳 Bank account integration

\* 📱 Dedicated Android/iOS application

\* 🔔 Smart bill payment reminders

\* 📊 Advanced financial analytics

\* 💡 Personalized saving recommendations

\* 🔍 Anomaly and unusual-spending detection

\* 📑 Improved receipt understanding using vision-language models

\* 🔐 Enhanced authentication and security

\* ☁️ Cloud deployment

\* 🗣️ Voice-based financial assistant

\* 📅 Monthly and yearly financial reports



\---



\# 💡 Why ExpenseAI?



Traditional expense trackers primarily focus on recording transactions.



ExpenseAI attempts to go a step further by combining:



```text

Expense Tracking

&#x20;      +

Machine Learning

&#x20;      +

OCR

&#x20;      +

SMS/UPI Processing

&#x20;      +

Generative AI

&#x20;      +

Financial Analytics

```



This creates a foundation for an intelligent personal financial management system rather than simply a digital expense diary.



\---



\# 👩‍💻 Developer



\*\*Adonna222\*\*



B.Tech Artificial Intelligence \& Data Science

Vimal Jyothi Engineering College



\### Areas of Interest



\* Artificial Intelligence

\* Machine Learning

\* Generative AI

\* Agentic AI

\* Data Science

\* Intelligent Applications



\---



\# ⭐ Project Status



\*\*Status:\*\* Active Development 🚧



ExpenseAI is a portfolio project focused on exploring the integration of \*\*AI/ML, automation, OCR, and conversational AI\*\* into personal finance management.



\---



\## 📜 License



This project is intended for educational and portfolio purposes.



A formal open-source license can be added in future releases.



