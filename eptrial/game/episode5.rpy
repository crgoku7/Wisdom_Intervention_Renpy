#episode 5
define mc = Character("MC", color="#00BFFF")
define friend1 = Character("Y", color="#8A2BE2")
define friend2 = Character("friend2", color="#FF69B4")
define riya = Character("Riya", color="#FF4500")
define teacher = Character("Teacher", color="#32CD32")
define classmate1 = Character("Classmate", color="#FFD700")

# Define Character Images (Adding different emotions for characters)
image mc_normal = "images/mc_normal.jpg"
image mc_concerned = "images/mc_concerned.jpg"
image mc_confident = "images/mc_confident.jpg"
image mc_annoyed = "images/mc_annoyed.jpg"
image mcc_thinking = "images/mcc_thinking.jpg"

image friend1_smiling = "images/friend1_smiling.jpg"
image friend2_thinking = "images/friend2_thinking.jpg"

image riya_nervous = "images/riya_nervous.jpg"
image riya_sad = "images/riya_sad.jpg"
image riya_apologetic = "images/riya_apologetic.jpg"

image teacher_neutral = "images/teacher_neutral.jpg"

# Backgrounds
image classroom = "images/classroom_background.jpg"
image school_corridor = "images/school_corridor.jpg"
image cafeteria = "images/canteen_background.jpg"
image bedroom = "images/room.jpg"

image journal = "images/journal.jpg"

label school_morning:

    scene school_corridor
    with fade

    '''show mc_normal at left
    show friend1_smiling at center
    show friend2_thinking at right'''
    show trio

    friend1 "Another day of school, huh? Ready for whatever comes?"
    
    show mc_confident
    mc "Yeah, I feel ready. Let's see what today brings."

    show friend2_thinking
    friend2 "I feel like something's going to happen today. You know, like one of those weird vibes?"

    show mc_normal
    mc "Maybe, but it’s probably just another school day for us."

    friend1 "Come on, it can’t be that boring with us around! Let’s make it a good one."
    
    show mc_normal
    mc "Let’s go before we’re late!"

    scene classroom
    with fade

    '''show mc_normal at left
    show friend1_smiling at center
    show friend2_thinking at right'''

    mc "The classroom bufriend2friend2es with chatter as we settle in for the day."

    show riya_nervous at center

    riya "Uh, everyone? Can I have your attention, please?"

    show mc_concerned at left

    mc "Riya's voice shakes. She looks like she’s been crying."

    riya "I... I lost some of the field trip money on the way to school. I’m really sorry."

    show riya_sad

    riya "It was an accident, I didn’t mean to, and it won’t happen again."

    mc "The room falls silent, and everyone’s eyes are on her."

    show teacher_neutral at center

    teacher "MC, as the class monitor, what should we do next?"

    hide riya_nervous
    hide teacher_neutral

    show mc_thinking at left

    mc "I can feel the weight of everyone's eyes on me. What should I do?"

    # First Question: What do you think of your classmate?
    menu:
        "She is not responsible":
            show mc_annoyed
            mc "I can't believe she lost the money. This shows she’s irresponsible."
            $ opinion_of_riya = "not_responsible"

        "She made a mistake and was honest about it":
            show mc_confident
            mc "At least she’s being honest. Everyone makes mistakes."
            $ opinion_of_riya = "honest_mistake"

        "She must have used the money for something":
            show mc_annoyed
            mc "Could she have used the money for something else? I’m not sure I trust her."
            $ opinion_of_riya = "used_money"

        "In future, she should not be given any important task":
            show mc_annoyed
            mc "Maybe she isn’t suited for handling responsibilities like this."
            $ opinion_of_riya = "no_tasks"

    show mc_thinking at left

    mc "What is she feeling right now?"

    # Second Question: How do you think Riya feels?
    menu:
        "She is unapologetic":
            show riya_neutral at center
            mc "She doesn’t seem sorry. Maybe she doesn’t care."
            $ riya_feeling = "unapologetic"

        "She is sad":
            show riya_sad at center
            mc "She looks really upset."
            $ riya_feeling = "sad"

        "She regrets the mistake":
            show riya_apologetic at center
            mc "I can see she regrets this. She seems really sorry."
            $ riya_feeling = "regretful"

        "Denying her mistake":
            show riya_neutral at center
            mc "Maybe she’s in denial. She doesn’t seem fully aware of how serious this is."
            $ riya_feeling = "denial"

    hide riya_sad
    hide riya_neutral

    show mc_normal at left

    mc "Now, what should I do about this situation?"

    # Third Question: What do you do next?
    menu:
        "You talk, understand and tell her to be careful next time":
            show mc_normal
            mc "Riya, I know you didn’t mean for this to happen. Just be more careful in the future."
            show riya_apologetic at center
            riya "I will. I’m really sorry."
            $ action_taken = "compassion"

            show teacher_neutral at right
            teacher "That was a good way to handle it. Thank you, MC."

        "Punish Riya in front of everyone and ask her to write an apology letter":
            show mc_confident
            mc "Riya, you’ll need to write an apology letter to the class for losing the money."
            show riya_sad at center
            riya "But—"
            show mc_annoyed
            mc "No excuses. This was important."
            $ action_taken = "punishment"

            show teacher_neutral
            teacher "That’s one way to handle it, though maybe a bit harsh."

        "Ignore the mistake and ask everyone to pay for the lost money":
            show mc_thinking
            mc "Let’s all just pitch in and cover the lost money."
            show friend1_smiling at left
            friend1 "Wait, why should we pay for her mistake?"
            show friend2_thinking at right
            friend2 "Yeah, that doesn’t seem fair."
            $ action_taken = "ignore"

        "You will pay for the lost money":
            show mc_normal
            mc "I’ll cover it. No need to make a big deal."
            show friend1_smiling at center
            friend1 "Are you sure?"
            mc "Yeah, it’s fine."
            $ action_taken = "pay_money"

    scene cafeteria
    with dissolve

    mc "After class, we all head to the cafeteria for lunch."

    show friend1_smiling at left
    show friend2_thinking at right

    friend1 "That was intense."
    friend2 "Yeah, but I think you handled it well."

    mc "I hope so. It’s not easy making decisions like that in front of everyone."


