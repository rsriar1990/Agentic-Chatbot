import streamlit as st
from src.langgraph_agenticai.ui.streamlitui.loadui import LoadStreamlitUI

def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph AgenticAI application with streamlit UI.
    This function initialis=zes the UI , handles user input, configures the LLM Model,
    sets up the graph based on the selected use case, and display the output while
      implementing exception handling for robutness.
    """

    ### LOAD UI

    ui=LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI")
        return
    
    user_message = st.chat_input("Enter your message")