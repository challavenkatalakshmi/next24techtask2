from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

# Create a new instance of a ChatBot
chatbot = ChatBot('InteractiveBot', 
                  logic_adapters=[
                      'chatterbot.logic.BestMatch',
                      'chatterbot.logic.MathematicalEvaluation',
                      'chatterbot.logic.TimeLogicAdapter'
                  ])

# Create trainers for the chatbot
corpus_trainer = ChatterBotCorpusTrainer(chatbot)
list_trainer = ListTrainer(chatbot)

# Train the chatbot based on the English corpus
corpus_trainer.train('chatterbot.corpus.english')

# Enhanced training data with diverse topics
custom_conversations = [
    ["Hello", "Hi there!", "How are you?", "I'm good, thank you! How about you?", "I'm great, thanks for asking!", "You're welcome."],
    ["What is your name?", "I am a chatbot created by OpenAI."],
    ["Who created you?", "I was created by the team at OpenAI."],
    ["What is the capital of France?", "The capital of France is Paris."],
    ["What is the capital of Japan?", "The capital of Japan is Tokyo."],
    ["What is the largest ocean on Earth?", "The largest ocean on Earth is the Pacific Ocean."],
    ["Who was the first President of the United States?", "The first President of the United States was George Washington."],
    ["When was the Declaration of Independence signed?", "The Declaration of Independence was signed on July 4, 1776."],
    ["What is the speed of light?", "The speed of light is approximately 299,792 kilometers per second."],
    ["What is the chemical symbol for water?", "The chemical symbol for water is H2O."],
    ["Who won the FIFA World Cup in 2018?", "France won the FIFA World Cup in 2018."],
    ["Who holds the record for the most home runs in a single MLB season?", "Barry Bonds holds the record for the most home runs in a single MLB season with 73."],
    ["Who directed the movie 'Inception'?", "Christopher Nolan directed the movie 'Inception'."],
    ["Who played the character of Harry Potter in the movies?", "Daniel Radcliffe played the character of Harry Potter in the movies."],
    ["What is Python?", "Python is a high-level, interpreted programming language known for its readability and versatility."],
    ["What is a function in programming?", "A function is a block of code designed to perform a specific task."],
    ["What is a variable?", "A variable is a storage location identified by a memory address and a symbolic name that contains some known or unknown quantity of information."],
    ["What is 5 plus 7?", "5 plus 7 is 12."],
    ["What is the square root of 16?", "The square root of 16 is 4."],
    ["Tell me a fun fact.", "Did you know? The honeybee is the only insect that produces food eaten by humans."],
    ["Give me another fun fact.", "Did you know? The longest time between two twins being born is 87 days."],
    ["Tell me a joke.", "Why don't scientists trust atoms? Because they make up everything!"],
    ["Do you know another joke?", "Why did the scarecrow win an award? Because he was outstanding in his field!"],
    ["What is the weather like today?", "I'm a chatbot and don't have real-time data, but you can check your local weather forecast online."],
    ["Will it rain tomorrow?", "I'm not sure. Please check your local weather forecast."],
    ["What is artificial intelligence?", "Artificial intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think and learn like humans."],
    ["What is machine learning?", "Machine learning is a subset of artificial intelligence that involves the use of algorithms and statistical models to enable computers to improve their performance on a task through experience."],
    ["What is natural language processing?", "Natural language processing (NLP) is a field of artificial intelligence that focuses on the interaction between computers and humans through natural language."],
    ["How do I improve my coding skills?", "Practice regularly, read documentation, work on projects, and learn from others by contributing to open source."],
    ["How can I stay healthy?", "Eat a balanced diet, exercise regularly, get enough sleep, and avoid stress."],
    ["What time is it?", "I'm a chatbot and don't have real-time data, but you can check the time on your device."],
    ["What day is it?", "I'm a chatbot and don't have real-time data, but you can check the date on your device."],
    ["Can you tell me a story?", "Once upon a time, in a land far, far away..."],
    ["Do you like music?", "I don't have preferences, but music is a wonderful form of art."]
]

for conversation in custom_conversations:
    list_trainer.train(conversation)

