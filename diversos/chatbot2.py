from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("Vitor")

treinar = ChatterBotCorpusTrainer(chatbot)

treinar.train("chatterbot.corpus.portuguese")
while True:
    request = input("Você: ")
    response = chatbot.get_response(request)
    print(f"bot: {response}")
