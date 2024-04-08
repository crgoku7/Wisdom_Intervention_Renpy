label Sit_ritwik:
    "Making yourself comfortable, you take a glance at the book"
    "~Some fancy name I'll think of later~"
    "Seems to be a pretty fancy book"
    "The boy notices your interest"
    "Boy" "Are you a new student?"
    p "Ah! yes"
    r "Hi, I am Ritwik, I'am in grade 7th"
    p "Hi my name is.."
    $player_name = renpy.input("What is your name?")
    define p = Character("[player_name]")
    p "[player_name], I'll also be joining in grade 7th"
    $main_player.change_npc_rel("Ritwik", 10)

    #Personality Questions come here
    $current_time += 15
    return

label Sit_shreya:
    "Making yourself comfortable, you look in an around the bus"
    "Students chatting with their friends, some busy reading and some.."
    "Some just looking outside the window"
    "Girl" "WOAH!"
    p "Wha.. what happened?!"
    "Girl" "Nothing you just scared me, I usu.. never mind"
    "She goes back to looking outside"
    p "Umm, sorry for scaring you, I didn't mean it"
    "Girl" "Ah never mind"
    "Girl" "By the way, never seen you around, are you new here?"
    p "Yes, I am a new student, my name is.."
    $player_name = renpy.input("What is your name?")
    define p = Character("[player_name]")
    p "[player_name], I'll be joining in grade 7th, and you are?"
    s "Oh! I am Shreya, I'm also in 7th grade"
    $main_player.change_npc_rel("Shreys", 10)


    #Personality Questions come here

    $current_time += 15
    return