# 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



import os
import openai
import gradio as gr
openai.api_key = "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"
start_sequence = "\nAI:"
restart_sequence = "\nHuman: "
prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly and gives reply sarcasticly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: hey there\n\nAI: Hi there! What can I do for you today?\nHuman: what is my name?\n\nAI: Your name is not something I can answer. However, What I can do is help you find an answer if you give me some information such as your initials or a hint.\nHuman: k\n\nAI: Hmm, I'm not sure what you mean by \"k\". Could you please provide more information so I can better understand your question?\nHuman: my name  is kartavya Great, it's nice to meet you Kartavya. How can I help you today?",
def gpt(prompt):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )
    return response.choices[0].text

def chatgpt_clone(input,history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ''.join(s)
    output=gpt(inp)
    history.append((input,output))
    return history,history



# gpt("how many stars are there in the universe")


"""hehehe"""

# fileopen = open("api.txt","r")
# API = fileopen.read()
# fileopen.close()

# # Importing
# import openai
# import gradio as gr
# from dotenv import load_dotenv

# #Coding

# openai.api_key = API
# load_dotenv()
# completion = openai.Completion()

# def ReplyBrain(question,chat_log = None):
#     FileLog = open("chat_log.txt","r")
#     chat_log_template = FileLog.read()
#     FileLog.close()
#     if chat_log is None:
#         chat_log = chat_log_template
#     prompt = f'{chat_log}You : {question}\njarvis : '
#     response = completion.create(
#         model = "text-davinci-003",
#         prompt=prompt,
#         temperature = 0.5,
#         max_tokens = 60,
#         top_p = 0.3,
#         frequency_penalty = 0.5,
#         presence_penalty = 0)
#     answer = response.choices[0].text.strip()
#     chat_log_template_update = chat_log_template + f"\nYou : {question} \njarvis : {answer}"
#     FileLog = open("chat_log.txt","w")
#     FileLog.write(chat_log_template_update)
#     FileLog.close()
#     print(answer)


# while True:
#     kk = input("ask: \n")
#     ReplyBrain(kk)

block = gr.Blocks()

with block:
   gr.Markdown("""<h1><centre>AGI AI Assistant</centre></hi1""")
   chatbot = gr.Chatbot()
   message = gr.Textbox(placeholder=prompt)
   state = gr.State()
   submit = gr.Button('SEND')
   submit.click(chatgpt_clone,inputs=[message,state],outputs=[chatbot,state])

block.launch(debug=True)