label lunch_with_friends:

    scene cafeteria
    with dissolve

    show mc_normal at left
    show friend1_smiling at center
    show friend2_thinking at right

    friend1 "So, how's the day been for you so far?"

    mc "It's been... interesting, to say the least."

    friend1 "I saw how you handled the whole Riya thing. Tough call, but you did good."

    show mc_thinking
    mc "Thanks. It wasn't easy, but I tried to be fair."

    friend1 "Speaking of which, how are you? We haven’t hung out with you much since the sorting."

    show friend2_shy at right
    mc "Oh, there she is! friend2! Come sit with us!"

    show friend2_shy at right
    friend2 "Hey... Sorry I haven’t been around much."

    mc "No worries. How's it going with your house?"

    show friend2_shy
    friend2 "It's been... okay, I guess. I haven’t really talked to anyone much. I'm just not sure I fit in."

    mc "Why’s that?"

    show friend2_shy
    friend2 "I don't know. Everyone seems to know each other already, and I just feel out of place. It's hard to put myself out there."

    show mc_normal
    mc "I get it. Honestly, I’ve felt the same. But trust me, you belong there. Just give it time."

    friend2 "I don’t know. It’s hard."

    show mc_confident
    mc "I think you should try to get involved in some activities. It'll help you connect with others."

    friend2 "You think?"

    mc "Absolutely. In fact, I’m gonna do the same. We’ve got to put ourselves out there."

    friend2 "Thanks. I’ll give it a try."

    show mc_normal
    mc "Good. Let’s both make an effort."

    scene school_corridor
    with fade

    mc "After lunch, I head to my house’s club room, feeling inspired."

    scene house_meetingroom
    with dissolve

    show mc_normal at left

    mc "I see a list of activities and sign up for one that catches my eye—game time."

    show mc_confident

    mc "I wasn’t sure how I’d do, but it turns out, I’m pretty good! The games were a lot of fun, and for the first time since I got here, I feel more confident about my place."

    scene house_meetingroom
    with fade

    mc "Afterward, I head back home, feeling a bit more at ease with how things are going."

    scene bedroom
    with fade

    mc "It’s been a long week. I sit down at my desk, pull out my journal, and start reflecting on everything that’s happened."

    show journal at center
    mc "I flip through the pages, thinking about my house, the decisions I’ve made, and the people I’ve met."

    mc "Did I make the right choice with my house? Should I have stood up for P earlier in the canteen?"

    # Journal Reflection
    menu:
        "Whether you selected the right house or not":
            show mcc_thinking
            mc "Did I choose the right house? There’s a part of me that wonders if I would’ve been better off in another one."
            mc "But then again, every house has its challenges, right? Maybe this is where I’m meant to grow."
        
        "Does getting the first quifriend2 question wrong mean I don’t belong there?":
            show mc_annoyed
            mc "That quifriend2 question... Ugh. Did getting it wrong mean I don’t really belong in this house?"
            mc "But mistakes happen. One wrong answer doesn’t define me."

        "Should I have helped P or not?":
            show mcc_thinking
            mc "P needed help, but standing up to the senior felt like a big risk. Should I have spoken up sooner?"
            mc "I did what I thought was right, but now I wonder if I could’ve done more."

        "Why did you make the choice you did with Riya?":
            show mc_confident
            mc "With Riya, I tried to be fair. She made a mistake, and I could’ve punished her harshly, but what would that solve?"
            mc "I think I handled it okay. I just hope she learned from it."

        "Are you satisfied with the choices you made?":
            show mcc_thinking
            mc "Am I satisfied with the choices I’ve made so far? I don’t know. It’s been hard, but I’m trying to do what’s right."
            mc "I guess time will tell if I’m on the right track."

    mc "I close my journal, feeling a bit better now that I’ve written my thoughts down. Tomorrow’s another day, another chance to grow."

    scene bedroom
    with fade

    mc "I lie back on my bed, thinking about everything that’s happened. School isn’t easy, but it’s teaching me more than I expected."

    jump new_week
    #return
