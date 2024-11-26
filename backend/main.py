from fastapi import FastAPI
from pydantic import BaseModel
from llama_index.core import VectorStoreIndex, Settings
from llama_index.core.tools import QueryEngineTool
from llama_index.core.agent import ReActAgent
from llama_parse import LlamaParse
from llama_index.llms.openai import OpenAI

app = FastAPI()

Settings.llm = OpenAI(model="gpt-4o-mini", temperature=0)
documents = LlamaParse(result_type="markdown").load_data("resources/Shrek.txt")
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

query_tool = QueryEngineTool.from_defaults(
    query_engine,
    name="Shrek",
    description="A RAG engine which is an expert in Shrek",
)

agent = ReActAgent.from_tools([query_tool], verbose=True)

class UserQuery(BaseModel):
    question: str

@app.post("/ask")
def ask_question(user_query: UserQuery):
    if user_query.question.strip().upper() == "Q":
        return {"response": "Terminating service."}
    response = agent.chat(user_query.question)
    return {"response": response}
