import requests
from dotenv import load_dotenv
from langchain.agents import create_agent

# Load the .env file
load_dotenv()

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    response = requests.get(f"https://wttr.in/{city}?format=j1")
    return response.json()

agent = create_agent(
    model="openai:gpt-5.5",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in Lahore?"}]}
)
print(result["messages"][-1].content)