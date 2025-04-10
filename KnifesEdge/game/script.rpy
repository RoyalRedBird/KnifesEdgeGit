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
default FightAverted = False
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
            jump act1part2

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

    ainhra "Look I just go outside to get reference photos and go home. Usually anyway."

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

    return


label act1part3:

    okra "Ooo! Sweet! What kind is it? If you don't mind."

    ainhra "It's a 13 inch screen tablet, 2.5k, spent like two weeks trying to figure out which one to get."

    ainhra "It's no Wowcom, but it's still pretty cool!"

    ainhra "But yeah! Once we get out of here it'll be {i}all mine.{/i}"

    okra "Well... Since you're the artsy type..."

    ainhra "Hm?"

    okra "Can I see your drawings?"

    ainhra "..."

    "Ainhra's eyes widen at the idea. Immediately pulling out his phone."

    ainhra "Behold!"

    "Ainhra shows off all of his recent work to Okra, swiping through dozens of his illustrations."

    "A lot of it is very Studio Trigger-esque, with only one or two 'realistic' portraits to see."

    "Okra, simply put, is mesmerized."

    okra "Oh my god this is so {i}cool!{/i}"

    ainhra "And this is just the start!"

    "Ainhra opens up another app, an online comic hosting site. Luckily it still runs offline."

    "He pulls up a manga by the name of 'Starswirl vs. The End of Time' a maagical girl sort of thing with some light eldritch trappings."

    "A manga illustrated by {i}Ainhra Sydrillen.{/i}"

    ainhra "It's nowhere near done but it's coming along!"

    okra "Dude..."
    
    okra "Holy shit..."

    "Ainhra is beaming at this point."

    ainhra "Heh! Glad you like it!"

    ainhra "{i}causeispentlikefourmonthsonthis{/i}"

    ainhra "But enough about me, what about you?"

    okra "What {i}about{/i} me?"

    ainhra "Like, you know... What do you get up to?"

    okra "I mean... I know this sounds pretty stereotypical of me but I'd say I'm pretty good at dueling."

    ainhra "Ooo..."

    okra "Almost all the other orcs my age can't really keep up with me, I'm kind of a terror at the rec center if you know what I mean."

    ainhra "So you're just that good?"

    okra "I mean yeah! And I do {i}like{/i} fighting, its a good workout and it keeps you on your toes."

    okra "But it's not everything I am."

    okra "{i}I also really, really, really like The Owl Lodge.{/i}"

    okra "{i}And Aquaphibia.{/i}"

    okra "{i}Pretty much everything that comes out of Walt Studios if I'm gonna be honest.{/i}"

    ainhra "Wait really!? I fuckin' love The Owl Lodge!"

    okra "You do?!"

    ainhra "Heck yeah! I may be a weeb but I'm not one to disparage the great Danilla Terraco!"

    ainhra "{i}But Walt Studios can go rot in the howling dark for what they did.{/i}"

    okra "Oh absolutely! Don't even get me started on the Outside In 2 debacle."

    ainhra "..."

    okra "..."

    ainhra "{b}{i}Yo have you seen her new show with those other guys online?!?!{/b}{/i}"

    okra "{b}{i}How can't I? I can't wait!{/b}{/i}"

    nvl show dissolve

    nvlNar "As the two make their way through the sewers, they continue to yap about animation, their favorite shows, and the state of the Walt Company."

    nvlNar "And yap."

    nvlNAr "And yap..."

    nvlNar "{i}And yap...{/i}"

    nvlNar "And it keeps going for a while..."

    nvlNar "Until eventually..."

    nvl hide dissolve

    okra "But you really haven't seen Aquaphibia yet?"

    ainhra "I KNOW I need to see it but I still need to get around to a lot of stuff and-"

    "Ainhra hears something just up ahead."

    ainhra "Okra shh."

    okra "!!!"

    "The two huddle behind the nearest corner, listening for something?"

    ainhra "You hear that right?"

    "Its the sound of chatter, two girls down the tunnel."

    okra "Yeah I hear them too..."

    "The two try and listen into what they're talking about."

    "Hobgoblin" "You sure they're still down here? We've been stuck in this hellhole for an hour."

    "Faerie" "Yup! This place is a maze and I don't think they could get that far down here."

    "Faerie" "Still, you know we could just... leave?"

    "Faerie" "Cut, run and hope for the best?"

    "Hobgoblin" "With {i}her{/i} breathing down our necks? I doubt it."

    "Hobgoblin" "Crossing her is a bad idea and I really don't want to go back to juvie again, {i}especially{/i} if it's 'cause of her."

    "Faerie" "That's true. {i}Ugh.{/i}"

    "Faerie" "I just don't want to get into any more trouble than we have to okay?"

    "Hobgoblin" "{i}*Sigh*{/i} I know Cai, but so far the bare minimum seems to be breaking a few kneecaps."

    "Hobgoblin" "And you know I want to be down here just as much as you do."

    "Faerie" "I know. But at least I'm stuck here with you!"

    "Hobgoblin" "And I woudn't want it any other way."

    "From what you two can gather, it looks like they want to be down here as much as you."

    "Not at all."

    okra "Maybe... We could talk to them? Try and bargain our way out of this?"

    ainhra "We could, but why not seize the initiative? Ambush 'em?"

    okra "Ngh... I'd rather not. Neither of us want to be here and I'd just feel dirty doing that."

    ainhra "Fine. And sneaking around them is out of the question. There isn't much 'around' to sneak through down here."

    ainhra "I just hope they're reasonable."

    okra "Fingers crossed!"

    "With their minds made up, they make their approach."

    "And the two girls don't look particularlly thrilled to see them."

    "Hobgoblin" "Ah crap..."

    okra "Heyyyy..."

    ainhra "Yo."

    "Faerie" "Yo..."

    "Hobgoblin" "..."

    "Hobgoblin" "Were you listening in on us?"

    okra "For a bit."

    "Hobgoblin" "For how long?"

    ainhra "About a minute."

    "Hobgoblin" "Then I guess you know why we're here then?"

    okra "Yup."

    "Hobgoblin" "Then why even reveal yourself?"

    okra "Well you don't want to be here, and we want to get out of here. So maybe we could talk this out? Walk away peacefully?"

    "Faerie" "{i}*Sigh.{/i} If only..."

    "Hobgoblin" "Look. You guys seem okay, and I'd also like to go home."

    "Hobgoblin" "But we don't have a choice here."

    "Hobgoblin" "Our boss..."

    "Faerie" "Has us by the throat. Proverbially and literally speaking."

    "Faerie" "And she wants what you have, all of it. Preferably by way of curb stomping."

    ainhra "So that's how it's gonna be then? You're not even gonna try and figure something out?"

    "Hobgoblin" "Like I said, I'm not taking my chances with her!"

    "As Ainhra and the Hobgoblin girl continue their exchange, Okra notices the Faerie girl thinking about something."

    "Whatever could it be?"

    menu:

        "Okra: *Let her think.*":
            jump CaimilPunchRoute

        "Okra: Then I guess we're done talking?":
            jump FightScenePreamble


