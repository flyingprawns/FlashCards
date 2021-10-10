import tkinter
from tkinter import messagebox
import pandas
import random

CARD_FRONT_IMAGE_PATH = "./images/card_front.png"
CARD_BACK_IMAGE_PATH = "./images/card_back.png"
NEXT_BUTTON_IMAGE_PATH = "./images/next.png"
FLIP_BUTTON_IMAGE_PATH = "./images/flip.png"
BACKGROUND_COLOR = "#B1DDC6"
FLASHCARD_CATEGORY_FONT = ("Arial", 40, "italic")
FLASHCARD_CONTENT_FONT = ("Arial", 60, "bold")
FLASHCARD_DATA_PATH = "./data/french_words.csv"


# --------------------- DATA PROCESSING ---------------------- #
# Create a list of dictionaries called "flashcard_list".
# Each dictionary looks like: {'French': 'WORD', 'English': 'WORD'}
flashcard_data = pandas.read_csv(FLASHCARD_DATA_PATH)
flashcard_list = flashcard_data.to_dict(orient="records")

# -------------------- FLASHCARD FUNCTIONALITY --------------- #
category_name_front = 'French'
category_name_back = 'English'
current_flashcard = None
current_side = None


def display_current_flashcard():
    global current_side
    if current_side == "FRONT":
        # Change image
        flashcard.itemconfig(flashcard_image, image=front_image)
        # Change text
        flashcard.itemconfig(flashcard_category_text, text=category_name_front)
        flashcard.itemconfig(flashcard_content_text, text=current_flashcard[category_name_front])
        # Change text color
        flashcard.itemconfig(flashcard_category_text, fill='black')
        flashcard.itemconfig(flashcard_content_text, fill='black')
    elif current_side == "BACK":
        # Change image
        flashcard.itemconfig(flashcard_image, image=back_image)
        # Change text
        flashcard.itemconfig(flashcard_category_text, text=category_name_back)
        flashcard.itemconfig(flashcard_content_text, text=current_flashcard[category_name_back])
        # Change text color
        flashcard.itemconfig(flashcard_category_text, fill='white')
        flashcard.itemconfig(flashcard_content_text, fill='white')
    else:
        pass
    return


def select_random_flashcard():
    # Pick random flashcard
    random_flashcard = random.choice(flashcard_list)
    # Save the flashcard and set the side to "FRONT"
    global current_flashcard
    global current_side
    current_flashcard = random_flashcard
    current_side = "FRONT"
    return


def flip_current_card():
    global current_side
    if current_side == "FRONT":
        current_side = "BACK"
    elif current_side == "BACK":
        current_side = "FRONT"
    else:
        pass
    return


# --------------------- GUI BUTTONS ---------------------------#
def next_card_button():
    if len(flashcard_list) == 0:
        # Reset flashcard status
        global current_flashcard
        global current_side
        current_flashcard = None
        current_side = None
        # Tell user they have finished studying
        messagebox.showinfo(title="Congratulations!", message="You've studied all the cards.")
        return
    else:
        select_random_flashcard()
        display_current_flashcard()
        flashcard_list.remove(current_flashcard)
        return


def flip_card_button():
    if current_flashcard is None:
        return
    else:
        flip_current_card()
        display_current_flashcard()
        return


# --------------------- GUI INTERFACE -------------------------#
# GUI Window
window = tkinter.Tk()
window.title("Flashcards")
window.minsize(width=900, height=770)
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# Flashcard
front_image = tkinter.PhotoImage(file=CARD_FRONT_IMAGE_PATH)
back_image = tkinter.PhotoImage(file=CARD_BACK_IMAGE_PATH)
flashcard = tkinter.Canvas(width=800, height=540, highlightthickness=0, background=BACKGROUND_COLOR)
flashcard_image = flashcard.create_image(400, 270, anchor=tkinter.CENTER, image=front_image)
flashcard_category_text = flashcard.create_text(400, 150, text="Buttons:", font=FLASHCARD_CATEGORY_FONT)
flashcard_content_text = flashcard.create_text(400, 270, text="\n\n\n Flip          Next", font=FLASHCARD_CONTENT_FONT)
flashcard.grid(row=1, column=1, columnspan=2, pady=10)

# "Flip" button
wrong_button_image = tkinter.PhotoImage(file=FLIP_BUTTON_IMAGE_PATH)
wrong_button = tkinter.Button(image=wrong_button_image, highlightthickness=0, bd=0, anchor=tkinter.CENTER,
                              command=flip_card_button)
wrong_button.grid(row=2, column=1, pady=7)

# "Next" button
right_button_image = tkinter.PhotoImage(file=NEXT_BUTTON_IMAGE_PATH)
right_button = tkinter.Button(image=right_button_image, highlightthickness=0, bd=0, anchor=tkinter.CENTER,
                              command=next_card_button)
right_button.grid(row=2, column=2, pady=7)

# GUI Window Mainloop
window.mainloop()
