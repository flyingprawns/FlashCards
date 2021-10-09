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
window.config(padx=20, pady=20, background=BACKGROUND_COLOR)

# Flashcard
flashcard = tkinter.Canvas(width=700, height=500, highlightthickness=0)
flashcard_front_image = tkinter.PhotoImage(file=CARD_FRONT_IMAGE_PATH)
flashcard.create_image(350, 250, image=flashcard_front_image)
flashcard.grid(row=1, column=1, columnspan=2)

# Exit GUI window
window.mainloop()
