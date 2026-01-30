import random
import tkinter as tk
from tkinter import ttk
import random
import json
import os
from tkinter import ttk, messagebox, simpledialog  # simpledialog for name input

''' 1 for snake 0 for gun -1 for water
'''
  
   
class SnakeWaterGunGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Water Gun - Advanced GUI")
        self.root.geometry("400x500")
        self.root.configure(bg="lightblue")
        
        self.choices = {"Snake": 1, "Water": -1, "Gun": 0}
        self.reverse = {1: "Snake 🐍", -1: "Water 💧", 0: "Gun 🔫"}
        self.player_score = 0
        self.computer_score = 0
        self.load_scores()
        
        self.setup_ui()

    # to entering the name of the player for better exp.
    def get_player_name(self):
        self.player_name = tk.simpledialog.askstring("Player Name", "Enter your name:", parent=self.root)
        if not self.player_name:
            self.player_name = "Player"
        self.player_name = self.player_name.strip().title()
    

    def setup_ui(self):
        # Title
        title = tk.Label(self.root, text="Snake Water Gun", font=("Arial", 24, "bold"), bg="lightblue", fg="darkblue")
        title.pack(pady=20)
        
        # Scores
        self.score_label = tk.Label(self.root, text="You: 0 | Computer: 0", font=("Arial", 16, "bold"), bg="white", relief="solid", padx=20)
        self.score_label.pack(pady=10)
        
        # Player vs Computer frame
        vs_frame = tk.Frame(self.root, bg="lightblue")
        vs_frame.pack(pady=20)
        
        self.player_label = tk.Label(vs_frame, text="You: ?", font=("Arial", 18), bg="lightgreen", width=15, height=2, relief="raised")
        self.vs_label = tk.Label(vs_frame, text="VS", font=("Arial", 20, "bold"), bg="lightblue")
        self.comp_label = tk.Label(vs_frame, text="Computer: ?", font=("Arial", 18), bg="lightcoral", width=15, height=2, relief="raised")
        
        self.player_label.pack(side=tk.LEFT, padx=10)
        self.vs_label.pack(side=tk.LEFT, padx=10)
        self.comp_label.pack(side=tk.LEFT, padx=10)
        
        # Result
        self.result_label = tk.Label(self.root, text="", font=("Arial", 20, "bold"), bg="yellow", width=30, height=2, relief="solid")
        self.result_label.pack(pady=20)
        
        # Buttons frame
        btn_frame = tk.Frame(self.root, bg="lightblue")
        btn_frame.pack(pady=20)
        
        tk.Button(btn_frame, text="Snake 🐍", font=("Arial", 14), width=12, height=2,
                  command=lambda: self.play(1), bg="green", fg="white", relief="raised").pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Water 💧", font=("Arial", 14), width=12, height=2,
                  command=lambda: self.play(-1), bg="blue", fg="white", relief="raised").pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Gun 🔫", font=("Arial", 14), width=12, height=2,
                  command=lambda: self.play(0), bg="orange", fg="white", relief="raised").pack(side=tk.LEFT, padx=10)
        
        # Reset
        tk.Button(self.root, text="Reset Game", font=("Arial", 14), width=20, height=2,
                  command=self.reset, bg="red", fg="white").pack(pady=20)
    
    def play(self, player_choice):
        comp_choice = random.choice([0, 1, -1])
        self.player_label.config(text=f"You: {self.reverse[player_choice]}")
        self.comp_label.config(text=f"Comp: {self.reverse[comp_choice]}")
        
        if player_choice == comp_choice:
            result = "Draw!"
            self.result_label.config(bg="gray")
        else:
            diff = (player_choice - comp_choice + 3) % 3
            if diff == 1:
                result = "You Win! 🎉"
                self.player_score += 1
                self.result_label.config(bg="lightgreen")
            else:
                result = "You Lose! 😢"
                self.computer_score += 1
                self.result_label.config(bg="lightcoral")
        
        self.result_label.config(text=result)
        self.score_label.config(text=f"You: {self.player_score} | Computer: {self.computer_score}")
        self.save_scores()
        for btn in self.root.winfo_children()[5].winfo_children():  # Disable buttons
            btn.config(state="disabled")
        self.root.after(2000, self.enable_buttons)
    
    def reset(self):
        self.player_label.config(text="You: ?")
        self.comp_label.config(text="Computer: ?")
        self.result_label.config(text="")
        self.enable_buttons()
    
    def enable_buttons(self):
        for btn in self.root.winfo_children()[5].winfo_children():
            btn.config(state="normal")
    
    def save_scores(self):
        with open("scores.json", "w") as f:
            json.dump({"player": self.player_score, "computer": self.computer_score}, f)
    
    def load_scores(self):
        if os.path.exists("scores.json"):
            with open("scores.json", "r") as f:
                data = json.load(f)
                self.player_score = data.get("player", 0)
                self.computer_score = data.get("computer", 0)

if __name__ == "__main__":
    root = tk.Tk()
    app = SnakeWaterGunGUI(root)
    root.mainloop()



    computer = random.choice([0 , -1 , 1 ]) 
    yourstr = input("Enter your Choice :- ").strip().capitalize() 
    your_dic =  {"Snake" : 1 , "Water" : -1, "Gun" : 0 } 
    reverse_dic = { 1 : "Snake" , -1 : "Water" , 0 : "Gun" }
    try:
        you = your_dic[yourstr]
        print(f"You choose the = {reverse_dic[you]} \nComputer choose =  {reverse_dic[computer]}")
        
        if (computer == you):
            print("Your match is draw !!")
        elif (computer == 1 and you == 0):
            print("You Won !! ")
        elif (computer == 1 and you == -1):
            print("You lose !! ")
        elif (computer == 0 and you == 1):
            print("You lose !! ")
        elif (computer == 0 and you == -1):
            print("You Won !! ")
        elif (computer == -1 and you == 1):
            print("You Won !! ")    
        elif (computer == -1 and you == 0):
            print("You lose !! ")
    except KeyError:
        print("Invalid input. Please choose Snake, Water, or Gun.")


    

















    