label CaimilPunchRoute:

    $ CaimilPunch = True

    "You give the Faerie a bit more time to finish her thoughts as the other two continue to argue, and then..."

    "Faerie" "Zirkli?"

    zirkli "Yeah?"

    "Faerie" "I need you to punch me in the face!"

    zirkli "Wh- Caimil, no I- Why?!"

    caimil "Think about it! As long as we make it {i}look{/i} like we got our butts kickked and make it {i}look{/1} like we actually tried, we could get out of this!"

    caimil "{i}Besides,{/i} I turned out fine after the first time!"

    zirkli "That was an ACCIDENT! I didn't {i}want{/i} to hit you!"

    caimil "But everything still turned out fine! And none of us here want to fight so..."

    zirkli "Look I get the bizarre logic behind this plan but I just... No..."

    caimil "..."

    caimil "Orc! What's your name?"

    okra "It's Okra?"

    caimil "Okra! I need you to punch me in the face!"

    okra "But I don't want to either!"

    caimil "Aw come on! Just pretend I'm trying to stab you or something!"

    okra "But you aren't?!"

    zirkli "Caimil you're made of glass please don't make him punch you."

    caimil "It's either I get hurt or everyone here gets hurt it's basic utilitarianism!"

    zirkli "Caimil {i}please...{/i}"

    "As Okra's eyes dart around in confusion and slight panic, he spots some weak looking bricks in the wall."

    "Maybe... You could get Caimil to reconsider that way?"

    "It {i}will{/i} hurt though."

    menu:

        "Okra: *Punch the bricks."

        "Okra: Look I'd rather just fight this out.":
            jump SparStart

    "You take in a deep breath and clear your head."

    "Without even thinking, you punch the bricks with all the might you can muster. Reducing them to power and chunks of rock."

    okra "You see what you're dealing with here?"

    "The pain hits your right hand all at once, as does the bleeding. To call this unpleasant would be putting it lightly."

    okra "Ow. Nhg. Ow. Owowowowowowowow......"

    okra "Please don't make me do this again... I don't think I can handle another one."

    caimil "..."

    caimil "{i}Okay you have a point.{/i}"

    zirkli "*Sigh...* Alright fine... I'll do it."

    caimil "Woo!"

    zirkli "Just hold still..."

    "Caimil holds her hands behind her back."

    zirkli "You ready?"

    caimil "Yup!"

    zirkli "One. Two..."

    "Zirkli winds up her right arm for the punch."

    zirkli "Three!"

    "A loud, dull thud reverberates through the sewers as Zirkli's blow connects with Caimil's face. Followed by the sound of her falling to the ground."

    "It {i}looks{/i} pretty bad, her left eye is starting to swell and there's a bit of brusing too."

    "But Caimil looks pleased with the outcome."

    "The same can't be said for Zirkli."

    "And everyone else."

    ainhra "Are you okay?"

    caimil "Yeah! And no. But mostly yeah!"

    caimil "It's nothing my mom can't patch up. Don't worry."

    zirkli "Caimil... Are you sure this is going to work?"

    caimil "Positive!"

    caimil "And besides, Lyrdae's cool, I'm sure she can vouch for us!"

    okra "Lyrdae?"

    caimil "Oh her? I thought you knew her."

    caimil "Drow, bangs and a ponytail, leather jacket?"

    "She's one of your pursuers, along with the other two."

    okra "Wait her! Yeah she was also trying to chase me down!"

    ainhra "Same!"

    caimil "Look, she'd rather be doing anything else right now, same with the other two."

    caimil "So I'm sure she can think of a way to spin this so nobody gets hurt!"

    ainhra "So you're sure we're gonna be fine?"

    caimil "I'm certain!"

    "Everyone breathes a collective sigh of relief, knowing that nobody has to fight."

    $ FightAverted = True

