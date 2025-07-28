import streamlit as st
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model_name="gpt-4o", openai_api_key=api_key)

# UI：ここから画面に表示される内容
st.title("専門家に質問できるAIチャット")
st.markdown("質問と相談したい専門家を選んで、AIの回答を確認しましょう。")

experts = {
    "栄養士": "あなたは栄養士です。食事と健康について専門的に答えてください。",
    "キャリアアドバイザー": "あなたはキャリアアドバイザーです。仕事・転職について助言してください。",
}

question = st.text_input("質問を入力してください：")
expert = st.radio("専門家を選んでください：", list(experts.keys()))

def ask_llm(text, role):
    messages = [
        SystemMessage(content=experts[role]),
        HumanMessage(content=text)
    ]
    return llm(messages).content

if st.button("質問する") and question:
    response = ask_llm(question, expert)
    st.subheader("AIの回答：")
    st.write(response)