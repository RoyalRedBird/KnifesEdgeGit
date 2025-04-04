# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define e = Character("Eileen")

#Core Duo
define okra = Character("Okra")
define ainhra = Character("Ainhra")

#Fight Duo
define zirkli = Character("Zirkli")
define caimil = Character("Caimil")

#Mean Girl Trio
define kaii = Character("Kaii")
define lyrdae = Character("Lyrdae")
define abrakse = Character("Abrakse")

#NVL Mode Characters

define nvlNar = nvl_narrator

#Core Duo
define okraNvl = Character("Okra", kind=nvl)
define ainhraNvl = Character("Ainhra", kind=nvl)

#Fight Duo
define zirkliNvl = Character("Zirkli", kind=nvl)
define caimilNvl = Character("Caimil", kind=nvl)

#Mean Girl Trio
define kaiiNvl = Character("Kaii", kind=nvl)
define lyrdaeNvl = Character("Lyrdae", kind=nvl)
define abrakseNvl = Character("Abrakse", kind=nvl)

#Flags
default TrioLore = False
default CaimilPunch = False
default UkhroLore = False
default ArtShare = False
default OkraPunch = False

default ZirCaiEpilogue = False
default TrioEpilogue = False


# The game starts here.

#Story Layout:
#Ainhra Prologue/Okra Prologue

#ACT 1----------------------------------------------------------------------------------------------------------

#Act 1-1 Okra and Ainhra run into each other.
#Act 1-2 The two geek out a bit about what shows they like, Ainhra shows off.
    #Bad Ending 1 - Okra mocks Ainhra, both get mad.

#Act 1 Fight
#Preamble, and Caimil thinking.
    #Caimilpunch branches from here. Set CaimilPunch flag to true.
    #If Okra convicnes Zirkli to make the punch, skip to the post-fight.
        #Set CrisisAverted flag to true.
    #If not, the fight commences, though with the knowledge that everybody will walk away from this.
        #Set SparFight flag to true.

#Multiple bad endings can be achieved if either Ainhra or Okra fight dirty, win or lose its a bad ending.

#After the fight, the four chat. The party can ask the two about their bosses/your pursuers.
    #If the player does ask about this, set the TrioLore flag to true.
#If the CaimilPunch route was taken, the party can ask about how this wasn't the first time Zirkli punched Caimil in the face.
    #It's a whole thing about VR headsets, Caimil thinks its funny, Zirkli does not.

#The two point the party towards a possible exit and wish the two well, end of Act 1.

#ACT 2-------------------------------------------------------------------------------------------------------

#Ainhra asks Okra about how he basically became a different person when fighting.
#Okra talks about this masculine facade, goes into a huge rant about masking, outs himself as Autistic.
#Okra is embarassed, but Ainhra can relate, not 1 to 1 but enough.
#Okra puts on a mask of stoic, cold, "Orcish" masculinity so that nobody bothers him or mocks him for being on the spectrum.
#Ainhra hides behind his work because he's had his fair share of getting called cringe, on top of parent's that aren't big fans of his medium.

#Ainhra rembers his friend Ukhro, how he got own-zoned by someone that seems like Okra's facade.
#If Ainhra brushes off the question, they continue walking through the subway tunnels.

#If Ainhra asks about it, set the UkhroLore flag to true.
    #Turns out Okra was that kid, and Ukhro did fairly well for himself, fighting for a grand total of 15 seconds.
    #And it also turns out Ukhro is really big into art himself, though more of a Disney kind of person.
    #He's also pretty cool and Okra is mesmerized, the two talk about how Okra could meet him.

#Suddenly, train.
#The two dodge out of the way, Ainhra is more or less fine, Okra is having a meltdown from all the noise and stress.
#Time runs short but Ainhra can't just get him to move in this state, not that he blames him.

#Ainhra can either wait for Okra to compose himself, or try and get him to move now.
    #If he tries the latter, Okra lashes out from all the everything and runs away. Okra especially is quite devastated. Bad Ending.

#If Ainhra waits, he gives Okra some space and time to breathe, eventually he's in a state to get out of the tunnels.
#Okra is deeply embarassed at letting Ainhra see him like this, but Ainhra doesn't mind.
#Okra is genuinely touched by his compassion, also, they start to feel a draft. A possible exit!

#ACT 3---------------------------------------------------------------------------------------------------------

