import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses for the virtual assistant
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi! How can I assist you today?"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you for asking.", "I'm great! How about you?"]
    ],
    [
        r"(.*)name(.*)|what is your name ?",
        ["You can call me ChatBot.", "I'm ChatBot, nice to meet you!"]
    ],
    [
        r"what can you do ?|what are your capabilities ?",
        ["I can help you with various tasks such as setting reminders, providing information, or just having a chat."]
    ],
    [
        r"who created you ?|who made you ?",
        ["I was created by a team of developers at Team 5."]
    ],
    [
        r"how can I contact support ?|how to get help ?",
        ["You can contact our support team at support@example.com for assistance."]
    ],
    [
        r"tell me a joke|say something funny",
        ["Why don't scientists trust atoms? Because they make up everything!", 
         "I'm reading a book on anti-gravity. It's impossible to put down!", 
         "What do you call fake spaghetti? An impasta!"]
    ],
    [
        r"(.*)weather(.*)",
        ["You can check the weather forecast on websites like Weather.com or by using weather apps on your phone."]
    ],
    [
        r"(.*)news(.*)",
        ["You can stay updated with the latest news by visiting news websites or using news apps on your phone."]
    ],
    [
        r"thank you|thanks",
        ["You're welcome!", "No problem!", "Glad I could help!"]
    ],
    [
        r"exit|bye|goodbye",
        ["Goodbye!", "See you later!", "Take care!"]
    ],
    [
        r"(.*)",
        ["Sorry, I didn't understand that. Can you please rephrase?", "I'm still learning. Could you repeat that?"]
    ]
]


def ai_virtual_assistant():
    """
    AI Virtual Assistant function.

    This function initializes an AI-powered virtual assistant and starts a conversation with the user.

    Parameters:
        None

    Returns:
        None
    """
    print("Hi! I'm your AI-powered virtual assistant. How can I assist you today?")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()


if __name__ == "__main__":
    nltk.download('punkt')  # Download NLTK data if not already downloaded
    ai_virtual_assistant()
