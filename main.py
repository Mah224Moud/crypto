import ascii_table as ASCII


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


def get_ascii_from_table(binary_number: str, ascii_table: dict) -> str:
    """
    Returns the ASCII character corresponding to the given binary number.

    Parameters:
        binary_number (str): The binary number to be converted to an ASCII character.
        ascii_table (dict): A dictionary containing the ASCII table.

    Returns:
        str: The ASCII character corresponding to the given binary number.
    """
    bin_to_int = int(binary_number, 2)
    return ascii_table.get(str(bin_to_int))


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
    print("\nNombre d'erreurs trouvées: ", cpt)
    return {
        "complet": complet,
        "couper": cut
    }


def get_transcription(divided_into_8: list) -> dict:
    """
    Transcribes a list of 8-digit binary numbers into ASCII characters.

    Parameters:
    - divided_into_8 (list): A list of 8-digit binary numbers to be transcribed.

    Returns:
    - result (str): A string containing the ASCII characters transcribed from the binary numbers.
    """
    result1 = ""
    result2 = ""
    for i in divided_into_8:
        result1 += get_ascii(i)
        result2 += get_ascii_from_table(i, ASCII.ASCII)

        """ print(
            f"Mot: {i} ==> {get_ascii(i)} ==> {get_ascii_from_table(i, ASCII.ASCII)}") """
    return {
        "result1": result1,
        "result2": result2
    }


def main():
    FILE_NAME = "lettre.txt"
    SPLIT_IN_7 = []
    SPLIT_IN_8 = []
    FILE_CONTENT = readFile(FILE_NAME)
    CORRECTED_LETTER = "lettre_corrige.txt"
    CORRECTED_LETTER_WITHOUT_BIT = "lettre_corrige_sans_bit.txt"
    ASCII_TABLE = ASCII.ASCII

    split_into(SPLIT_IN_7, FILE_CONTENT, 7)

    binary = calcul(SPLIT_IN_7)
    complet = binary.get("complet")
    cut = binary.get("couper")

    saveFile(CORRECTED_LETTER, complet)
    saveFile(CORRECTED_LETTER_WITHOUT_BIT, cut)

    fileContent = readFile(CORRECTED_LETTER_WITHOUT_BIT)
    split_into(SPLIT_IN_8, fileContent, 8)
    get_transcription(SPLIT_IN_8)

    transcription = get_transcription(SPLIT_IN_8)
    ascii_builtin = transcription.get("result1")
    ascii_homemade = transcription.get("result2")

    saveFile("ascii_builtin.txt", ascii_builtin)
    saveFile("ascii_homemade.txt", ascii_homemade)


if __name__ == "__main__":
    main()
