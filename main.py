import tkinter as tk
import random

root = tk.Tk()

root.overrideredirect(True)
root.attributes("-topmost", True)
root.config(bg="black")
root.wm_attributes("-transparentcolor", "black")

root.update()

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
win_w = root.winfo_width()
win_h = root.winfo_height()

x = screen_w - win_w - 50
y = screen_h - win_h - 50

root.geometry(f"+{x}+{y}")

exit_menu = tk.Menu(root, tearoff=0)
exit_menu.add_command(label="Exit", command=root.destroy)


def popup(event):
    try:
        exit_menu.tk_popup(event.x_root, event.y_root)
    finally:
        exit_menu.grab_release()


root.bind("<Button-3>", popup)

pet_image = tk.PhotoImage(file="idle.png")

label = tk.Label(root, image=pet_image, bg="black", bd=0)
label.pack(side="bottom")

label.image = pet_image  # pyright: ignore

speech_bubble = tk.Label(
    root,
    text="",
    fg="black",
    bg="white",
    font=("Arial", 10),
    wraplength=150,
    justify="center",
    borderwidth=2,
    relief="ridge",
)
speech_bubble.pack(side="top", fill="x", padx=10, pady=5)
speech_bubble.pack_forget()


def say_something():
    lines = ["did you drink water yet?", "dont stare at the screen for too long"]

    speech_bubble.config(text=random.choice(lines))
    speech_bubble.pack(side="top", fill="x", padx=10, pady=5)

    root.update()
    new_h = root.winfo_height()
    screen_h = root.winfo_screenheight()

    x = root.winfo_x()
    y = screen_h - new_h - 50
    root.geometry(f"+{x}+{y}")
    root.after(5000, lambda: speech_bubble.pack_forget())


root.bind("<Button-1>", lambda e: say_something())  # talking woking

root.mainloop()
