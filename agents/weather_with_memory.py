from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.checkpoint.serde.jsonplus import JsonPlusSerializer

from schemas.weather import ResponseFormat, UserContext
from tools.weather import get_weather, get_location

load_dotenv()
serde = JsonPlusSerializer(allowed_msgpack_modules=[ResponseFormat, UserContext])
checkpointer = InMemorySaver(serde=serde)

model = init_chat_model(
    model='gpt-4.1-mini',
    temperature=0.2
)

agent = create_agent(
    model=model,
    system_prompt="You are a helpful weather assistant who is funny but helpful.",
    tools=[get_weather, get_location],
    response_format=ResponseFormat,
    context_schema=UserContext,
    checkpointer=checkpointer
)

config = {
    'configurable': {
        'thread_id': str(1),
        'user_id': str(1001)
    }
}


response = agent.invoke(
    {
        'messages':[
            {'role': 'user', 'content': 'What is the weather today ?'}
        ]
    },
    context=UserContext(location='Lahore'),
    config=config
)

print(response['structured_response'].summary)
print(response['structured_response'].temperature_celcius)

response = agent.invoke(
    {
        'messages':[
            {'role': 'user', 'content': 'Is this normal in these days ?'}
        ]
    },
    context=UserContext(location='Lahore'),
    config=config
)

print(response['structured_response'].summary)
print(response['structured_response'].temperature_celcius)