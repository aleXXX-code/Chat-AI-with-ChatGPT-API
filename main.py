import configparser
import openai
import gradio as gr

cfg = configparser.ConfigParser()
cfg.read('api_key.ini')

openai.api_key = cfg["OpenAI_API"]["api_key"]

start_sequence = "\nAI:"
restart_sequence = "\nME: "
prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\nAI: I am an AI created by OpenAI. How can I help you today?"


def openai_model(prompt):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt = prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )
    return response.choices[0].text

def chat_output(chat, text):
    text = text or []
    ls = [sum(text, ())]
    ls.append(chat)
    ch = ' '.join(s)
    output = openai_model(ch)
    text.append((chat, output))
    return text, text

def run():
    block = gr.Blocks()
    with block:
        gr.Markdown("""<h1><center>Chat AI with ChatGPT API</center></h1>""")
        chat = gr.Chatbot()
        text = gr.Textbox(placeholder=prompt)
        state = gr.State()
        submit = gr.Button("Send")
        submit.click(chat_output, inputs=[text, state], outputs=[chat, state])
    block.launch(debug=True)

if __name__ == "__main__":
    run()