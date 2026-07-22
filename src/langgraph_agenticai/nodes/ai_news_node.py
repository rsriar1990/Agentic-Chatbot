from tavily import TavilyClient
from langchain_core.prompts import ChatPromptTemplate

class AINewsNode:
    def __init__(self,llm):
        """
        Initialize the AINewsNode with API keys for Tavily and GROQ
        """
        self.tavily = TavilyClient()
        self.llm = llm
        # This is used to capture various steps in this file so that later can be used for steps shown
        self.state = {}

    def fetch_news(self,state:dict) -> dict:
        """
        Fetch AI News based on the specified frequency.
        Args:
            state (dict): The state dictionary containing 'frequency'.
        Returns:
            dict: Updated state with 'news_date' key containing fetched news.
        """

        frequency = state['messages'][0].content.lower()
        self.state['frequency'] = frequency
        time_range_map = {'daily': 'd', 'weekly': 'w', 'monthly': 'm', 'year': 'y'}
        days_map = {'daily':1, 'weekly':7, 'monthly':30, 'year':365}

        response = self.tavily.search(
            query="Top Artificial Intelligence (AI) technology news in USA and globly",
            topic="news",
            time_range=time_range_map[frequency],
            include_answer="advanced",
            max_results=15,
            days=days_map[frequency],
            # include_domain=["techcrunch.com", "venturebeast.com/ai", ...] # uncomment and add domains if needed

        )

        state['news_data'] = response.get('results',[])
        self.state['news_data'] = state['news_data']
        return state
    


    def summarize_news(self, state:dict) -> dict:
        """
        Summarize the fethed news using LLM.

        Args:
        state (dict): The state dictionary containing 'news_data'.

        Returns:
            dict: Updated state with 'summary' key containing the summarized news.
        """

        news_items = self.state['news_date']

        prompt_template = ChatPromptTemplate.from_messages([
            ("system", """Summarize AI news articles into markdown format. for each item include:
             -Date in **YYYY-MM-DD** format IST timezone
             -Concise sentenses summary from latest news
             -sort news by date wise (latest first)
             -Source URL aslink
             Use format:
             - [Summary](URL)"""),
             ("user","Articles:\n{articles}")
        ])

        articles_str = "\n\n".join([
            f"Content: {item.get('content', '')}\nURL: {item.get('URL','')}\nDate: {item.get('published_date','')}"
            for item in news_items
        ])

        response = self.llm.invoke(prompt_template.format(articles=articles_str))
        state['summary'] = response.content
        self.state['summary'] = state['summary']
        return self.state
    
    def save_result(self,state):
        frequency = self.state['frequency']
        summary =self.state['summary']
        filename= f"./AINews/{frequency.lower()}_summary.md"
        with open(filename, 'w') as f:
            f.write(f"# {frequency.capitalize()} AI News Summary\n\n")
            f.write(summary)
            self.state['filename'] = filename
            return self.state