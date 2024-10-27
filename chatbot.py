import random
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer 


chatbot = ChatBot('MyBot')

   
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

   
print("Чат-бот запущен! Напишите 'exit' для выхода.")
while True:
       user_input = input("Вы: ")
       if user_input.lower() == 'exit':
           break
       response = chatbot.get_response(user_input)
       print("Бот:", response)
def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "ОРЕЛ"
    else:
        return "РЕШКА"