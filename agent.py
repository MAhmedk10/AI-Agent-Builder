import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

# API Keys
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# Models
gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GEMINI_API_KEY
)
groq_llm = ChatGroq(model="llama-3.3-70b-versatile",
           groq_api_key=GROQ_API_KEY
)

# Tool
search_tool = TavilySearch(max_results=2)


def get_response_from_agent(model_name, model_provider, system_prompt, messages_list, allow_search):
    # 1️⃣ Choose LLM based on provider & model
    if model_provider.upper() == "GROQ":
        llm = ChatGroq(model=model_name, groq_api_key=GROQ_API_KEY)
    elif model_provider.upper() == "GEMINI":
        llm = ChatGoogleGenerativeAI(model=model_name, google_api_key=GEMINI_API_KEY)
    else:
        raise ValueError(f"Unsupported model provider: {model_provider}")

    # 2️⃣ Enable or disable tools
    tools = [search_tool] if allow_search else []

    # 3️⃣ Create the agent
    graph = create_react_agent(model=llm, tools=tools)

    # 4️⃣ Build the LangChain message objects
    messages = []
    if system_prompt:
        messages.append(SystemMessage(content=system_prompt))

    # Ensure each message from list becomes a HumanMessage
    for msg in messages_list:
        if isinstance(msg, str):
            messages.append(HumanMessage(content=msg))
        else:
            raise ValueError(f"Each message must be a string. Got: {type(msg)}")

    # 5️⃣ Prepare state and invoke
    state = {"messages": messages}
    response = graph.invoke(state)

    # 6️⃣ Extract AI responses
    ai_messages = [
        message.content
        for message in response.get("messages", [])
        if isinstance(message, AIMessage)
    ]

    return ai_messages[-1] if ai_messages else None

    # # 7️⃣ Print output
    # print("🤖 AI Response:")
    # print("=" * 50)
    # for i, msg in enumerate(ai_messages):
    #     if msg.strip():
    #         print(f"Response {i+1}:")
    #         print(msg)
    #         print("-" * 30)
