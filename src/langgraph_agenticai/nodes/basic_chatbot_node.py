from src.langgraph_agenticai.state.state import State


class BasicChatbotNode:
    """
    Basic Chatbot logic implementation
    """
    def __init__(self,model):
        self.llm=model

    def process(self,state:State)->dict:
        """
        Processes the input and generate chat response.
        """
        return {'messages':self.llm.invoke(state['messages'])}