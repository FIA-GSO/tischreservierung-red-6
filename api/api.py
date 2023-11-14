import flask
from flask import request   # wird benötigt, um die HTTP-Parameter abzufragen
from flask import jsonify   # übersetzt python-dicts in json


app = flask.Flask(__name__)
app.config["DEBUG"] = True  # Zeigt Fehlerinformationen im Browser, statt nur einer generischen Error-Message


@app.route('/', methods=['GET'])
def home():

    return flask.send_file('index.html')

@app.route('/freieTische', methods=['GET'])
def freie_tische():
    if 'zeitpunkt' in request.args:
        wunschzeitpunkt = str(request.args['zeitpunkt'])
    else:
        return "Error: bitte Zeipunkt angeben.", 400
    
    # TODO wunschzeitpunkt auf nächste halbe Stunde aufrunden (18:00 --> 18:30)
    # TODO SQLite Datenbank erzeugen (create_buchungssystem.sql) und einbinden
    # TODO Abfrage an SQLite Datenbank absetzen
    # TODO Ergebnis der Abfrage als JSON zurückgeben
    # TODO Überprüfen, ob Parameter dem Muster yyyy-mm-dd hh:mm entspricht
    
    
    return wunschzeitpunkt, 200
    

if __name__ == "__main__":
    app.run()
