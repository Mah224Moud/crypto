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

    return content.replace("\n", "").replace(" ", "")


def saveFile(filename: str, content: list):
    """
        Saves the given content to a file with the specified filename.
        Parameters:
        - filename (str): The name of the file to save the content to.
        - content (list): The content to be saved to the file.
        Returns:
        None
    """
    with open(filename, "w") as f:
        f.write(content)


def split_into(storage: list, file_content: str, howMany):
    """
    Split the given file content into chunks of length 7 and append them to the storage list.

    Parameters:
    - storage (list): A list to store the split chunks.
    - file_content (str): The content of the file to be split.

    Returns:
    - None
    """
    for i in range(0, len(file_content), howMany):
        storage.append(file_content[i:i+howMany])


def correct(number: int) -> int:
    """
    Returns 1 if the input number is equal to 0, otherwise returns 0.

    Parameters:
        number (int): The input number to be checked.

    Returns:
        int: 1 if the input number is equal to 0, otherwise 0.
    """
    return 1 if number == 0 else 0


def sum_binary(numbers: list) -> int:
    """
    Calculates the sum of a list of binary numbers and returns the last digit.

    Parameters:
        numbers (list): A list of binary numbers.

    Returns:
        int: The last digit of the sum of the binary numbers.
    """
    return int(bin(sum(numbers))[-1])


def get_ascii(binary_number: str) -> str:
    bin_to_int = int(binary_number, 2)
    return chr(bin_to_int)


def left_and_right(list_to_split: str) -> dict:
    """
    Splits a given string into two lists, "left" and "right", based on the indices 0 to 3 and 4 to the end of the string respectively.

    Parameters:
        list_to_split (str): The string to be split into two lists.

    Returns:
        dict: A dictionary containing the "left" and "right" lists.
            - "left" (list): A list of integers obtained by converting the first four characters of the input string to integers.
            - "right" (list): A list of integers obtained by converting the remaining characters of the input string to integers.
    """
    return {
        "left": list(map(int, list_to_split[0:4])),
        "right": list(map(int, list_to_split[4:]))
    }


def calcul(divided_into_7: list) -> dict:
    """
    A function that takes a list of 7-digit binary numbers and processes each number to correct any errors in specific digits. It prints intermediate results and corrections made. The corrected numbers are then concatenated and returned as a single string.

    Parameters:
    - divided_into_7 (list): A list of 7-digit binary numbers to be processed.

    Returns:
    - result (str): A string containing the corrected binary numbers concatenated together.
    """
    complet = ""
    cut = ""
    cpt = 0
    for i in divided_into_7:
        # print(f"Mot: {i}")
        c1 = int(i[0])
        c2 = int(i[1])
        c3 = int(i[2])
        c4 = int(i[3])
        c5 = int(i[4])
        c6 = int(i[5])
        c7 = int(i[6])

        left = left_and_right(i).get("left")
        right = left_and_right(i).get("right")

        # print(f"gauche: {left}, droite: {right}")

        res5 = {"c5": sum_binary([c1, c2, c3])}
        res6 = {"c6": sum_binary([c1, c2, c4])}
        res7 = {"c7": sum_binary([c2, c3, c4])}

        res5["status"] = True if res5["c5"] == c5 else False
        res6["status"] = True if res6["c6"] == c6 else False
        res7["status"] = True if res7["c7"] == c7 else False

        # print(res5, res6, res7)

        if res5["status"] == False and res6["status"] == False and res7["status"] == True:
            print("C1 est erroné !!!")
            cpt += 1
            c1 = correct(c1)
        if res5["status"] == False and res6["status"] == False and res7["status"] == False:
            print("C2 est erroné !!!")
            c2 = correct(c2)
            cpt += 1
        if res5["status"] == False and res7["status"] == False and res6["status"] == True:
            print("C3 est erroné !!!")
            c3 = correct(3)
            cpt += 1
        if res6["status"] == False and res7["status"] == False and res5["status"] == True:
            print("C4 est erroné !!!")
            c4 = correct(4)
            cpt += 1

        complet += "".join(list(map(str, ([c1, c2, c3, c4]+right))))
        cut += "".join(list(map(str, ([c1, c2, c3, c4]))))

        # print(f"Avant: {left+right}\nAprès: {[c1, c2, c3, c4]+right}")

        res5.clear()
        res6.clear()
        res7.clear()

        # print("")
    print(f"\nNombre d'erreurs trouvées: {cpt} \n")
    return {
        "complet": complet,
        "couper": cut
    }


def get_transcription(divided_into_8: list) -> str:
    """
    Transcribes a list of 8-digit binary numbers into ASCII characters.

    Parameters:
    - divided_into_8 (list): A list of 8-digit binary numbers to be transcribed.

    Returns:
    - result (str): A string containing the ASCII characters transcribed from the binary numbers.
    """
    result = ""
    result2 = ""
    for i in divided_into_8:
        result += get_ascii(i)

        """ print(
            f"Mot: {i} ==> {get_ascii(i)} ==> {get_ascii_from_table(i, ASCII.ASCII)}") """
    return result


def decode_vigenere(cipher_text: str, key: str) -> str:
    decalage = 65
    decoded = ""
    total = 26
    k_position = 0
    for i in cipher_text:
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


def get_vernam(cipher_text: str, key: str) -> str:
    decalage = 65
    result = ""
    for t, k in zip(cipher_text, key):
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


def decode_vernam(cipher_text: str, key: str) -> str:
    decalage = 65
    result = ""
    for t, k in zip(cipher_text, key):
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
    FILE_NAME = "lettre.txt"
    KEY = "python"
    SPLIT_IN_7 = []
    SPLIT_IN_8 = []
    FILE_CONTENT = readFile(FILE_NAME)
    CORRECTED_LETTER = "lettre_corrige.txt"
    CORRECTED_LETTER_WITHOUT_BIT = "lettre_corrige_sans_bit.txt"
    VIGENERE_TRANSCRIPTION = "vigenere_transcription.txt"
    ASCII_TRANSCRIPTION = "ascii_transcription.txt"
    VERNAM_CODAGE = "chiffre_de_vernam.txt"

    split_into(SPLIT_IN_7, FILE_CONTENT, 7)

    binary = calcul(SPLIT_IN_7)
    complet = binary.get("complet")
    cut = binary.get("couper")

    saveFile(CORRECTED_LETTER, complet)
    saveFile(CORRECTED_LETTER_WITHOUT_BIT, cut)
    print("Binaire corrigé !!! \n")

    fileContent = readFile(CORRECTED_LETTER_WITHOUT_BIT)
    split_into(SPLIT_IN_8, fileContent, 8)
    get_transcription(SPLIT_IN_8)

    ascii_transcription = get_transcription(SPLIT_IN_8)
    saveFile("ascii_transcription.txt", ascii_transcription)

    print("Transcription en ascii!!!\n")

    transcription_vigenere = decode_vigenere(ascii_transcription, KEY)
    saveFile(VIGENERE_TRANSCRIPTION, transcription_vigenere)

    print("Décodage de Vigenere!!!\n")

    key_length = len(transcription_vigenere)

    random_key = generate_random_key(key_length)
    saveFile("cle_aleatoire.txt", random_key)

    print(f"Génération d'une clé aléatoire de {key_length} caratères!!!\n")

    vernam = get_vernam(transcription_vigenere, random_key)
    saveFile(VERNAM_CODAGE, vernam)

    print("Codage de vernam appliquer !!!")


if __name__ == "__main__":
    main()
