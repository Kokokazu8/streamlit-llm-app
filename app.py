#事前準備
# 環境変数、Streamlit用のインポート
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
# LangChain用のインポート
# 追加パッケージ
# pip install langchain==0.3.0 openai==1.47.0 langchain-community==0.3.0 langchain-openai==0.2.2 httpx==0.27.2
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

#LLMt定義の初期化
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

st.title("Lessson21提出物:LLM機能を搭載したWebアプリ")

st.write("##### 動作モード1: ファッションスタイリスト")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで、場所に即したファッションを提案します。")
st.write("##### 動作モード2: 首都の解説")
st.write("首都名を入力することで、その国の首都に関する情報を提供します。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["１：ファッションスタイリスト", "２：首都の解説"]
)

st.divider()

if selected_item == "１：ファッションスタイリスト":
    input_message = st.text_input(label="お出かけの場所を入力してください。")

else:
    country_name = st.text_input(label="国名を入力してください。")

if st.button("実行"):
    st.divider()

    if selected_item == "１：ファッションスタイリスト":
        if input_message:
            # メッセージの定義
            messages = [
                SystemMessage(content="あなたは優秀なファッションスタイリストです。"),
                HumanMessage(content=f"{input_message}にふさわしいコーディネートを教えてください。"),
            ]
            result = llm(messages)
            st.write("提案ファッション:\n")
            st.write(f"{result.content}")

        else:
            st.error("お出かけの場所を入力してから「実行」ボタンを押してください。")

    else:
        if country_name:
            # メッセージの定義
            messages = [
                SystemMessage(content="あなたは優秀な旅行ガイドです。"),
                HumanMessage(content=f"{country_name}の首都と、首都の概要を教えてください。"),
            ]
            result = llm(messages)
            st.write("結果:\n")
        
            st.write(f"{country_name}の首都に関する情報を提供します。\n")
            st.write(f"{result.content}")

        else:
            st.error("国名を入力してから「実行」ボタンを押してください。")