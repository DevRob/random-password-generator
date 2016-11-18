import random

#comment/uncomment prohibited_characters to exclude/include special characters.

prohibited_characters = []
prohibited_characters.extend([x for x in range(48)]) #from "NUL" to "/"
prohibited_characters.extend([x for x in range(58, 65)]) #from ":" to "@"
prohibited_characters.extend([x for x in range(91, 97)]) #from "[" to "'"
prohibited_characters.extend([x for x in range(123, 128)]) #from "{" to "DEL"
prohibited_characters.extend([x for x in range(128, 256)]) #Extended ASCII Codes
#print [chr(x) for x in prohibited_characters]

def pwdGen(length, password):
    character = int(random.SystemRandom().random() * 1000) % 255
    if character in prohibited_characters:
        return pwdGen(length, password)
    else:
        if length == 0:
            return password
        else:
            password.append(chr(character))
    return pwdGen(length - 1, password)

password = pwdGen(16, []) #change length if you want shorter or longer character chain.
print('Your random password: ',''.join(password))