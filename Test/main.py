import random as rand


def readFile(filename: str) -> str:
    """
    Read the content of the file specified by the filename parameter and return it as a string.

    Parameters:
    filename (str): The name of the file to read.

    Returns:
    str: The content of the file as a string.
    """
    content = ""
    with open(filename, 'r') as f:
        content = f.read()

    return content


def saveFile(filename: str, content: str) -> str:
    with open(filename, 'w') as f:
        f.write(content)


def split(content: str, howMany: int) -> list:
    content = content.replace("\n", "")
    result = []
    for i in range(0, len(content), howMany):
        result.append(content[i:i+howMany])
    return result


def get_left_and_right(binary: str):
    return {
        "left": binary[0:4],
        "right": binary[4:]
    }


def sum_binaries(binaries: list) -> int:
    return sum(binaries) % 2


def correct(binary: int) -> int:
    return 0 if binary == 1 else 1


def get_hamming(binaries: list) -> dict:
    corrected = ""
    no_parity = ""
    counter = 0
    for i in binaries:
        # print(f"Mot: {i}")
        c1 = int(i[0])
        c2 = int(i[1])
        c3 = int(i[2])
        c4 = int(i[3])
        c5 = int(i[4])
        c6 = int(i[5])
        c7 = int(i[6])

        direction = get_left_and_right(i)
        left = direction.get("left")
        right = direction.get("right")

        # print(f"gauche: {left}, droite: {right}")

        resC5 = {"res": sum_binaries([c1, c2, c3])}
        resC6 = {"res": sum_binaries([c1, c2, c4])}
        resC7 = {"res": sum_binaries([c2, c3, c4])}

        resC5["status"] = True if resC5["res"] == c5 else False
        resC6["status"] = True if resC6["res"] == c6 else False
        resC7["status"] = True if resC7["res"] == c7 else False

        if resC5["status"] == False and resC6["status"] == False and resC7["status"] == True:
            print("C1 est erroné")
            c1 = correct(c1)
            print("C1 est corrigé\n")
            counter += 1
        if resC5["status"] == False and resC6["status"] == False and resC7["status"] == False:
            print("C2 est erroné")
            c2 = correct(c2)
            print("C2 est corrigé\n")
            counter += 1
        if resC5["status"] == False and resC7["status"] == False and resC6["status"] == True:
            print("C3 est erroné")
            c3 = correct(c3)
            print("C3 est corrigé\n")
            counter += 1
        if resC6["status"] == False and resC7["status"] == False and resC5["status"] == True:
            print("C4 est erroné")
            c4 = correct(c4)
            print("C4 est corrigé\n")
            counter += 1
        # print(f"Avant: {list(i)}")
        """ print(
            f"Apres: {[str(c1), str(c2), str(c3), str(c4), str(c5), str(c6), str(c7)]}\n") """

        corrected += str(c1) + str(c2) + str(c3)+str(c4) + right+"\n"
        no_parity += str(c1) + str(c2) + str(c3)+str(c4) + "\n"

    print(f"Nombre d'erreurs trouvées: {counter}\n")

    return {
        "corrected": corrected,
        "no parity bits": no_parity
    }


def get_ascii(binary_number: str) -> str:
    bin_to_int = int(binary_number, 2)
    return chr(bin_to_int)


def get_transcription(binaries: list) -> str:
    result = ""
    for i in binaries:
        result += get_ascii(i)

        """ print(
            f"Mot: {i} ==> {get_ascii(i)} ==> {get_ascii_from_table(i, ASCII.ASCII)}") """
    return result


def decode_vigenere(text: str, key: str) -> str:
    decalage = 65
    decoded = ""
    total = 26
    k_position = 0
    for i in text:
        if (k_position >= len(key)):
            k_position = 0
        if i.isalpha():
            c = ord(i.upper()) - decalage
            k = ord(key[k_position].upper()) - decalage
            k_position += 1

            calcul = (c - k + total) % total
            if i.isupper():
                decoded += chr(calcul+decalage)
            else:
                decoded += chr(calcul+decalage).lower()
        else:
            decoded += i
    return decoded


def generate_random_key(lenght: int) -> str:
    random_key = ""
    letters = "".join(chr(i) for i in range(97, 123))
    random_key = "".join(rand.SystemRandom().choice(letters)
                         for _ in range(lenght))
    return random_key


def get_vernam(text: str, key: str) -> str:
    decalage = 65
    result = ""
    for t, k in zip(text, key):
        tval = ord(t.upper()) - decalage
        kval = ord(k.upper()) - decalage
        calcul = (tval + kval) % 26
        if t.isalpha():
            if t.isupper():
                result += chr(calcul + decalage).upper()
            else:
                result += chr(calcul + decalage).lower()
        else:
            result += t
    return result


def decode_vernam(text: str, key: str) -> str:
    decalage = 65
    result = ""
    for t, k in zip(text, key):
        tval = ord(t.upper()) - decalage
        kval = ord(k.upper()) - decalage

        calcul = (tval - kval) % 26
        if t.isalpha():
            if t.isupper():
                result += chr(calcul + decalage).upper()
            else:
                result += chr(calcul + decalage).lower()
        else:
            result += t
    return result


def main():
    LETTER = "lettre.txt"
    CORRECTED = "lettre_corrigee.txt"
    NO_PARITY = "lettre_sans_bit_de_parite.txt"
    TRANSCRIPTION = "transcription.txt"
    KEY = "PYTHON"
    VIGENERE = "decodage_vigenere.txt"
    VERNAM = "encodage_vernam.txt"
    RAND_KEY = "cle_aleatoire.txt"

    letter = readFile(LETTER)
    split_7 = split(letter, 7)

    hamming = get_hamming(split_7)
    corrected = hamming.get("corrected")
    saveFile(CORRECTED, corrected)
    print(f"Lettre corrigée et enregistrée dans: '{CORRECTED}'\n")

    no_parity = hamming.get("no parity bits")
    saveFile(NO_PARITY, no_parity)
    print(
        f"Lettre corrigée sans les bits de parités et enregistrée dans: '{NO_PARITY}'\n")

    split_8 = split(no_parity, 8)
    transcription = get_transcription(split_8)
    saveFile(TRANSCRIPTION, transcription)
    print(
        f"Transcription effectuée et enregistrée dans: '{TRANSCRIPTION}'\n")

    vigenere = decode_vigenere(transcription, KEY)
    saveFile(VIGENERE, vigenere)
    print(
        f"Decodage de Vigenere éffectué sur la transcription à l'aide de la clé '{KEY}' enregistré dans '{VIGENERE}'\n")

    randomKey = generate_random_key(len(vigenere))
    saveFile(RAND_KEY, randomKey)
    print(
        f"Clé aléatoire de longueur {len(randomKey)} générée et enregistré dans '{RAND_KEY}' '\n")

    vernam = get_vernam(vigenere, randomKey)
    saveFile(VERNAM, vernam)
    print(
        f"Text encodé à nouveau via l'algorithme de Vernam et enregistré dans '{VERNAM}'\n")


if __name__ == "__main__":
    main()
