init python:
    def create_button_pattern(type):
        pattern = []
        if type == "easy":
            for i in range(4):
                pattern.append(renpy.random.randint(0,3))
        if type == "medium":
            for i in range(6):
                pattern.append(renpy.random.randint(0,3))
        if type == "hard":
            for i in range(8):
                pattern.append(renpy.random.randint(0,3))
        return pattern

    def set_difficulty(button):
        global current_difficulty
        if button =="right" and difficulties.index(current_difficulty) < len(difficulties)-1:
            current_difficulty = difficulties[difficulties.index(current_difficulty)+1]
        elif button =="left" and difficulties.index(current_difficulty) > 0:
            current_difficulty = difficulties[difficulties.index(current_difficulty)-1]
        renpy.restart_interaction()

    def light_buttons():
        global input_ready
        global correct_picks
        global current_button_index
        global red_button_lit
        global blue_button_lit
        global green_button_lit
        global yellow_button_lit

        if current_button_index < len(current_button_pattern):
            button_lit = buttons[current_button_pattern[current_button_index]]
            if button_lit == "red":
                red_button_lit = True
                blue_button_lit = False
                green_button_lit = False
                yellow_button_lit = False
            elif button_lit == "blue":
                red_button_lit = False
                blue_button_lit = True
                green_button_lit = False
                yellow_button_lit = False
            elif button_lit == "green":
                red_button_lit = False
                blue_button_lit = False
                green_button_lit = True
                yellow_button_lit = False
            elif button_lit == "yellow":
                red_button_lit = False
                blue_button_lit = False
                green_button_lit = False
                yellow_button_lit = True

            if correct_picks == current_button_index:
                input_ready = True
                correct_picks = 0

            current_button_index += 1
            renpy.restart_interaction()

        else:
            input_ready = True
            renpy.restart_interaction()

    def off_buttons():
        global red_button_lit
        global blue_button_lit
        global green_button_lit
        global yellow_button_lit

        red_button_lit = False
        blue_button_lit = False
        green_button_lit = False
        yellow_button_lit = False


    def check_user_input(button):
        global current_button_index
        global input_ready
        global correct_picks
        global user_picks
        global selected_button_index

        if buttons.index(button) == current_button_pattern[selected_button_index]:
            correct_picks += 1
            user_picks += 1
            if selected_button_index == user_picks:
                selected_button_index = 0
                current_button_index = 0
                user_picks = 0
                input_ready = False
            else:
                selected_button_index +=1
            renpy.restart_interaction()
        else:
            renpy.show_screen("game_over")
            renpy.hide_screen("simon_says")
        if correct_picks == len(current_button_pattern):
            renpy.show_screen("simon_says_menu")
            #renpy.transitions(Fade(1,0,1))
            renpy.hide_screen("simon_says")


transform half_size:
    zoom 0.5

screen simon_says:
    image "/images/Backgrounds/background.png" at half_size
    if red_button_lit:
        imagebutton idle "/images/Backgrounds/red-button-lit.png" align(0.15, 0.65) at half_size
    if not red_button_lit:
        imagebutton auto "/images/Backgrounds/red-button-%s.png" align(0.15, 0.65) action [SetVariable("red_button_lit", True) , Function(check_user_input, button = "red")] at half_size
    
    if blue_button_lit:
        imagebutton idle "/images/Backgrounds/blue-button-lit.png" align(0.35, 0.52) at half_size
    elif not blue_button_lit:
        imagebutton auto "/images/Backgrounds/blue-button-%s.png" align(0.35, 0.52) action [SetVariable("blue_button_lit", True) , Function(check_user_input, button = "blue")] at half_size

    if green_button_lit:
        imagebutton idle "/images/Backgrounds/green-button-lit.png" align(0.65, 0.52) at half_size
    elif not green_button_lit:
        imagebutton auto "/images/Backgrounds/green-button-%s.png" align(0.65, 0.52) action [SetVariable("green_button_lit", True) , Function(check_user_input, button = "green")] at half_size

    if yellow_button_lit:
        imagebutton idle "/images/Backgrounds/yellow-button-lit.png" align(0.88, 0.65) at half_size
    elif not yellow_button_lit:
        imagebutton auto "/images/Backgrounds/yellow-button-%s.png" align(0.88, 0.65) action [SetVariable("yellow_button_lit", True) , Function(check_user_input, button = "yellow")] at half_size

    if not input_ready:
        timer 1.0 action Function(light_buttons) repeat True
    if red_button_lit or blue_button_lit or green_button_lit or yellow_button_lit:
        timer 0.5 action Function(off_buttons) repeat True

    #imagebutton auto "/images/Backgrounds/red-button-%s.png" align(0.15, 0.65) action NullAction() at half_size
    #imagebutton auto "/images/Backgrounds/blue-button-%s.png" align(0.35, 0.52) action NullAction() at half_size
    #imagebutton auto "/images/Backgrounds/green-button-%s.png" align(0.65, 0.52) action NullAction() at half_size
    #imagebutton auto "/images/Backgrounds/yellow-button-%s.png" align(0.88, 0.65) action NullAction() at half_size

screen simon_says_menu:
    modal True
    image "/images/Backgrounds/background.png" at half_size
    frame:
        background "#00000080"
        xfill True
        yfill True
        frame:
            background Frame("/images/UI/menu-background.png")
            xysize(int(1548/2), int(941/2))
            align(0.5,0.5)
            text "Difficulty: [current_difficulty]" size 30 color "#ffffff" outlines[(absolute(2),"#000000",0,0)] align(0.5,0.45) at half_size
            imagebutton idle "/images/UI/arrow-left.png" align(0.25,0.46) anchor(0.5,0.5) action Function(set_difficulty, button="left") at half_size
            imagebutton idle "/images/UI/arrow-right.png" align(0.75,0.46) anchor(0.5,0.5) action Function(set_difficulty, button="right") at half_size
            imagebutton idle "/images/UI/play-button.png" align(0.3,0.8) anchor(0.5,0.5) action [Hide("simon_says_menu"),Show("simon_says")] at half_size
            imagebutton idle "/images/UI/quit-button.png" align(0.8,0.8) anchor(0.5,0.5) action NullAction() at half_size


label sisa:
    #$test_variable = create_button_pattern("easy")
    #$print(test_variable)
    $button_pattern_easy = create_button_pattern("easy")
    $button_pattern_medium = create_button_pattern("medium")
    $button_pattern_hard = create_button_pattern("hard")
    $current_button_pattern = button_pattern_easy
    $difficulties = ["easy","medium","hard"]
    $current_diffuculty = "easy"
    $red_button_lit = False
    $blue_button_lit = False
    $green_button_lit = False
    $yellow_button_lit = False
    $buttons = ("red","blue","green","yellow")
    $current_button_index = 0
    $input_ready = False
    $correct_picks = 0
    $user_picks = 0
    $selected_button_index = 0

    call screen simon_says
    return