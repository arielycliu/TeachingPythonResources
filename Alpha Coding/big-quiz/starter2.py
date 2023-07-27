import pgzrun

# Initialize variables
from pgzero import clock

WIDTH = 1280
HEIGHT = 720

main_box = Rect(0, 0, 820, 240)
timer_box = Rect(0, 0, 240, 240)
answer_box1 = Rect(0, 0, 495, 165)
answer_box2 = Rect(0, 0, 495, 165)
answer_box3 = Rect(0, 0, 495, 165)
answer_box4 = Rect(0, 0, 495, 165)

main_box.move_ip(50, 40)
timer_box.move_ip(990, 40)
answer_box1.move_ip(50, 358)
answer_box2.move_ip(735, 358)
answer_box3.move_ip(50, 538)
answer_box4.move_ip(735, 538)

answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]
score = 0
time_left = 60

# Set-up quiz questions
q_example = ["What is the capital of France?",
            "London", "Paris", "Berlin", "Tokyo", 2]

q1 = ["Which element is the first element in the periodic table?",
      "Boron", "Helium", "Hydrogen", "Oxygen", 3]
q2 = ["What is Scotland's national animal?",
      "unicorn", "wildcat", "pine marten", "puffins", 1]
q3 = ["How old was the oldest person to ever live?",
      "112", "122", "132", "113", 2]
q4 = ["How many hearts do octopuses have?",
      "2", "1", "4", "3", 4]
q5 = ["Which symbol is used to make Python comments?",
      "!", "#", "--", "//", 2]

questions = [q1, q2, q3, q4, q5]
question = questions.pop(0)

def draw():
    # Draw main boxes to fill with text later
    screen.fill("black")
    screen.draw.filled_rect(main_box, "cornflowerblue")
    screen.draw.filled_rect(timer_box, "black")

    # Draw answer boxes and fill in text for timer and question
    for box in answer_boxes:
        screen.draw.filled_rect(box, "darkolivegreen1")
        screen.draw.textbox(str(time_left), timer_box, color=("white"))  # Write the remaining time
        screen.draw.textbox(question[0], main_box, color=("white"))

    # Write answers text into answer boxes
    index = 1
    for box in answer_boxes:
        screen.draw.textbox(question[index], box, color=("black"))
        index = index + 1


def game_over():
    global question, time_left
    message = f"Game over. You got {str(score)} questions correct"
    question = [message, ":)", ":o", ":D", ";)", 5]
    time_left = 0


def correct_answer():  # runs when you get the correct answer
    global question, score, time_left
    # Changes question, options, timer
    score += 1  # score = score + 1
    if questions != []:
        question = questions.pop(0)
        time_left = 60
    else:
        print("Game over!")
        game_over()


def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        correct_index = question[5]   # returning correct answer
        if box.collidepoint(pos):
            print("Clicked on answer " + str(index))
            if index == correct_index:
                print("You got it correct!")
                correct_answer()
            else:
                game_over()
        index = index + 1


def update_time_left():
    global time_left
    if time_left != 0:
        time_left = time_left - 1
    else:
        game_over()


clock.schedule_interval(update_time_left, 1.0)
pgzrun.go()
