# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
define p = Character("Player")
define r = Character("Ritwik", color = "#991111")
define s = Character("Shreya", color = "#660066")
define t = Character("Trina", color = "#007711")
define h = Character("Headmaster", color = "#dddddd")

# name of the character.
init python:
    class Player_class():
        def __init__(self):
            self.name = "Player"
            self.stats = {'Strength':5, 'Intelligence': 5, 'Charisma': 5}
            self.npc_rel = {}
            self.mood = "Neutral"
            
        def change_npc_rel(self, npc_name, value):
            if npc_name in self.npc_rel:
                self.npc_rel[npc_name] += value
            else:
                self.npc_rel[npc_name] = value
            if self.npc_rel[npc_name]<0:
                self.npc_rel[npc_name] = 0
            if value>0:
                renpy.notify(f"Affinity with {npc_name} increased.")
            else:
                renpy.notify(f"Affinity with {npc_name} decreased.")
        def change_stats(self, stat, value):
            self.stats[stat]+=value
            if self.stats[stat]<0:
                self.stats[stat] = 0
            if value>0:
                renpy.notify(f"Your {stat} increased")
            else:
                renpy.notify(f"Your {stat} decreased")
        def change_mood(self, newmood):
            self.mood = newmood
            renpy.notify(f"Mood changed to {newmood}")
        
        

    def get_current_time():
        global current_time
        hour = current_time//60
        minute = current_time-hour*60
        if minute<10:
            minute = "0"+str(minute)
        formated_time = f"{hour}:{minute}"
        return formated_time
    
    def show_player_profile():
        renpy.show_screen("player_profile")
        
    def customize_character(type, direction):
        global haircolor
        global eyecolor
        global headcolor

        if type=="finish":
            pass


        if direction == "right":
            if type == "hair":
                haircolor = haircolors[(haircolors.index(haircolor)+1)%len(haircolors)]
            elif type == "eyes":
                eyecolor = eyecolors[(eyecolors.index(eyecolor)+1)%len(eyecolors)]
            elif type == "head":
                headcolor = headcolors[(headcolors.index(headcolor)+1)%len(headcolors)]
        if direction == "left":
            if type == "hair":
                haircolor = haircolors[(haircolors.index(haircolor)-1)%len(haircolors)]
            elif type == "eyes":
                eyecolor = eyecolors[(eyecolors.index(eyecolor)-1)%len(eyecolors)]
            elif type == "head":
                headcolor = headcolors[(headcolors.index(headcolor)-1)%len(headcolors)]

        renpy.retain_after_load()
    
    main_player = Player_class()



image player = Composite(
                (1000,1000),
                (0,0),"player/male/head-[headcolor].png",
                (0,0),"player/male/brow.png",
                (0,0),"player/male/hair-[haircolor].png",
                (0,0),"player/male/eye-[eyecolor].png"
                )

screen clock:
    frame:
        xalign 0 yalign 0
        vbox:
            
            text get_current_time()
        
            #add "player" at half_size align(0.5,0.5)
            #text "Strength: [main_player.stats[Strength]]"
            #text "Intelligence: [main_player.stats[Intelligence]]"
            #text "Charisma: [main_player.stats[Charisma]]"


transform half_size:
    zoom 0.5
transform arrows:
    zoom 0.5
    anchor (0.5,0.5)
    on hover:
        zoom 0.55
    on idle:
        zoom 0.5

screen player_select:
    add "player" at half_size align(0.5,0.5)

    #gender buttons
    imagebutton idle "UI/male_symbol.png" align(0.3,0.2) action Function(customize_character, type = "male", direction = "on") at arrows
    imagebutton idle "UI/female_symbol.png" align(0.7,0.2) action Function(customize_character, type = "female", direction = "on") at arrows
    #Hair
    imagebutton idle "UI/arrow-right.png" align(0.7,0.35) action Function(customize_character, type = "hair", direction = "right") at arrows
    imagebutton idle "UI/arrow-left.png" align(0.3,0.35) action Function(customize_character, type = "hair", direction = "left") at arrows

    #Eyes
    imagebutton idle "UI/arrow-right.png" align(0.7,0.5) action Function(customize_character, type = "eyes", direction = "right") at arrows
    imagebutton idle "UI/arrow-left.png" align(0.3,0.5) action Function(customize_character, type = "eyes", direction = "left") at arrows

    #head
    imagebutton idle "UI/arrow-right.png" align(0.7,0.65) action Function(customize_character, type = "head", direction = "right") at arrows
    imagebutton idle "UI/arrow-left.png" align(0.3,0.65) action Function(customize_character, type = "head", direction = "left") at arrows

    imagebutton idle "UI/finish.png" align(0.5,0.9) action Return()
    
screen player_profile:
    vbox:
        #add "player" at half_size align(0.5,0.5)
        text "Strength: [main_player.stats[Strength]]"
        text "Intelligence: [main_player.stats[Intelligence]]"
        text "Charisma: [main_player.stats[Charisma]]"

        imagebutton idle "UI/finish.png" align(0.5,0.9) action Return()


#image room = im.Scale("room.png", 1280, 720)

transform player_transform:
    zoom 0.5
    align (0.0,0.7) 
# The game starts here.

