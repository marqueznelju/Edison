from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

# Name of bot
bot = ChatBot('Edison')

trainer = ListTrainer(bot)

# Storage Adapter
bot = ChatBot(
        'Edison',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        logic_adapter=[ # Sepecifying logic adapter
            'chatterbot.logic.MathematicalEvaluation',
            'chatterbot.logic.TimeLogicAdapter'
        ],
        db_uri='sqlite:///database.sqlite3'
)

# Training bot with existing words. Adding more is better
trainer.train([
    "Sup",
    "bruh!",
    "WTF",
    "u r well cum",
    "thank u",
])

# Getting response from Edison
while True:
    try:
        i = bot.get_response(input())
        print(i)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break