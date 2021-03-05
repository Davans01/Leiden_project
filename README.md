# Leiden

## Installatie

### Software

Download en installeer Node.js op <https://nodejs.org/en/>.

Zorg ervoor dat "tools for native modules" geïnstalleerd zijn, dat wordt gevraagd tijdens de installatie.

Dit download en installeert dan ook Python 3.9 voor jou.

Download en installeer PostgreSQL met <https://www.enterprisedb.com/downloads/postgres-postgresql-downloads>.

### Database

Wanneer geïnstalleerd is, open pgAdmin 4. Dit opent een browser tab, geef pgAdmin hetzelfde wachtwoord als dat je bij de installatie van postgres gebruikte.

Maak een nieuwe gebruiker voor het project met rechtermuisknop op "Login/Group Roles". Geef het een naam, een wachtwoord onder definition, en geef het een login onder privileges.

Maak een nieuwe database voor het project met rechtermuisknop op "Databases". Houd de eigenaar op postgres. Onder de security tab geef je de nieuwe gebruiker alle privileges (zonder grant option).

### Project opzet

Clone dit project via git: `git clone https://github.com/Davans01/Leiden_project.git`

Kopieër `example.env` en noem het `.env`

Open de map die git maakt met een je code editor, start in je editor een terminal.

Creëer een Python omgeving: `python -m venv venv`

Start de omgeving: `. .\venv\Scripts\Activate.ps1`

Sta lokale PowerShell scripts toe met `Set-ExecutionPolicy RemoteSigned` als dat nodig is.

Installeer Python dependencies: `pip install -Ur requirements.txt`

Installeer yarn: `npm i -g yarn`

Installeer JavaScript dependencies: `yarn install`

Open `.env` die je eerder gemaakt hebt, en zet `DATABASE_URI` op `postgres://gebuiker:wachtwoord@localhost:5432/database`.

Zet de database op met `flask db upgrade`.

Start een terminal en run `yarn serve` om de frontend op te starten, start nog een terminal en run `flask run` om de backend op te starten.

De backend runt op `http://localhost:5000`, en de frontend op `http://localhost:8080/`.
