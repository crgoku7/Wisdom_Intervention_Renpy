# The script of the game goes in this file.

init python:
    import datetime
    import urllib.request
    import urllib.parse
    import os
    import json

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

    # Function to send player data and file to the FastAPI server
    def send_data_to_server(player_name, haircolor, eyecolor, headcolor):
        try:
            # Prepare the data to be sent
            data = {
                'player_name': player_name,
                'haircolor': haircolor,
                'eyecolor': eyecolor,
                'headcolor': headcolor
            }
            data_json = json.dumps(data).encode("utf-8")


            renpy.say('s',"Before Request")
            # Construct the HTTP request
            req = urllib.request.Request('http://localhost:8000/upload/', data=data_json, method='POST')
            req.add_header('Content-Type', 'application/json')


            # Send the request
            renpy.say('s',"Request Sent")
            with urllib.request.urlopen(req) as response:

                server_response = response.read().decode('utf-8')
                # Process server response as needed
            
        except Exception as e:
            # s = str(e)
            # renpy.say("Error:", s)
            pass
    #"tushar", "black", 'brown', "fair"
    #player_name, haircolor, eyecolor, headcolor
            
            

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
    

    
    



# Declare characters used by this game. The color argument colorizes the
define p = Character("Player")
define r = Character("Ritwik", color = "#991111")
define s = Character("Shreya", color = "#660066")
define t = Character("Trina", color = "#007711")
define h = Character("Headmaster", color = "#dddddd")

# name of the character.

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
    
# ... your existing code ...

# ... your existing code ...

# Define the player_profile screen
screen player_profile:
    modal True
    # Background image (optional)
    # image bg = "path/to/background.jpg"
    frame:
        xalign 0.5 yalign 0.25 
        # Create sections using vbox
        vbox:  # Notice the colon after vbox
            # Player Info Section
            hbox:
                textbutton f"Name: {main_player.name}"
                textbutton f"Age: 14 Years Old"
                # Add a birth_year variable to your Player_class and initialize it in the init function
            label "Player Info"
            
            # Space between sections
            #ypad=10

            # Player Stats Section
            vbox:
                textbutton f"Strength: {main_player.stats['Strength']}"
                textbutton f"Intelligence: {main_player.stats['Intelligence']}"
                textbutton f"Charisma: {main_player.stats['Charisma']}"
            label "Stats"
        
            # Space between sections

            # Player Relations Section
            vbox:
            # Loop through NPC relations and display their names and affection points
                for npc_name in main_player.npc_rel.keys():
                    textbutton f"{npc_name}: {main_player.npc_rel[npc_name]}"
                label "Relations"
            textbutton "Close":
                action Hide("player_profile")

    # Center the sections on screen
    # anchor:
    #     vcenter vbox_sections  # This line should refer to the vbox itself, not vbox_sections




#image room = im.Scale("room.png", 1280, 720)

transform player_transform:
    zoom 0.5
    align (0.0,0.7) 
# The game starts here.

label look_mirror:
    show player at player_transform
    "Hmmm"

default main_player = Player_class()
default tutorial_complete = 0

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

    call episode_1
    
