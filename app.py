import os
import dotenv
import streamlit as st
import langchain
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv # is used to read the variables present in the .env files

load_dotenv() # it have readed the .env files

os.environ["GOOGLE_API_KEY"]=os.getenv("gaK")

cm=ChatGoogleGenerativeAI(model="gemini-2.5-pro")


if "conver" not in st.session_state:
    st.session_state["conver"]=[]
    st.session_state["memory"]=[]
    st.session_state["memory"].append(("system","answer as a three year old child"))


user_data=st.chat_input("user_message")

if user_data:
    st.session_state["memory"].append(("human",user_data))
    with st.chat_message("human"):
        st.write(user_data)

    output=cm.invoke(st.session_state["memory"])

    st.session_state["memory"].append(("ai",output.content))

    st.session_state["conver"].append({"role":"human","data":user_data})
    st.session_state["conver"].append({"role":"ai","data":output.content})

    if user_data=="bye":
        st.session_state["conver"]=[]
        st.session_state["memory"]=[]

for y in st.session_state["conver"]:
    with st.chat_message(y["role"]):
        st.write(y["data"])

