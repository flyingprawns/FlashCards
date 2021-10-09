import tkinter

CARD_FRONT_IMAGE_PATH = "./images/card_front.png"
CARD_BACK_IMAGE_PATH = "./images/card_back.png"
RIGHT_BUTTON_IMAGE_PATH = "./images/right.png"
WRONG_BUTTON_IMAGE_PATH = "./images/wrong.png"
BACKGROUND_COLOR = "#B1DDC6"

# --------------------- GUI INTERFACE -------------------------#
# GUI Window
window = tkinter.Tk()
window.title("Flashcards")
window.minsize(width=800, height=500)
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# Flashcard
flashcard = tkinter.Canvas(width=800, height=540, highlightthickness=0, background=BACKGROUND_COLOR)
flashcard_front_image = tkinter.PhotoImage(file=CARD_FRONT_IMAGE_PATH)
flashcard.create_image(400, 270, image=flashcard_front_image, anchor=tkinter.CENTER)
flashcard.grid(row=1, column=1, columnspan=2, pady=10)

# "Wrong" button
wrong_button_image = tkinter.PhotoImage(file=WRONG_BUTTON_IMAGE_PATH)
wrong_button = tkinter.Button(image=wrong_button_image, highlightthickness=0, bd=0, anchor=tkinter.CENTER)
wrong_button.grid(row=2, column=1, pady=7)

# "Right" button
right_button_image = tkinter.PhotoImage(file=RIGHT_BUTTON_IMAGE_PATH)
right_button = tkinter.Button(image=right_button_image, highlightthickness=0, bd=0, anchor=tkinter.CENTER)
right_button.grid(row=2, column=2, pady=7)

# Exit GUI window
window.mainloop()
