import nest_asyncio
nest_asyncio.apply()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from llama_index.core import VectorStoreIndex, Settings
from llama_index.core.tools import QueryEngineTool
from llama_index.core.agent import ReActAgent
from llama_parse import LlamaParse
from llama_index.llms.openai import OpenAI
from dotenv import load_dotenv
import os


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://your-frontend-domain.com", "https://shrek-chat-1.onrender.com/"],
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Allow all headers
)


load_dotenv()  # Load variables from .env file

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API key is missing. Please provide it in the .env file.")


Settings.llm = OpenAI(model="gpt-4o-mini", temperature=0, api_key=api_key)

async def setup_agent():

    documents = await LlamaParse(result_type="markdown").aload_data("backend/resources/Shrek.txt")

    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()

    query_tool = QueryEngineTool.from_defaults(
        query_engine,
        name="Shrek",
        description="A RAG engine which is an expert in Shrek",
    )

    agent = ReActAgent.from_tools([query_tool], verbose=True)
    return agent

agent = None

@app.on_event("startup")
async def initialise_agent():
    global agent
    agent = await setup_agent()

@app.get("/")
async def root():
    return {"message": "App is running"}

class UserQuery(BaseModel):
    question: str


@app.post("/ask")
def ask_question(user_query: UserQuery):
    if agent is None:
        return {"error": "Agent is not initialised yet. Try again later."}
    response = agent.chat(user_query.question)
    return {"response": response}