#Welcome to the Catacombs.
#Ainhra's sketching away in his shetchbook, despite the lack of light.
#Okra's watching along, mostly because its cool but also its a nice distraction from all the skulls.
#Ainhra asks if Okra draws, Okra isn't sure he wants to answer, his art isn't good and he gave up a few weeks ago.
#If Okra lies and says he doesn't, Ainhra is a bit disappointed, but they move on.

#If Okra does share his art, he's hesitant, but he does show off some of the screecaps he has of his sketchbook.
    #Set the ArtShare flag to true.
    #Okra prepares for the worst, but to his surprise, Ainhra's rather appreciative, it's not a masterwork but its a good start!
    #Okra mentions he want's to draw but he's worried it'll still look bad, Ainhra does everything he can to get him to start again.
    #IT WORKS!
    #Oh hey the exit!

#Oh no the mean girl trio finally caught up to them.
#The demon girl starts trying to get into Ainhra's head.
#The trio reveals themselves, Abrakse being held up by Lyrdae, and Kaii looking especially desperate.

#If the TrioLore flag is true, Okra can mention that they know why they're here, much to the surprise of Kaii.
    #They'd rather be anywhere else right now, but their boss has her, her friends and her family by the throat.
    #It's either gonna be them, or you, and it isn't gonna be you.
    #Kaii's friends are also with her to the bitter end.

#PSYCHIC BOSS BATTLE COMMENCE
#Ainhra needs to keep his resolve up in order to avoid getting possessed.
#Most of your ways of keeping your resolve up come from taking the social paths earlier in the game.
    #Mainly the UkhroLore and ArtShare flags, those unlock the best paths.

#If Ainhra breaks, Abrakse possesses him and helps Kaii beat Okra to a pulp.
    #Ainhra feels terrible about letting Okra down like this, they both part ways broken and defeated. Bad Ending.
    #If Ainhra holds out long enough, Okra wins and puts the other two on the backfoot, Lyrdae puts herself between Okra and Abrakse.
    #The trio leave them be after being defeated.

#If Ainhra manages to break Abrakse's hold on him, the psychic backlash causes Abrakse to reel and collapse to the floor in agony.
    #Kaii rushes over to her to make sure she's okay, Abby is barely holding on. Kaii is utterly terrified.
    #She needs to collect, but she can't fight like this and she can't leave Abby like this.
    #Lyrdae asks Kaii to consider cutting their losses, but between Abby and the stress of pissing off her boss, she claws at Lyrdae's face.
    #Kaii draws blood, much to her horror.
    #Kaii asks the duo to get out of here and let them be.
    #The two part ways, the trio fleeing into the catacombs and the duo ascending the ladder.

#FREEDOM!

#If both the UkhroLore and ArtShare flags are true, Ainhra asks Okra to tag along with him to grab his art tablet and shop art supplies.
    #Okra accepts, friendship formed! TRUE ENDING.

#Otherwise, the two wish each other well and part ways. They probably won't talk to each other again. NEUTRAL END.





label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    "Welcome to Knife's Edge!"

    "Before we begin, a few conent warnings for the audience..."

    "This game contains the following: "

    "Violence against/between minors. \nDepictions of sensory overload. \nMishandling of sensory overload. \nDemonic posession. \nThe R-Slur."

    "With that out of the way..."

    "Our story follows the desperate escapades of two kids that have found themselves in the crosshairs of some rather powerful people"

    "They must navigate the winding underground beneath the city of Solstrum to evade the wrath of their pursuers."

    "But our story has to start somewhere, so..."

    menu:

        "Who's do you wish to start this story with?"

        "Child of Grushnakh":
            jump okraPrologue

        "Child of Illendril":
            jump ainhraPrologue

        "No time, get me to the start.":
            jump act1part1

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

