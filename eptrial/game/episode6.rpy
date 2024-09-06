#episode 6
define ritvik = Character("Ritvik", color="#FFD700")
label new_week:

    scene school_corridor
    with dissolve

    show mc_cheerful at left
    show y_happy at center
    show z_smiling at right

    mc "Morning, guys! How are you both doing?"

    friend2 "Whoa, someone’s in a good mood!"

    friend1 "Yeah, you're unusually cheery today!"

    mc "I just decided to be a better house member and class prefect. Starting the week with positive vibes!"

    friend1 "Well, your positivity is working for me too! Thanks for the advice last week. I’m feeling a lot better about my house now."

    show mc_happy
    mc "Really? That’s great to hear, Z! I’m glad it helped."

    show mc_thinking
    mc "But I’m still figuring things out for myself. I’m staying positive, though."

    show ritvik at right
    ritvik "Hey, have you guys heard the latest about that girl from the other section? Oh man, wait until you hear this one..."

    scene classroom_background
    with dissolve

    mc "Ritvik, one of your closest friends, loves making jokes and comments about others, but sometimes his humor goes too far. Today, he makes a cruel joke about a girl from the other section."

    show girl_crying at center
    mc "The comment is harsh, and it makes the girl cry."

    show mc_thinking
    mc "It’s awkward. Ritvik doesn’t seem to care, but it bothers you deeply. His jokes are getting out of hand, especially when they hurt others."

    # Choice for MC's perspective on the girl
    
    mc "How would she bes feeling?"
    menu:
        "Maybe she cries over everything":
            mc "Maybe she’s just sensitive. Some people can’t take a joke."
        "She doesn’t have any sense of humor":
            mc "It’s just a joke. People need to lighten up."
        "She is feeling terrible about herself right now":
            mc "No one should feel this bad because of a joke. I need to do something."
        "She is fine and doesn’t mind the joking":
            mc "Maybe it didn’t really hurt her, but it still feels wrong."

    mc "Seeing her cry makes you feel uncomfortable. You know that Ritvik crosses the line sometimes. What should you do?"

    # Decision on what to do next
    mc "what should i do next?"
    menu:
            "Confront Ritvik separately":
                jump confront_ritvik
            "Just laugh along with him":
                jump laugh_with_ritvik
            "Ignore the comment":
                mc "Maybe it’s better to just ignore it. He’ll move on eventually."
                return
            "Take the matter to the teacher":
                mc "I’ll take this to the teacher. Maybe they can handle it better than I can."
                return

label confront_ritvik:

    scene hallway
    with fade

    show mc_confident at left
    show ritvik at right

    mc "Ritvik, I need to talk to you about what happened today."

    ritvik "What’s up? You’re not about to get all serious on me, are you?"

    
    mc "How should I confront him?"
    menu:
            "Get angry and hit him":
                mc "You get frustrated and lash out, punching Ritvik in anger."
                show ritvik_angry at right
                ritvik "What the hell? What’s wrong with you?"
                mc "You storm off, but now things feel worse. Violence wasn’t the answer."
                return
            "Make him feel bad about himself":
                mc "You know, you really hurt that girl with your joke. I hope you feel proud of yourself."
                show ritvik_guilty at right
                ritvik "I didn’t mean to hurt her..."
                mc "Well, you did. Maybe you should think before you speak."
                return
            "Call him an evil person and break friendship":
                mc "I can’t believe you’d say something so mean. You’re an awful person, and I don’t want to be friends with you anymore."
                show ritvik_angry at right
                ritvik "Oh, so you’re the perfect one, huh? Fine. I don’t need you anyway."
                mc "You walk away, but you’ve now lost a friend. Z supports you, but things are tense with Ritvik now."
                return
            "Make him understand the nature and consequence of his actions":
                mc "Ritvik, do you realize what you said really hurt her? It’s not funny when someone else is in pain."
                show ritvik_thinking at right
                ritvik "I was just joking, but... I guess I didn’t think about how she’d feel."
                mc "You need to understand that words have consequences. You’re better than this."
                show ritvik_sad at right
                ritvik "I didn’t mean to hurt her. I’ll try to be more careful next time."
                mc "Thanks. That’s all I’m asking."

                scene hallway
                with fade

                mc "You handled the situation well. Z appreciates your honesty, and the girl is thankful. But things between you and Ritvik are strained now."

                show z_happy at right
                z "You did the right thing. I know Ritvik’s your friend, but he needed to hear that."
                return

label laugh_with_ritvik:

    scene cafeteria
    with fade

    show mc_normal at left
    show ritvik at right

    mc "You laugh along with Ritvik, trying to brush off the situation."

    show z_angry at right
    friend2 "How could you laugh at that? Do you not see how hurt she was?"

    mc "Z looks angry, and the girl who was the target of the joke is crying. You feel uncomfortable, but it’s too late to take back your reaction."

    scene cafeteria
    with fade

    mc "You lose respect from Z and the girl, and you feel conflicted about laughing along."

    return
