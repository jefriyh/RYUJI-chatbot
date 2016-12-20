# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Ryuji")
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "bye",
    "See you"
]

chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)

say = raw_input("Ask something : ")
while(say!="bye"):
    response = chatbot.get_response(say)
    print(response)
    say = raw_input("Ask something : ")
    
response = chatbot.get_response(say)
print(response)
