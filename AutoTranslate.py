import re
import os
from deep_translator import GoogleTranslator

# Chemin du répertoire contenant les fichiers
directory = 'C:\\Users\\Felzow47\\Desktop\\extract'

# Chemin du sous-dossier où stocker les fichiers traduits
translated_directory = os.path.join(directory, 'translated_files')

# Créer le sous-dossier s'il n'existe pas déjà
if not os.path.exists(translated_directory):
    os.makedirs(translated_directory)
    print(f"[DEBUG] Dossier de traduction créé : {translated_directory}")
else:
    print(f"[DEBUG] Dossier de traduction déjà existant : {translated_directory}")

# Liste des extensions de fichiers à ne pas traduire
file_extensions = ['.ogg', '.mp3', '.wav', '.jpg', '.png', '.webm', '.ttf']

# Fonction pour déterminer si un texte doit être traduit
def is_translatable(text):
    text = text.strip()
    
    # Vérifier si le texte se termine par une extension de fichier connue
    if any(text.lower().endswith(ext) for ext in file_extensions):
        return False
    
    # Si le texte est alphanumérique sans espaces (probablement un identifiant), ne pas traduire
    if re.match(r'^[\w\d_]+$', text):
        return False
    
    # Si le texte contient des balises et des retours à la ligne, le considérer comme traduisible
    if re.search(r'\{[^}]+\}', text) or '\n' in text:
        return True
    
    # Autoriser les textes contenant des retours à la ligne et autres caractères spéciaux
    if len(text) > 0:
        return True
    # Vérifier si le texte contient des caractères de chemin
    if '/' in text or '\\' in text:
        return False
            
    # Sinon, le texte est probablement non traduisible
    return False

# Fonction pour traduire uniquement le texte entre guillemets
def translate_text_in_code(file_path, source_lang='en', target_lang='fr'):
    print(f"[DEBUG] Ouverture du fichier : {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Expression régulière pour capturer le texte entre guillemets
    pattern = r'\"(.*?)(?<!\\)\"'
    matches = re.findall(pattern, content)

    # Initialisation du traducteur
    translator = GoogleTranslator(source=source_lang, target=target_lang)

    # Traduire chaque texte individuellement
    for i, match in enumerate(matches, start=1):
        if is_translatable(match):
            try:
                translated = translator.translate(match)
                print(f"[DEBUG] Texte avant traduction {i}/{len(matches)} : {match}")  # Affiche le texte trouvé avant la traduction
                content = content.replace(f'"{match}"', f'"{translated}"')
                print(f"[DEBUG] Texte traduit {i}/{len(matches)} : {translated}")  # Affiche le texte traduit
               # print(f"[DEBUG] Avancement : {i}/{len(matches)} ({(i / len(matches)) * 100:.2f}%)")  # Affiche l'avancement
            except Exception as e:
                print(f"[DEBUG] Exception lors de la traduction du texte '{match}': {e}")
        else:
            print(f"[DEBUG] Texte non traduisible {i}/{len(matches)} : {match}")  # Affiche un message pour les textes non traduisibles

    # Écrire le contenu traduit dans le sous-dossier 'translated_files'
    translated_file = os.path.join(translated_directory, f'translated_{os.path.basename(file_path)}')
    print(f"[DEBUG] Écriture du fichier traduit : {translated_file}")
    with open(translated_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[DEBUG] Fichier traduit et sauvegardé : {translated_file}\n")

# Parcourir tous les fichiers .rpy dans le répertoire
print(f"[DEBUG] Recherche de fichiers .rpy dans le répertoire : {directory}")
for filename in os.listdir(directory):
    if filename.endswith('.rpy'):
        file_path = os.path.join(directory, filename)
        print(f"[DEBUG] Fichier trouvé : {file_path}")
        translate_text_in_code(file_path)
    else:
        print(f"[DEBUG] Fichier ignoré (non .rpy) : {filename}")
