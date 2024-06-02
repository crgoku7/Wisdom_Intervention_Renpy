label episode_2:
    $current_time = 480
    scene classroom
    "You reach the class on time, with Ritwik and Trina."
    "You can hear all kinds of discussions taking place."
    "You look around for a place to sit."
    show rich_kids
    "One group of students, all flaunting thier new gadget and accessories."
    "They all seem to be wearing branded shoes and watches."
    show nerdy-kids
    "Another group in engrossed in academic discussions."
    "They seem to be discussing about the achievments to Newton and Einstien."
    show sports-kids
    "Lastly, you catch the talks about the lastest sports matches going around in another group."
    "They all seem to be pretty enthusiactic about sports, some looking pretty atheletic."
    scene classroom
    "Unsure where to sit, you look at Ritwik and Trina"
    r "So, where do you think we should sit?"

    menu:
        "Sit with the cool kids":
            $ group = "rich"
            p "Let's try mingling with the rich kids. Thier gadgets look pretty cool."

            "The trio heads over to the group of rich kids, trying to fit in."
            jump episode_2_rich

        "Sit with the nerds":
            $ group = "nerds"
            p "Let's join the nerds. We might learn something new."
            "The trio heads over to the group of nerds, ready to engage in intellectual discussions."
            jump episode_2_nerds

        "Sit the sports geeks":
            $ group = "sports"
            p "Let's join the sports enthusiasts. We could use some physical activity."
            "The trio heads over to the group of sports enthusiasts, eager to talk about their favorite games."
            jump episode_2_sports

label episode_2_rich:
    scene rich_kids
    "The rich kids look at the trio curiously as they approach."
    p "Hi, can we join you?"
    "The rich kids glance at each other before one of them nods."

    jump episode_2_rich_conversation

label episode_2_nerds:
    scene nerdy-kids
    "The nerds barely look up from their books as the trio approaches."
    p "Hey, mind if we join you?"
    "One of the nerds looks up, pushes up their glasses, and nods."

    jump episode_2_nerds_conversation

label episode_2_sports:
    scene sports-kids
    "The sports enthusiasts welcome the trio with friendly smiles."
    p "Can we join you guys?"
    "One of the sports enthusiasts grins and pats a seat next to them."
   
    jump episode_2_sports_conversation



label episode_2_rich_conversation:
    scene rich_kids
    "As you sit with the rich kids, you try to get into thier conversation."
    "Student 1" "Dude, who do you think the dance team captain is gonna be this year."
    "Student 2" "Don't know man, but Samir and Maira both are pretty good, should be either or them"
    "Student 1" "Yeah!, both of them are pretty dope, didn't come to class today did they?"
    "Student 2" "Yeah, I dont' see them."
    "Hmmm, Samir and Maira is it, seem to be pretty popular."
    

    "Nothing much happens and its soon time for the Lunch Break"

    jump lunch_break

label episode_2_nerds_conversation:
    scene nerdy-kids
    "Among the nerds, all of them are talking about different Maths and Science concepts."
    "Student 1" "What's the smallest bone in the human body?"
    "Student 2" "Its the stapes bone in the ear, 2.8 millimeters long."
    "Student 2" "My turn, what's the longest?"
    p "I know that, its.."
    menu:
        "Tibia":
            "The boy looks at you with indifference."
            "Student 2" "Wrong."
        "Femur":
            "Student 2" "Hmm, Correct."
            "You feel happy inside, giving the correct answer."
        "Fibula":
            "The boy looks at you with indifference."
            "Student 2" "Wrong."
        "Humerus":
            "The boy looks at you with indifference."
            "Student 2" "Wrong."

    "Nothing much happens and its soon time for the Lunch Break"

    

    jump lunch_break

label episode_2_sports_conversation:
    scene sports-kids
    "Sitting with the sports enthusiasts, you realise that these people can talk about sports non-stop."
    "Student 1" "Hey, the sports trails are coming soon right?"
    "Student 2" "Yeah, they happen in a week or two I think."
    "Student 1" "Man, I hope I get into the team."
    "Student 2" "Well, getting into the team is not that tough, let's see who'll be the sports captain."
    "Hmm looks like becoming the sports captain in a big deal."
    "Nothing much happens and its soon time for the Lunch Break"


    jump lunch_break




label lunch_break:
    scene cafeteria
    "During the lunch break, the cafeteria buzzes with students chatting and enjoying their meals."

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

