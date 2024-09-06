# defining characters: Episode 4
define X = Character("Me")
define senior1 = Character("Rohan")
define senior2 = Character("Vishal")
define senior3 = Character("Akansha")

# defining images
image school_corridor = "images/school_corridor.jpg"
image house_meetingroom = "images/meetingroom.jpg"

# define the houses
define water = "Water"
define fire = "Fire"
define earth = "Earth"
define air = "Air"
define sky = "Sky"
define trishanku = "Trishanku"

label start:
    scene school_corridor
    with fade

    X "Today is the day I have to choose a house that best fits my personality."

    "Which house do you want to choose?"

    menu:
        "Fire - Passion and determination":
            $ chosen_house = fire
        "Water - Flexibility and adaptivity":
            $ chosen_house = water
        "Earth - Stability and groundedness":
            $ chosen_house = earth
        "Air - Intellect and cleverness":
            $ chosen_house = air
        "Sky - Creativeness and expansiveness":
            $ chosen_house = sky

    X "I think [chosen_house] suits me best!"

    # first house meeting
    scene house_meetingroom
    with fade

    X "This is my first house meeting. I am so excited to meet everyone."

    if chosen_house == fire:
        senior1 "Welcome to the House of Fire! We are known for passion and determination."
        senior2 "This is your first house meeting. From this day onwards, you're a proud member of the House of [chosen_house]."
        senior2 "Today, we will introduce you to who we are and get you familiar with the history and glory of our house. At the end of the session, there will be a small compatibility test, so do listen carefully."

        senior2 "Founded during the early days of the school, the House of Fire emerged as a symbol of ambition and vigor."
        "Its establishment was driven by the desire to cultivate leadership and determination among students."

        senior3 "We believe in:
            1. Strength in Passion: True strength comes from pursuing one’s passions with unwavering determination.
            2. Leadership and Courage: We value bravery and the ability to lead with integrity.
            3. Overcoming Challenges: We believe that obstacles are opportunities for growth and self-improvement."

        senior2 "Over the years, we have had many achievements:
            - We are renowned for spearheading groundbreaking projects and initiatives within the school.
            - We are known for consistently having member leaders who excel in various fields.
            - We have achieved numerous victories in competitive sports, reflecting our dynamic and energetic spirit."

        senior3 "And we hope you carry on the name and pride that comes with it gracefully."
        senior1 "Here's to the new year and new stories."

        $ quiz_questions = [
            "What is the main value of the House of Fire?",
            "Which achievement is most associated with the House of Fire?", 
            "Which trait best describes your approach to achieving goals?"
        ]
        $ quiz_options = [
            ["Flexibility and adaptability", "Creativity and expansiveness", "Passion and determination", "Stability and groundedness"],  # Options for Question 1
            ["Exceptional community service", "Dominating academic competitions",  # Options for Question 2
            "Innovative projects and leadership in sports", "Artistic and cultural contributions"], 
            ["I tackle challenges head-on with enthusiasm and determination.", # Options for Question 3
            "I adapt to circumstances and find new ways to overcome obstacles.", 
            "I rely on practical solutions and a steady, methodical approach.",
            "I analyze the situation carefully and think of creative solutions."]  
        ]
        $ correct_answers = ["Passion and determination", "Innovative projects and leadership in sports", "I tackle challenges head-on with enthusiasm and determination."]

    elif chosen_house == water:
        senior1 "Welcome to the House of Water! We are celebrated for flexibility and adaptability."
        senior2 "This is your first house meeting. From this day onwards, you're a proud member of the House of [chosen_house]."
        senior2 "Today, we will introduce you to who we are and get you familiar with the history and glory of our house. At the end of the session, there will be a small compatibility test, so do listen carefully."

        senior2 "The House of Water was established to represent adaptability and empathy. It was inspired by the flowing nature of water, which can shape itself to fit any container while nurturing growth. The house’s founders aimed to create a supportive environment where students could thrive by embracing change and fostering strong connections with others."

        senior3 "We believe in:
            1. Flexibility is Key: Being open to new experiences.
            2. Empathy and Understanding: We believe in the power of emotional intelligence and building strong relationships.
            3. Balance and Harmony: We value the ability to maintain balance in all aspects of life."

        senior2 "Over the years, we have had many achievements:
            - We are known for exceptional involvement in community outreach and service projects.
            - We excel in group projects and team-based activities due to our cooperative spirit.
            - We are skilled in mediating disputes and fostering harmony within the school."

        senior3 "And we hope you carry on the name and pride that comes with it gracefully."
        senior1 "Here's to the new year and new stories."

        $ quiz_questions = [
            "What is a core belief of the House of Water?",
            "Which achievement is most closely related to the House of Water?", 
            "How do you handle unexpected changes or challenges?"
        ]
        $ quiz_options = [
            ["Flexibility is key and balance is important.", "Imagination and creative freedom are essential.", 
            "Passion and leadership drive success.", "Practicality and reliability are crucial."],  # Options for Question 1
            ["High academic performance and debate success", "Community outreach and collaborative success",  # Options for Question 2
            "Artistic and cultural innovations", "Groundbreaking projects and sports victories"], 
            ["I embrace them and find new ways to adapt.", # Options for Question 3
            "I stick to my plan and try to overcome the challenge with determination.", 
            "I seek practical solutions and a stable approach.",
            "I think creatively to come up with innovative solutions."]  
        ]
        $ correct_answers = ["Flexibility is key and balance is important.", "Community outreach and collaborative success", "I embrace them and find new ways to adapt."]

    elif chosen_house == earth:
        senior1 "Welcome to the House of Earth! We represent stability and groundedness."
        senior2 "This is your first house meeting. From this day onwards, you're a proud member of the House of [chosen_house]."
        senior2 "Today, we will introduce you to who we are and get you familiar with the history and glory of our house. At the end of the session, there will be a small compatibility test, so do listen carefully."

        senior2 "Founded on principles of stability and reliability, the House of Earth represents the solid foundation upon which the school is built. Its history is rooted in the idea that a strong, grounded approach is essential for personal and academic success. The house was named for its role in providing stability and support to the school community."

        senior3 "We believe in:
            1. Foundation of Strength: It is important to be dependable and maintaining a strong sense of responsibility.
            2. Practicality and Resilience: We value practical approaches to problem-solving and resilience in the face of adversity.
            3. Tradition and Integrity: We hold tradition and moral integrity in high regard."

        senior2 "Over the years, we have had many achievements:
            - We have consistently performed high in academics due to our disciplined and focused approach.
            - Many members of our house serve in key positions in student government and other official roles.
            - We are known for their contributions to maintaining school traditions and enhancing the school’s overall structure."
            
        senior3 "And we hope you carry on the name and pride that comes with it gracefully."
        senior1 "Here's to the new year and new stories."

        $ quiz_questions = [
            "Which value is central to the House of Earth?",
            "Which achievement is most closely related to the House of Water?", 
            "What is your preferred method for solving problems?"
        ]
        $ quiz_options = [
            ["Flexibility and adaptability", "Creativity and expansiveness", "Intellect and Clever", "Stability and groundedness"],  # Options for Question 1
            ["Exceptional artistic contributions", "Innovative and creative projects",  # Options for Question 2
            "Leadership in student governance and high academic performance", "Success in community service and teamwork"], 
            ["By sticking to a practical and steady approach.", "By adapting and finding flexible solutions.", 
            "By creatively thinking of new ideas.", "By leading with passion and determination."]  #Options for Question3
        ]
        $ correct_answers = ["Stability and groundedness", "Leadership in student governance and high academic performance", "By sticking to a practical and steady approach."]

    elif chosen_house == air:
        senior1 "Welcome to the House of Air! We are celebrated for intellect and cleverness."
        senior2 "This is your first house meeting. From this day onwards, you're a proud member of the House of [chosen_house]."
        senior2 "Today, we will introduce you to who we are and get you familiar with the history and glory of our house. At the end of the session, there will be a small compatibility test, so do listen carefully."

        senior2 "The House of Air has its origins are linked to a vision of fostering a culture of curiosity and mental agility. The house is inspired by the idea that just as air is vital for life, so is intellectual exploration crucial for personal growth."

        senior3 "We believe in:
            1. Curiosity Drives Knowledge: We encourage a constant quest for knowledge and intellectual growth.
            2. Innovative Thinking: We value creativity and the ability to think outside the box.
            3. Wit and Wisdom: We believe in the power of cleverness and insightful problem-solving."

        senior2 "Over the years, we have had many achievements:
            - We dominate in academic competitions and quizzes, showcasing their sharp minds.
            - We are known for innovative and original projects in various fields, from science to the arts.
            - Many of our members are influential in academic and debate circles within the school."

        senior3 "And we hope you carry on the name and pride that comes with it gracefully."
        senior1 "Here's to the new year and new stories."

        $ quiz_questions = [
            "What is a core belief of the House of Air?",
            "Which achievement is most closely linked to the House of Air?", 
            "How do you approach learning and new ideas?"
        ]
        $ quiz_options = [
            ["Practicality and responsibility are essential.", "Creativity and imaginative thinking drive progress.", 
            "Flexibilty and balance are key to success.", "Passion and leadership are the primary values."],  # Options for Question 1
            ["High achievements in community service and collaboration", "Dominance in sports and innovative projects",  # Options for Question 2
            "Success in artistic and cultural pursuits", "Excellence in academic competitions and intellectual leadership"], 
            ["By seeking creative and innovative approaches.", # Options for Question 3
            "By following practical and grounded methods.", 
            "By adapting and being flexible in how I learn.",
            "By leading with passion and determination."]  
        ]
        $ correct_answers = ["Creativity and imaginative thinking drive progress.", "Dominance in sports and innovative projects", "By seeking creative and innovative approaches."]

    elif chosen_house == sky:
        senior1 "Welcome to the House of Sky! We are known for creativity and expansiveness."
        senior2 "This is your first house meeting. From this day onwards, you're a proud member of the House of [chosen_house]."
        senior2 "Today, we will introduce you to who we are and get you familiar with the history and glory of our house. At the end of the session, there will be a small compatibility test, so do listen carefully."

        senior2 "The House of Sky was established to embody creativity and expansiveness. Its history is marked by a desire to inspire students to think beyond conventional limits and explore their creative potential. The house’s founders envisioned a space where imagination could soar as high as the sky."

        senior3 "We believe in:
            1. Imagination Knows No Limits: To explore and embrace their creative potential without boundaries.
            2. Freedom of Expression: We value the freedom to express oneself and explore new ideas.
            3. Vision and Innovation: We believe in the power of visionary thinking to drive progress and innovation."

        senior2 "Over the years, we have had many achievements:
            - We are recognized for unique and imaginative solutions to problems and challenges.
            - We are known for Known for outstanding achievements in arts, music, and other creative endeavors.
            - We play a key role in enhancing the school’s cultural and artistic landscape."

        senior3 "And we hope you carry on the name and pride that comes with it gracefully."
        senior1 "Here's to the new year and new stories."

        $ quiz_questions = [
            "What is a key belief of the House of Sky?",
            "Which achievement is most associated with the House of Sky?", 
            "What motivates you the most in your creative pursuits?"
        ]
        $ quiz_options = [
            ["Flexibility and adaptability are crucial.", "Imagination and boundless creativity are essential.", 
            "Practicality and responsibility are the most important.", "Passion and leadership are central to success."],  # Options for Question 1
            ["High achievements in community service and collaboration", "Innovative and creative projects",  # Options for Question 2
            "Success in artistic and cultural pursuits", "Excellence in academic competitions and intellectual leadership"], 
            ["The freedom to explore and express new ideas.", # Options for Question 3
            "The practicality and stability of the project.", 
            "The challenge and determination to achieve goals.",
            "The ability to adapt and find flexible solutions."]  
        ]
        $ correct_answers = ["Imagination and boundless creativity are essential.", "Success in artistic and cultural pursuits", "The freedom to explore and express new ideas."]

    #the quiz part
    mc "WOW! This is all so cool and fascinating. I am so excited to give the quiz and see how well I fit in"

    $ score = 0
    python:
        for i, question in enumerate(quiz_questions):
            renpy.say("mc", question)
            options = quiz_options[i]
            correct_answer = correct_answers[i]
            choice = renpy.display_menu([
                (options[0], 0),
                (options[1], 1),
                (options[2], 2),
                (options[3], 3)
            ])
            if options[choice] == correct_answer:
                score += 1


    if score == 3:
        mc "I did great! I got all the questions right."
    elif score == 2:
        mc "Not bad, but I missed one question."
    else:
        mc "I didn't do so well. My score is quite low."

    #mc sad slightly
    mc "Although.."
    mc "Everyone seems so happy. I wonder if I wont fit in."
    senior "Don't worry about the score. It's just a way to learn more about the house. You'll fit in just fine!"



