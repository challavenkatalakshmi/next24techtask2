import tkinter as tk
from tkinter import scrolledtext
from chatbot import chatbot
from PIL import Image, ImageTk

class ChatBotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive ChatBot")
        
        self.chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', height=20, width=50, bg="#f4f4f4", fg="#333")
        self.chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        self.user_input = tk.Entry(root, font=("Arial", 14))
        self.user_input.pack(padx=10, pady=10, fill=tk.X, expand=True)
        self.user_input.bind("<Return>", self.get_response)
        
        self.send_button = tk.Button(root, text="Send", font=("Arial", 12), bg="#4CAF50", fg="white", command=self.get_response)
        self.send_button.pack(padx=10, pady=10)
        
        self.chat_box.tag_configure("user", foreground="blue")
        self.chat_box.tag_configure("bot", foreground="green")

    def get_response(self, event=None):
        user_message = self.user_input.get()
        if user_message.strip():
            self.chat_box.config(state='normal')
            self.chat_box.insert(tk.END, f"You: {user_message}\n", "user")
            self.user_input.delete(0, tk.END)
            
            bot_response = chatbot.get_response(user_message)
            self.chat_box.insert(tk.END, f"Bot: {bot_response}\n", "bot")
            self.chat_box.config(state='disabled')
            self.chat_box.yview(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatBotApp(root)
    root.geometry("500x600")
    root.mainloop()


