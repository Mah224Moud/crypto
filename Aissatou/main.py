import random
contenu = ""
# Ouvrir le fichier en mode lecture
with open('lettre.txt', 'r') as fichier:
    # Lire tout le contenu du fichier
    contenu = fichier.read()

# Diviser le contenu en groupes de 7 caractères
groups = [contenu[i:i+7] for i in range(0, len(contenu), 7)]
print(f"découper en 7:", groups)

# Traitement de chaque groupe pour effe#ctuer les calculs et corrections décrits
corrected_groups = []
errors = []

for group in groups:
    # Ignorer les groupes qui n'ont pas exactement 7 caractères
    if len(group) != 7:
        continue

    # Convertir chaque caractère du groupe en entier
    bits = list(map(int, group))
    gauche = bits[:4]
    droite = bits[4:]
    print(f"gauche:", gauche)
    print(f"droite:", droite)
    # Calculer les vérifications de parité
    resc5 = (droite[0] == (gauche[0] + gauche[1] + gauche[2]) %
             2) if len(droite) > 0 else None
    resc6 = (droite[1] == (gauche[0] + gauche[1] + gauche[3]) %
             2) if len(droite) > 1 else None
    resc7 = (droite[2] == (gauche[1] + gauche[2] + gauche[3]) %
             2) if len(droite) > 2 else None

    # Vérifier les erreurs et les corriger
    if resc7 and not resc5 and not resc6:
        print(f"c1 Eroné:")
        # Erreur dans le bit c1
        gauche[0] = 1 - gauche[0]
        print(f"c1:", gauche[0])
        errors.append(f"Erreur corrigée dans c1 du groupe {group}")
    elif not resc7 and resc5 and resc6:
        # Erreur dans le bit c7
        droite[2] = 1 - droite[2]
        errors.append(f"Erreur corrigée dans c7 du groupe {group}")
    elif not resc7 and not resc5 and resc6:
        # Erreur dans le bit c3
        gauche[2] = 1 - gauche[2]
        errors.append(f"Erreur corrigée dans c3 du groupe {group}")
    elif not resc7 and resc5 and not resc6:
        # Erreur dans le bit c4
        gauche[3] = 1 - gauche[3]
        errors.append(f"Erreur corrigée dans c4 du groupe {group}")

    # Recompiler le groupe corrigé
    corrected_group = ''.join(map(str, gauche + droite))
    corrected_groups.append(corrected_group)

# Afficher les groupes corrigés et les erreurs détectées
# Afficher les 10 premiers groupes corrigés
print("Groupes corrigés :", corrected_groups[:10])
# Afficher les 10 premières erreurs corrigées
print("Erreurs trouvées et corrigées :", errors[:10])


# Ouvrir un fichier en mode écriture
with open("resultat_correction.txt", "w") as fichier:
    # Écrire les groupes corrigés dans le fichier
   # fichier.write("Groupes corrigés :\n")
    for groupe in corrected_groups:
        fichier.write(groupe)

    # Ajouter une ligne vide entre les groupes corrigés et les erreurs
    fichier.write("\n")

    # Écrire les erreurs détectées et corrigées dans le fichier
   # fichier.write("Erreurs trouvées et corrigées :\n")
    # for erreur in errors:
    # fichier.write(erreur + "\n")

    print("Résultat de la correction enregistré dans 'resultat_correction.txt'")


# Ouvrir le fichier pour lire son contenu
with open('resultat_correction.txt', 'r') as fichier:
    # Lire tout le contenu du fichier
    contenur = fichier.read()

# Définir la liste résultante pour stocker les parties gauches avec la méthode de Hamming
gauche_hamming = []

# Diviser le contenu en groupes de 7 caractères
groups = [contenur[i:i+7] for i in range(0, len(contenur), 7)]

# Parcourir chaque groupe de la liste groups
for group in groups:
    # Ignorer les groupes qui ne sont pas exactement de 7 caractères
    if len(group) != 7:
        continue

    # Extraire la partie gauche
    gauche = group[:4]

    # Ajouter la partie gauche à la liste gauche_hamming
    gauche_hamming.append(gauche)

