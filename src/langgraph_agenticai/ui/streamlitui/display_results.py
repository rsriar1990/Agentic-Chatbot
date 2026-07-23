import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage,ToolMessage
import json


class DisplayResultStreamlit:
    def __init__(self,usecase,graph,user_message):
        self.usecase= usecase
        self.graph= graph
        self.user_message= user_message
        
    def display_result_on_ui(self):
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message
        if usecase == "Basic Chatbot":
            for event in graph.stream({'messages':("user",user_message)}):
                print(event.values())
                for value in event.values():
                    print(value['messages'])
                    with st.chat_message("user"):
                        st.write(user_message)
                        with st.chat_message("assistant"):
                            st.write(value["messages"].content)
        elif usecase=="Chatbot with Web":
            # Prepare state and invoke the graph
            initial_state = {"messages": [user_message]}
            res = graph.invoke(initial_state)
            for message in res["messages"]:
                if type(message) == HumanMessage:
                    with st.chat_message("user"):
                        st.write(message.content)
                elif type(message) == ToolMessage:
                    with st.chat_message("ai"):
                        st.write("Tool Call Start")
                        st.write(message.content)
                        st.write("Tool Call End")
                elif type(message) == AIMessage and message.content:
                    with st.chat_message("assistant"):
                        st.write(message.content)

        elif usecase == "AI News":
            frequency = user_message  # "Daily", "Weekly", "Monthly"
        
            with st.spinner("Fetching and summarizing news..."):
                try:
                    # 1. Run the LangGraph to generate the summary file
                    initial_state = {
                        "messages": [HumanMessage(content=frequency)]
                        }
        
                    result_state = graph.invoke(initial_state)
        
                            # 2. Get filename from state (set in save_result)
                    filename = result_state.get("filename")
                    if not filename:
                        filename = f"./AINews/{frequency.lower()}_summary.md"
        
                        # 3. Read and display markdown
                        with open(filename, "r") as file:
                            markdown_content = file.read()
        
                        st.markdown(markdown_content, unsafe_allow_html=True)
        
                except FileNotFoundError:
                    AI_NEWS_PATH = f"./AINews/{frequency.lower()}_summary.md"
                    st.error(f"News not generated or File not found: {AI_NEWS_PATH}")
                except Exception as e:
                    st.error(f"An error occured: {str(e)}")
          


