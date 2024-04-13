
label freeroam:
    show entrance
    p "Back Home!"
    if tutorial_complete == 0:
        call episode_1_cleared
        $tutorial_complete = 1
    return

label episode_1_cleared:
    show room
    "You change your clothes and lay down on your bed."
    "It was an eventful day today."
    "Just the first of many more to come."

    "You have made many connections today, you can check them in the player profile menu."
    
    #show player profile
    screen button_example():
        frame:
            xpos 80 ypos 0
            textbutton "View Profile":
                action Show("player_profile")
    show screen button_example

    "Your actions will decide how the relationships and attributes change."