gauche_hamming.append("".join(map(str, gauche)))

# Afficher la liste résultante
print("Liste des parties gauches avec la méthode de Hamming:", gauche_hamming)

# Ouvrir un fichier en mode écriture
with open("resultat_gauche.txt", "w") as fichier:
    # Écrire les groupes corrigés dans le fichier
   # fichier.write("Groupes corrigés :\n")
    for groupe in gauche_hamming:
        fichier.write(groupe)
# Diviser le contenu en groupes de 8 caractères
with open('resultat_gauche.txt', 'r') as fichier:
    # Lire tout le contenu du fichier
    contenur = fichier.read()

groups8 = [contenur[i:i+8] for i in range(0, len(contenur), 8)]

# Écriture des groupes dans le fichier
with open('resultat_division8.txt', "w") as f:
    for groupe in groups8:
        f.write(groupe + "\n")

print(f"division par 8", groups8)


# Ouvrir le fichier en mode lecture
with open("resultat_division8.txt", "r") as fichier:
    # Lire les lignes du fichier
    lignes = fichier.readlines()

    # Convertir chaque valeur binaire en ASCII
    correspondances_ascii = []
    for ligne in lignes:
        valeur_binaire = ligne.strip()
        valeur_entiere = int(valeur_binaire, 2)
        # Vérifier si la valeur entière correspond à un caractère ASCII valide
        if 0 <= valeur_entiere < 128:
            correspondances_ascii.append(chr(valeur_entiere))
        else:
            print("Erreur : La valeur binaire", valeur_binaire,
                  "ne correspond pas à un caractère ASCII valide.")

# Afficher les correspondances
for correspondance in correspondances_ascii:
    print(correspondance)


# Écriture des groupes dans le fichier
with open('correspondances_ascii.txt', "w") as t:
    for groupe in correspondances_ascii:
        t.write(groupe)

print(f"correspondances_ascii", correspondances_ascii)


def decrypt_vigenere(ciphertext, key):
    # Cette fonction aide à convertir une lettre en sa position numérique (A=0, B=1, ..., Z=25)
    def letter_to_number(letter):
        return ord(letter.upper()) - ord('A')

    # Cette fonction convertit un numéro en lettre, en supposant que 0=A, 1=B, ..., 25=Z
    def number_to_letter(number):
        return chr(number + ord('A'))

    plaintext = []
    key_index = 0  # Index pour suivre la position dans la clé

    for char in ciphertext:
        if char.isalpha():  # On traite seulement les lettres alphabétiques
            # Calcul du décalage
            c_num = letter_to_number(char)
            k_num = letter_to_number(key[key_index % len(key)])
            new_num = (c_num - k_num) % 26
            plaintext.append(number_to_letter(new_num))

            key_index += 1  # Avancer dans la clé seulement si on a traité une lettre
        else:
            plaintext.append(char)  # Garder les autres caractères tels quels

    return ''.join(plaintext)


# Exemple d'utilisation
with open('correspondances_ascii.txt', 'r') as file:
    ciphertext = file.read()

# ciphertext="AC"
key = "PYTHON"
decrypted_message = decrypt_vigenere(ciphertext, key)
print("Texte déchiffré :", decrypted_message)


# Écriture des groupes dans le fichier
with open('Texte déchiffré.txt', "w") as t:
    for groupe in decrypted_message:
        t.write(groupe)


def chiffrement_vernam(message, cle):
    """
    Chiffre le message en utilisant la méthode de chiffrement de Vernam.

    Args:
        message (str): Le message à chiffrer.
        cle (str): La clé aléatoire de même longueur que le message.

    Returns:
        str: Le message chiffré.
    """
    message_chiffre = ""

    for i, lettre in enumerate(message):
        # Convertir la lettre du message en nombre (0-25)
        num_message = ord(lettre.upper()) - ord('A')
        # Convertir la lettre de la clé en nombre (0-25)
        num_cle = ord(cle[i]) - ord('A')
        # Calculer la lettre chiffrée
        num_chiffre = (num_message + num_cle) % 26
        # Convertir le nombre chiffré en lettre
        lettre_chiffree = chr(num_chiffre + ord('A'))
        # Ajouter la lettre chiffrée au message chiffré
        message_chiffre += lettre_chiffree

    return message_chiffre


