"""
Contains selection of jokes in different categories and functions for serving them
Emil Rekola <emil.rekola@hotmail.com>
"""

import random

jokes = {
    "dad jokes": [
        "What did the ocean say to the beach? Nothing, it just waved",
        "I only know 25 letters of the alphabet. I don't know y",
        "What did Baby Corn say to Mama Corn? Where's Pop Corn?",
        "I don't trust those trees... They seem kind of shady",
        "I don't trust stairs... They're always up to something",
        "What concert costs just 45 cents? 50 Cent featuring Nickelback!",
        "Why did the math book look so sad? Because of all of its problems!",
        "How does a penguin build its house? Igloos it together",
        "Why don’t crabs give to charity? Because they’re shellfish",
        "Why did the man name his dogs Rolex and Timex? Because they were watch dogs",
        "My wife asked me to sync her phone, so I threw it into the ocean. I don’t know why she’s mad at me",
        "What do you call a dog that can do magic? A Labracabrador",
        "What do you call a fish with no eye? A fsh",
        "What kind of noise does a witch’s vehicle make? Brrrroooom, brrroooom",
        "Why don’t skeletons ever go trick or treating? Because they have no body to go with",
        "Why do vampires seem sick? They’re always coffin"
    ],
    "dark humour": [
        "Why can't orphans play baseball? They don't know where home is",
        "What's yellow and can't swim? A bus full of children",
        "Why do orphans go to church? So they have someone to call father",
        "What does a website for orphans look like? Pretty empty, there’s not even a homepage",
        "Siri, why am I still single? *Siri activates front camera*",
        "What does my dad have in common with Nemo? They both can’t be found",
        "What do you call a cheap circumcision? A rip-off",
        "Why are friends a lot like snow? If you pee on them, they disappear",
        "My grandfather says I’m too reliant on technology. I called him a hypocrite and unplugged his life support",
        "My girlfriend dumped me, so I stole her wheelchair. Guess who came crawling back",
        "Where did Suzy go after getting lost on a minefield? Everywhere",
        "Suicide is wrong, but if you jump off a bridge and yell parkour; it's a failed stunt",
        "What’s blue and doesn’t fit? A dead epileptic",
        "Why was the leper hockey game cancelled? There was a face off in the corner"
    ],
    "yo mama": [
        "Yo mama's so ugly that when she looks out the window she gets arrested for indecent exposure",
        "Yo mama is so fat, I took a picture of her last Christmas and it's still printing",
        "Yo mama is so fat when she got on the scale it said, 'I need your weight not your phone number'",
        "Yo mama's so fat, that when she fell, no one was laughing but the ground was cracking up",
        "Yo mama is so fat when she sat on WalMart, she lowered the prices",
        "Yo mama is so fat that Dora can't even explore her",
        "Yo mama is so ugly she made One Direction go another direction",
        "Yo mama's so stupid, she put two quarters in her ears and thought she was listening to 50 Cent",
        "Yo mama so stupid she stuck a battery up her ass and said, 'I GOT THE POWER!'",
        "Yo mama is so stupid she brought a spoon to the super bowl",
        "Yo mama is so fat she doesn't need the internet, because she's already world wide",
        "Yo mama's so fat she needs cheat codes for Wii Fit",
        "Yo mama's so fat, if she was a Star Wars character, her name would be Admiral Snackbar",
        "Yo mama's so stupid, she thought a quarterback was a refund",
        "Yo mama's so poor, the ducks throw bread at her",
        "Yo mama's so classless, she's a Marxist utopia",
        "Yo mama's so poor, Nigerian princes wire her money"
    ],
    "sports": [
        "What's the difference between England and a teabag? A teabag could stay in the cup for longer",
        "What is a ghosts favorite position in soccer? Ghoul keeper",
        "Why did the golfer wear two pairs of pants? A: In case he got a hole in one",
        "What's the difference between baseball and politics? In baseball you're out if you're caught stealing",
        "Ice hockey is basically just guys wearing knife shoes fighting each other with long sticks for the last Oreo",
        "Refusing to go to the gym counts as resistance training, right?",
        "I'm taking part in a stair climbing competition. Guess I better step up my game",
        "If you run in front of a car you'll get tired, but if you run behind the car you'll get exhausted",
        "I recently added squats to my workouts by moving the beer into the bottom shelf of the fridge",
        "My tennis opponent was not happy with my serve. He kept returning it",
        "What tea do hockey players drink? Penaltea",
        "I am known at the gym as the 'before picture'",
        "Why is a baseball game a good place to go on a hot day? Because there are lots of fans",
        "Why is a tennis game a noisy game? Because each player raises a racket",
        "My dog Minton ate all my shuttlecocks. Bad Minton",
        "What do you call a girl standing in the middle of a tennis court? Annette",
        "Where do zombies like to go swimming? The Dead Sea",
        "What's the object of a Jewish football game? To get the quarterback",
        "Why didn't the dog want to play football? It was a boxer"
    ],
    "blonde": [
        "Two blondes fell down a hole. One said, 'It's dark in here isn't it?' "
        "The other replied, 'I don't know; I can't see'",
        "Why can't a blonde dial 911? She can't find the eleven",
        "What did the blonde say when she saw the Cheerios box? 'Omg, donut seeds'",
        "Why did the blonde put her iPad in a blender? Because she wanted to make apple juice",
        "How do you confuse a blonde? Put her in a circle and tell her to go to the corner",
        "A blonde drops off her dress to the dry cleaners\nThe lady says, 'Come Again!'\nThe blonde says, "
        "'No, it's toothpaste this time'",
        "What do you call a blonde with a brain? A golden retriever",
        "I knew a blonde that was so stupid, she put lipstick on her forehead because she wanted to make up her mind",
        "Why did the blonde like lightning? She thought someone was taking a picture of her",
        "How do you get a one handed blonde down from a tree? Wave at her",
        "How do you keep a blonde busy? Give her a piece of paper that has 'Please turn over' written on both sides.",
        "What do you call it when a blonde dyes her hair brunette? Artificial intelligence",
        "How can you get a blonde to laugh on Saturday? Tell her a joke on Wednesday",
        "Why can't blondes tie shoes? They just can't grasp the concept that the long thing "
        "goes around the hole, not into it."
    ]
}


def get_random_joke() -> str:
    """
    Randomize a joke from any category

    :return: Random joke from random category
    """

    random_category = random.choice(list(jokes.keys()))
    return random.choice(jokes[random_category])


def get_random_joke_from_category(category: str) -> str:
    """
    Randomize a joke from a category. If the given category is invalid -> randomize the category

    :param category: Name of the joke category
    :return: Random joke
    """

    if category.lower() in jokes:
        return random.choice(jokes[category])

    else:
        notification = f"Given category '{category}' was not recognized, here is a random joke:"
        joke = get_random_joke()
        return f"{notification}\n{joke}"


def get_categories() -> str:
    """
    Return a string with all supported joke categories
    :return: Str with all categories
    """

    return ", ".join([key.capitalize() for key in jokes.keys()])