#Canteen scene
# Define Characters with their dialogue color
define mc = Character("MC", color="#00BFFF")
define friend = Character("Friend", color="#FFA500")
define senior = Character("Senior", color="#FF0000")
define P = Character("P", color="#32CD32")
define housemate = Character("Housemate", color="#FFD700")

# Define Character Images
image mc_normal = "images/mc_normal.jpg"
image mc_surprised = "images/mc_surprised.jpg"
image friend = "images/friend_normal.jpg"
image senior_angry = "images/senior_angry.jpg"
image P = "images/P_worried.jpg"
image housemate_fallen = "images/housemate_fallen.jpg"
image sad = "images/sad.jpg"

# Define Background Images
image canteen = "images/canteen_background.jpg"
image incident = "images/bully_incident.jpg"

label canteen_scene:

    scene canteen
    with fade

    show mc_normal at left
    show friend at right

    mc "It was a good meeting. I'm glad we're in the same house."
    friend "Yeah, let's grab something to eat and celebrate our first day!"

    # Transition to the canteen scene
    mc "As we were enjoying our time, something caught our attention."

    scene incident
    with fade
    
    show P at top
    show housemate_fallen at right
    show senior_angry at left

    mc "A guy, P, accidentally pushed another student, who is from our house."
    mc "I saw that it wasn't P's fault, but our house senior started badgering him."

    senior "Watch where you're going, Trishanku trash!"
    P "I'm sorry, I didn't mean to—"
    senior "Apologies won't cut it. Know your place!"

    mc "This is getting out of hand. What should I do?"

    # Choice point for the player
    menu:
        "Stand up to the senior and take P's side":
            $ choice = "stand_up"
            mc "Excuse me, it wasn't his fault. He didn't do it on purpose."
            senior "Who do you think you're talking to? Don't meddle in things you don't understand."
            mc "But he—"
            senior "Enough. Next time, keep your mouth shut if you know what's good for you."

            mc "I tried to help, but now it feels like I've only made things worse."
            friend "Let's just go. This isn't worth getting into trouble over."
            mc "Yeah, maybe you're right..."

        "Just watch as you stand by":
            $ choice = "stand_by"
            mc "I feel bad for P, but if I interfere, it might just make things worse for me too."
            mc "..."
            mc "The senior eventually walks away, and P looks relieved but hurt."
            mc "I can't shake off the feeling that I should have done something."

            friend "Hey, you okay?"
            mc "Yeah, just thinking..."
            friend "It wasn't your fight. Sometimes it's better to stay out of these things."
            mc "I know, but it still doesn't feel right."

label after_canteen:

    scene canteen
    with fade
    
    show sad

    mc "Today was supposed to be a good day, but now I can't stop thinking about what happened in the canteen."
    
    if choice == "stand_up":
        mc "Standing up for P felt like the right thing to do, but now I'm worried about the consequences with my house."
    elif choice == "stand_by":
        mc "Maybe staying out of it was the safe choice, but it doesn't feel good knowing I could have helped."

    mc "This school year is already more complicated than I thought..."

    jump school_morning
    #return








