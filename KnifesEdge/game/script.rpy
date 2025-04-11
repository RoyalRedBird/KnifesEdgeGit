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

    "Before we begin, a few content warnings for the audience..."

    "This game contains the following: "

    "Violence against/between minors. \nDepictions of sensory overload. \nMishandling of sensory overload. \nDemonic possession. \nThe R-Slur."

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

    ainhra "Well I don't exactly know where I am either but I think I passed by an entrance to the sewers?"

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

    nvlNar "As the temporary bond between the two kids breaks down at light-speed, they storm away from each other in a huff."

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

    "A lot of it is very Studio Trigger-esque, with only one or two 'realistic' portraits to see. Self-portraits to be precise."

    "Okra, simply put, is mesmerized."

    okra "Oh my god this is so {i}cool!{/i}"

    ainhra "And this is just the start!"

    "Ainhra opens up another app, an online comic hosting site. Luckily it still runs offline."

    "He pulls up a manga by the name of 'Starswirl vs. The End of Time' a magical girl sort of thing with some light eldritch trappings."

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

    okra "I mean... I know this sounds pretty stereotypical of me but I'd say I'm pretty good at fightin'."

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

    nvlNar "As the two make their way through the sewers, they continue to yap about the shows they like to spend hours binging at 1AM. And they just keep yapping."

    nvlNar "And yapping."

    nvlNar "And yapping..."

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

    "Faerie" "That's true. {i}Ngh.{/i}"

    "Faerie" "I just don't want to get into any more trouble than we have to okay?"

    "Hobgoblin" "{i}*Sigh*{/i} I know Cai, but so far the bare minimum seems to be breaking a few kneecaps."

    "Hobgoblin" "And you know I want to be down here just as much as you do."

    "Faerie" "I know. But at least I'm stuck here with you!"

    "Hobgoblin" "And I wouldn't want it any other way."

    "From what you two can gather, it looks like they want to be down here as much as you."

    "Which is to say, not at all."

    okra "Maybe... We could talk to them? Try and bargain our way out of this?"

    ainhra "We could, but why not seize the initiative? Ambush 'em?"

    okra "Ngh... I'd rather not. Neither of us want to be here and I'd just feel dirty doing that."

    ainhra "Fine. And sneaking around them is out of the question. There isn't much 'around' to sneak through down here."

    ainhra "I just hope they're reasonable."

    okra "Fingers crossed!"

    "With their minds made up, they make their approach."

    "And the two girls don't look particularly thrilled to see them."

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

    "Faerie" "And she wants what you have, all of it. Preferably by way of a good curb stomping."

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

    caimil "Think about it! As long as we make it {i}look{/i} like we got our butts kicked and make it {i}look{/1} like we actually tried, we could get out of this!"

    caimil "{i}Besides,{/i} I turned out fine after the first time!"

    zirkli "That was an ACCIDENT! I didn't {i}want{/i} to hit you!"

    caimil "But everything still turned out fine! And none of us here want to fight so..."

    zirkli "Look I get the bizarre logic behind this plan but I just... No..."

    caimil "..."

    caimil "Orc! What's your name?"

    okra "It's Okra?"

    caimil "..."

    caimil "Okra! I need you to punch me in the face!"

    okra "But I don't want to either!"

    caimil "Aw come on! Just pretend I'm trying to stab you or something!"

    okra "But you aren't though?!"

    zirkli "Caimil you're made of glass please don't make him punch you."

    caimil "It's either I get hurt or everyone here gets hurt it's basic utilitarianism!"

    zirkli "Caimil {i}please...{/i}"

    "As Okra's eyes dart around in confusion and slight panic, he spots some weak looking bricks in the wall."

    "Maybe... You could get Caimil to reconsider that way?"

    "It {i}will{/i} hurt though."

    menu:

        "Okra: *Punch the bricks.*":
            jump BrickPunch

        "Okra: Look I'd rather just fight this out.":
            jump SparStart


label BrickPunch:

    "You take in a deep breath and clear your head."

    "Without even thinking, you punch the bricks with all the might you can muster. Reducing them to powder and chunks of rock."

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

    "It {i}looks{/i} pretty bad, her left eye is starting to swell and there's a bit of bruising too."

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

    jump AfterFight

