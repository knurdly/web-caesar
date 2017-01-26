def encrypt(text, rot):
    final=""

    for i in text:
        if ( ord(i) > 96 and ord(i) < 123):
            cypher = rotate_character(i,rot)
            final += str(cypher)
        elif ( ord(i) > 64 and ord(i) < 91):
            cypher = rotate_character(i,rot)
            final += str(cypher)
        else:
            final += str(i)
    return final

#converts letter to a number
def alphabet_position(letter):
    if letter.islower() == True:
        letter = (ord(letter[0]) - 97)
    elif letter.isupper() == True:
        letter = (ord(letter[0]) - 65)
    return(letter)

#converts letter to a new letter by rotation
def rotate_character(char, rot):
    new = char

    rotation = int(rot % 26)
    if new.islower() == True:
        new = (alphabet_position(new) + rotation) % 26
        new += 97
        new = chr(new)
    elif new.isupper() == True:
        new = (alphabet_position(new) + rotation) % 26
        new += 65
        new = chr(new)
    return new
