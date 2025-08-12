from pydantic import BaseModel
from fastapi import FastAPI
from agent import get_response_from_agent

app = FastAPI(title="LangGraph AI Agent")
ALLOWED_MODEL_NAMES=["llama3-70b-8192", "llama-3.3-70b-versatile", "gemini-2.5-flash","gemini-1.5-flash","openai/gpt-oss-20b","openai/gpt-oss-120b"]


class RequestState(BaseModel):
    model_name:str
    model_provider:str
    system_prompt:str
    messages:list[str]
    allow_search:bool



@app.post("/chat")
def end_point(request:RequestState):
    """
    API Endpoint to interact with the Chatbot using LangGraph and search tools.
    It dynamically selects the model specified in the request
    """
    LLM_ID = request.model_name
    Provider = request.model_provider
    SystemPrompt = request.system_prompt
    UserMessages = request.messages
    AllowSearch = request.allow_search

    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error":"Invalid model name, Kindly select a valid model name"}
    else:
        response = get_response_from_agent(
            messages_list=UserMessages,
            allow_search=AllowSearch,
            system_prompt=SystemPrompt,
            model_provider=Provider,
            model_name=LLM_ID
        )
        return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9999)

