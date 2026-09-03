from dotenv import load_dotenv

from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage

from utils import decode_file

load_dotenv()

model = init_chat_model(
    model='gpt-4.1-mini',
    temperature=0.1
)

messages = [
    HumanMessage([
        {'type': 'text', 'text': 'Which mountain is there in the picture ?'},
        {
            'type': 'image', 
            'base64': decode_file('image.jpg'), 
            'mime_type': 'image/jpeg'
        },
        # {
        #     'type': 'image', 
        #     'url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQV2VHD0QSN4uIgFrxTywPXtZP5M-K2MxQgQc0oBEeJJV1cH2E7tP9E-c32'
        # },
    ])
]

response = model.stream(messages)

for chunk in response:
    print(chunk.content, end="", flush=True)