label SparStart:

    okra "Look I'd rather just fight this out."

    okra "I know you don't want anyone else to get hurt but I just can't bring myself to do it."

    okra "Although..."

    "Everyone's eyes are on Okra."

    okra "We could just fight, and leave each other be after?"

    okra "Mess each other up and make it look convincing you know?"

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

    nvl clear

    menu (nvl=True):

        "Ainhra":
            nvlNar "The Half-Elven wizard it is!"
            jump AinhraFight1

        "Okra":
            nvlNar "The Orcish barbarian it is!"
            jump OkraFight1

label AinhraFight1:

    nvlNar "The Faerie tries to knock Ainhra off his feet by disturbing the concrete beneath his, but he swiftly steps out of the way."

    nvlNar "He tries to retaliate by sending a hail of magical darts hurdling towards her, but she disappears in the blink of an eye only to reappear elsewhere the next, dodging his move."

    nvlNar "He tries sending another barrage towards her, but now he's the one caught off guard as she shifts up the ground beneath his feat, sending him stumbling into a wall."

    nvlNar "And as you come to a halt, a weave of magical vines sprout from the cracks in the tunnel ensnaring you."

    nvlNar "The vines are dotted with small flowers that span the entire color wheel, and they smell quite pleasant, you even feel yourself start to drift asleep."

    nvlNar "He should probably figure something out before he dozes off."

    nvlNar "The only spell you can pull off now would be to materialize an ethereal hand, but what should he use it with?"

    nvl clear

    menu (nvl=True):

        "There's a brick on the floor, that seems usable.":
            jump AinhraDirty

        "Slap her in the face.":
            jump AinhraFight2

label AinhraFight2:

    nvlNar "Using what willpower he has left, he materializes a hand made of raw magic."

    nvlNar "And he uses said magic hand to slap her across the face."

    nvlNar "The sound it makes was surprisingly loud, echoing throughout the tunnels."

    nvlNar "And with that slap her concentration lapses long enough for the vines to stop putting him to sleep. Now's his chance!"

    nvlNar "Think fast!"

    menu (nvl=True):

        "Mage Bolt into the Faerie's face.":
            jump AinhraWin

        "Mage Bolt into the vines.":
            jump AinhraLose

label AinhraWin:

    nvlNar "Using this window of opportunity, he sends one final hail of darts into the Faeries face, and all of them manage to hit their mark this time."

    nvlNar "The Faerie is knocked to the floor, her hands cupping one of her eyes and she cusses the pain away."

    nvlNar "He probably got his eye, a realization that makes him cringe a little bit."

    nvlNar "As the vines around Ainhra fade away into nothing and the Hobgoblin notices her friend on the floor, she surrenders."

    if CaimilPunch:
        nvlNar "Maybe he did end up going overboard..."
        jump AinhraPostSpar

    else:
        nvlNar "Though he did win, he rushes over to the Faerie to make sure they're okay."
        jump AinhraPostWin

label AinhraPostSpar:

    ainhra "Caimil right? Are you okay?!"

    nvlNar "Ainhra gets a good look at her eye, it doesn't look pretty."

    caimil "Yeah but no but... I'm good."

    caimil "It's nothing my mom can't figure out, besides, the black eye'll definitely help our case!"

    ainhra "I guess so but... I still feel icky about that."

    caimil "Dude it's fine, don't worry about it!"

    caimil "Smooth moves by the way!"

    ainhra "Yeah! Uh, you too."

    nvlNar "The conversation kind of dies as neither are really fighting types, they rarely use their magic like this as it is, if at all."

    nvlNar "Meanwhile Okra and Zirkli are chatting up a storm, analyzing their fight and figuring out what went right and wrong for the both of them."

    nvlNar "It would be fascinating if either of them were into this stuff, and it's still kind of interesting to listen in on."

    ainhra "So uh... Want to interrupt?"

    caimil "Nah, might as well catch a break while they're talking."

    ainhra "I guess that sounds good."

    nvlNar "The two rest until the Orc and the Hobgoblin are done talking about how best to beat the other and eventually the convo does end."

    nvlNar "Now for other things!"

    jump AfterFight

