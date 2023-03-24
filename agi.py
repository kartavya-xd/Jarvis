import pyttsx3
import speech_recognition as sr
import openai
import gradio as gr
from dotenv import load_dotenv

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def STT():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)
    try:
        print("recognizing....")
        query = r.recognize_google(audio, language= "en-in")
        print(query)
        return query.lower()
    except Exception as e:
        print(e)
        speak("")
        return None


fileopen = open("api.txt","r")
API = fileopen.read()
fileopen.close()
openai.api_key = API
load_dotenv()
completion = openai.Completion()

def gpt_output(question,chat_log = None):
    FileLog = open("chat_log.txt","r")
    chat_log_template = FileLog.read()
    FileLog.close()
    if chat_log is None:
        chat_log = chat_log_template
    prompt = f'{chat_log}You : {question}\nVision : '
    response = completion.create(
        model = "text-davinci-003",
        prompt=prompt,
        temperature = 0.5,
        max_tokens = 60,
        top_p = 0.3,
        frequency_penalty = 0.5,
        presence_penalty = 0)
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f"\nYou : {question} \nVision : {answer}"
    FileLog = open("chat_log.txt","w")
    FileLog.write(chat_log_template_update)
    FileLog.close()
    print(answer)
    speak(answer)
    # return answer


while True:
    kk = STT()
    gpt_output(kk)


