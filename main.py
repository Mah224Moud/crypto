
def readFile(filename: str) -> str:
    content = ""
    with open(filename, 'r') as f:
        content = f.read()

    return content


LETTRE = "test.txt"
DECOUPAGE_EN_7 = []
tesst = readFile(LETTRE)


def decoupage(stockage: list, mots: str):
    for i in range(0, len(tesst), 7):
        stockage.append(tesst[i:i+7])


decoupage(DECOUPAGE_EN_7, LETTRE)


for i in DECOUPAGE_EN_7:
    c1 = int(i[0])
    c2 = int(i[0])
    c3 = int(i[0])
    c4 = int(i[0])
    c5 = int(i[0])
    c6 = int(i[0])
    c7 = int(i[0])
    """ gauche = []
    droite = []
    for index, charactere in enumerate(i[0:7], 0):
        if (index <= 3):
            gauche.append(int(charactere))
        else:
            droite.append(int(charactere))
    c5 =  """
