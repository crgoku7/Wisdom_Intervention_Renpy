
label episode_1:
    scene room
    "{b}{cps=50}Triiiiiiiiiing.....{/cps}" 
    "{b}{cps=50}Tringggggggggg.....{/cps}" 
    
    p "{cps=25}Wha...What time is it.."
    p "{cps=25}WHAT! its already 7:30, main gate closes at 8!!"
    p "{cps=25}I need to hurry.{/cps}"
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show screen clock

    menu:
        "Brush your teeth":
            call Brush
        "Skip it, I'm late":
            call No_brush
    

    call Breakfast_choice
    
    #Way to School
    show entrance
    "You quickly make your way out to the school"
    $current_time +=2
    $temp = get_current_time()
    p "Ok, so its [temp] right now.."
    scene bus-stop
    if current_time>465:
        "You quickly make your way to the bus stop"
        "Only to find that you've missed the bus..."
        call No_school_bus
    else:
        $current_time = 465
        "Against all odd you managed to reach the bus stop in time and board the bus"
        call School_bus
    scene school-open
    "Soon you reach school"
    if current_time>480:
        'You find that the School Gates are closed'
        p "Excuse me,I'am sorry for being late, its my first day.."
        p "Can you please open the gates?"
        "Guard" "What is your name kid?"
        p "My name is ..."
        $player_name = renpy.input("What is your name?")
        "The guard writes your name in his Register..."
        define p = Character("[player_name]")
        "Guard" "Hmm, I'll let you off today, since its the first day, But don't be late again"
        "You quickly rush inside, and make your way towards the assembly area."
        
    else:
        $current_time = 480
        "You head inside the school, following the crowd of students"
        "Feeling more excited than nervous for your first day at school"
        "You head towards the assembly area."

    call Headmaster_Speech

    scene classroom
    "You move out of the assembly hall, and try to find your class."
    call Ritwik_Player_Convertation
    call Ritwik_Player_Trina_Convertation
    call Situation2
    "Nothing much happens rest of the day, and its time to go back home."
    call episode_2

    return

label Brush:
    
    show bathroom
    "you quickly enter the bathroom and take a look in the mirror"
    p "Hmm, let me fix my looks.."
    #Set player avatar here:
    show background
    call screen player_select
    scene bathroom
    show player at Transform(zoom = 0.5, xalign = 0.5, yalign = -0.1)
    p "I look amazing!"
    "Without wasting much time you start brushing your teeth quickly"
    "Explaining to yourself its better being few minutes late than having a bad breath"
    $brushed = True
    init python:
        main_player.change_stats("Charisma", 1)
    $current_time+=7

    return



label No_brush:

    "You argue that there's no time left to brush your teeth, rather you just rinse your mouth with water a few times."
    $current_time+=2
    return

label Breakfast_choice:
    scene room
    "You get dressed up fast and look at your watch"
    $current_time+=5
    
    if current_time>=465:
        p "Oh no no, theres not much time left"
    else:
        p "Okay, I've got this, there's still some time"
    scene entrance

    "You put on your shoes and just as you are about to leave for school"
    "Grrrrrr......"
    "You hear your tummy grumble"

    menu:
        "Grab something to eat from the kitchen":
            call Breakfast
        "Forget it I'll be late":
            call No_breakfast

    return

label Breakfast:
    scene kitchen

    $current_time += 10
    "You quickly dash to the kitchen, and rummage through the fridge to look for something to eat."
    "You find some brown bread and peanut butter, which you spread over and gulp with a glass of milk."
    return

label No_breakfast:
    if brushed:
        "Having spent sometime in getting freshed up, you realise you are really running out of time now"
        p "Its better to skip the breakfast, I'll find something on the way"
    else:
        "You think that neither hygine nor hunger can stop you from reaching school on time and postpone the morning meal"
        p "I've gotta reach school as soon as possible, it's the first day..."

    return

label School_bus:
    "You reach just in time for the school bus, breathing a sigh of relief while boarding it."
    "You look around and see 2 empty seats"
    "One is besides a boy, who is reading some book"
    "The other is with a girl, who is looking outside the window"
    menu:
        "You choose to sit with the Boy":
            call Sit_ritwik
        "You choose to sit with the Girl":
            call Sit_shreya

    return

label No_school_bus:
    "You try to contemplate and find your next course of action"
    "When you see a car approach you"
    p "Hey! can you please give me a lift"
    if brushed:
        "Stranger" "Yeah sure, Hop in"
        p "Thank you so much!"
        "Stranger" "You look to be from XYZ school, What's your name?"
        p "My name, it's.."
        $player_name = renpy.input("What is your name?")
        "Stranger" "Oh, that's a really nice name."
        define p = Character("[player_name]")
        p "Thanks"
    else:
        "Stranger" "Umm, sorry I'am running a bit late"
        "He says while making a face"
        "It seems not brushing your teeth was a bad decision on your part."
        "What a bad start to first day of school you think, while looking at a puddle"
        "The puddle, showing you your face"
        scene background
        call screen player_select
        p "No! I won't ruin my first day"
        "Thinking this you run towards your school"

    $current_time += 15
    return

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




