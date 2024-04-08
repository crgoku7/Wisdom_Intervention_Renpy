

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

    python:

        
        import datetime
        import urllib.request
        import urllib.parse
        import os
        import json
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
                s = str(e)
                renpy.say("Error:", s)
        #"tushar", "black", 'brown', "fair"
        #player_name, haircolor, eyecolor, headcolor
        send_data_to_server(player_name, haircolor, eyecolor, headcolor)
            
    return
