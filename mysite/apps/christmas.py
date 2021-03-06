import random

def Joke():
    jokes = [{
        "joke": "What does Santa suffer from if he gets stuck in a chimney?",
        "response": "Claustrophobia!"
    },
    {
        "joke":"What do you call a line of men waiting for a haircut?" ,
        "response": "A barberqueue"
    },
    {
        "joke": "Why was the turkey in the pop group?" ,
        "response": "Because he was the only one with drumsticks!"
    },
    {
        "joke": "What do you call a boomerang that does not come back?" ,
        "response": "A stick"
    },
    {
        "joke": "What do snowmen wear on their heads?" ,
        "response": "Ice caps"
    },
    {
        "joke": "Why was the snowman looking through the carrots?" ,
        "response": "He was picking his nose"
    },
    {
        "joke": "Two snowmen were standing in a field. One said:",
        "response": "Can you smell carrots?"
    },
    {
        "joke": "What did Adam say the day before Christmas?" ,
        "response": "It's Christmas, Eve"
    },
    {
        "joke": "What did Cinderella say when her photos didn't arrive on time?" ,
        "response": "One day my prints will come"
    },
    {
        "joke": "When do vampires like racing?" ,
        "response": "When it's neck and neck"
    },
    {
        "joke": "What's a dog's favourite carol?" ,
        "response": "Bark, the herald angels sing"
    },
    {
        "joke": "What do snowmen have for breakfast?",
        "response": "Snowflakes"
    },
    {
        "joke":"What does Santa do when his elves misbehave?" ,
        "response": "He gives them the sack"
    },
    {
        "joke": "What do you give a dog for Christmas?",
        "response": "A mobile bone"
    },
    {
        "joke": "Why did the pony have to gargle?" ,
        "response": "Because it was a little horse" 
    },
    {
        "joke": "Why are Christmas trees very bad at knitting?" ,
        "response": "Because they always drop their needles" 
    },
    {
        "joke": "What is good King Wenceslas favourite pizza?" ,
        "response": "One that's deep-pan, crisp and even"
    },
    {
        "joke": "What do Santa's little helpers learn at school?" ,
        "response": "The elf-abet!"
    },
    {
        "joke": "What do you call a train loaded with toffee?" ,
        "response": "A chew chew train"
    },
    {
        "joke": "Why did the banana go to the doctors?" ,
        "response": "Because it wasn't peeling very well"
    },
    {
        "joke": "Why couldn't the skeleton go to the Christmas party?" ,
        "response": "He had no body to go with"
    },
    {
        "joke": "What happened to the man who stole an advent calendar?" ,
        "response": "He got 25 days"
    },
    {
        "joke": "Who hides in the bakery at Christmas?" ,
        "response": "A mince spy"
    },
    {
        "joke": "What is the best Christmas present?" ,
        "response": "A broken drum, you can't beat it!"
    },
    {
        "joke": "What do you call a woman who stands between two goal posts?" ,
        "response": "Annette"
    },
    {
        "joke": "What has four legs but can't walk?" ,
        "response": "A table"
    },
    {
        "joke": "What goes 'Oh, Oh, Oh'?" ,
        "response": "Santa walking backwards"
    },
    {
        "joke": "Why did Santa have to go to the hospital?" ,
        "response": "Because of his poor elf"
    },
    {
        "joke": "What do frogs wear on their feet?" ,
        "response": "Open toad sandles"
    },
    {
        "joke": "Why are pirates called pirates?",
        "response": "Because they arrrrrrr!"
    },
    {
        "joke": "What do you call a blind reindeer?",
        "response": "No eye deer"
    },
    {
        "joke": "What's round and bad tempered?",
        "response": "A vicious circle"
    },
    {
        "joke": "How do you know if Santa's been in your garden shed?",
        "response": "You've got three extra hoes"
    },
    {
        "joke": "What's yellow and dangerous?" ,
        "response": "Shark-infested custard"
    },
]
    number = random.randint(0,(len(jokes)-1))
    return jokes[number]

def Trivia():
    number = random.randint(0,13)
    trivia = [
    {"trivia":"US President Franklin Pierce introduced what to White House Christmas tradition in 1856?",
    "response":"The Christmas tree"
    },
        {"trivia":"What is the chemical formula of snow?",
        "response":"H20"
        },
            {"trivia":"Which charity in 1949 was the first to produce a Christmas card?",
            "response":"UNICEF"
            },
                {"trivia":"What red-blooming Christmas plant came originally from Mexico?",
                "response":"The Poinsettia"
                },
                    {"trivia":"Brandy is made from distilling what?",
                    "response":"Wine"
                    },
                        {"trivia":"White Christmas, a cake made of coconut, crisped rice and dried fruit, is popular in which country?",
                        "response":"Australia"
                        },
                            {"trivia":"Who is the narrator in the 2000 film The Grinch Who Stole Christmas?",
                            "response":"Anthony Hopkins"
                            },
                                {"trivia":"Pine needles are said to be a good source of which vitamin?",
                                "response":"Vitamin C"
                                },
                                    {"trivia":"In which Christmas carol does this line feature: 'Bring me flesh, and bring me wine, bring me pine logs hither'",
                                    "response":"Good King Wenceslas"
                                    },
                                        {"trivia":"What is the birth sign of people born on 25 December?",
                                        "response":"Capricorn"
                                        },
                                            {"trivia":"What was the title of the first Christmas TV special Peanuts cartoon? (For a bonus, what year did it debut?)",
                                            "response":"A Charlie Brown Christmas (1965)"
                                            },
                                                {"trivia":"Which two states in the US have towns called Christmas?",
                                                "response":"Arizona and Florida"
                                                },
                                                    {"trivia":"Which hugely popular actor was born on Christmas day 1899?",
                                                    "response":"Humphrey Bogart"
                                                    },
                                                        {"trivia":"La Befana is the legendary character who delivers Christmas presents to children in which country?",
                                                        "response":"Italy"
                                                        },
    ]
    return trivia[number]
