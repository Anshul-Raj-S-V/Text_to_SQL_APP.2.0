import os
import psycopg2
from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


# ✅ 1. Load environment variables
load_dotenv()


# ======================================================
# 🧠 1. Function: Generate SQL from Natural Language
# ======================================================
def get_sql_query(user_query: str) -> str:
    """
    Converts a natural language question to an SQL query using Groq LLaMA.
    """
    prompt = ChatPromptTemplate.from_template("""
        You are an expert SQL translator.
        The PostgreSQL database contains a table STUDENT with columns:
        NAME, COURSE, SECTION, MARKS.

        Examples:
        Q: How many students are in total?
        A: SELECT COUNT(*) FROM STUDENT;

        Q: Show all students studying Data Science.
        A: SELECT * FROM STUDENT WHERE COURSE = 'Data Science';

        Q: Show students with marks above 90.
        A: SELECT * FROM STUDENT WHERE MARKS > 90;

        Only return the SQL query, without explanation or markdown formatting.
        Question: {user_query}
    """)

    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.3-70b-versatile"
    )

    chain = prompt | llm | StrOutputParser()
    sql_query = chain.invoke({"user_query": user_query})
    return sql_query.strip()


# ======================================================
# 🗄️ 2. Function: Execute SQL query on PostgreSQL
# ======================================================
def execute_sql_query(sql_query: str):
    """
    Executes a SQL query on PostgreSQL and returns the result.
    Handles both SELECT and non-SELECT queries.
    """
    try:
        conn = psycopg2.connect(
            host=os.getenv("PG_HOST"),
            database=os.getenv("PG_DATABASE"),
            user=os.getenv("PG_USER"),
            password=os.getenv("PG_PASSWORD"),
            port=os.getenv("PG_PORT", 5432)
        )
        cur = conn.cursor()
        cur.execute(sql_query)

        if cur.description:  # Query returns data (e.g., SELECT)
            rows = cur.fetchall()
        else:
            conn.commit()  # For INSERT/UPDATE/DELETE
            rows = ["✅ Query executed successfully."]

        cur.close()
        conn.close()
        return rows

    except Exception as e:
        return [f"❌ Error executing query: {e}"]


# ======================================================
# 💬 3. Streamlit Frontend
# ======================================================
def run_streamlit_ui():
    """
    Launches the Streamlit web interface for Text-to-SQL chatbot.
    """
    st.set_page_config(page_title="Text-to-SQL (PostgreSQL)", page_icon="🧠")
    st.title("🧠 Natural Language to SQL - PostgreSQL Chat Assistant")

    user_query = st.text_input("💬 Ask a question:")
    if st.button("Run Query"):
        with st.spinner("🧠 Thinking... Generating SQL..."):
            sql_query = get_sql_query(user_query)

        st.subheader("🔍 Generated SQL Query:")
        st.code(sql_query, language="sql")

        with st.spinner("⚙️ Running query on PostgreSQL..."):
            results = execute_sql_query(sql_query)

        st.subheader("📊 Query Results:")
        for row in results:
            st.write(row)


# ======================================================
# 🚀 4. Entry Point
# ======================================================
if __name__ == "__main__":
    run_streamlit_ui()
