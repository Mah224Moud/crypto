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


def split_into_7(storage: list, file_content: str):
    """
    Split the given file content into chunks of length 7 and append them to the storage list.

    Parameters:
    - storage (list): A list to store the split chunks.
    - file_content (str): The content of the file to be split.

    Returns:
    - None
    """
    for i in range(0, len(file_content), 7):
        storage.append(file_content[i:i+7])


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


def calcul(divided_into_7: list) -> str:
    """
    A function that takes a list of 7-digit binary numbers and processes each number to correct any errors in specific digits. It prints intermediate results and corrections made. The corrected numbers are then concatenated and returned as a single string.

    Parameters:
    - divided_into_7 (list): A list of 7-digit binary numbers to be processed.

    Returns:
    - result (str): A string containing the corrected binary numbers concatenated together.
    """
    result = ""
    for i in divided_into_7:
        print(f"Mot: {i}")
        c1 = int(i[0])
        c2 = int(i[1])
        c3 = int(i[2])
        c4 = int(i[3])
        c5 = int(i[4])
        c6 = int(i[5])
        c7 = int(i[6])

        left = left_and_right(i).get("left")
        right = left_and_right(i).get("right")

        print(f"gauche: {left}, droite: {right}")

        res5 = {"c5": sum_binary([c1, c2, c3])}
        res6 = {"c6": sum_binary([c1, c2, c4])}
        res7 = {"c7": sum_binary([c2, c3, c4])}

        res5["status"] = True if res5["c5"] == c5 else False
        res6["status"] = True if res6["c6"] == c6 else False
        res7["status"] = True if res7["c7"] == c7 else False

        print(res5, res6, res7)

        if not (res5["status"] and res6["status"]) and res7["status"]:
            print("C1 est erroné !!!")
            c1 = correct(c1)
        if not (res5["status"] and res6["status"] and res7["status"]):
            print("C2 est erroné !!!")
            c2 = correct(c2)
        if not (res5["status"] and res7["status"]) and res6["status"]:
            print("C3 est erroné !!!")
            c3 = correct(3)
        if not (res6["status"] and res7["status"]) and res5["status"]:
            print("C4 est erroné !!!")
            c4 = correct(4)

        result += "".join(list(map(str, [c1, c2, c3, c4])))

        print("final: ", left, [c1, c2, c3, c4])

        res5.clear()
        res6.clear()
        res7.clear()

        print("")
    return result


def main():
    FILE_NAME = "test.txt"
    SPLIT_IN_7 = []
    FILE_CONTENT = readFile(FILE_NAME)
    NEW_FILE_PATH = "resultat.txt"

    split_into_7(SPLIT_IN_7, FILE_CONTENT)
    newContent = calcul(SPLIT_IN_7)

    saveFile(NEW_FILE_PATH, newContent)


if __name__ == "__main__":
    main()
