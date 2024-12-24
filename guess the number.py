import tkinter as tk
from tkinter import messagebox
import random

class GuessTheNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number Game")
        self.root.geometry("400x300")
        self.root.config(bg="#f5f5f5")

        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.title_label = tk.Label(root, text="Guess the Number!", font=("Arial", 20, "bold"), bg="#f5f5f5", fg="#2d2d2d")
        self.title_label.pack(pady=10)

        self.instruction_label = tk.Label(root, text="Guess a number between 1 and 100", font=("Arial", 14), bg="#f5f5f5", fg="#5a5a5a")
        self.instruction_label.pack(pady=5)

        self.guess_entry = tk.Entry(root, font=("Arial", 14), width=15, bd=2, relief="solid")
        self.guess_entry.pack(pady=10)

        self.guess_button = tk.Button(root, text="Guess", font=("Arial", 14), bg="#4CAF50", fg="white", command=self.check_guess)
        self.guess_button.pack(pady=10)

        self.attempts_label = tk.Label(root, text="Attempts: 0", font=("Arial", 12), bg="#f5f5f5", fg="#2d2d2d")
        self.attempts_label.pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return

        self.attempts += 1
        self.attempts_label.config(text=f"Attempts: {self.attempts}")

        if guess < self.secret_number:
            messagebox.showinfo("Try Again", "Too low! Try a higher number.")
        elif guess > self.secret_number:
            messagebox.showinfo("Try Again", "Too high! Try a lower number.")
        else:
            messagebox.showinfo("Congratulations!", f"Congratulations! You guessed the number in {self.attempts} attempts.")
            self.reset_game()

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.attempts_label.config(text="Attempts: 0")
        self.guess_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    game = GuessTheNumberGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
