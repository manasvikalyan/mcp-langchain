
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["mathserver.py"],
                "transport": "stdio",
            },
            "weather": {
                "url": "http://localhost:8000/mcp",
                "transport": "streamable_http",
            },
            "news": {
            "command": "python",
            "args": ["newsserver.py"],
            "transport": "stdio",
            }
        }
    )

    tools = await client.get_tools()
    model = ChatGroq(model="qwen-qwq-32b")
    agent = create_react_agent(model, tools)

    print("🤖 AI Agent is ready! Ask any question. Type 'exit' to quit.")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in {"exit", "quit"}:
            print("👋 Exiting.")
            break

        try:
            response = await agent.ainvoke({"messages": [{"role": "user", "content": user_input}]})
            print("Assistant:", response["messages"][-1].content)
        except Exception as e:
            print("❌ Error:", str(e))

asyncio.run(main())


# from langchain_mcp_adapters.client import MultiServerMCPClient
# from langgraph.prebuilt import create_react_agent
# from langchain_groq import ChatGroq

# from dotenv import load_dotenv
# load_dotenv()

# import asyncio

# async def main():
#     client = MultiServerMCPClient(
#         {
#             "math": {
#                 "command": "python",
#                 "args": ["mathserver.py"],
#                 "transport": "stdio",
#             },
#             "weather": {
#                 "url": "http://localhost:8000/mcp",  # it should be running 
#                 "transport": "streamable_http",
#             }
#         }
#     )
    
#     import os
#     os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

#     tools=await client.get_tools()
#     model=ChatGroq(model="qwen-qwq-32b")
#     agent=create_react_agent(
#         model,tools
#     )

#     math_response = await agent.ainvoke(
#         {"messages": [{"role": "user", "content": "what's (3 + 5) x 12?"}]}
#     )

#     print("Math response:", math_response['messages'][-1].content)

#     weather_response = await agent.ainvoke(
#         {"messages": [{"role": "user", "content": "what is the weather in gurgaon?"}]}
#     )
#     print("Weather response:", weather_response['messages'][-1].content)

# asyncio.run(main())

