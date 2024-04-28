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
    """
    Saves the given content to a file with the specified filename.

    Parameters:
        filename (str): The name of the file to save the content to.
        content (str): The content to be saved to the file.

    Returns:
        str: The content that was saved to the file.
    """
    with open(filename, 'w') as f:
        f.write(content)


def is_aphabet(text: str) -> bool:
    """
    Check if the given text is a valid alphabet character.

    Parameters:
        text (str): The text to be checked.

    Returns:
        bool: True if the text is a valid alphabet character, False otherwise.
    """
    return "A" <= text.upper() <= "Z"


def split(content: str, howMany: int) -> list:
    """
    Splits a given string into substrings of a specified length.

    Parameters:
        content (str): The string to be split.
        howMany (int): The length of each substring.

    Returns:
        list: A list of substrings, each with length `howMany`.
    """
    content = content.replace("\n", "")
    result = []
    for i in range(0, len(content), howMany):
        result.append(content[i:i+howMany])
    return result


def get_left_and_right(binary: str):
    """
    Splits a given binary string into two parts, "left" and "right", by extracting the first 4 characters as the "left" and the rest as the "right".

    Parameters:
        binary (str): The binary string to be split into "left" and "right".

    Returns:
        dict: A dictionary containing the "left" and "right" parts of the binary string.
            - "left" (str): The first 4 characters of the input binary string.
            - "right" (str): The characters from the 4th position to the end of the input binary string.
    """
    return {
        "left": binary[0:4],
        "right": binary[4:]
    }


def sum_binaries(binaries: list) -> int:
    """
    Calculates the sum of a list of binary numbers and returns the result modulo 2.

    Parameters:
        binaries (list): A list of binary numbers.

    Returns:
        int: The sum of the binary numbers modulo 2.
    """
    return sum(binaries) % 2


def correct(binary: int) -> int:
    """
    A function that takes in a binary number and returns 0 if the number is equal to 1, otherwise it returns 1.

    Parameters:
        binary (int): The binary number to be checked.

    Returns:
        int: 0 if the binary number is equal to 1, otherwise 1.
    """
    return 0 if binary == 1 else 1


def get_hamming(binaries: list) -> dict:
    """
    Calculates the Hamming distance for a list of binary numbers.

    Parameters:
        binaries (list): A list of binary numbers.

    Returns:
        dict: A dictionary containing the corrected binary numbers with parity bits and the binary numbers without parity bits.
    """
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
        "no control bits": no_parity
    }


def get_ascii(binary_number: str) -> str:
    """
    Converts a binary number to its corresponding ASCII character.

    Parameters:
        binary_number (str): The binary number to be converted.

    Returns:
        str: The corresponding ASCII character.
    """
    bin_to_int = int(binary_number, 2)
    return chr(bin_to_int)


def get_transcription(binaries: list) -> str:
    """
    Transcribes a list of binary numbers into ASCII characters.

    Parameters:
    - binaries (list): A list of binary numbers to be transcribed.

    Returns:
    - result (str): A string containing the ASCII characters transcribed from the binary numbers.
    """
    result = ""
    for i in binaries:
        result += get_ascii(i)

        """ print(
            f"Mot: {i} ==> {get_ascii(i)} ==> {get_ascii_from_table(i, ASCII.ASCII)}") """
    return result


def decode_vigenere(text: str, key: str) -> str:
    """
    Decodes a text using the Vigenère cipher algorithm.

    Parameters:
        text (str): The text to be decoded.
        key (str): The decryption key.

    Returns:
        str: The decoded text.
    """
    decalage = 65
    decoded = ""
    total = 26
    k_position = 0
    for i in text:
        if (k_position >= len(key)):
            k_position = 0
        if is_aphabet(i):
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
    """
    Generates a random key of a specified length.

    Parameters:
        lenght (int): The length of the random key to be generated.

    Returns:
        str: The randomly generated key.
    """
    random_key = ""
    letters = "".join(chr(i) for i in range(97, 123))
    random_key = "".join(rand.SystemRandom().choice(letters)
                         for _ in range(lenght))
    return random_key


def get_vernam(text: str, key: str) -> str:
    """
    Calculates the Vernam cipher for the given text and key.

    Parameters:
        text (str): The text to be encrypted.
        key (str): The key used for encryption.

    Returns:
        str: The encrypted text.
    """
    decalage = 65
    result = ""
    for t, k in zip(text, key):
        tval = ord(t.upper()) - decalage
        kval = ord(k.upper()) - decalage
        calcul = (tval + kval) % 26
        if is_aphabet(t):
            if t.isupper():
                result += chr(calcul + decalage).upper()
            else:
                result += chr(calcul + decalage).lower()
        else:
            result += t
    return result


