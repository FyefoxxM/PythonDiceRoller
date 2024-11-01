import tkinter as tk
from tkinter import ttk
import random

class DiceSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Simulator")
        self.root.geometry("400x500")
        
        # Dice face configurations using ASCII art
        self.d4_faces = {
            1: "  ╱▲╲\n ╱ 1 ╲\n╱     ╲\n‾‾‾‾‾‾‾",
            2: "  ╱▲╲\n ╱ 2 ╲\n╱     ╲\n‾‾‾‾‾‾‾",
            3: "  ╱▲╲\n ╱ 3 ╲\n╱     ╲\n‾‾‾‾‾‾‾",
            4: "  ╱▲╲\n ╱ 4 ╲\n╱     ╲\n‾‾‾‾‾‾‾"
        }
        
        self.d6_faces = {
            1: "┌─────────┐\n│         │\n│    ●    │\n│         │\n└─────────┘",
            2: "┌─────────┐\n│  ●      │\n│         │\n│      ●  │\n└─────────┘",
            3: "┌─────────┐\n│  ●      │\n│    ●    │\n│      ●  │\n└─────────┘",
            4: "┌─────────┐\n│  ●   ●  │\n│         │\n│  ●   ●  │\n└─────────┘",
            5: "┌─────────┐\n│  ●   ●  │\n│    ●    │\n│  ●   ●  │\n└─────────┘",
            6: "┌─────────┐\n│  ●   ●  │\n│  ●   ●  │\n│  ●   ●  │\n└─────────┘"
        }

        # Create and configure the main frame
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Number of dice selector
        ttk.Label(self.main_frame, text="Number of Dice:").grid(row=0, column=0, pady=5)
        self.num_dice = ttk.Spinbox(self.main_frame, from_=1, to=5, width=5)
        self.num_dice.set(1)
        self.num_dice.grid(row=0, column=1, pady=5)

        # Dice type selector
        ttk.Label(self.main_frame, text="Dice Type:").grid(row=1, column=0, pady=5)
        self.dice_type = ttk.Combobox(self.main_frame, values=["d4", "d6", "d8", "d12", "d20"], width=5)
        self.dice_type.set("d6")
        self.dice_type.grid(row=1, column=1, pady=5)

        # Roll button
        self.roll_button = ttk.Button(self.main_frame, text="Roll Dice!", command=self.roll_dice)
        self.roll_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Results display
        self.result_text = tk.Text(self.main_frame, height=15, width=40, font=('Courier', 10))
        self.result_text.grid(row=3, column=0, columnspan=2, pady=10)

        # History display
        ttk.Label(self.main_frame, text="Roll History:").grid(row=4, column=0, columnspan=2, pady=5)
        self.history_text = tk.Text(self.main_frame, height=5, width=40)
        self.history_text.grid(row=5, column=0, columnspan=2, pady=5)

        self.roll_history = []

    def roll_single_die(self, sides):
        """Simulate rolling a single die with given number of sides."""
        return random.randint(1, sides)

    def get_dice_face(self, value, dice_type):
        """Get ASCII art representation of a die face."""
        if dice_type == 4:
            return self.d4_faces.get(value, str(value))
        elif dice_type == 6:
            return self.d6_faces.get(value, str(value))
        return str(value)

    def roll_dice(self):
        """Handle the dice rolling action and update the display."""
        try:
            num_dice = int(self.num_dice.get())
            dice_type = int(self.dice_type.get()[1:])  # Extract number from 'd6', 'd20' etc.
            
            # Clear previous results
            self.result_text.delete(1.0, tk.END)
            
            # Roll the dice and calculate total
            rolls = [self.roll_single_die(dice_type) for _ in range(num_dice)]
            total = sum(rolls)
            
            # Display results
            if dice_type in [4, 6]:  # Show ASCII art for d4 and d6
                for roll in rolls:
                    self.result_text.insert(tk.END, self.get_dice_face(roll, dice_type) + "\n\n")
            else:
                roll_str = ", ".join(str(roll) for roll in rolls)
                self.result_text.insert(tk.END, f"Rolls: {roll_str}\n")
            
            self.result_text.insert(tk.END, f"\nTotal: {total}")
            
            # Update history
            roll_record = f"{num_dice}d{dice_type}: {rolls} = {total}"
            self.roll_history.append(roll_record)
            if len(self.roll_history) > 5:  # Keep only last 5 rolls
                self.roll_history.pop(0)
            
            # Update history display
            self.history_text.delete(1.0, tk.END)
            for record in self.roll_history:
                self.history_text.insert(tk.END, record + "\n")

        except ValueError:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Please enter valid numbers")

if __name__ == "__main__":
    root = tk.Tk()
    app = DiceSimulator(root)
    root.mainloop()