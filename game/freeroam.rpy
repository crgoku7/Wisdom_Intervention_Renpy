screen room_to_hall():
    modal True
    imagebutton:
        xpos 0
        ypos 0
        idle "images/map_nav/transparent_idle.png"
        hover "images/map_nav/room2hall_hover.png"
        action Call("livingroom")








label freeroam:
    show entrance
    p "Back Home!"
    $main_player.name = player_name
    if tutorial_complete == 0:
        call episode_1_cleared
        $tutorial_complete = 1
    
    p "Hmm..What should I do next?"
    "You have lunch and do the basic chores."
    "Soon its time to go to bed."
    "Triiiiiing.........."
    "Its a new day, rise and shine."
    call bathroom
    call kitchen
    call entrance






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

    return
label bedroom:
    return
label livingroom:
    "This is the living room"
    return
    

label entrance:
    show entrance
    "You leave for school."
    return
label kitchen:
    show kitchen
    "You have your breakfast."
    return
label bathroom:
    show bathroom
    "You take a bath and get fresh."
    return

