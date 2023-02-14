import openai
from config import *



openai.api_key = APIOPENAI
model_engine = 'text-davinci-003'
max_tokens = 128

COMMANDS = {"add to shopping list": ("хлеб", "морковь", ),
            "set a reminder": ("напомнить в 20:00", ),
            }
COMMANDS2 = {1: 'add to shopping list',
             2: 'set a reminder',
             3: 'different'
            }
shop_list = ['']
reminder_list = ['']




def gpt_dialog(prompt):
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return completion.choices[0].text









