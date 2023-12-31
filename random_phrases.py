from random import choice

TEXT  = 0
VOICE = 1

# sorry for the bad format :(
PHRASES = [
    [
        ["Ich hasse", "Mikrophone"],
        "Ich hasse Mikrophone"
    ],
    [
        ["Ich liebe", "Schokobrötchen"],
        "Ich liebe Schokobrötchen"
    ],
    [
        ["O.o", ""],
        "Was guckst du so blöd"
    ],
    [
        [">:(", ""],
        "Du elendiger NPC"
    ],
    [
        ["Geh HEIM!", ""],
        "Geh doch nach Hause!"
    ],
    [
        ["Ich gehe!", ""],
        "Ich hau ab!"
    ]
]


# do some sanity checks
for phrase in PHRASES:
    assert len(phrase) == 2, f"Missing keywords in phrase {phrase}"
    assert type(phrase[TEXT]) == list, f"Wrong text type in phrase {phrase}"
    assert len(phrase[TEXT][0]) <= 16 and len(phrase[TEXT][1]) <= 16, f"Phrase {phrase} is too long"
print("All registered phrases are in the correct format")


def get_random_phrase() -> dict[int, str]:
    return choice(PHRASES)
