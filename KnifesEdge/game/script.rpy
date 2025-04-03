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

