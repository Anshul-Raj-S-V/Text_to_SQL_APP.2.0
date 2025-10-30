#  Text-to-SQL Chat Assistant (PostgreSQL + Groq LLaMA 3.3)🧠

Transform natural language into real-time SQL queries with the power of **LLMs and PostgreSQL**!
This intelligent Streamlit app lets users interact with their database conversationally — no SQL knowledge required.

---
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-orange.svg)](https://streamlit.io)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16.x-blue.svg)](https://www.postgresql.org)
[![Groq](https://img.shields.io/badge/Groq-LLaMA_3.3-purple.svg)](https://groq.com)
[![LangChain](https://img.shields.io/badge/LangChain-Framework-green.svg)](https://www.langchain.com)
[![dotenv](https://img.shields.io/badge/dotenv-Env_Config-lightgrey.svg)](https://pypi.org/project/python-dotenv/)

--
### 🚀 **Overview**

This project demonstrates how **LLMs (Large Language Models)** can simplify data access by converting **English questions into SQL queries**, running them automatically on a **PostgreSQL** database, and displaying results instantly.

Whether you’re a **data analyst**, **developer**, or **business user**, this assistant bridges the gap between **natural language** and **structured data**.

---

### 💡 **Key Features**

✅ Convert natural language to SQL queries using **Groq LLaMA 3.3**

✅ Connects to a **PostgreSQL database** for real-time query execution

✅ View and explore database results directly in the **Streamlit web interface**

✅ Handles both `SELECT` and data manipulation queries (`UPDATE`, `INSERT`, `DELETE`)

✅ Fully modular architecture with environment-based configuration

---

### 🧩 **Tech Stack**

| Layer                      | Technology Used                         | Description                                                       |
| -------------------------- | --------------------------------------- | ----------------------------------------------------------------- |
| 🧠 **LLM Engine**          | **Groq API (LLaMA 3.3 - 70B)**          | Translates human questions into optimized SQL queries             |
| 🗄️ **Database**           | **PostgreSQL**                          | Stores structured student data (NAME, COURSE, SECTION, MARKS)     |
| 💻 **Web Framework**       | **Streamlit**                           | Interactive web-based interface for the chatbot                   |
| ⚙️ **Integration & Tools** | **LangChain**, **dotenv**, **psycopg2** | Handles prompt chaining, environment variables, and DB connection |

---

### 🧪 **System Architecture**

```
User Input (English)
        ↓
Groq LLaMA 3.3 via LangChain
        ↓
SQL Query Generation
        ↓
PostgreSQL Database Execution
        ↓
Results Displayed in Streamlit UI
```

---

### 📚 **Setup Instructions**

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Anshul-Raj-S-V/Text_to_SQL_APP_2.0.git
cd Text_to_SQL_APP_2.0
```

#### 2️⃣ Create Virtual Environment & Install Dependencies

```bash
python -m venv venv
venv\Scripts\activate   # (Windows)
pip install -r requirements.txt
```

#### 3️⃣ Create a `.env` File

Create a `.env` file in your project root:

```bash
PG_HOST=localhost
PG_DATABASE=studentdb
PG_USER=postgres
PG_PASSWORD=yourpassword
PG_PORT=5432
GROQ_API_KEY=your_groq_api_key
```

#### 4️⃣ Run the App

```bash
streamlit run main.py
```

---

### 🧮 **Sample PostgreSQL Table**

```sql
CREATE TABLE STUDENT (
    NAME VARCHAR(25),
    COURSE VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
);

INSERT INTO STUDENT (NAME, COURSE, SECTION, MARKS) VALUES
('Student1', 'Data Science', 'A', 90),
('Student2', 'Data Science', 'B', 100),
('Student3', 'AI', 'A', 86),
('Student4', 'AI', 'B', 92),
('Student5', 'DevOps', 'A', 75),
('Student6', 'Machine Learning', 'B', 88),
('Student7', 'Data Analytics', 'A', 83),
('Student8', 'Cyber Security', 'B', 79),
('Student9', 'Robotics', 'A', 91),
('Student10', 'Cloud Computing', 'B', 87);
```

---

### 🌍 **Why It’s Relevant**

In modern enterprises, **data accessibility bottlenecks** slow down decision-making.
This project shows how **AI-driven natural language querying** can:

* Empower **non-technical users** to access insights directly
* Reduce dependency on data teams for simple queries
* Accelerate **analytics workflows** and improve **data democratization**
* Integrate seamlessly into **BI dashboards** or **enterprise applications**

---

### 💼 **Business Scope**

| Use Case                                | Description                                                  |
| --------------------------------------- | ------------------------------------------------------------ |
| 🏢 **Enterprise Analytics**             | Let business teams query company data conversationally       |
| 💻 **Data-as-a-Service Platforms**      | Embed Text-to-SQL for intuitive database exploration         |
| 🧬 **Healthcare / Finance / Education** | Simplify access to domain databases securely                 |
| 📈 **Internal Tools**                   | Improve productivity and lower the technical barrier to data |

---

### 🔮 **Future Enhancements**

* 🧠 Add **multi-table joins** and **schema awareness**
* 🎤 Integrate **voice input + text-to-speech**
* 📊 Visualize query results (charts, graphs)
* 🔐 Add **user authentication** for secure access

---

### 🏷️ **Tags**

`#AI` `#LangChain` `#PostgreSQL` `#Groq` `#TextToSQL`
`#LLM` `#Python` `#Streamlit` `#DataAnalytics` `#Innovation`

---

