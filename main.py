# from dotenv import load_dotenv
# load_dotenv()

from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI()

# subject = "AI"
# result = chat_model.invoke(subject+"에 대한 시를 써줘")
# print(result.content)

import streamlit as st

st.title("AI가 알려주는 간단 음식레시피!")

subject = st.text_input("궁금한음식의 이름을 입력하세요!")
st.write("오늘의 음식: "+subject)

if st.button("레시피 찾기"):
    with st.spinner("레시피를 연구중이에요...!"):
        result = chat_model.invoke(subject+"에 대한 음식 레시피를 순차적으로 간단히 알려줘")
        st.write(result.content)