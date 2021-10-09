import tkinter
import pandas
import random

CARD_FRONT_IMAGE_PATH = "./images/card_front.png"
CARD_BACK_IMAGE_PATH = "./images/card_back.png"
RIGHT_BUTTON_IMAGE_PATH = "./images/right.png"
WRONG_BUTTON_IMAGE_PATH = "./images/wrong.png"
BACKGROUND_COLOR = "#B1DDC6"
FLASHCARD_CATEGORY_FONT = ("Arial", 40, "italic")
FLASHCARD_CONTENT_FONT = ("Arial", 60, "bold")
FLASHCARD_DATA_PATH = "./data/french_words.csv"
CATEGORY_NAME_FRONT = 'French'
CATEGORY_NAME_BACK = 'English'

# --------------------- DATA PROCESSING ---------------------- #
# Create a list of dictionaries called "flashcard_list".
# Each dictionary looks like: {'French': 'WORD', 'English': 'WORD'}
flashcard_data = pandas.read_csv(FLASHCARD_DATA_PATH)
flashcard_list = flashcard_data.to_dict(orient="records")


# -------------------- FLASHCARD FUNCTIONALITY --------------- #
def display_flashcard(new_category_text, new_content_text):
    flashcard.itemconfig(flashcard_category_text, text=new_category_text)
    flashcard.itemconfig(flashcard_content_text, text=new_content_text)
    return


def display_random_flashcard():
    random_flashcard = random.choice(flashcard_list)
    display_flashcard(CATEGORY_NAME_FRONT, random_flashcard[CATEGORY_NAME_FRONT])
    return


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
flashcard_category_text = flashcard.create_text(400, 150, text="category", font=FLASHCARD_CATEGORY_FONT)
flashcard_content_text = flashcard.create_text(400, 270, text="content", font=FLASHCARD_CONTENT_FONT)
flashcard.grid(row=1, column=1, columnspan=2, pady=10)

# "Wrong" button
wrong_button_image = tkinter.PhotoImage(file=WRONG_BUTTON_IMAGE_PATH)
wrong_button = tkinter.Button(image=wrong_button_image, highlightthickness=0, bd=0, anchor=tkinter.CENTER,
                              command=display_random_flashcard)
wrong_button.grid(row=2, column=1, pady=7)

# "Right" button
right_button_image = tkinter.PhotoImage(file=RIGHT_BUTTON_IMAGE_PATH)
right_button = tkinter.Button(image=right_button_image, highlightthickness=0, bd=0, anchor=tkinter.CENTER,
                              command=display_random_flashcard)
right_button.grid(row=2, column=2, pady=7)

# Exit GUI window
window.mainloop()