label okraPrologue:

    nvl show dissolve

    nvlNar "Its a warm and rather sunny Wednesday morning, the sun is shining through your blinds as you rouse yourself from your eight hour slumber."

    nvlNar "(Or six, or seven, getting to bed after binging The Owl House last night was a bit of a chore.)"

    menu (nvl=True):

        nvlNar "You're currently tucked into bed all warm and comfy like, perhaps a bit too comfy, you kinda don't want to get out of bed, but you have plans. Not big plans, but plans nonetheless."

        "Get out of bed.":
            nvlNar "As comfy as your bed might be, you have things to do."

        "Sleep in":
            nvlNar "You decide the day can wait just a bit longer as you close your eyes again for a few more minutes of sleep. It may be a Wednesday, but its a Wednesday in July, so there's nothing to worry about."

            nvlNar "A few minutes pass and the desire to not get out of bed grows somewhat, but so does the desire to get out of bed. It's been fun, but you still have things to do."

    "You push your blanket off of you, the cool of your air-conditioned room washes over your skin, its refreshing if a slight jolt to the senses."

    "Your room on the other hand is bathed in the 9AM glow of the sun. Perfectly lit without the need to turn on your light."

    


label ainhraPrologue:

    nvlNar "Still not done aaaaaaaaaaa"


label act1part1:

    "Today was supposed to be straightforward."

    "A warm, summer Wednesday afternoon just like all the rest."

    "But fate, or what have you, had other plans today. For today you are being hunted, the mark for a band of delinquents."

    "Delinquents who will stop at nothing to see you crushed under heel and stripped of anything valuable."

    "In their pursuit, you manage to lose them by entering the underground tunnels."

    "But with the route back no doubt being watched by your pursuers, there is nowhere else to go but further into the tunnels."

    #Fade in to tunnels goes here.

    "You've spent the past half-hour walking through these tunnels and you haven't even managed to find natural light, let alone an exit."

    "And the buzzing of the lights is getting to your head and the smell just makes it even worse."

    "You wonder if you're even gonna make it out of this place, reception is non-existent here and these tunnels are already a winding labyrinth."

    "If you end up lost here it might just mean the end of you."

    "Your head stirs with dread as the thought of you never making it out of here seems more and more real."

    "You're almost get lost in your own head for a moment, when suddenly..."

    #BANG!

    "Orc" "Ow..."

    "HalfElf" "Ngh... my {i}brain...{/i}"

    "Orc" "{b}{i}!!!{/i}{/b}"

    "HalfElf" "{b}{i}!!!{/i}{/b}"

    "Orc" "Wait a minute..."

    "Orc" "You aren't with {i}them{/i} are you?"

    "HalfElf" "Them? Them who?"

    "Orc" "The drow, fox and the devil? They chased me in here!"

    "HalfElf" "Wait {b}THEM?{/b} They're the reason I'm down here too!"

    "HalfElf" "I barely got down here in one piece..."

    "Orc" "Wait really?"

    "The two share a look of relief"

    "Orc" "So you aren't trying to mug me?"

    "HalfElf" "Nope, just running. And running and running away."

    "HalfElf" "And then I ran into you. Sorry."

    "Orc" "Ah! It's fine it didn't even hurt that bad don't worry!"

    "HalfElf" "That's cool."

    "HalfElf" "Say... Since we're in this mess together..."

    "HalfElf" "Wanna team? If you want."

    "Orc" "Heck yeah I wanna team! I don't wanna be down here alone!"

    "HalfElf" "Woo! Thank Illendril..."

    "HalfElf" "Though uh... What's your name?"

    okra "Ah uh... It's Okra."

    ainhra "Ainhra! Nice to meet 'ya!"

    ainhra "Since were basically fighting for our lives down here, what can you do?"

    okra "I'm pretty good with a sparring axe, but I can work with my fists if I have to. What about you?"

    ainhra "Well, you could say I have a few tricks up my sleeve..."

    okra "Like?"

    "Ainhra summons a magical ball of energy in his hand."

    okra "..."

    okra "Cool!"

    ainhra "I only got my M-1 license a few months ago, but I know a bit of force magic."

    okra "Sweet! Though uh... you got any ideas on how to get out of here?"

    ainhra "Hmm..."

    okra "Please tell me you have something I've been stuck here for half an hour and I'm still lost."

    ainhra "Well I don't exactly know where I am either but I think I passed by an enterance to the sewers?"

    "Okra tenses up at the thought of having to even be in the sewers."

    okra "Well it's something, lead the way."

    "Some time passes, they get twisted and turned around amidst the myriad tunnels beneath the city."

    "But eventually, they do find a way into the sewer network!"

    "And still, the wandering continues."

    "And continues."

    "And continues."

    ainhra "..."

    ainhra "So..."

    okra "Hm?"

    ainhra "How'd you end up here? In the {i}labyrinth?{/i}"

    okra "Well..."

    okra "I got out of bed, left the house."

    ainhra "Mhm..."

    okra "And then I went on a walk..."

    okra "And then I got cornered... And I got scared..."

    okra "And then I {i}punchedherintheface.{/i}"

    okra "And ran."

    okra "Away."

    okra "Into the tunnels."

    menu:

        "Ainhra: Literally just a walk?":
            $ OkraPunch = False
            jump act1part1

        "Ainhra: Wait you hit her?!":
            jump okraPunch