label Headmaster_Speech:
    scene headmaster
    h "Good morning and very welcome to all of you present here."
    h "Today starts the beginning of the new academic year."
    h "May your year be filled with wisdom, passion and enthusiasm."
    h "Remember, you’re all instructed to follow the school rules."
    h "We boast five esteemed Houses, each embodying a powerful element"
    h "Each house will have their own characteristics and their activities will be defined by it. "
    
    h "They are as follows"
    h "Neer (water): Adaptable and ever-flowing, like the currents of knowledge."
    h "Agni (fire): Burning with passion and unwavering determination."
    h "Avani (earth): Rooted in stability and a grounded spirit."
    h "Vyom (sky): Where boundless creativity takes flight."
    h "Marut (air): Sharpening intellect with the swiftness of wind."
    h "The house selection process will start next month. Dismissed!"
    return



label Ritwik_Player_Convertation:
    r " Hey, are you lost?"
    p "Yes, it seems I don't know where to go."
    r "Which class are you in?"
    p "7B"
    r "I am in the same class. Its this way, let’s go."
    # They both walk towards the class.
    
    if "Ritwik" in main_player.npc_rel:
        pass
    else:
        r "By the way, I am Ritwik."
        p "I am [p]. Thanks for helping me, Ritwik."
        r " Its no problem."
        $main_player.change_npc_rel('Ritwik',10)
    r "By the why [p], Where are you from?"
    p "I am from Mumbai. What about you?"
    r "I am from Indore. Have you thought about which house you will choose?"
    p "Not yet. I am kind of confused. I feel like I want to part of all the houses at once." 
    r "Thats interesting. I think-"
    'Ritwik bumps into someone while walking.'
    r "I am so sorry."
    return

label Ritwik_Player_Trina_Convertation:
    'He realizes its his friend, Trina.'
    r "Oh, hi Trina."
    t "Hey Ritwik"
    r "Meet [p]. [p], this is Trina, my friend. We travel in the same bus." 
    # Trina and you shake hands
    t "Hi [p], how are you?"
    p "Hi Trina, nice to meet you. I am good."
    $main_player.change_npc_rel("Trina", 10)
    'The three of you soon move inside the class, and decide to sit together.'
    'You feel nice to have made two new friend so quickly'
    $main_player.change_mood("Happy")
    "Today being the first day of school, nothing interesting happens in the classes"
    "With the teachers taking a basic introduction of all students"
    return

label Situation2:
    "Soon the Lunch Break starts"
    "You are sitting along with Ritwik and Trina, having fun together"
    "Trina seems to be very kind and polite"
    "While Ritwik has a great sense of humor"
    r 'Why don\'t scientists trust atoms?'
    p "Why?"
    r 'Because they make up everything!, Hahahah!'
    menu:
        "Laugh Along":
            p 'Hahahaha'
            $main_player.change_npc_rel("Ritwik", 5)
        "What a lame joke":
            p "Hmm, ok and?"
            r "Duh!, that was the joke man"
            $main_player.change_npc_rel("Ritwik", -5)
    r "Oh, anyways, look whose over there, Ms. Shy-reya"
    "The girl looks towards [r] and ignores him"
    r "What happened Ms. Shy shy not in the mood to say anything?"

    menu:
        "Laugh along with Ritwik":
            'You find the situation funny and laugh along with Ritwik'
            if "Shreya" in main_player.npc_rel:
                "Shreya looks towards you with teary eyes"
            else:
                "The girl looks towards your group with teary eyes"
            t "Stop both of you!"
            t "Shreya, I'm really sorry on behalf of both of them"
            $main_player.change_npc_rel("Shreya", -10)
            $main_player.change_npc_rel("Trina", -2)
            $main_player.change_stats("Charisma", -1)
            
        "Stop and Confront Ritwik":
            p 'Ritwik, This is not funny.'
            if "Shreya" in main_player.npc_rel:
                p "I am really sorry Shreya, on behalf of him"
                r "Wha-, man, I, I am sorry Shreya, didn't mean to hurt you."
                "Shreya looks towards you relief"

            else:
                r'I was just having some fun, chill man'
                p 'That is not the way you have fun, you should apologise to her.'
                r "Wha-, man, I, I am sorry Shreya, didn't mean to hurt you."
                "Shreya looks towards you relief"
            $main_player.change_npc_rel("Shreya", 10)
            $main_player.change_npc_rel("Trina", 2)

    
            
    return




