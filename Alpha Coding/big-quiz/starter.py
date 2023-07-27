# Importing the library
import pgzrun

# Initialize variables


# Rect takes in 4 parameters. The first two are the coordinates of the top-left
# corner of the box and the last two are the coordinates of the bottom-right
# corner of the box
main_box = Rect(0, 0, 820, 240) # This sets the box size to 820 px wide and 240 px high
timer_box = Rect(0, 0, 240, 240)
answer_box1 = Rect(0, 0, 495, 165)

# Move the boxes to the correct positions
# move_ip() moves each rectangle to the place you want it on the screen
main_box.move_ip(50, 40)

# Create a list of answer boxes


# Set-up the quiz questions
q1 = ["What's the capital of France?", "London", "Paris", "Berlin", "Tokyo", 2]


def draw():
    pass


def game_over():
    pass


def correct_answer():
    pass

def on_mouse_down(pos):
    pass

def update_time_left():
    pass


pgzrun.go()