# Message à chiffrer
with open('Texte déchiffré.txt', 'r') as fichier:
    message = fichier.read()

# message = "LE 02 MARS 1952, A MURRAY HILL, A QUI DE DROIT, CHER ALAN TURING, JE VOUS FAIS PARVENIR LE DEBUT DE MON DISCOURS CREATIVE THINKING QUE JE VAIS PRONONCER A BELL LABS DANS QUELQUESJOURS, CAR JE MENTIONNE VOTRE NOM ET SOUHAITE AVOIR VOTRE ACCORD. UN TRES PETIT POURCENTAGE DE LA POPULATION PRODUIT LA PLUS GRANDE PROPORTION DES IDEES IMPORTANTES. CELA S'APPARENTE A UNE IDEE PRESENTEE PAR UN MATHEMATICIEN ANGLAIS, TURING, SELON LAQUELLE LE CERVEAU HUMAIN EST UN PEU COMME UN MORCEAU D'URANIUM. LE CERVEAU HUMAIN, S'IL EST AU DESSUS DU SEUIL CRITIQUE ET QUE VOUS Y TIREZ UN NEUTRON, D'AUTRES SERAIENT PRODUITS EN PLUS PAR L'IMPACT. CELA CONDUIT A UNE EMISSION EXTREMEMENT EXPLOSIVE, A L'AUGMENTATION DE LA QUANTIT D'URANIUM. TURING DIT QUE C'EST QUELQUE CHOSE COMME LES IDEES DANS LE CERVEAU HUMAIN. IL Y A DES GENS QUI, SI VOUS LEUR ENVOYEZ UNE IDEE DANS LE CERVEAU, VOUS EN OBTIENDREZ UNE DEMI-IDEE. IL Y A D'AUTRES PERSONNES QUI SONT AU-DELA DE CE POINT OU ELLES PRODUISENT DEUX IDEES POUR CHAQUE IDEE ENVOYEE. CE SONT LES PERSONNES AU-DELA DU SOMMET DE LA COURBE. JE NE VEUX PAS PARATRE EGOCENTRIQUE, JE NE PENSE PAS ETRE AU-DELA DE LA COURBE ET JE NE CONNAIS PERSONNE QUI LE SOIT. MAIS JE CONNAIS DES GENS QUI L'ETAIENT. JE PENSE, PAR EXEMPLE, QUE TOUT LE MONDE SERA D'ACCORD POUR DIRE QU'ISAAC NEWTON SERAIT BIEN AU SOMMET DE CETTE COURBE. QUAND ON PENSE QU'A L'AGE DE 25 ANS, IL AVAIT PRODUIT SUFFISAMMENT DE SCIENCES, DE PHYSIQUE ET DE MATHEMATIQUES POUR RENDRE 10 OU 20 HOMMES CELEBRES - IL A PRODUIT LE THEOREME BINOMIAL, LE CALCUL DIFFERENTIEL ET INTEGRAL, LES LOIS DE LA GRAVITATION, LES LOIS DU MOUVEMENT, LA DECOMPOSITION DE LA LUMIERE BLANCHE, ET AINSI DE SUITE. MAINTENANT, QU'EST-CE QUI PERMET D'ACCEDER A CETTE PARTIE DE LA COURBE ? QUELLES SONT LES EXIGENCES DE BASE ? JE PENSE QUE NOUS POURRIONS DEFINIR TROIS CHOSES QUI SONT RELATIVEMENT NECESSAIRES POUR LA RECHERCHE SCIENTIFIQUE OU POUR TOUTE SORTE D'INVENTIONS, DE MATHEMATIQUES, DE PHYSIQUE OU AUTRE. JE NE PENSE PAS QU'UNE PERSONNE PUISSE SE PASSER DE L'UNE DE CES TROIS CHOSES.LE PREMIER EST EVIDENT : LA FORMATION ET L'EXPERIENCE. VOUS N'ATTENDEZ PAS  DE NOS JOURS D'UN AVOCAT, AUSSI BRILLANT SOIT-IL, QU'IL VOUS DONNE UNE NOUVELLE THEORIE DE LA PHYSIQUE, DES MATHEMATIQUES OU DE L'INGENIERIE.LE DEUXIEME ELEMENT EST UNE CERTAINE DOSE D'INTELLIGENCE OU DE TALENT. EN D'AUTRES TERMES, IL FAUT AVOIR UN QI ASSEZ ELEVE POUR FAIRE UN BON TRAVAIL DE RECHERCHE. JE NE PENSE PAS QU'IL EXISTE UN BON INGENIEUR OU UN BON SCIENTIFIQUE QUI PUISSE SE DEBROUILLER AVEC UN QI DE 100, QUI EST LA MOYENNE DES ETRES HUMAINS. EN D'AUTRES TERMES, IL DOIT AVOIR UN QI SUPERIEUR A CELA. TOUTES LES PERSONNES PRESENTES DANS CETTE SALLE ONT UN QI NETTEMENT SUPERIEUR. ON POURRAIT DIRE QUE C'EST UNE QUESTION D'ENVIRONNEMENT ; L'INTELLIGENCE EST UNE QUESTION D'HEREDITE.JE NE PENSE PAS QUE CES DEUX ELEMENTS SOIENT SUFFISANTS. JE PENSE QU'IL Y A UNE TROISIEME COMPOSANTE ICI, UNE TROISIEME COMPOSANTE QUI EST CELLE QUI FAIT UN EINSTEIN OU UN ISAAC NEWTON. FAUTE D'UN MEILLEUR MOT, NOUS L'APPELLERONS MOTIVATION. EN D'AUTRES TERMES, VOUS DEVEZ AVOIR UNE SORTE D'IMPULSION, UNE SORTE DE DESIR DE TROUVER LA REPONSE, UN DESIR DE DECOUVRIR CE QUI FAIT FONCTIONNER LES CHOSES. SI VOUS N'AVEZ PAS CELA, VOUS AUREZ BEAU AVOIR TOUTE LA FORMATION ET TOUTE L'INTELLIGENCE DU MONDE, VOUS N'AUREZ PAS DE QUESTIONS ET VOUS NE TROUVEREZ PAS DE REPONSES. CLAUDE SHANNON"
# Générer une clé aléatoire de même longueur que le message
masque = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
                 for _ in range(len(message)))

