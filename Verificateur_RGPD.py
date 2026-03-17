#Vérificateur de conformité RGPD - Léonard Torossian

#Il faut d'abord que le programme puisse lire les fichiers pdf, pour cela j'utilise la librairie pdfplumber qui permet d'extraire le texte des fichiers pdf
import pdfplumber

#Pour demander à l'utilisateur de déposer le lien du fichier dans le terminal plutot que de le coller dans le code
fichier_pdf = input("collez le chemin du fichier pdf ici")

with pdfplumber.open(fichier_pdf) as pdf:
    resultat = ""
    for page in pdf.pages:
        resultat += page .extract_text()

#Ensuite pour la verification je definis les termes à verifier et les regroupes dans un dictionnaire 
termes_RGPD = {
"Consentement explicite" : ["consentement", "consent", "donne son accord", "autorise"],
"Droit d'accès" : ["Droit d'accès", "droit d'acceder"],
"Droit à l'effacement" : ["effacement", "droit à l'oubli", "oubli"],
"Droit d'opposition" : ["opposition", "droit d'opposition"],
"Durée de conservation" :["conservation","durée"],
"Coordonnées DPO" : ["dpo", "délégué à la protection"],
"Transfert hors UE" : ["transfert" ,"hors UE", "États-Unis"],     
}

#La boucle va verifier si les mots clés sont présents et ajoute à une liste la clée du dictionnaire qui correspond, puis enfin print le score final clauses présentes/ total 
Clauses_RGPD_presentes = []

for exigence, mots_cles in termes_RGPD.items(): 
    if any(terme.lower() in resultat.lower() for terme in mots_cles):
        print(f"{exigence}: OK ")
        Clauses_RGPD_presentes.append(exigence)
    else: print (f"{exigence}: clause manquante ") 
print(f"les clauses RGPD présentes dans le document sont :{Clauses_RGPD_presentes}")
print (f"score RGPD = {len(Clauses_RGPD_presentes)}/{len(termes_RGPD)}")