label SparStart:

    okra "Look I'd rather just fight this out."

    okra "I know you don't want anyone else to get hurt but I just can't bring myself to do it."

    okra "Although..."

    "Everyone's eyes are on Okra."

    okra "We could just fight, and leave each other be after?"

    okra "Mess each other up? Make it look convincing?"

    "Zirkli takes notice."

    zirkli "Now {i}that{/i} I can do."

    ainhra "Wait we're actually doing this?"

    okra "Yup!"

    "Okra and Zirkli prepare themselves for a fight, a smirk on both their faces."

    zirkli "Just don't hold back alright?"

    okra "Wasn't planning on it."

    "Ainhra looks to Caimil, he just shrugs, as does she."

    caimil "I mean... Since we're here."

    ainhra "And {i}you{/i} still need to look the part right?"

    caimil "Yep. Just don't go overboard okay?"

    ainhra "I couldn't even if I tried."

    "The other two awkwardly prepare their magics for one of the duels of all time."

    jump FightStart

label FightScenePreamble:

    okra "Then I guess we're done talking?"

    "Hobgoblin" "I guess we are."

    "Everyone steels themselves for a brawl, it's either gonna be you, or them."

    "Though for you Ainhra, you swear you could see your friend and the Hobgoblin grinning."

    "Okra and the Hobgoblin lunge for each other, you ready yourself for whatever the Faerie has in store."

    "FIGHT TIME GOGOGOGOGO"


label FightStart:

    nvl show dissolve

    nvlNar "Welcome to The Fight Scene(tm)"

    nvlNar "While there's one big fight happening, Ainhra and Okra have their own duels to deal with."

    nvlNar "And you can only focus on one fight, for sanity reasons."

    nvlNar "So, who will you focus on?"

    menu (nvl=True):

        "Ainhra":
            nvlNar "The Half-Elven wizard it is!"
            jump AinhraFight

        "Okra":
            nvlNar "The Orcish barbarian it is!"
            jump OkraFight1


label OkraFight1:

    nvlNar "Okra takes a swing at the incoming hobgoblin but she swiftly didges out of the way."

    nvlNar "The hobgoblin jabs at his gut, and Okra responds with a headbutt. Both are knocked away from each other."

    nvlNar "The hobgoblin retakes the initiative as she surges towards him, she goes for a sweeping motion which forces Okra to brace himself and block low."

    nvlNar "But as her swing starts, her leg arcs up and Okra gets kicked in the face. {i}Hard.{/i}"

    nvlNar "Okra is reeling from the impact and nearly stumbles over but manages to regain his footing before Zirkli closes the gap."

    nvlNar "What next?"

    menu(nvl=True):

        "Brace for Impact":
            jump OkraFight2

        "Go for her hair. (Unfinished)":
            jump OkraDirty1

