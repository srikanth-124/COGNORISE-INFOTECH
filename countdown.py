import tkinter as tk
from tkinter import messagebox

# Sample timer duration (2 minutes 30 seconds)
initial_time = 2 * 60 + 30

def update_timer():
    global time_left
    if time_left > 0:
        mins, secs = divmod(time_left, 60)
        time_str = f'{mins:02d}:{secs:02d}'
        timer_label.config(text=time_str)
        time_left -= 1
        root.after(1000, update_timer)
    else:
        messagebox.showinfo("Time's up", "The countdown has ended!")

def start_timer():
    global time_left
    try:
        time_left = initial_time
        update_timer()
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for minutes and seconds.")

root = tk.Tk()
root.title("Countdown Timer")
root.geometry("300x200")

tk.Label(root, text="Minutes:").pack()
entry_minutes = tk.Entry(root)
entry_minutes.pack()

tk.Label(root, text="Seconds:").pack()
entry_seconds = tk.Entry(root)
entry_seconds.pack()

timer_label = tk.Label(root, text="00:00", font=("Helvetica", 48))
timer_label.pack()

start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.pack()

root.mainloop()