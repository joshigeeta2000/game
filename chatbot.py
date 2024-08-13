from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

# Initialize the chatbot
chatbot = ChatBot('MyBot')

# Train the chatbot with English corpus data
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# Train with custom data
custom_conversations = [
    "Hello",
    "Hi there!",
    "How can I help you?",
    "I need some assistance with my order.",
    "Sure, I can help you with that.",
    "What are your business hours?",
    "We are open from 9 AM to 5 PM, Monday to Friday."
]
trainer = ListTrainer(chatbot)
trainer.train(custom_conversations)

# Command-line interface for the chatbot
print("Chat with MyBot. Type 'exit' to end the conversation.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("MyBot: Goodbye!")
        break
    response = chatbot.get_response(user_input)
    print(f"MyBot: {response}\n")
