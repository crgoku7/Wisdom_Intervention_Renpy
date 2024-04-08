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