label AinhraPostWin:

    ainhra "Hey! Are you okay! I didn't mean to hurt you that bad I swear!"

    nvlNar "The Faerie turns to you, her left hand covering up a blackened swollen eye."

    "Faerie" "..."

    "Faerie" "A slap... Really?"

    ainhra "Huh? Wh-"

    "Faerie" "Why must you humiliate me with such a low blow?!"

    ainhra "Wait, I'm sorry?!"

    "Faerie" "You disgrace me with such a brutish maneuver! I would have preferred it if you just threw a brick at my skull!"

    "Faerie" "Hmph!"

    nvlNar "She turns away in a huff."

    ainhra "Well... I'm sorry I slapped you in the face. I was just trying to get you to lay off without fracturing your skull."

    ainhra "It was the best I could come up with in a split second and-"

    nvlNar "Ainhra sees her starting to chuckle, the facade of indignation cracking."

    ainhra "Hey!"

    nvlNar "She bursts into laughter."

    "Faerie" "Heh! You should have seen the look on your face!"

    "Faerie" "But yeah! I was just screwing with you."

    ainhra "What? So you aren't actually bothered about the slap?"

    "Faerie" "Nah! I thought it was kinda funny actually!"

    ainhra "Well that's a relief but... Your eye..."

    "Faerie" "Ah yeah that. Yeah it's bad but I think I can make this work for all of us!"

    "Faerie" "Besides, it's nothing a healing balm and some sleep can't fix."

    ainhra "That's good, but how are you going to make this work?"

    "Faerie" "Well, our boss is insane, a power hungry freak who will stop at nothing to make sure everyone fears her."

    "Faerie" "But our friends, the ones after you, they're much more reasonable."

    "Faerie" "They don't want to be here either but they have a beating quota to fulfil."

    "Faerie" "But if we can tell them that you got one over us, they'll probably let us go."

    "Faerie" "And this black eye is our ticket!"

    "Faerie" "So uh... Thanks! In a bizarre way."

    ainhra "You're welcome! Uh..."

    "Faerie" "Ah! Forgot to introduce myself."

    caimil "I'm Caimil! And my friend over there is Zirkli!"

    caimil "We've been friends since like, kindergarten so where she goes, I go. And vice versa."

    caimil "But yeah! Sorry we had to run into each other like this."

    ainhra "It's fine, it could be worse."

    caimil "True! But don't jinx it."

    nvlNar "He and Caimil share her plan to get out of this without having to fight one another, and much to her delight, Okra and Zirkli are quite receptive."

    nvlNar "Them having beaten each other up also helps with her plan, so that's good."

    nvlNar "In the end, crisis averted!"

    jump AfterFight

