import tkinter as tk

root = tk.Tk()

root.overrideredirect(True)
root.attributes("-topmost", True)
root.config(bg="black")
root.wm_attributes("-transparentcolor", "black")
root.geometry("200x200+500+500")

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
label.pack()

label.image = pet_image  # pyright: ignore


root.mainloop()
