import tkinter as tk
from tkinter import messagebox
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
 

word_list = [
    'apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon',
    'mango', 'nectarine', 'orange', 'peach', 'pear', 'plum', 'quince', 'raspberry', 'strawberry', 'tangerine',
    'watermelon', 'avocado', 'blueberry', 'cantaloupe', 'dragonfruit', 'grapefruit', 'honeydew', 'jackfruit', 'kiwifruit', 'lime',
    'mulberry', 'nectar', 'olive', 'pineapple', 'pomegranate', 'raspberry', 'starfruit', 'tomato', 'ugli', 'vanilla',
    'walnut', 'xigua', 'yellowberry', 'zucchini', 'airplane', 'bicycle', 'computer', 'dolphin', 'elephant', 'furniture',
    'giraffe', 'house', 'island', 'jungle', 'kangaroo', 'lamp', 'mountain', 'notebook', 'octopus', 'pencil', 
    'quilt', 'robot', 'sunflower', 'telescope', 'umbrella', 'vaccine', 'window', 'xylophone', 'yacht', 'zebra'
]

print("HANGMAN GAME")
class HangmanGame:
    def __init__(self, master):  
        self.master = master
        self.master.title("Hangman Game")
        self.master.geometry('600x400')  # Size 
        self.master.eval('tk::PlaceWindow . center')  

        self.lives = 6 
        self.chosen_word = random.choice(word_list)
        self.display = ['_'] * len(self.chosen_word)
        self.guessed_letters = set()

        # Create labels and buttons
        self.word_label = tk.Label(master, text=" ".join(self.display), font=("Courier", 20))
        self.word_label.pack(pady=20)

        self.hangman_label = tk.Label(master, text=stages[self.lives], font=("Courier", 15))
        self.hangman_label.pack(pady=25)

        self.guess_entry = tk.Entry(master)
        self.guess_entry.pack(pady=10)

        self.guess_button = tk.Button(master, text="Guess", command=self.make_guess)
        self.guess_button.pack(pady=10)

        self.lives_label = tk.Label(master, text=f"Lives left: {self.lives+1}", font=("Helvetica", 15))  # Display 7 initially
        self.lives_label.pack(pady=10)

    def make_guess(self):
        guessed_letter = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)

        if guessed_letter in self.guessed_letters:
            messagebox.showinfo("Error", "You already guessed that letter!")
            return

        self.guessed_letters.add(guessed_letter)

        if guessed_letter in self.chosen_word:
            for pos, letter in enumerate(self.chosen_word):
                if letter == guessed_letter:
                    self.display[pos] = guessed_letter
            self.word_label.config(text=" ".join(self.display))
        else:
            self.lives -= 1
            self.hangman_label.config(text=stages[self.lives])
            self.lives_label.config(text=f"Lives left: {self.lives+1}")
            if self.lives == 0:
                messagebox.showinfo("Game Over", f"You lost! The word was '{self.chosen_word}'.")
                self.hangman_label.config(text=stages[0])  
                self.lives_label.config(text="Lives left: 0")  # lives to 0
           

        if "_" not in self.display:
            messagebox.showinfo("You Win!", "Congratulations, you guessed the word!")
            #

root = tk.Tk()
hg = HangmanGame(root)  
root.mainloop()