label look_mirror:
    show player at player_transform
    "Hmmm"

label start:
    $player_name = "Player"
    $current_time = 450
    $brushed = False
    $haircolors = ["a", "b", "c"]
    $eyecolors = ["black", "brown", "blue"]
    $headcolors = ["a", "b", "c"]
    $haircolor = haircolors[0]
    $eyecolor = eyecolors[0]
    $headcolor = headcolors[0]
   
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

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
        "Guard" "Hmm, I'll let you off today, since its the first day, But don't be late again"
        "You quickly rush inside, and make your way towards the assembly area."
        
    else:
        $current_time = 480
        "You head inside the school, following the crowd of students"
        "Feeling more excited than nervous for your first day at school"
        "You head towards the assembly area."

    call Headmaster_Speech
    scene classroom
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

label episode_2:
    scene classroom
    "As the trio enters the classroom, they notice the students are divided into various groups."
    show rich_kids
    "There are the rich kids, flaunting their expensive gadgets and designer clothes."
    show nerdy-kids
    "The nerds, engrossed in their books and intellectual discussions."
    show sports-kids
    "And the sports enthusiasts, energetically discussing the latest games and their own athletic exploits."
    scene classroom
    "The trio looks at each other, unsure of where to go."
    p "Where should we go?"

    menu:
        "Join the rich kids":
            $ group = "rich"
            p "Let's try mingling with the rich kids."
            "The trio heads over to the group of rich kids, trying to fit in."
            jump episode_2_rich

        "Join the nerds":
            $ group = "nerds"
            p "Let's join the nerds. We might learn something new."
            "The trio heads over to the group of nerds, ready to engage in intellectual discussions."
            jump episode_2_nerds

        "Join the sports enthusiasts":
            $ group = "sports"
            p "Let's join the sports enthusiasts. We could use some physical activity."
            "The trio heads over to the group of sports enthusiasts, eager to talk about their favorite games."
            jump episode_2_sports

label episode_2_rich:
    scene rich_kids
    "The rich kids look at the trio curiously as they approach."
    p "Hi, can we join you?"
    "The rich kids glance at each other before one of them nods."

    jump lunch_break

label episode_2_nerds:
    scene nerdy-kids
    "The nerds barely look up from their books as the trio approaches."
    p "Hey, mind if we join you?"
    "One of the nerds looks up, pushes up their glasses, and nods."

    jump lunch_break

label episode_2_sports:
    scene sports-kids
    "The sports enthusiasts welcome the trio with friendly smiles."
    p "Can we join you guys?"
    "One of the sports enthusiasts grins and pats a seat next to them."
   
    jump lunch_break

label lunch_break:
    scene cafeteria
    "During the lunch break, the cafeteria buzzes with students chatting and enjoying their meals. You spot a fellow classmate, shy and reserved, having a conversation with some students from a different house."

    show pushy-students
    "The students from the other house seem full of energy, unaware that they are being pushy in their conversation."

    
    "You recognizes the shy classmate, belonging to Trishanku house, caught in an uncomfortable situation."

    p "Hmm, I wonder if I should do something about it."

    menu:
        "Help the classmate":
            p "Deciding to intervene, you approache the group."
            "Hey, everything okay here?"

            if group == "rich":
                "The pushy students from the other house look at the you with disdain, recognizing you as part of the 'rich' group."

            elif group == "nerds":
                "The pushy students glance you, thinking he's just another bookworm."

            elif group == "sports":
                "The pushy students give tyou a once-over, noting your athletic appearance."

            "Ignoring the judgments, you turn to the shy classmate and asks, 'You okay?'"

            menu:
                "Explain the situation to the classmate":
                    p "You discreetly informs the shy classmate about the reputation of the other house, offering support."

                    if group == "rich":
                        p "The pushy students roll their eyes and continue their conversation, no longer interested in you."

                    elif group == "nerds":
                        p "The pushy students dismiss you and the shy classmate, continuing with their discussion."

                    elif group == "sports":
                        p "The pushy students exchange glances, clearly unimpressed with the your interference."

                    "However, the shy classmate appreciates the help, and a student from Trishanku house, whom you recognize, nods in gratitude."

                    #points += 5
                    jump lunch_reward

                "Back off and avoid trouble":
                    p "Deciding not to get involved, you back away, leaving the shy classmate to deal with the pushy students."

                    if group == "rich":
                        p "The pushy students exchange smirks, having successfully excluded you from their conversation."

                    elif group == "nerds":
                        p "The pushy students don't pay much attention to you, too engrossed in their own discussion."

                    elif group == "sports":
                        p "The pushy students continue their conversation, barely acknowledging your presence."

                    "The shy classmate looks disappointed, and the student from Trishanku house gives you a disapproving look."

                    jump lunch_no_reward

label lunch_reward:
    p "The lunch break continues, and as you return to your own group, They notice some admiring glances from students of Trishanku house."

    p "Seems like showing empathy has earned me some brownie points!"

    jump lunch_continue

label lunch_no_reward:
    p "The lunch break continues, and as you returns to your own group, they can't help but feel a bit guilty about not helping the shy classmate."

    jump lunch_continue

label lunch_continue:
    "You spends the rest of the lunch break with their group, gossiping about various things and enjoying the company of their housemates."


    
