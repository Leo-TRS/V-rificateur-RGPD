Vérificateur de conformité RGPD 
Projet Python - Léonard Torossian
Analyse un contrat PDF et détecte les clauses RGPD présentes et manquantes, avec un score de conformité final.

Installation - python -m pip install pdfplumber
Utilisation - Lancez le verificateur_RGPD.py puis collez le chemin de votre fichier PDF dans le terminal. 2 contrats exemples sont a dispositions pour tester le verificateur, l'un avec la totalité des clauses, l'autre avec des clauses manquantes. 
Résultat - Le programme affiche clause par clause ce qui est présent ou manquant, et calcule un score final (ex: 5/7).


!! Cet outil est un premier filtre automatique, non substituable à un audit juridique complet. 
