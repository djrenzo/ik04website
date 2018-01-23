# Project voorstel, Groep IK04
###### Dieko de Graaf, Julien Coudron, Didier Dirks
###### 11855185, 11892420, 11450916

---


## Photo Sharing Website
### Samenvatting
Het doel van onze website is om bezoekers van steden, zoals toeristen, te helpen met het vinden van populaire bezienswaardigheden. Het laat gebruikers foto's uit hun omgeving zien. Gebruikers kunnen dan die bepaalde foto's 'raten', door middel van een :x: of een :heart:. Foto's met het hoogste aantal :heart: komen op een scoreboard, specifiek voor elke locatie. Op deze manier zijn de toeristen in staat de meest gelikete (en dus populairste) plekken te vinden en bezoeken. Gebruikers kunnen ook de andere gebruikers volgen om foto's van hen te zien, maar kunnen alleen maar foto's raten die in de omgeving van hun specifieke locatie genomen zijn. Deze website is uniek omdat het locatie aspect gebruikers alleen toestaat de foto's in de specifieke locatie te 'raten'. Hierdoor geven wij onze gebruikers de mogelijkheid om hun omgeving verder te verkennen.

---


### Schetsen

1.	Ontvangstpagina voor inloggen en registreren met informatie van webapplicatie.
2.  Ingelogde gebruikers home scherm. Ook de mogelijkheid tot uploaden en eigen profiel bekijken. Deze foto's kunnen ook gesorteerd worden op aantal behaalde likes, tijd van posten of afstand. Je krijgt de populairste foto's uit de omgeving te zien.
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

### Features
-    Gebruikers kunnen publiekelijk foto’s posten met of zonder begeleidende tekst. 

-    Alle gebruikers kunnen elkaar “volgen” als ze zich beiden in dezelfde omgeving bevinden. Hierna kunnen beide elkaar foto's bekijken en :two_hearts:. 
 
-    Gebruikers kunnen in plaats van een eigen foto ook een gif zoeken uit een online API zoals die van http://api.giphy.com. Op deze manier zijn gebruikers in staat 

-    Locaties bij geüploade foto’s toevoegen. Dit geeft de mogelijkheid aan gebruikers om andere foto’s te bekijken die genomen zijn in de omgeving van de gebruiker. 

-    Als gebruiker kan je alleen foto’s uit de omgeving beoordelen of als je iemand volgt. Eventueel door naar links/rechts te swipen.

-    Als gebruiker kan je trofeeën verzamelen als jouw foto’s bepaalde scores behalen (dit gaat per omgeving). Met alle scores wordt per omgeving een scorebord weergegeven. Hierop zijn de populairste foto’s te zien.

-    Gebruikers kunnen de afstand van zichzelf tot de foto's zien, en eventueel een routebeschrijving van hun huidige locatie naar de locatie van de foto.

- Gebruikers kunnen alleen reageren op foto's met GIFjes. GIFjes worden ondersteund door de Giphy API.
---

### Minimum Viable Product
-    [x] Gebruikers kunnen publiekelijk foto’s posten met of zonder begeleidende tekst. 

-    [x] Alle gebruikers kunnen elkaar “volgen” en zo de foto’s bekijken en :two_hearts:. 
 
-    [x] Gebruikers kunnen in plaats van een eigen foto ook een gif zoeken uit een online API zoals die van http://api.giphy.com

-    [x] Locaties bij geüploade foto’s toevoegen. Dit geeft de mogelijkheid aan gebruikers om andere foto’s te bekijken die genomen zijn in de omgeving van de gebruiker. Locatie verkrijgen door geolocation API van html5 te gebruiken

-    [x] Als gebruiker kan je alleen foto’s uit de omgeving beoordelen. Eventueel door naar links/rechts te swipen.

-    [ ] Extra: Gebruikers kunnen alleen reageren op foto's met GIFjes. GIFjes worden ondersteund door de Giphy API.

-    [ ] Extra: Als gebruiker kan je trofeeën verzamelen als jouw foto’s bepaalde scores behalen (dit gaat per omgeving). Met alle scores wordt per omgeving een scorebord weergegeven. Hierop zijn de populairste foto’s te zien.

-    [ ] Extra: Gebruikers kunnen de afstand van zichzelf tot de foto's zien, en eventueel een routebeschrijving naar de locatie van de foto

---

### Afhankelijkheden
#### Databronnen
Locatie verkrijgen door HTML5 Geolocation.
https://www.w3schools.com/html/html5_geolocation.asp

Google maps API. Gebruiken om afstand te bepalen en coördinaten omzetten naar locatie.
https://developers.google.com/maps/

Giphy API voor het implementeren van GIFjes.
http://api.giphy.com/

#### Externe Componenten

Wij hebben nog geen externe componenten 

#### Concurrerend Bestaand
Zelfde idee als applicatie variant:
http://www.piximity.me/
#### Moeilijkste Delen

Het implementeren van de gebruikerslocatie.

---

### Sanity Check

De sanity check is uitgevoerd.




