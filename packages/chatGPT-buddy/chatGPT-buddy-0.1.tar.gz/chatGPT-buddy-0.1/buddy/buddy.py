import speech_recognition as sr
import gtts
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch
import os

def run():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = recognizer.listen(source)

    command = recognizer.recognize_google(audio)
    print("You said: " + command)

    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    input_ids = torch.tensor(tokenizer.encode(command)).unsqueeze(0)  # Batch size 1
    outputs = model(input_ids, labels=input_ids)
    loss, logits = outputs[:2]
    response = tokenizer.decode(torch.argmax(logits[0, -1]), skip_special_tokens=True)

    print(response)
    tts = gtts.gTTS(text=response, lang='en')
    tts.save("response.mp3")
    os.system("start response.mp3")

if __name__ == '__main__':
    run()