label okraPunch:

    $ OkraPunch = True

    ainhra "Wait you {i}hit{/i} her?!"

    okra "What was I supposed to do?! They were all right against my face and I got scared and I didn't wanna give them my wallet or my phone or my shoes so I just sorta..."

    okra "{i}Decked her in the face.{/i}"

    ainhra "I see."

    okra "And then I ran! And they almost caught me before I managed to find a way in here."

    okra "So yeah."

    okra "Also I'm fairly sure that devil was looking for a fight. Judging by the unhinged grin on her face while she was chasin' me."

    ainhra "Huh, that's terrifying."

    ainhra "But anyway, I'm honestly surprised you managed to get away. All things considered."

    okra "You know what? I am too."

    okra "But yeah, I ran and ran, found a door to the underground and barricaded myself in."

    okra "I waited for them to leave and I tried to get out but the door jammed."

    okra "And now I'm here."

    okra "Though how did you get away from them?"

    ainhra "Oh I just ran and ran and ran."

    ainhra "They didn't even try and shake me down they just yelled 'That's him! Get him!' and started chasing me."

    ainhra "I found my own way down here and kept running and running."

    okra "And then you ran into me!"

    ainhra "Exactly!"

    okra "Dang. Guess we're both lucky or cursed."

    ainhra "Maybe..."

    jump act1part2


label act1part2:

    if OkraPunch == True:
        ainhra "So you were {i}just{/i} walking around when you got jumped?"

    else:
        ainhra "Literally just a walk?"

    okra "{i}What do you mean?{/i}"

    ainhra "You didn't have something in mind? Like at all?"

    okra "{i}No?{/i} I just wanted to get out of the house."

    ainhra "..."

    ainhra "{i}Why?{/i}"

    okra "What do you mean why? People go on walks all the time and today is good day for a walk and the sun's out and the sky is bright and {i}everything was supposed to be normal but it's not and now I'm here being chased by gangsters.{/i}"

    ainhra "Hey! I didn't mean it like that. I just don't really get out of the house just to touch grass."

    okra "Touch grass?"

    ainhra "Wait you don't know what that means?"

    okra "I know what touching grass means but why'd you have to phrase it like that?"

    ainhra "Well I- I just..."

    okra "Do you even know what the sun is?"

    ainhra "Of course I know what the sun is! I j-"

    ainhra "..."

    ainhra "Look I just go outside to get reference photos and go home. Usually anway."

    okra "References? Like for art?"

    ainhra "Yeah!"

    okra "Ah! So that's what you were doing?"

    ainhra "Well, not today."

    ainhra "My new screen tablet got dropped off at my art store and I {i}wanted{/i} to go grab it."

    ainhra "But then... {i}this{/1} happened."

    menu:

        "Okra: Ooo! Sweet!":
            jump act1part3

        "Okra: That sounds {i}lame.{/i}":
            jump badend1


label badend1:

    okra "That sounds {i}lame.{/i}"

    ainhra "I'm- I'm sorry?!"

    okra "I said what I said. And I said that sounds {i}cringe.{/i}"

    ainhra "..."

    ainhra "You take that back right now..."

    okra "Nah. What you're talking about sounds like nerd shit."

    ainhra "..........."

    ainhra "Well fuck you then."

    okra "Fuck you too!"

    "Okra and Ainhra" "Hmph!"

    nvl show dissolve

    nvlNar "As the temprary bond between the two kids breaks down at lightspeed, they storm away from each other in a huff."

    nvlNar "Okra heads back to the access corridors, Ainhra heads further into the sewers."

    nvlNar "Some time passes and Okra's emotions start to simmer down."

    nvlNar "And as his calm returns to him, a sense of regret washes over him, and a thought enters his mind."

    nvlNar "'Why did I even say that?!'"

    nvlNar "Bad Ending #1"

    renpy.full_restart()


label act1part3:



    