def decode_vernam(text: str, key: str) -> str:
    """
    Decodes a text using the Vernam cipher algorithm for the given text and key.

    Parameters:
        text (str): The text to be encrypted.
        key (str): The key used for encryption.

    Returns:
        str: The decoded text.
    """
    decalage = 65
    result = ""
    for t, k in zip(text, key):
        tval = ord(t.upper()) - decalage
        kval = ord(k.upper()) - decalage

        calcul = (tval - kval) % 26
        if is_aphabet(t):
            if t.isupper():
                result += chr(calcul + decalage).upper()
            else:
                result += chr(calcul + decalage).lower()
        else:
            result += t
    return result


class Node:
    def __init__(self, frequency, character=None, left=None, right=None):
        """
        Initializes a new instance of the `Node` class.

        Args:
            frequency (int): The frequency of the node.
            character (Optional[str]): The character associated with the node. Defaults to None.
            left (Optional[Node]): The left child node. Defaults to None.
            right (Optional[Node]): The right child node. Defaults to None.
        """
        self.character = character
        self.frequency = frequency
        self.left = left
        self.right = right

    def __repr__(self):
        """
        Return a string representation of the Node object.

        Returns:
            str: A string representation of the Node object in the format "Node(character, frequency)".
        """
        return f"Node({self.character}, {self.frequency})"


def determines_frequencies(data: str) -> dict:
    """
    Determines the frequencies of each character in a given string.

    Parameters:
        data (str): The input string.

    Returns:
        dict: A dictionary where the keys are the characters in the string and the values are the frequencies of each character.
    """
    frequency = {}
    for i in data:
        frequency[i] = data.count(i)
    return frequency


def sort_by_frequency_asc(nodes: dict) -> None:
    """
    Sorts the nodes dictionary by frequency in ascending order.

    Parameters:
        nodes (dict): A dictionary containing nodes and their frequencies.

    Returns:
        None
    """
    return dict(sorted(nodes.items(), key=lambda i: i[1], reverse=False))


def build_tree(frequencies: dict) -> Node:
    """
    Builds a binary tree from a dictionary of character frequencies.

    Args:
        frequencies (dict): A dictionary where the keys are characters and the values are their corresponding frequencies.

    Returns:
        Node: The root node of the binary tree.

    Description:
        This function builds a binary tree from a dictionary of character frequencies. It creates a list of nodes, where each node represents a character and its frequency. The nodes are then sorted by frequency in ascending order and paired up to form parent nodes. This process continues until there is only one node left, which is the root node of the binary tree.

        The function uses the following steps:
        1. Iterate over the characters and frequencies in the input dictionary.
        2. Create a node for each character and add it to the list of nodes.
        3. While there are more than one node in the list, sort the nodes by frequency in ascending order.
        4. Pop the two nodes with the lowest frequencies from the list.
        5. Create a parent node with the sum of the frequencies of the two child nodes and the child nodes as left and right children.
        6. Add the parent node to the list of nodes.
        7. Repeat steps 3-6 until there is only one node left, which is the root node.
        """
    nodes = []
    for character, frequency in frequencies.items():
        nodes.append(Node(frequency, character))
    while len(nodes) > 1:
        nodes.sort(key=lambda node: node.frequency)
        left = nodes.pop(0)
        right = nodes.pop(0)
        parent = Node(frequency=left.frequency +
                      right.frequency, left=left, right=right)
        nodes.append(parent)
    return nodes[0]


def generate_code(node: Node, prefix: str = "") -> dict:
    """
    A recursive function that generates a dictionary of binary codes for characters based on a given binary tree node. 
    It traverses the binary tree starting from the given node and recursively generates the binary codes for each character. 
    If the node represents a character, it returns a dictionary with the character as the key and the binary code as the value. 
    If the node does not represent a character, it recursively calls itself on the left and right child nodes, adding "0" to the prefix when moving left and "1" when moving right, and combines the generated dictionaries. 
    Returns a dictionary where the keys are characters and the values are their corresponding binary codes.
    Args:
        node (Node): The current node in the binary tree.
        prefix (str): The binary code prefix for the current node. Defaults to an empty string.
    Returns:
        dict: A dictionary where the keys are characters and the values are their corresponding binary codes.
    """
    if node.character:
        return {node.character: prefix}
    else:
        return {**generate_code(node.left, prefix + "0"), **generate_code(node.right, prefix + "1")}


def huffman_compression(data: str, codes: dict):
    """
    Compresses the given data using Huffman coding.

    Args:
        data (str): The input string to be compressed.
        codes (dict): A dictionary mapping each character in the input string to its corresponding Huffman code.

    Returns:
        str: The compressed string obtained by concatenating the Huffman codes of each character in the input string.
    """
    result = ""
    for i in data:
        result += codes[i] + " "
    return result


