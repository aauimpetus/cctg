# The game starts here.
label questionsGame:

    # Initialize the setup. 
    call make_question_list from _call_make_question_list

    # Show the background. 
    show background

    # Introduce the game. 
    "Welcome to trivia!"
    "Pick the answer choice you think is correct."
    "After you've made your choice, the correct answer will come up."
    "Try to score as many points as possible!"
    "Good luck!"


# Show the current question. 
label begin_game:

    # Initializing setup on each turn for testing purposes.
    # Can be commented out in the final game. 
    #call make_question_list from _call_make_question_list_1
    # Otherwise, get the next question. 
    # If the player has run out of questions, end the game. 
    if current_question_idx >= len(question_list):
        jump finished

    # Otherwise, get the next question. 
    $ current_question = question_list[current_question_idx]

    # Introduce the question. 
    # Note that Python indexing starts at 0, which is why we need to add 1. 
    $ adjusted_idx = current_question_idx + 1
    "Here's question [adjusted_idx]."

    # Show the text for the current question. 
    show text [current_question.question] at slide_up_center
    pause 0.4
    play sound pop


# Show a menu displaying all four answer choices. 
menu:
    "[current_question.a1]":
        $ player_response = current_question.a1
        call start_after from _call_start_after

    "[current_question.a2]":
        $ player_response = current_question.a2
        call start_after from _call_start_after_1

    "[current_question.a3]":
        $ player_response = current_question.a3
        call start_after from _call_start_after_2

    "[current_question.a4]":
        $ player_response = current_question.a4
        call start_after from _call_start_after_3


# Process the player's response. 
label start_after:

    # Hide the question and show the correct response. 
    show text [current_question.question] at flip
    pause 0.5
    hide text [current_question.question]
    show text [current_question.correct] at unflip

    # If the player responds correctly:
    if (player_response == current_question.correct):
        play sound ding
        pause 0.5
        "You got it right! Great job!"
        $ score += current_question.point_value

    # If the player responds incorrectly:
    else:
        play sound dizzy
        pause 1.3
        "You didn't get it right, but good try!"

    # Display the current score and start again. 
    "Your current score is [score]."

    # Increment the question counter. 
    $ current_question_idx += 1

    # Hide the current correct answer. 
    show text [current_question.correct] at flip
    pause 0.5
    hide text [current_question.correct]

    # Jump back to the start of the turn. 
    jump begin_game


# Finish the game.
label finished:

    # Display the player's final score. 
    play sound victory
    "Congratulations! Your final score is [score]."

    jump end


label end:

    # Hide the dialogue window.
    window hide

    # Direct the player back to the main menu. 
    $ MainMenu(confirm=False)()

    

return
