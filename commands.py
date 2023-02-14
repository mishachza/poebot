import openai
from config import *



openai.api_key = APIOPENAI
model_engine = 'text-davinci-003'
max_tokens = 128
prompt = ''
COMMANDS = {'add to shopping list': '',
            'clear shopping list': '',
            'shopping list': '',
            'set a reminder': {'datetime': '',
                               'reminder text': ''},
            'reminder list': ''}
COM_GPT = {1: f'analyze:{prompt},',
             2: f'fill out the list{COMMANDS}',
             3: f'reply to the:{prompt}'}

class Сommands_handler:

    def __init__(self, prompt):
        prompt = f'analyze:{prompt}, ' \
                 f'fill out the dictionary:{COMMANDS},'

        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            temperature=0.5,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        print(completion.choices[0].text)
        return completion.choices[0].text





# Пример запроса:
# проанализируи "Завтра в 13 часов напомни купить туалетка хлеб стиральный порошок сыр рис"
# заполни список





