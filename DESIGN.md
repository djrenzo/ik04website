# Technisch ontwerp, Groep IK04
###### Dieko de Graaf, Julien Coudron, Didier Dirks
###### 11855185, 11892420, 11450916

---


### Controllers: 
**Gebruiker registreert** 
```
@app.route(“/register”, methods=["GET", "POST"])
def register():
```
**Gebruiker logt in**

``` 
@app.route(“/login”, methods=["GET", "POST"])
def login():
```
**Krijg informatie over de website te zien**
```
@app.route(“/about”, methods=["GET", "POST"]) 
def about():
```
**Gebuiker krijgt home pagina te zien**
```
@app.route(“/home”)
login required
def home():
```
**Gebruiker verandert password**
```
@app.route(“/change_password”, methods=["GET", "POST"])
login required
def change_password():
```
**Gebruiker logt uit**

```
@app.route(“/log_out”)
login required
def log_out():
```
**Gebruiker krijgt een profiel te zien**

```
@app.route(“/profile”) 
login required
def profiel():
```
**Gebruiker uploadt een foto**

```
@app.route(“/upload”, methods=["GET", "POST"])
login required
def upload():
```
**Gebruiker krijgt zijn eigen award te zien**

```
@app.route(“/award”)
login required
def award():
```
**Gebruiker krijgt de foto's van de mensen die hij volgt te zien**

```
@app.route(“/photo_friends”)
login required
def photo_friends():
```
**Gebruiker krijgt foto’s uit omgeving te zien die kan sorteren op score, afstand of tijd**
```
@app.route(“/photo_surrounding”)
login required
def photo_surrounding():
```
**Gebruiker ziet aangeklikte foto en kan reactie plaatsen of/en raten**
```
@app.route(“/see_photo_surrounding”, methods=["GET", "POST"])
login required
def see_photo():
```
**Gebruiker ziet aangeklikte foto en kan reactie plaatsen**
```
@app.route(“/see_photo_friends”, methods=["GET", "POST"])
login required
def see_photo():
```

**Gebruiker kan zoeken naar gebruikers (optioneel)**
```
@app.route(“/search”, methods=["GET", "POST"])
login required
def search():
```

# Views:

1.	Ontvangstpagina voor inloggen en registreren met informatie van webapplicatie.
2.	Ingelogde gebruikers home scherm. Ook de mogelijkheid tot uploaden en eigen profiel bekijken. Deze foto's kunnen ook gesorteerd worden op aantal behaalde likes, tijd van posten of afstand. Je krijgt de populairste foto's uit de omgeving te zien.
3.	Pagina met foto’s van mensen die je volgt. (gesoorteerd op tijd van posten)
4.	Pagina waar een foto met bijschrift bekeken kan worden en waar een ingelogde gebruiker een reactie kan geven op de foto. Bij elke foto staat ook de afstand tot de locatie van de foto en jou huidige locatie.
5.	Profielpagina van een gebruiker met de door de gebruiker geposte foto’s. In een apart tablad wordt de trofeeën voortgang weergegeven. Hier ook de mogelijkheid tot het profiel te volgen. 
6.	Inlogpagina voor een bezoekers van deze website.
7.	Schematische weergave van de links op de website.
---
1. <a href="https://ibb.co/mscu6m"><img src="https://thumb.ibb.co/mscu6m/pagina1.jpg" alt="pagina1" border="0"></a>
2. <a href="https://ibb.co/nE2rK6"><img src="https://thumb.ibb.co/nE2rK6/pagina2.jpg" alt="pagina2" border="0"></a>
3. <a href="https://ibb.co/gSSu6m"><img src="https://thumb.ibb.co/gSSu6m/pagina3.png" alt="pagina3" border="0"></a>
4. <a href="https://ibb.co/moFQCR"><img src="https://thumb.ibb.co/moFQCR/pagina4.jpg" alt="pagina4" border="0"></a>
5. <a href="https://ibb.co/ivwRK6"><img src="https://thumb.ibb.co/ivwRK6/pagina5.jpg" alt="pagina5" border="0"></a>
6. <a href="http://ibb.co/gQF1wm"><img src="http://thumb.ibb.co/gQF1wm/IMG_3003.jpg" alt="IMG_3003" border="0"></a>
7. <a href="http://ibb.co/m2TzhR"><img src="http://thumb.ibb.co/m2TzhR/IMG_3002.jpg" alt="IMG_3002" border="0"></a>


---

# Models:
**Laat foutmelding zien**
```
apology():
```
**Geeft de latitude en longitude van gebruiker via HTML5 Geolocation**

```
get_location():
```
**Geeft de afstand van huidige locatie tot locatie van een foto**

```
get_distance(): 
```
**Haalt foto uit database door te zoeken naar foto id**

```
get_picture():
```
**Een gebruiker volgen, deze gebruiker wordt toegevoegd aan de database met mensen die je volgt**
```
follow():
```
**Zoek naar personen op basis van de gebruikersnaam**
```
search():
```

---

# Plugins and frameworks:
Bootstrap - http://getbootstrap.com