message_chiffre = chiffrement_vernam(message, masque)
print("Message chiffré :", message_chiffre)
print("Clé aléatoire :", masque)

# Écriture des résultats dans un fichier
with open('resultat_chiffrement.txt', 'w') as fichier:
    fichier.write("Message chiffré : " + message_chiffre + "\n")
    fichier.write("Clé aléatoire : " + masque)


def read_text_file(resultat_chiffrement):
    with open("resultat_chiffrement.txt", 'r') as file:
        return file.read()


'''
# Exemple d'utilisation
filename = 'resultat_chiffrement.txt'
text = read_text_file(filename)
compressed_text, huffman_codes = compress(text)

def compress(text):
    # Compter la fréquence des caractères dans le texte
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    # Créer une file de priorité pour les caractères en fonction de leur fréquence
    priority_queue = [(count, [char, ""]) for char, count in frequency.items()]
    heapq.heapify(priority_queue)
    
    # Construire l'arbre de Huffman
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        for pair in left[1:]:
            pair[1] = '0' + pair[1]
        for pair in right[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(priority_queue, (left[0] + right[0], left[1] + right[1]))
    
    # Créer un dictionnaire pour stocker les codes de Huffman
    huffman_codes = {char: code for char, code in priority_queue[0][1:]}
    
    # Compresser le texte en utilisant les codes de Huffman
    compressed_text = ''.join(huffman_codes[char] for char in text)
    
    return compressed_text, huffman_codes

def decompress(compressed_text, huffman_codes):
    # Inverser le dictionnaire des codes de Huffman
    reversed_codes = {code: char for char, code in huffman_codes.items()}
    
    # Décompresser le texte en utilisant les codes de Huffman inversés
    decompressed_text = ''
    code = ''
    for bit in compressed_text:
        code += bit
        if code in reversed_codes:
            decompressed_text += reversed_codes[code]
            code = ''
    
    return decompressed_text

# Exemple d'utilisation
text = "Ceci est un exemple de texte à compresser en utilisant l'algorithme de Huffman."
compressed_text, huffman_codes = compress(text)
print("Texte compressé:", compressed_text)
print("Codes de Huffman:", huffman_codes)

decompressed_text = decompress(compressed_text, huffman_codes)
print("Texte décompressé:", decompressed_text)


'''


