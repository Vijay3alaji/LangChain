from fastapi import FastAPI
from langchain.chat_models import ChatOpenAI
from langchain.serve import add_routes
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI  # Assuming you're using OpenAI models
from langchain_ollama import OllamaEmbeddings
from dotenv import load_dotenv
import os
import uvicorn

load_dotenv()

os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server"

)

add_routes(
    app,
    OpenAI(),
    path="/openai"
)
model=OpenAI()

##ollama llama2
llm=OllamaEmbeddings(model="llama2")

prompt1=PromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2=PromptTemplate.from_template("Write me an poem about {topic} for a 5 years child with 100 words")

add_routes(
    app,
    prompt1|model,
    path="/essay"
)

add_routes(
    app,
    prompt2|llm,
    path="/poem"
)


if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)