label OkraFight1:

    nvlNar "Okra takes a swing at the incoming hobgoblin but she swiftly dodges out of the way."

    nvlNar "The hobgoblin jabs at his gut, and Okra responds with a headbutt. Both are knocked away from each other."

    nvlNar "The hobgoblin retakes the initiative as she surges towards him, she goes for a sweeping motion which forces Okra to brace himself and block low."

    nvlNar "But as her swing starts, her leg arcs up and Okra gets kicked in the face. {i}Hard.{/i}"

    nvlNar "Okra is reeling from the impact and nearly stumbles over but manages to regain his footing before Zirkli closes the gap."

    nvlNar "What next?"

    nvl clear

    menu(nvl=True):

        "Brace for Impact":
            jump OkraFight2

        "Go for her hair.":
            jump OkraDirty1


    label OkraDirty1:

        nvlNar "In a desperate gambit to get the upper hand, you lunge for her hair and pull on it as hard as you can."

        nvlNar "As you yank on her hair she screams and shouts, her cries and curses echoing throughout the tunnels."

        nvlNar "She tries to claw back control, to get you on the back foot, but you maintain your footing regardless."

        nvlNar "After a few more moments of struggle you manage to grab one of her arms, and you decided to put all your strength into one big throw."

        nvlNar "But what will you throw the hobgoblin at? Or who?"

        nvl clear

        menu(nvl=True):

            "The Faerie":
                jump BadEnd2

            "The Wall":
                jump BadEnd3

    label BadEnd2:

        nvlNar "You throw the Hobgoblin into the faerie, sending both of them crashing into a wall. The faerie getting sandwiched in the process."

        nvlNar "And to make sure that neither of them get back up, you slam yourself into the two, crushing both with your body weight."

        nvlNar "The faerie is unconscious beneath the hobgoblin, and the hobgoblin herself is barely responsive. Unable to even spit curses at you, let alone get up."

        nvlNar "You won. But you don't feel good about it in the slightest."

        nvlNar "And when you look at Ainhra, you see a mix of reservation and fear in his eyes."

        nvlNar "The brutality you displayed was too much for him to bear witness to."

        nvlNar "And he leaves you behind, to find his own way out."

        nvlNar "And as he disappears into the darkness, one thought enters your head."

        nvlNar "You don't even blame him."

        nvlNar "Bad Ending #2"

        return

    label BadEnd3:

        nvlNar "You throw the hobgoblin into the concrete wall, her body making a resounding thud when it makes contact."

        nvlNar "To put her out of commission for good, you try and slam into her with all your body weight."

        nvlNar "But just before you reach her, the ground shifts and gives way, causing you to stumble and fall into the wall."

        nvlNar "In one moment, you see Fae magic radiating from the Faerie's hand."

        nvlNar "In the next moment, you see the Hobgoblin's boot over your head, and rage in her eyes."

        nvlNar "And in the next, a flash of light, and then darkness."

        nvlNar "..."

        nvlNar "It felt like hours before you would once again regain consciousness."

        nvlNar "Your face feels like its been beaten in with a sledgehammer, as does the rest of your body."

        nvlNar "On top of that, your wallet and phone have been stolen from you."

        nvlNar "And as your eyes slowly focus on the sewer grate leading outside, you are greeted by the pale moonlight above, and the sound of passing cars."

        nvlNar "You, as well as Ainhra, are in a world of hurt. Literally, and metaphorically speaking."

        nvlNar "But at least nobody is chasing you anymore."

        "Bad Ending #3"

        return

label OkraFight2:

    nvlNar "He puts up his arms and braces himself for the worst. And within moments a hailstorm of punches make their way to him."

    nvlNar "No matter what you try to do you can't seem to block anything, and its wearing on you fast."

    nvlNar "You need look for an opening, or make one."

    nvlNar "You wait for the slightest lapse in her assault and shove her away from you."

    nvlNar "What next?"

    nvl clear

    menu(nvl=True):

        "Uppercut her now!":
            jump OkraLose

        "Get in close.":
            jump OkraWin


label OkraLose:

    nvlNar "Okra tries to go for a killing blow, an uppercut with everything he has."

    nvlNar "But he's too far, and she has plenty of time to react. And now you're left wide open."

    nvlNar "Before he even has time to register how bad of a position he's in, he takes a kick to the kidney, one to the stomach and a final one to the head. Knocking hom to the floor."

    nvlNar "His head is rattling in his skull and he's in no position to fight like this. Especially after an onslaught like that."

    nvlNar "You surrender, as does Ainhra as he sees that you've been bested."

    if CaimilPunch:
        nvlNar "You were so close! But alas, you whiffed."
        jump OkraPostLoseSpar

    else:
        nvlNar "You prepare for the worst as the hobgoblin looms above you."
        jump OkraPostLose

