"""Verify the one-letter artist transformations from Jane Street's Hint Singles."""

from string import ascii_lowercase


TRANSFORMATIONS = (
    ("Weezer", "Wheezer"),
    ("Spin Doctors", "Spine Doctors"),
    ("Bad Bunny", "Bald Bunny"),
    ("Miley Cyrus", "Miley Cyprus"),
    ("Luke Combs", "Luke Combos"),
    ("State Champs", "Statue Champs"),
    ("Johnny Cash", "Johnny Crash"),
    ("Foo Fighters", "Food Fighters"),
    ("Billy Joel", "Billy Jor-El"),
    ("Men at Work", "Menu at Work"),
    ("Chappell Roan", "Chappell Roman"),
    ("Bob Dylan", "Bomb Dylan"),
    ("Fleetwood Mac", "Fleetwood Mace"),
    ("Big Thief", "Brig Thief"),
    ("Lana Del Rey", "Lana Deli Rey"),
    ("Linkin Park", "Linkin Spark"),
    ("Cardi B", "Cardio B"),
    ("Pet Shop Boys", "Pet Shop Buoys"),
    ("David Bowie", "David Bowtie"),
    ("The Cure", "The Curse"),
    ("Erykah Badu", "Erykah Baidu"),
    ("Hanson", "Chanson"),
    ("Mariah Carey", "Mariah Car Key"),
)

EXPECTED_MESSAGE = "HELPOURDRUMMERISOUTSICK"


def normalise(text):
    """Remove spaces and punctuation, then convert to lowercase."""
    return "".join(
        character.lower()
        for character in text
        if character.lower() in ascii_lowercase
    )


def inserted_letter(original, modified):
    """Return the single letter inserted into original to make modified."""
    original = normalise(original)
    modified = normalise(modified)

    if len(modified) != len(original) + 1:
        raise ValueError("The modified name must contain exactly one extra letter.")

    original_index = 0
    modified_index = 0
    extra = None

    while original_index < len(original) and modified_index < len(modified):
        if original[original_index] == modified[modified_index]:
            original_index += 1
            modified_index += 1
        elif extra is None:
            extra = modified[modified_index]
            modified_index += 1
        else:
            raise ValueError("The names differ by more than one insertion.")

    if extra is None:
        extra = modified[modified_index]
        modified_index += 1

    if original_index != len(original) or modified_index != len(modified):
        raise ValueError("The names do not match by one insertion.")

    return extra.upper()


def verify_transformations():
    """Check every pair and reconstruct the hidden message."""
    extracted_message = "".join(
        inserted_letter(original, modified)
        for original, modified in TRANSFORMATIONS
    )

    if extracted_message != EXPECTED_MESSAGE:
        raise AssertionError("The extracted message does not match the puzzle solution.")

    return extracted_message


def main():
    message = verify_transformations()
    print(f"Verified {len(TRANSFORMATIONS)} transformations.")
    print(f"Extracted message: {message}")


if __name__ == "__main__":
    main()
