import openai
import configparser

cfg = configparser.ConfigParser()
cfg.read("api_key.ini")

openai.api_key = cfg['OpenAI_API']['api_key']

while True:
    model_engine = "text-davinci-003"

    command = input("Enter Chat Here :")

    if 'exit' in command.lower() or 'quit' in command.lower():
        break

    Cmp = openai.Completion.create(engine=model_engine, prompt=command, max_tokens=1024, n=1, stop=None, temperature=0.5)

    respon = Cmp.choices[0].text

    print(respon)