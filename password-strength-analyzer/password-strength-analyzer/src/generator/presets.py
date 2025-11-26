from typing import List

PREDEFINED_WORDLISTS: List[str] = [
    "password",
    "123456",
    "qwerty",
    "abc123",
    "letmein",
    "welcome",
    "monkey",
    "iloveyou",
    "admin",
    "password1",
    "sunshine",
    "123456789",
    "qwertyuiop",
    "12345678",
    "12345",
    "1234567",
    "football",
    "princess",
    "dragon",
    "passw0rd",
    "123123"
]

def get_presets() -> List[str]:
    return PREDEFINED_WORDLISTS.copy()