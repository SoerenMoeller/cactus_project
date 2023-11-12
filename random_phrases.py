from random import choice

TEXT  = 0
VOICE = 1
PHRASES = [
    {
        TEXT: "Ich hasse Mikrophone",
        VOICE: "Ich hasse Mikrophone"
    }
]


def get_random_phrase() -> dict[int, str]:
    return choice(PHRASES)