''''

contenu = ""
# Ouvrir le fichier en mode lecture
with open('t.txt', 'r') as fichier:
    # Lire tout le contenu du fichier
    contenu = fichier.read()

# Diviser en groupes de 7 caractères
groupes = [contenu[i:i+7] for i in range(0, len(contenu), 7)]



# Afficher les groupes
print("Groupes de 7 caractères :", groupes)

# Afficher toutes les parties du fichier après le découpage
for groupe in groupes:
    print("Partie du fichier :", groupe)

## Parcourir chaque groupe
for i in groupes:
    prin# Path to the uploaded file
file_path = '/mnt/data/Letrre.txt'

# Reading the content of the file
with open(file_path, 'r') as file:
    content = file.read()t(f"Voici le decoupage de 7: {i}")

    # Vérifier si le groupe a au moins 4 caractères
    if len(i) < 4:
        print("La partie gauche est trop courte")
        continue  # Passer à la prochaine itération si la partie gauche est trop courte
    
    # Extraire les 4 premiers caractères pour la partie gauche
    gauche = i[:4]
    droite = i[4:]
# Extraire le reste pour la partie droite

print(f"gauche:", gauche)
print(f"droite:", droite)with open('t.txt', 'r') as fichier:
    # Lire tout le contenu du fichierlear
    contenu = fichier.read()

# Diviser le contenu en groupes de 7 caractères # Co# Path to the uploaded file
file_path = '/mnt/data/Letrre.txt'
with open('t.txt', 'r') as fichier:
    # Lire tout le contenu du fichierlear
    contenu = fichier.read()

# Diviser le contenu en groupes de 7 caractères # Co# Path to the uploaded file
file_path = '/mnt/data/Letrre.txt'

# Reading the content of the file
with open(file_path, 'r') as file:
    content = file.read()rriger l'erreur en inversant le bit
    c3 = 1 - c3  # Inversioncontinue
n inversant le bit
    c3 = 1 - c3  # Inversioncontinuewith open('t.txt', 'r') as fichier:
    # Lire tout le contenu du fichierlear
    contenu = fichier.read()

# Diviser le contenu en groupes de 7 caractères # Co# Path to the uploaded file
file_path = '/mnt/data/Letrre.txt'

# Reading the content of the file
with open(file_path, 'r') as file:with open('t.txt', 'r') as fichier:
    # Lire tout le contenu du fichierlear
    contenu = fichier.read()

# Diviser le contenu en groupes de 7 caractères # Co# Path to the uploaded file
file_path = '/mnt/data/Letrre.txt'

# Reading the content of the file
with open(file_path, 'r') as file:
    content = file.read()rriger l'erreur en inversant le bit
    c3 = 1 - c3  # Inversioncontinue

# Découper chaque groupe en deux parties
gauche = groupe[:4]with open('t.txt', 'r') as fichier:
    # Lire tout le contenu du fichierlear
    contenu = fichier.read()

# Diviser le contenu en groupes de 7 caractères # Co# Path to the uploaded file
file_path = '/mnt/data/Letrre.txt'

# Reading the content of the file
with open(file_path, 'r') as file:
    content = file.read()rriger l'erreur en inversant le bit
    c3 = 1 - c3  # Inversioncontinue

    # Corriger l'erreur en inversant le bit
    c1 = 1 - c1  # Inversion

if not resc7 and not resc5 and not resc6:
    print("C1 ERRONE")with open('t.txt', 'r') as fichier:
    # Lire tout le contenu du fichierlear
    contenu = fichier.read()

# Diviser le contenu en groupes de 7 caractères # Co# Path to the uploaded file
file_path = '/mnt/data/Letrre.txt'

# Reading the content of the file
with open(file_path, 'r') as file:
    content = file.read()rriger l'erreur en inversant le bit
    c3 = 1 - c3  # Inversioncontinue
 inversant le bitwith open('t.txt', 'r') as fichier:
    # Lire tout le contenu du fichierlear
    contenu = fichier.read()

# Diviser le contenu en groupes de 7 caractères # Co# Path to the uploaded file
file_path = '/mnt/data/Letrre.txt'

# Reading the content of the file
with open(file_path, 'r') as file:
    content = file.read()rriger l'erreur en invwith open('t.txt', 'r') as fichier:
    # Lire tout le contenu du fichierlear
    contenu = fichier.read()

# Diviser le contenu en groupes de 7 caractères # Co# Path to the uploaded file
file_path = '/mnt/data/Letrre.txt'

# Reading the content of the file
with open(file_path, 'r') as file:
    content = file.read()rriger l'erreur en inversant le bit
    c3 = 1 - c3  # Inversioncontinue

    content = file.read()rriger l'erreur en inversant le bit
    c3 = 1 - c3  # Inversion
with open(file_path, 'r') as file:
    content = file.read()rriger l'erreur en inversant le bit
    c3 = 1 - c3  # Inversion # Co# Path to the uploaded file
file_path = '/mnt/data/Letrre.txt'
 # Co# Path to the uploaded file
file_path = '/mnt/data/Letrre.txt'with open('t.txt', 'r') as fichier:
    # Lire tout le contenu du fichierlear
    contenu = fichier.read()

# Diviser le contenu en groupes de 7 caractères # Co# Path to the uploaded file
file_path = '/mnt/data/Letrre.txt'

# Reading the content of the file
with open(file_path, 'r') as file:
    content = file.read()rriger l'erreur en inversant le bit
    c3 = 1 - c3  # Inversioncontinue

with open(file_path, 'r') as file:
    content = file.read()rriger l'erreur en inversant le bit
    c3 = 1 - c3  # Inversion
# Reading the content of the filewith open('t.txt', 'r') as fichier:
    # Lire tout le contenu du fichierlear
    contenu = fichier.read()

# Diviser le contenu en groupes de 7 caractères # Co# Path to the uploaded file
file_path = '/mnt/data/Letrre.txt'

# Reading the content of the file
with open(file_path, 'r') as file:
    content = file.read()rriger l'erreur en inversant le bit
    c3 = 1 - c3  # Inversioncontinue
uploaded file
file_path = '/mnt/data/Letrre.txt'

# Reading the content of the file
with open(file_path, 'r') as file:
    content = file.read()rriger l'erreur en inversant le bit
    c3 = 1 - c3  # Inversion

# Afficher les bits corrigés
print(f"c1: {c1}, c2: {c2}, c3: {c3}, c4: {c4}, c5: {c5}, c6: {c6}, c7: {c7}")

# Ouvrir le fichier en mode écriture
with open('resultats_corriges.txt', 'w') as fichier_resultats:
    # Écrire les résultats corrigés dans le fichier # Co# Path to the uploaded file
file_path = '/mnt/data/Letrre.txt'

# Reading the content of the file
with open(file_path, 'r') as file:
    content = file.read()rriger l'erreur en inversant le bit
    c3 = 1 - c3  # Inversion
    '''
