import asyncio
from rich import print_json
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain_mcp_adapters.client import MultiServerMCPClient

from schemas.weather import ResponseFormat

load_dotenv()

async def main(): 
    client = MultiServerMCPClient(
        {
            "weather": {
                "transport": "http",
                "url": "http://localhost:8000/mcp",
            }
        }
    )

    tools = await client.get_tools()
    agent = create_agent(
        model='gpt-4.1-mini',
        tools=tools,
        response_format=ResponseFormat
    )
    response = await agent.ainvoke(
        {
            "messages": [HumanMessage("What is weather in Hunza ?")]
        }
    )

    print_json(response["messages"][-1].content)


if __name__ == '__main__':
    asyncio.run(main())