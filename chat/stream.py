from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

model = init_chat_model(
    model='gpt-4.1-mini',
    temperature=0.1
)

response = model.stream("What is openai")

for chunk in response:
    print(chunk.content, end="", flush=True)