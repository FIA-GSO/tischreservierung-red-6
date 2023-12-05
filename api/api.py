import flask
from flask import request  # wird benötigt, um die HTTP-Parameter abzufragen
from flask import jsonify # übersetzt python-dicts in json
import sqlite3
import random  # notwendig für das Erzeugen eines pins
import re  # notwendig für die Arbeit mit Regex


path_to_sqlite3_database = 'buchungssystem.sqlite'

def init_app(app):

    @app.route('/', methods=['GET'])
    def home():
        return "<h1>Tischreservierung</h1><br>Freie Tische anfragen: <a href='http://127.0.0.1:5000/api/v1/tische/frei?zeitpunkt=2022-02-02T18:15:00Z'>/api/v1/tische/frei?zeitpunkt=2022-02-02T18:15:00Z</href>"


    @app.route('/api/v1/tische/frei', methods=['GET'])
    def anfragen():
        """ Bsp. Aufruf http://127.0.0.1:5000/api/v1/tische/frei?zeitpunkt=2022-02-02T18:15:00Z """

        query_parameters = request.args
        zeitpunkt = query_parameters.get('zeitpunkt')
        if not zeitpunkt:  # true, falls kein Parameter angegeben wurde
            return "Kein Zeitpunkt angegeben", 400
        if validate_date_format(zeitpunkt) == False:
            return "Zeitformat fehlerhaft", 400
        zeitpunkt = round_time_to_half_hour(zeitpunkt)

        query = create_query_free_tables(zeitpunkt)
        conn = sqlite3.connect(path_to_sqlite3_database)
        conn.row_factory = dict_factory
        cur = conn.cursor()  # https://www.tutorialspoint.com/python_data_access/python_sqlite_cursor_object.htm
        results = cur.execute(query).fetchall()
        conn.close()
        return jsonify(results), 200

    def validate_date_format(dateTime: str):
        """Überprüft, ob ein DateTime-String einem bestimmten Muster entspricht."""
        # Regex-Muster: https://regex101.com/r/xz7hfg/3
        regPatternInternetTimeFormat = ("^[0-9]{4}-[0-1][0-9]-[0-3][0-9]T[0-2][0-9]:[0-5][0-9]:[0-5][0-9](.[0-9][0-9])?Z?")
        isInternetTimeFormat = re.search(regPatternInternetTimeFormat, dateTime)
        if isInternetTimeFormat:
            return True
        return False


    def round_time_to_half_hour(datetime: str):
        """ Verändert einen DateTime-String so, dass der Zeitpunkt zur halben Stunde beginnt. 2022-02-02T18:17:00 --> 2022-02-02T18:30:00 """
        # Regex-Muster: https://regex101.com/r/pQfJWb/1
        regPatternMinutes = "(:[0-5][0-9](:[0-5][0-9])?)"
        result = re.sub(regPatternMinutes, "):30:00", datetime)
        return result

    def create_query_free_tables(zeitpunkt):
        sqlite_timestamp = create_sqlite_timestamp(zeitpunkt)
        subquery = "SELECT tischnummer FROM reservierungen WHERE zeitpunkt LIKE '" + sqlite_timestamp + ("' AND storniert = 'False'")  # alle belegten Tische zum Zeitpunkt X "
        query = "SELECT tischnummer, anzahlPlaetze FROM tische WHERE tischnummer NOT IN (" + subquery + ");"
        return query


    def create_sqlite_timestamp(zeitpunkt):
        regPattern = "T"
        sqlite_timestamp = re.sub(regPattern, " ", zeitpunkt)
        regPattern = "Z"
        sqlite_timestamp = re.sub(regPattern, "", sqlite_timestamp)
        return sqlite_timestamp


    def dict_factory(cursor, row):
        """Formt die Ausgabe von SQLite in ein brauchbares Format um"""
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

def create_app():
    app = flask.Flask(__name__)
    app.config["DEBUG"] = True  # Zeigt Fehlerinformationen im Browser, statt nur einer generischen Error-Message
    init_app(app)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run()