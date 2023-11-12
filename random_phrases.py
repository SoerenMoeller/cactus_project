from random import choice

TEXT  = 0
VOICE = 1
PHRASES = [
    [
        ["Ich hasse", "Mikrophone"],
        "Ich hasse Mikrophone"
    ],
    [
        ["", ""],
        "Ich liebe Schokobrötchen"
    ]
]


# do some sanity checks
for phrase in PHRASES:
    assert TEXT in phrase and VOICE in phrase, f"Missing keywords in phrase {phrase}"
    assert type(phrase[TEXT]) == list, f"Wrong text type in phrase {phrase}"
    assert len(phrase[TEXT][0]) <= 16 and len(phrase[TEXT][1]) <= 16, f"Phrase {phrase} is too long"
print("All registered phrases are in the correct format")


def get_random_phrase() -> dict[int, str]:
    return choice(PHRASES)