label OkraPostLose:

    "Your heart pounds as you expect to have your face stomped into the cold concrete pressing against your hands."

    "But to your surprise, she offers you a hand, a hand you timidly, but gladly accept."

    okra "Why... didn't you finish me off?"

    "Hobgoblin" "Look... You seem cool enough and you already know I don't want to be here."

    "Hobgoblin" "If I'm honest... I'd rather be home knitting. I have a scarf at home that's like halfway done."

    okra "Ooo that sounds nice actually!"

    "Hobgoblin" "Understatement. Not only do I get to unwind, but I get a comfy scarf in the end."

    okra "Sounds like a win-win if you ask me!"

    "She smiles."

    okra "But... What about your boss? You still have her to deal with."

    "Hobgoblin" "I know... I'm sure I can think of someth-"

    "Faerie" "No need! Have you two seen yourselves?"

    "Hobgoblin" "Hm?"

    okra "Huh?"

    "You took quite the beating from her, bruising across your arms, some swelling in your right cheek too."

    "But she didn't come out unscathed either. She's bruised up too."

    "Hobgoblin" "I took a few hits yeah, but what does that have to do with anything?"

    "Faerie" "You know, we could just say they messed us up and got away."

    "Faerie" "Besides, the boss is insane but Kaii and her friends are alright. I'm sure they'll let us off the hook."

    okra "You sure?"

    "Faerie" "For the most part yeah!"

    "Everyone breathes a collective sigh of relief, nobody has to get curb stomped woo!"

    okra "By the way uh... I didn't get your name."

    zirkli "It's Zirkli!"

    "She then points to the faerie."

    zirkli "And she's Caimil!"

    zirkli "We go back for a {i}while.{/i}"

    okra "I noticed!"

    zirkli "Heh. Stalker."

    okra "Hey! We were just trying to stay hidden. And gather intel and stuff."

    zirkli "So stalking?"

    okra "Shut up. :("

    "She snickers."

    zirkli "I'm just messing with ya'!"

    okra "Ah! {i}I knew that... Definitely.{/i}"

    okra "But uh... We're cool?"

    zirkli "Yeah, we're cool."

    jump AfterFight

label OkraPostLoseSpar:

    "Zirkli extends a hand to Okra and he takes it, letting her hoist him up to his feet."

    zirkli "You know? You weren't too bad."

    zirkli "But that last hit was kinda-"

    okra "Dumb?"

    zirkli "Yup."

    okra "I know. I guess I'm not used to just relying on my fists."

    okra "I'm more of a sparring axe person. Bit more reach and a lot more punch."

    okra "Not to mention I didn't even had time to think with that hail of punches you were putting out."

    "She smirks."

    okra "In the end, you got me really good. End of story. Well played!"

    zirkli "Heh! Thanks! Most people don't usually compliment me after I kick them to the floor."

    zirkli "{i}Usually they just call me a bitch.{/i}"

    okra "But speaking of..."

    zirkli "Hm?"

    okra "How did you pull off that kick to the face? {i}That{/i} was sick."

    zirkli "Wait really?"

    okra "I didn't even see it coming! I could use a move like that!"

    okra "Mostly at the rec center, not that anyone can really keep up with me."

    okra "And you. I can't just leave this at 0-1 forever."

    zirkli "That a challenge?"

    okra "And a promise."

    zirkli "Well if you really want to have another go, and you make it out of here intact, you free next Saturday? Iron Lion?"

    okra "Sure! I go there anyway on Saturdays. Cardio y'know?"

    zirkli "Then it's set then!"

    caimil "Hey, I don't want to interrupt but are you two done planning on beating the crap out of each other?"

    zirkli "We are, don't worry."

    jump AfterFight
    

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

    nvlNar "Okra offers her a hand up, but she declines and hoists herself onto her feet."

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

    jump AfterFight

label OkraPostSpar:

    okra "Hey? You alright?"

    zirkli "Enough... You?"

    okra "I'm good."

    okra "Man, I haven't had a brawl like that in a while!"

    zirkli "Really? {i}You{/i} get into fights often?"

    okra "Not on the streets but yeah. Inter-clan duels at the rec center and all that."

    zirkli "Ah, now that makes sense."

    okra "One thing though..."

    zirkli "Hm?"

    okra "..."

    okra "How did you do that kick to the face? {i}I wanna know!{/i}"

    zirkli "Wait really?"

    okra "Yeah dude that was so sick!"

    zirkli "Huh! Nobody really asks me about this sort of thing. Usually they just call me a bitch."

    okra "I mean you really got me good, and I wanna see if I can pull it off myself."

    okra "Nobody can really keep up with me either way, but it doesn't hurt to widen the gap."

    zirkli "Heh! Maybe later, you know where Iron Lion is right?"

    okra "Oh there? Yeah I go there every other weekend, mostly for cardio though."

    zirkli "Then I can expect you to show right?"

    okra "Oh absolutely!"

    ainhra "Hey are you guys done gawking at each other?"

    okra "Ah! Sorry!"

    "Zirkli rolls her eyes."

    jump AfterFight

label AfterFight:

