# LocatoGram
###### Dieko de Graaf, Julien Coudron, Didier Dirks
###### 11855185, 11892420, 11450916

---


## Photo Sharing Website
### Samenvatting
Het doel van onze website is om bezoekers van steden, zoals toeristen, te helpen met het vinden van populaire bezienswaardigheden. Het laat gebruikers foto's uit hun omgeving zien. Gebruikers kunnen dan die bepaalde foto's 'raten', door middel van een :thumbsdown: of een :thumbsup:. Op deze manier zijn de toeristen in staat de meest gelikete (en dus populairste) plekken te vinden en bezoeken. Gebruikers kunnen ook de andere gebruikers volgen om foto's van hen te zien, maar kunnen alleen maar foto's raten die in de omgeving van hun specifieke locatie genomen zijn. Deze website is uniek omdat het locatie aspect gebruikers alleen toestaat de foto's in de specifieke locatie te 'raten'. Hierdoor geven wij onze gebruikers de mogelijkheid om hun omgeving verder te verkennen.

---

### Features
-    Gebruikers kunnen publiekelijk foto’s posten met of zonder begeleidende tekst.

-    Alle gebruikers kunnen elkaar “volgen”. Hierna kunnen beide elkaar foto's bekijken.

-    Alle gebruikers kunnen gebruikers die zij volgen niet meer volgen.

-    Gebruikers kunnen foto's uit de omgeving waar zij zich bevinden bekijken en :two_hearts:.

-    Gebruikers kunnnen de locaties waar de foto is genomen bij het uploaden van een foto toevoegen. Dit geeft de mogelijkheid aan gebruikers om andere foto’s te bekijken die genomen zijn in de omgeving van de gebruiker.

-    Als gebruiker kan je trofeeën verzamelen als je  bepaalde scores behaalt.

-    Gebruikers kunnen alleen reageren op foto's met GIFjes. GIFjes worden ondersteund door de Giphy API.

-    Gebruikers kunnen hun eigen profiel bekijken met hun eigen foto's.



### Minimum Viable Product

-   [x] Gebruikers kunnen publiekelijk foto’s posten met of zonder begeleidende tekst.

-   [x] Alle gebruikers kunnen elkaar “volgen”. Hierna kunnen beide elkaar foto's bekijken.

-    Alle gebruikers kunnen gebruikers die zij volgen niet meer volgen.

-    Gebruikers kunnen foto's uit de omgeving waar zij zich bevinden bekijken en :two_hearts:.

-    Gebruikers kunnnen de locaties waar de foto is genomen bij het uploaden van een foto toevoegen. Dit geeft de mogelijkheid aan gebruikers om andere foto’s te bekijken die genomen zijn in de omgeving van de gebruiker.

-    Als gebruiker kan je trofeeën verzamelen als je  bepaalde scores behaalt.

-    Gebruikers kunnen alleen reageren op foto's met GIFjes. GIFjes worden ondersteund door de Giphy API.

-    Gebruikers kunnen hun eigen profiel bekijken met hun eigen foto's.

---

### Afhankelijkheden
#### Databronnen
Locatie verkrijgen door IP API.
http://ip-api.com/

Google maps API. Gebruiken om locatie bij foto toe te voegen.
https://developers.google.com/maps/

Giphy API voor het implementeren van GIFjes.
http://api.giphy.com/

SafyGiphy Python wrapper voor de Giphy API
https://github.com/StewPoll/safygiphy

Voorwaarde voor het correct functioneren van de website is het installeren van safygiphy.
Voer hiervoor het commando 'pip install safygiphy' uit.


#### Rolverdeling
-    Dieko: Heeft zich zoveel mogelijk beziggehouden met de locatie-functionaliteit en de Google API
-    Julien: Heeft het meerendeel van SQL queries geschreven en ervoor gezorgd dat de database goed functioneert.
-    Didier: Heeft zich met CSS en de layout/uiterlijk van de website beziggehouden, evenals de Giphy API en de model classes.

#### De Repo
In onze repo is naast de standaard application.py ook een helpers bestand te vinden. In dit helpers bestand staat een functie die de zogenaamde decorator '@login_required' bedient en een lookup() functie. Deze functie zoekt de bijbehorende locatie van een ip-adres. Daarnaast is een mapje 'upload' te vinden, hierin worden alle geuploade foto's bewaard. In het mapje 'static' staat het stylesheet bestand en in 'models' zijn de models bestanden en classes te vinden.

#### Moeilijkste Delen

Het implementeren van de gebruikerslocatie.
Het implementeren van de google kaart.
Het bijhouden van het aantal likes of dislikes in de database en deze weer ophalen uit de database.

---




