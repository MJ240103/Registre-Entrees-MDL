from flask import Flask, request, render_template
app = Flask(__name__)


@app.route("/", methods=['GET'])
def accueil():
    nom = request.args.get("nom")
    prenom = request.args.get("prenom")
    classe = request.args.get("classe")
    inout = request.args.get("inout")
    print(nom, prenom, classe, inout)

    import datetime
    jour = datetime.date.today()
    heure = datetime.datetime.now().time()
    print(jour, heure)

    import csv
    if nom != "" or prenom !="" or classe!="" or inout != "":
        with open('tab_utilisateurs.csv', mode='a') as csv_file:
            fieldnames = ['nom', 'prenom', 'classe', 'date', 'heure_arrivee', 'inout']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            #writer.writeheader()
            writer.writerow({'nom': nom, 'prenom': prenom, 'classe': classe, 'date' : jour, 'heure_arrivee' : heure, 'inout' : inout})
        
            csv_file.close()
    
    return render_template('form.html')

app.run(host='0.0.0.0', port=8080)
