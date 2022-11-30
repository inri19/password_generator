import random

caracteres = "AaÀàÂâÄäÃãBbCcçDdEeéÈèÊêËëFfGgHhIiÌìÎîÏïJjKkLlMmNnÑñOoÒòÔôÖöÕõPpQqRrSsTtUuÙùÛûÜüVvWwXxYyÿZz_-'.,;:!?@&§~^`¨°|()}{[]/\<>#"


nb_caractere = int(input('Nombre de caractere : '))
nb_mpd = int(input('Entrer le nombre de mot de passe que vous voulez : '))

for i in range(nb_mpd):

    mpd = ""

    for i in range(nb_caractere):

        mpd += random.choice(caracteres)

    print(mpd)