''''
with open('t.txt', 'r') as fichier:
    # Lire tout le contenu du fichierlear
    contenu = fichier.read()

# Diviser le contenu en groupes de 7 caractères # Co# Path to the uploaded file
file_path = '/mnt/data/Letrre.txt'

# Reading the content of the file
with open(file_path, 'r') as file:
    content = file.read()rriger l'erreur en inversant le bit
    c3 = 1 - c3  # Inversioncontinue

    # Convertir chaque caractère du groupe en entier
    bits = list(map(int, group))
    gauche = bits[:4]
    droite = bits[4:]
    print(f"gauche:",gauche)
    print(f"droute:",droite)

    # Calculer les vérifications de parité
    resc5 = (droite[0] == (gauche[0] + gauche[1] + gauche[2]) % 2) if len(droite) > 0 else None
    resc6 = (droite[1] == (gauche[0] + gauche[1] + gauche[3]) % 2) if len(droite) > 1 else None
    resc7 = (droite[2] == (gauche[1] + gauche[2] + gauche[3]) % 2) if len(droite) > 2 else None

'''
''''
   # Vérification et correction des erreurs sur les bits de gauche avec Hamming
if resc7 and not resc5 and not resc6:
    print(f" Erreur dans le bit c1 bit de parité:",gauche[0])
    gauche[0] = 1 - gauche[0]  # c1 est le premier bit de gauche
    errors.append(f"Erreur corrigée dans c1 du groupe {group}")
elif not resc7 and resc5 and resc6:
    # Erreur dans le bit c2 (bit de parité)
    gauche[1] = 1 - gauche[1]  # c2 est le deuxième bit de gauche
    errors.append(f"Erreur corrigée dans c2 du groupe {group}")
elif not resc7 and not resc5 and resc6:
    # Erreur dans le bit c4 (bit de données)
    gauche[3] = 1 - gauche[3]  # c4 est le quatrième bit de gauche
    errors.append(f"Erreur corrigée dans c4 du groupe {group}")
elif not resc7 and resc5 and not resc6:
    # Erreur dans le bit c3 (bit de données)
    gauche[2] = 1 - gauche[2]  # c3 est le troisième bit de gauche
    errors.append(f"Erreur corrigée dans c3 du groupe {group}")
    print(f" la liste corrigée: c1: {gauche[0]}, c2: {gauche[1]}, c3: {gauche[2]}, c4: {gauche[3]}, c5: {droite[0]}, c6: {droite[1]}, c7: {droite[2]}\n")
'''
'''
# Vérification et correction des erreurs sur les bits de gauche avec Hamming
# Vérifier chaque bit de parité et afficher les valeurs
print("Valeurs de parité calculées :", resc5, resc6, resc7)

if resc7 and not resc5 and not resc6:
    print("Erreur détectée dans c1 (bit de parité)")
    gauche[0] = 1 - gauche[0]
    print("Correction de c1, nouveau bit:", gauche[0])
    errors.append(f"Erreur corrigée dans c1 du groupe {group}")
elif not resc7 and resc5 and resc6:
    print("Erreur détectée dans c2 (bit de parité)")
    gauche[1] = 1 - gauche[1]
    print("Correction de c2, nouveau bit:", gauche[1])
    errors.append(f"Erreur corrigée dans c2 du groupe {group}")
elif not resc7 and not resc5 and resc6:
    print("Erreur détectée dans c4 (bit de données)")
    gauche[3] = 1 - gauche[3]
    print("Correction de c4, nouveau bit:", gauche[3])
    errors.append(f"Erreur corrigée dans c4 du groupe {group}")
elif not resc7 and resc5 and not resc6:
    print("Erreur détectée dans c3 (bit de données)")
    gauche[2] = 1 - gauche[2]
    print("Correction de c3, nouveau bit:", gauche[2])
    errors.append(f"Erreur corrigée dans c3 du groupe {group}")

# Recompiler le groupe corrigé
'''
'''
corrected_group = ''.join(map(str, gauche + droite))
corrected_groups.append(corrected_group) # Co# Path to the uploaded file
file_path = '/mnt/data/Letrre.txt'

# Reading the content of the file
with open(file_path, 'r') as file:
    content = file.read()rriger l'erreur en inversant le bit
    c3 = 1 - c3  # Inversion # Co# Path to the uploaded file
file_path = '/mnt/data/Letrre.txt'

# Reading the content of the file
with open(file_path, 'r') as file:
    content = file.read()rriger l'erreur en inversant le bit
    c3 = 1 - c3  # Inversion # Co# Path to the uploaded file
file_path = '/mnt/data/Letrre.txt'

# Reading the content of the file
with open(file_path, 'r') as file:
    content = file.read()rriger l'erreur en inversant le bit
    c3 = 1 - c3  # Inversion # Co# Path to the uploaded file
file_path = '/mnt/data/Letrre.txt'

# Reading the content of the file
with open(file_path, 'r') as file:with open('t.txt', 'r') as fichier:
    # Lire tout le contenu du fichierlear
    contenu = fichier.read()

# Diviser le contenu en groupes de 7 caractères # Co# Path to the uploaded file
file_path = '/mnt/data/Letrre.txt'

# Reading the content of the file
with open(file_path, 'r') as file:
    content = file.read()rriger l'erreur en inversant le bit
    c3 = 1 - c3  # Inversioncontinue
with open('t.txt', 'r') as fichier:
    # Lire tout le contenu du fichierlear
    contenu = fichier.read()

# Diviser le contenu en groupes de 7 caractères # Co# Path to the uploaded file
file_path = '/mnt/data/Letrre.txt'

# Reading the content of the file
with open(file_path, 'r') as file:
    content = file.read()rriger l'erreur en inversant le bit
    c3 = 1 - c3  # Inversioncontinue

    content = file.read()rriger l'erreur en inversanwith open('t.txt', 'r') as fichier:
    # Lire tout le contenu du fichierlear
    contenu = fichier.read()

# Diviser le contenu en groupes de 7 caractères # Co# Path to the uploaded file
file_path = '/mnt/data/Letrre.txt'

# Reading the content of the file
with open(file_path, 'r') as file:
    content = file.read()rriger l'erreur en inversanwith open('t.txt', 'r') as fichier:
    # Lire tout le contenu du fichierlear
    contenu = fichier.read()

# Diviser le contenu en groupes de 7 caractères # Co# Path to the uploaded file
file_path = '/mnt/data/Letrre.txt'

# Reading the content of the file
with open(file_path, 'r') as file:
    content = file.read()rriger l'erreur en inversant le bit
    c3 = 1 - c3  # Inversioncontinue
t le bit
    c3 = 1 - c3  # Inversioncontinue
t le bit
    c3 = 1 - c3  # Inversion # Co# Path to the uploadwith open('t.txt', 'r') as fichier:
    # Lire tout le contenu du fichierlear
    contenu = fichier.read()

# Diviser le contenu en groupes de 7 caractères # Co# Path to the uploaded file
file_path = '/mnt/data/Letrre.txt'
with open('t.txt', 'r') as fichier:
    # Lire tout le contenu du fichierlear
    contenu = fichier.read()

# Diviser le contenu en groupes de 7 caractères # Co# Path to the uploaded file
file_path = '/mnt/data/Letrre.txt'

# Reading the content of the file
with open(file_path, 'r') as file:
    content = file.read()rriger l'erreur en inversantwith open('t.txt', 'r') as fichier:
    # Lire tout le contenu du fichierlear
    contenu = fichier.read()

# Diviser le contenu en groupes de 7 caractères # Co# Path to the uploaded file
file_path = '/mnt/data/Letrre.txt'

# Reading the content of the file
with open(file_path, 'r') as file:
    content = file.read()rriger l'erreur en inversant le bit
    c3 = 1 - c3  # Inversioncontinue
 le bit
    c3 = 1 - c3  # Inversioncontinue

# Reading the content of the file
with open(file_path, 'r') as file:
    content = file.read()rriger l'erreur en inversant le bit
    c3 = 1 - c3  # Inversioncontinue
ed file
file_path = '/mnt/data/Letrre.txt'

# Reading the content of the file
with open(file_path, 'r') as file:
    content = file.read()rriger l'erreur en inversant le bit
    c3 = 1 - c3  # Inversion # Co# Path to the uploaded file
file_path = '/mnt/data/Letrre.txt'

# Reading the content of the file
with open(file_path, 'r') as file:
    content = file.read()rriger l'erreur en inversant le bit
    c3 = 1 - c3  # Inversion
 '''
'''with open('t.txt', 'r') as fichier:
    # Lire tout le contenu du fichierlear
    contenu = fichier.read()

# Diviser le contenu en groupes de 7 caractères # Co# Path to the uploaded file
file_path = '/mnt/data/Letrre.txt'

# Reading the content of the file
with open(file_path, 'r') as file:
    content = file.read()rriger l'erreur en inversant le bit
    c3 = 1 - c3  # Inversioncontinue
ur en inversant le bit
    c3 = 1 - c3  # Inversioncontinue
'''
