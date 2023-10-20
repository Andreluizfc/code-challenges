def ransom_note(ransom_note, magazine):
    """
    :type ransom_note: str
    :type magazine: str
    :rtype: bool
    """
    
    rn_count = {}
    magazine_count = {}

    for letter in ransom_note:
        rn_count[letter] = rn_count.get(letter, 0) + 1
    for letter in magazine:
        magazine_count[letter] = magazine_count.get(letter, 0) + 1

    for letter, count in rn_count.items():
        if letter not in magazine_count or count > magazine_count[letter]:
            return False
    return True

            