def calculate_bits(original_text: str, frequencies: dict, codes: dict) -> dict:
    """
    Calculates the total number of bits required to encode the original text using the provided frequencies and codes.

    Parameters:
        original_text (str): The original text to be encoded.
        frequencies (dict): A dictionary containing the frequencies of each character in the text.
        codes (dict): A dictionary of binary codes for characters.

    Returns:
        dict: A dictionary containing the original number of bits, the total number of bits after encoding, and the percentage reduction in bits.
    """
    total = 0
    original = len(original_text) * 8
    for i in frequencies:
        total += frequencies.get(i) * len(codes.get(i))
    percentage = round(((original - total)/original) * 100, 2)
    return {
        "original": original,
        "after": total,
        "percentage": percentage
    }


def reverse_dict(original_codes: dict) -> dict:
    if len(set(original_codes.values())) != len(original_codes):
        raise ValueError(
            "Les valeurs doivent être uniques pour inverser le dictionnaire sans perte de données.")
    return {value: key for key, value in original_codes.items()}


def huffman_decompression(compression_binaries: str, codes: dict):
    compression = compression_binaries.split(" ")
    codes = reverse_dict(codes)
    result = ""
    for i in compression:
        if i in codes:
            result += codes[i]
    return result


def main():
    LETTER = "lettre.txt"
    CORRECTED = "lettre_corrigee.txt"
    NO_CONTROL = "lettre_sans_bit_controle.txt"
    TRANSCRIPTION = "transcription_alphanumerique.txt"
    KEY = "PYTHON"
    VIGENERE = "decodage_vigenere.txt"
    VERNAM = "encodage_vernam.txt"
    RAND_KEY = "cle_aleatoire.txt"
    HUFFMAN = "compression_huffman.txt"
    HUFFMAN_DECOMPRESSION = "decompression_huffman.txt"

    letter = readFile(LETTER)
    split_7 = split(letter, 7)

    hamming = get_hamming(split_7)
    corrected = hamming.get("corrected")
    saveFile(CORRECTED, corrected)
    print(f"Lettre corrigée est enregistrée dans: '{CORRECTED}'\n")

    no_control = hamming.get("no control bits")
    saveFile(NO_CONTROL, no_control)
    print(
        f"Lettre corrigée sans les bits de controle et enregistrée dans: '{NO_CONTROL}'\n")

    split_8 = split(no_control, 8)
    transcription = get_transcription(split_8)
    saveFile(TRANSCRIPTION, transcription)
    print(
        f"Transcription binaire en ASCII 8bits effectuée et enregistrée dans: '{TRANSCRIPTION}'\n")

    vigenere = decode_vigenere(transcription, KEY)
    saveFile(VIGENERE, vigenere)
    print(
        f"Decodage de Vigenere éffectué sur la transcription à l'aide de la clé '{KEY}' enregistré dans '{VIGENERE}'\n")

    randomKey = generate_random_key(len(vigenere))
    saveFile(RAND_KEY, randomKey)
    print("Génération de la clé aléatoire ...")
    print(
        f"Clé aléatoire de longueur {len(randomKey)} générée et enregistré dans '{RAND_KEY}' '\n")

    vernam = get_vernam(vigenere, randomKey)
    saveFile(VERNAM, vernam)
    print(
        f"Text encodé à nouveau via l'algorithme de Vernam et enregistré dans: '{VERNAM}'\n")

    freq = determines_frequencies(vernam)
    root = build_tree(freq)
    codes = generate_code(root)
    huffman = huffman_compression(vernam, codes)
    result = calculate_bits(vernam, freq, codes)

    saveFile(HUFFMAN, huffman)

    print(f"Compression de Huffman ...")

    print(
        f"Fréquences de chaque caractère:\n{sort_by_frequency_asc(freq)}\n")

    print(f"Racine de l'arbre de Huffman: {root}\n")
    print(f"Codes:\n{codes}\n")
    print(
        f"Après compression, nous obtenons donc {result.get('after')} bits au lieu de {result.get('original')} soit ({len(vernam)} caractères x 8 bits par caractère).")
    print(
        f"La compression a reduit la taille des données de {result.get('percentage')}%.\n")

    print(
        f"Resultat de la compression enregistré dans: '{HUFFMAN}'.\n")

    decompress = huffman_decompression(huffman, codes)
    saveFile(HUFFMAN_DECOMPRESSION, decompress)
    print("Décompression de Huffman ...")
    print(
        f"Resultat de la décompression enregistré dans: '{HUFFMAN_DECOMPRESSION}'.\n")


if __name__ == "__main__":
    main()
