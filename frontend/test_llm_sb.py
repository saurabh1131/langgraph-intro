# from http.client import responses
# from pydantic import BaseModel
# from typing import Annotated, List, Generator
# # from langchain_openai import ChatOpenAI
# # llm setup
# # from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage, AIMessageChunk
# # from langgraph.graph.message import add_messages
# # from langgraph.graph import StateGraph, START, END
# # from langgraph.prebuilt import ToolNode
# # from langgraph.checkpoint.memory import MemorySaver
# # from scout.tools import query_db, generate_visualization
# # from scout.prompts import prompts

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            google_api_key="AIzaSyCvR-EJDDqU881df2CrjgDaQjejttoARXw",
            temperature=0.05
    )
response = llm.invoke("Hello, how are you?")
print(response.content)


# -------------------

from sqlalchemy import create_engine, text
engine = create_engine(
    "postgresql+psycopg2://postgres.xfuhyehhwmdfzmvmvslh:hKg7Bc9fxt2GSCbQ@aws-0-ap-south-1.pooler.supabase.com:6543/postgres?gssencmode=disable"
)
with engine.connect() as connection:
    result = connection.execute(text('SELECT * FROM onlyvans.creators LIMIT 1'))
    print(result.fetchone())  # Should print (1,)