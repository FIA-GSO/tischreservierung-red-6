Versionierung:
Es sollten verschiedene Versionen der API geben, wenn änderungen gemacht werden.
Die verschiedenen Versionen der API, sollten dabei mit /v1, v2... am Anfang der API aufgerufen werden können.
Da es sein könnte das eine neuere Version nicht mehr mit den Clients funktioniert. 
Die Version sollte dabei mit einer Versionnummer angegeben werden. 
Quelle: https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/

Diese wird in folgendem Format angegeben: 
Hauptversionsnummer (Große Änderungen).Nebenversionsnummer(Funktionale Erweiterungen).Revisionsnummer(Fehlerbehebungen)
z.B.: 2.3.6 --> api/v2/...
Quelle: https://de.wikipedia.org/wiki/Versionsnummer

Namenskonventionen:
Wenn in der API eine Eintät aufgerufen wird, wird diese als Nomen in der Mehrzahl 
und nur mit Kleinbuchstaben angegeben. 
Zusätzlich werden einzelne Worte durch ein Minus (kein Unterstrich, für bessere Lesbarkeit) getrennt.
Quelle: https://jax.de/blog/software-architecture-design/restful-apis-richtig-gemacht/

Außerdem ist die Konsitente Bennenung sehr wichtig, mit einem slash wird die Hirarchie 
zwischen den Ressourcen angegeben. 
Am Ende sollte jedoch nicht noch ein zusätzlicher shlash notwendig sein, 
um auf eine Ressource der API zugreifen zu können. 
Es ist zudem Best pratice, keine Dateiformate mit in der URL anzugeben.
Quelle: https://restfulapi.net/resource-naming/

Korrekter Einsatz der HTTP-Methoden:
Die GET-Methode wird genutzt, um eine Ressource aus der API abzurufen.
Die POST-Methode wird genutzt, um eine neue Ressource bzw. Sub-Ressource zu erstellen.
Die PUT-Methode und PATCH-Methode, sollte man verwenden um existierende Ressourcen aktualisieren zu können.
Und die DELETE-Methode sollte verwenden werden, um ein löschen von Ressourcen zu ermöglichen.

Zudem sollte jede Request eine sinvolle Antwort zurückerhalten:
Für Fehlerhafte Anfragen sollte der HTTP Code 400 als Antwort gesendet werden.
Bei Fehlern von Serverseite aus, sollte der HTTP Code 500 als Antwort gesendet werden.
Wenn die Anfrage ohne Probleme beantwortet werden konnte, sollte der HTTP Code 200 gesendet werden.
Quelle: https://swagger.io/resources/articles/best-practices-in-api-design/
