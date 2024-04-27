""" from collections import defaultdict, Counter
import heapq
w = [("w", 1), ("i", 3), ("k", 1), ("p", 1), ("e", 1), ("d", 1), ("a", 1)] """


# trier = dict(sorted(w.items(), key=lambda i: i[1], reverse=False))
""" trier = sorted(w, key=lambda x: x[1], reverse=False)
print(trier)

petit = trier[0][1]
same = False

final = []

for i, element in enumerate(trier, 0):
    if (element[1] == petit):
        same = True
        print(element, element[1])
 """

""" def huffman_encoding(data):
    if not data:
        return "", None

    # Calcul des fréquences des caractères
    frequency = Counter(data)
    # Création d'une file de priorité avec ces fréquences
    heap = [[weight, [symbol, ""]] for symbol, weight in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        # Fusion des deux noeuds les moins fréquents
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '1' + pair[1]
        for pair in hi[1:]:
            pair[1] = '0' + pair[1]
        # Ajouter le nouveau noeud à la file
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    # Génération des codes Huffman à partir de l'arbre
    codes = dict(heapq.heappop(heap)[1:])
    # Encodage du texte
    encoded_text = ''.join(codes[char] for char in data)

    return encoded_text, codes


def huffman_decoding(encoded_text, codes):
    reverse_codes = {v: k for k, v in codes.items()}
    current_code = ""
    decoded_text = ""

    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_codes:
            decoded_text += reverse_codes[current_code]
            current_code = ""

    return decoded_text


# Test de l'algorithme
data = "wikipedia"
encoded_data, codes = huffman_encoding(data)
print("Encoded data:", encoded_data, codes)
decoded_data = huffman_decoding(encoded_data, codes)
print("Decoded data:", decoded_data)
 """


class Node:
    def __init__(self, frequency, character=None, left=None, right=None):
        self.character = character
        self.frequency = frequency
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node({self.character}, {self.frequency})"


def sort_by_frequency_asc(nodes: dict) -> None:
    return dict(sorted(nodes.items(), key=lambda i: i[1], reverse=False))


def determines_frequencies(data: str) -> dict:
    frequency = {}
    for i in data:
        frequency[i] = data.count(i)
    return frequency


def build_tree(frequencies: dict) -> Node:
    nodes = []
    for character, frequency in frequencies.items():
        nodes.append(Node(frequency, character))
    while len(nodes) > 1:
        nodes.sort(key=lambda node: node.frequency)
        print(nodes)
        left = nodes.pop(0)
        right = nodes.pop(0)
        parent = Node(frequency=left.frequency +
                      right.frequency, left=left, right=right)
        nodes.append(parent)
    return nodes[0]


def generate_code(node: Node, prefix: str = "") -> dict:
    if node.character:
        return {node.character: prefix}
    else:
        return {**generate_code(node.left, prefix + "0"), **generate_code(node.right, prefix + "1")}


def encode(data: str, codes: dict):
    result = ""
    for i in data:
        result += codes[i]
    return result


def calculate_bits(original_text: str, frequencies: dict, codes: dict) -> dict:
    total = 0
    original = len(original_text) * 8
    for i in frequencies:
        total += frequencies.get(i) * len(codes.get(i))
    percentage = round(((original - total)/original) * 100, 2)
    return {
        "original": original,
        "after": total,
        "pourcentage": percentage
    }


text = "Wikipedia"
freq = determines_frequencies(text)
racine = build_tree(freq)
codes = generate_code(racine)
res = encode("Wikipedia", codes)

print(sort_by_frequency_asc(freq))
print(racine)
print(codes)
print(res)
print(calculate_bits(text, freq, codes))
