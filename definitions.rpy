### definitions
    

# Various definitions used in the game:

# Define the text bleep functionality for the speaker. 
# Uses bleep005 from https://dmochas-assets.itch.io/dmochas-bleeps-pack 
# Source: https://www.renpy.org/wiki/renpy/doc/cookbook/Expanded_Text_Bleeps 
init python:
    def text_bleep(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/bleep.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound", fadeout=1)

# Define the speaker character. Will be used later as the narrator. 
define av = Character(" ", callback=text_bleep)

# Define the question counter. 
default current_question_idx = 0

# Define the player's starting score. 
default score = 0

# Define the variable that stores the player's response. 
default player_response = ""

# Define the background image. 
image background = 'images/backgrounds/background.jpg'


# Audio definitions:
# Source: https://www.youtube.com/watch?v=vS-8Dtr_R50

# Popping sound effect for when a question comes up. 
# 2:13 in the source video. 
define audio.pop = "audio/pop.ogg"

# Hover sound for when a player hovers over an answer choice. 
# In the "keyboard/mouse" section in the source video (about 1:28?). 
define audio.hover = "audio/hover.ogg"

# Dinging sound effect for when a player selects the right answer. 
# 2:28 in the source video. 
define audio.ding = "audio/ding.ogg"

# Dizzy sound effect for when a player selects the wrong answer. 
# 3:51 in the source video. 
define audio.dizzy = "audio/dizzy.ogg"

# Victory sound effect for when a player finishes the game. 
# 3:43 in the source video. 
define audio.victory = "audio/victory.ogg"







# ATL and animation definitions:

# A transition to slide an element up from the bottom. 
transform slide_up_center:
    xalign 0.5
    yalign 3
    ease 0.75 yalign 0.3

# A transition to slide an element down to the bottom. 
transform slide_center_down:
    xalign 0.5
    ypos 150
    ease 0.75 ypos 1000

# A transition for the first part of a "flip".
transform flip:
    xzoom 1
    yalign 0.3
    ease 0.5 xzoom 0

# A transition for the second part of a "flip".
transform unflip:
    xzoom 0
    yalign 0.3
    ease 0.5 xzoom 1


