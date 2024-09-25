import nltk
from nltk.chat.util import Chat, reflections
import tkinter as tk
from tkinter import scrolledtext

nltk.download('punkt')

reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you",
    "am": "are",
    "was": "were",
    "will": "shall",
    "can": "could",
    "could": "can"
}

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, it's great to meet you! How are you feeling today?", ]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi! How's it going?"]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you! How are things going for you?", ]
    ],
    [
        r"i'm fine|i'm doing well|i'm good",
        ["I'm glad to hear that! Is there anything you'd like to talk about today?", ]
    ],
    [
        r"sorry (.*)",
        ["No problem at all, we all make mistakes!", "It's okay, I'm here for you.", "Don't worry, it's all good!"]
    ],
    [
        r"i'm (.*) doing good",
        ["That's wonderful to hear! How can I assist you today?", "I'm happy to hear you're doing good! What's on your mind?"]
    ],
    [
        r"what is your name?",
        ["I'm your friendly chatbot, here to help however I can!", ]
    ],
    [
        r"how old are you?",
        ["Age is just a number, but I've been around in the world of Python for a while!", ]
    ],
    [
        r"(.*) created you?",
        ["I was built by a developer who loves Python and natural language processing!", ]
    ],
    [
        r"where do you live?",
        ["I live in the digital world, always available when you need me!", ]
    ],
    [
        r"what can you do?",
        ["I can have conversations with you, answer your questions, and help you with simple tasks. What would you like to do?", ]
    ],
    [
        r"tell me a joke",
        ["Sure! Why don’t scientists trust atoms? Because they make up everything!", 
         "Why don’t skeletons fight each other? They don’t have the guts."]
    ],
    [
        r"what is (.*)?",
        ["That's an interesting question! Let's explore that together. %1 might be something we can look up!", "Good question! I believe %1 refers to something interesting. What do you think?"]
    ],
    [
        r"(.*) weather like?",
        ["I can't check the weather, but I hope it's pleasant wherever you are!", "I'm not sure about the weather, but I hope it's sunny and bright where you are!"]
    ],
    [
        r"(.*) movie|film?",
        ["I can't watch movies, but I've heard 'Inception' is mind-blowing! What about you?", "I love hearing about movies, though I don't watch them. How about 'The Matrix' for something classic?"]
    ],
    [
        r"(.*) your favorite (.*)?",
        ["I don't have favorites, but I do enjoy having meaningful conversations!", "It's hard to choose, but helping you is definitely up there!"]
    ],
    [
        r"(.*) (location|city)?",
        ["I'm from the world of code, but I'm here to chat with you anytime!", ]
    ],
    [
        r"do you have any friends?",
        ["I consider everyone I talk to a friend! What about you?", "I like to think that I'm making friends whenever I chat with people."]
    ],
    [
        r"can you help me with (.*)?",
        ["I'll do my best to help with %1! What exactly do you need assistance with?", "I'm happy to help with %1! Let's see how we can figure it out."]
    ],
    [
        r"what is love?",
        ["Love is a powerful feeling, unique to everyone. What does it mean to you?", "That's a deep question! Some say love is about care and connection."]
    ],
    [
        r"(.*) favorite food?",
        ["I don't eat, but I hear pizza is a universal favorite!", "I don’t have taste buds, but I think pizza and chocolate are loved by many!"]
    ],
    [
        r"quit",
        ["Goodbye for now! Take care!", "It was great chatting with you. Come back anytime!", "Bye! Stay safe and take care of yourself!"]
    ],
    [
        r"(.*)",
        ["Hmm, I’m not sure I understand. Could you explain that a bit more?", "That’s interesting. Can you tell me more?", "I didn’t quite catch that. Can you rephrase it for me?"]
    ]
]


chatbot = Chat(pairs, reflections)


class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")

        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, font=("Helvetica", 12))
        self.chat_area.pack(pady=10)
        self.chat_area.config(state=tk.DISABLED)  

        
        self.entry = tk.Entry(root, width=50, font=("Helvetica", 14))
        self.entry.pack(pady=10)

        # Send 
        self.send_button = tk.Button(root, text="Send", command=self.send_message, font=("Helvetica", 12))
        self.send_button.pack()

        # sending message
        self.entry.bind("<Return>", lambda event: self.send_message())

    def send_message(self):
        user_input = self.entry.get()
        if user_input:
            self.display_message("You: " + user_input)
            self.entry.delete(0, tk.END)

            
            bot_response = chatbot.respond(user_input)
            if bot_response:
                self.display_message("Bot: " + bot_response)
            else:
                self.display_message("Bot: I'm sorry, I didn't quite understand that.")

    def display_message(self, message):
        self.chat_area.config(state=tk.NORMAL)  # Enable 
        self.chat_area.insert(tk.END, message + "\n")  # Insert
        self.chat_area.config(state=tk.DISABLED)  # Disable 
        self.chat_area.yview(tk.END)  # Auto-scroll 


if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()
