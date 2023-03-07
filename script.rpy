label start:
    call screenshider
    "Hello and welcome to ClimateCafé the game, or at least the first alpha tech demo"
    "Story is still not done and also there are many things that will not work now, like the text here :-)"
    "You can already try the minigame named sameGame, which is a match many game to get rid of plastic items"
    "also some questions are alredy inside if you want to see how they look like"
    "graphics etc. in this version are minimal, to make sure the game first works and later it gets its nice graphics"
    "have fun and see you soon in the next release with more done."
    menu:
        "sameGame (works)":
            call matchgame
        "Numbers (may give error)":
            call memoria_game
        "Simon Says (WIP, will definetly crash)":
            call sisa
        "Sample of Questions":
            call questionsGame


label screenshider:
    hide screen SameGame
    hide screen scoreUI
    hide screen gameOver 