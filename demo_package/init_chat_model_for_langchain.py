from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()
import os
from langchain.messages import SystemMessage,HumanMessage


model = init_chat_model(model_provider='openai',
                        model='deepseek-chat',
                        api_key='sk-b9cb6c4e3aeb4411aefb479222a91a53',
                        base_url='https://api.deepseek.com/v1',
                        temperature=0)


if __name__ == '__main__':
    messages = [
        SystemMessage(content=os.getenv('PROMPT_SYSTEM')),
    ]
    human_mes = '你是?'
    # messages.append(HumanMessage(content=human_mes))
    # result = model.invoke(messages)
    # print(result.content)
    print(messages)