label OkraFight2:

    nvlNar "He puts up his arms and braces himself for the worst. And within moments a hailstorm of punches make their way to him."

    nvlNar "No matter what you try to do you can't seem to block anything, and its wearing on you fast."

    nvlNar "You need look for an opening, or make one."

    nvlNar "You wait for the slightest lapse in her assault and shove her away from you."

    nvlNar "What next?"

    menu(nvl=True):

        "Uppercut her now!":
            jump OkraLose

        "Get in close.":
            jump OkraWin


label OkraLose:

    nvlNar "Okra tries to go for a killing blow, an uppercut with everything he has."

    nvlNar "But he's too far, and she has plenty of time to react. And now you're left wide open."

    nvlNar "Before he even has time to register how bad of a position he's in, he takes a kick to the kidney, one to the stomach and a final one to the head. Knocking hom to the floor."

    nvlNar "You surrender, as does Ainhra as he sees that you've been bested."

    if CaimilPunch:
        nvlNar "You were so close! But alas, you whiffed."
        jump OkraPostLoseSpar

    else:
        nvlNar "You prepare for the worst as the hobgoblin looms above you."
        jump OkraPostLose

label OkraPostLoseSpar:

    "Zirkli extends a hand to Okra and he takes it, letting her hoist him up to his feet."

    

label OkraWin:

    nvlNar "Your turn."

    nvlNar "You get right into her face, trying to jab you but you're prepared this time."

    nvlNar "With your left hand you grab her arm and pull her towards you."

    nvlNar "And with your right, you put all your strength into a single, fight ending uppercut."

    nvlNar "You outpace her, giving her no time to react."

    nvlNar "BAM!"

    nvlNar "She's knocked onto the floor with a clack that echoes through the sewers. Dazed and disoriented."

    nvlNar "She surrenders, knowing she can't pull this back from here."

    nvlNar "And once the Faerie sees her friend on the floor, she gives up as well."

    nvlNar "You thought yourself a skilled fighter, but she really pushed you to the limit. Keeping you on the defensive constantly."

    nvlNar "Okra offerrs her a hand up, but she declines and hoists herself onto her feet."

    nvlNar "But as she gets back up, one thought is reverberating through his mind."

    okraNvl "(Holy crap that fake-out was so {i}fucking{/i} cool!)"

    if CaimilPunch == True:
        jump OkraPostSpar
        
    else:
        jump OkraPostWin


label OkraPostWin:

    "Hobgoblin" "Well. Thanks for not stomping my face in! Appreciate it."

    okra "I mean I already won, and that's not how I do things, you know?"

    "Hobgoblin" "Ye' know what? That's fair."

    okra "Besides, you want to get out of here to right? Uh... I didn't get your name."

    "Hobgoblin" "Yeah I'd rather be home right now. Or anywhere else."

    zirkli "And it's Zirkli, nice to meet you to uh..."

    okra "Okra!"

    zirkli "Gotcha."

    zirkli "Still, we're gonna be in some serious shit now. Ugh."

    "Faerie" "I mean... You do look pretty battered Zirkli."

    zirkli "You look worse for wear too Caimil but... What are you getting at exactly?"

    caimil "We could just {i}pretend{/i} that they just got one over us! Say they were just too much for us!"

    zirkli "That sounds cool but, are you sure this is gonna work?"

    caimil "I mean the boss is insane but Kaii and her friends are alright. I'm sure they'll let us off the hook."

    okra "You sure?"

    caimil "For the most part yeah!"

    "Everyone breathes a collective sigh of relief, nobody has to get curb stomped woo!"

label OkraPostSpar:

    okra "Hey? You alright?"

    zirkli "Enough... You?"

    okra "I'm good."

    okra "Man, I haven't had a brawl like that in a while!"

    zirkli "Really? {i}You{/i} get into fights often?"

    okra "Not on the streets but yeah. Clan duels at the rec center and all that."

    zirkli "Ah, now that makes sense."

    okra "One thing though..."

    zirkli "Hm?"

    okra "..."

    okra "How did you do that kick to the face? {i}I wanna know!{/i}"

    zirkli "Wait really?"

    okra "Yeah dude that was so sicK!"

    zirkli "Huh! Nobody really asks me about this sort of thing. Usually they just call me a bitch."

    okra "I mean you really got me good, and I wanna see if I can pull it off myself."

    okra "Nobody can really keep up with me, but it doesn't hurt to widen the gap."

    zirkli "Heh! Maybe later, you know where Iron Lion is right?"

    okra "Oh there? Yeah I go there every other weekend, mostly for cardio though."

    zirkli "Then I can expect you to show right?"

    okra "Oh absolutely!"

    ainhra "Hey are you guys done gawking at each other?"

    okra "Ah! Sorry!"

    "Zirkli rolls her eyes."

