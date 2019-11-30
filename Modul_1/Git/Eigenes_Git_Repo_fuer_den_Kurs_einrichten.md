# Ein Git-Repositorium für den Kurs erstellen

# Schritt 1 - Ordner und Dateien erstellen

Öffne die Git Bash und gehe in eine Ordner Deiner Wahl. Erstelle dort
einen neuen Ordner (ersetze "Konrad" mit Deinem Namen).

```
mkdir Zertifikatskurs_Data_Librarian_2019_Konrad
```

Wechsel in diesen Ordner

```
cd Zertifikatskurs_Data_Librarian_2019_Konrad
```

Erstelle mit [echo](http://linuxcommand.org/lc3_man_pages/echoh.html)
und dem ">"-Operator eine neue [Markdown](https://markdown.de/)-Datei
mit einer Überschrift.

```
echo "# Zertifikatskurs Data Librarian" > README.md
```

Erstelle einen Unterordner

```
mkdir Modul_1
```

Und erstelle in diesem Unterordner eine weitere Markdown-Datei mit
einer Überschrift.

```
echo "Modul 1" > Modul_1/README.md
```

## Schritt 2 - Lokales Git-Repositorium erstellen und Datein hinzufügen

Initialisiere ein Git-Repositorium.

```
git init 
```

Für die beiden neuen Dateien in die Staging-Area

```
git add README.md Modul_1/README.md
```

und commite die Änderungen in das Repositorium.

```
git commit -m "Initial commit"
```

## Schritt 3 - Repositorium auf GitHub erstellen und mit lokalem verknüpfen

Erstelle auf GitHub ein neues Repositorium. Dazu gehe auf die Seite
https://github.com/new und erstelle ein gleichnamiges
Repositorium. Wähle wenn Du möchtest die Option "Private". Zum
Verknüpfen gehe in die Bash und dort in den Ordner deines lokalen
Repositorium und gebe dort die Befehle ein, die Dir GitHub unter
... or push an existing repository from the command line"
empfielt. Z.b. (Achtung - Nutzernamen anpassen!)

```
git remote add origin git@github.com:konrad/Zertifikatskurs_Data_Librarian_2019_Konrad.git
```
und

```
git push -u origin master
```

Füge mich dann als Collaborator auf GitHub hinzu: "Settings" >
"Collaborators" und dort meinen Nutzernamen "konrad") eingeben.

Ein paar Wort zu den privaten Repositorien auf GitHub. GitHub ist ein
Unternehmen (das von Microsoft gekauft wurde) und möchte natürlich
Geld einnehmen. Es gibt einem die Möglichkeit offene Repositorien mit
vielen Mitwirkenden zu hosten. Wenn man ein privates Repositorium
erstellt, kannst man zwei weitere Leute hinzufügen. Möchte man private
Repositorien mit mehreren Mitarbeitenden haben, muss man zahlen.  Für
unsere Zwecke sollte das ersteinmal reichen. Mehr zu den Preisen von
GitHub und den damit verknüpften Features findest Du
[hier](https://github.com/pricing). Für die Hochschulausbildung hat
GitHub aber ein Programm namens [GitHub
Education](https://education.github.com/). Hier kann man sich unter
Angabe einer Email-Adresse einer Hochschule die Vorzüge einer
Pro-Accounts für 2 Jahre geben lassen
([Link](https://education.github.com/discount)). Das würde ich
empfehlen zu tun.

Wer dazu nicht die Möglchkeit hat, kann mich (Konrad)
kontaktieren. Wir können das Repositorium unter meinen Account laufen
lassen (man kann [Repositoriuen
transferieren](https://help.github.com/en/github/administering-a-repository/transferring-a-repository)).


## Schritt 4 - Fügt Eure Dateien hinzu

Fügt Eure Dateien (Jupyter Notebook, Skripte) zu dem Repositorium
lokal hinzu und pusht die Änderungen zu GitHub.
