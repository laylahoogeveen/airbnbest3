# Review
## Review door Wouter, 17-12-19

## Algemeen

Hele nette code, ziet er strak en verzorgd uit. Ik heb hier heel weinig op aan te merken. Heel leuk ook trouwens de optie om aantekeningen te delen met andere gebruikers en dat zij die ook kunnen weigeren mocht het ongevraagd binnenkomen. Hieronder een paar kleine opmerkingen: meer heb ik niet kunnen vinden. 

## Opmerkingen

- __regel 185 in views.py:__  hier staat een if statement met verder geen elif of else of een andere regel code die uitgevoerd wordt als er niet wordt voldaan aan de if conditie, wat gebeurt er als request.method == GET? 

*Niks, dat klopt. share_notes heeft informatie nodig die uit een formulier komt. Ik had bij een get eigenlijk gewoon moeten verwijzen naar notes of iets dergelijks.*

- __regel 34 in account.py:__ misschien gebruiksvriendelijker om JavaScript te gebruiken. Zelfde geldt voor regel 38.

*Klopt, ik was dat nog van plan, maar dat ben ik eigenlijk vergeten. Ik wilde dit er sowieso wel inhouden, omdat je JavaScript kan uitschakelen. Hoe dan ook, JavaScript is nodig om mijn website optimaal (of überhaupt) te kunnen gebruiken.*

-  __regel 43 en 47 in account.py:__ dit zou ook gebruiksvriendeljker zijn om het met JavaScript te doen, alleen zou ik zelf niet weten hoe dat zou moeten

*Idem.*

- Waarom views.py en account.py in aparte files? 

*Voor overzicht.*

- Misschien dat ik me vergis maar het programma kan volgens mij nooit bij regel 80 in account.py terecht komen -> overbodig?

*Dit is wat je te zien krijgt als je dus niet post, maar get. Dan krijg je dus de normale pagina te zien. Pas als je post, dus je gebruikersnaam en wachtwoord invoert, verandert er wat. Je gaat door naar index, of je krijgt een foutmelding als je gebruikersinformatie niet klopt.*

- Models zien er ook prima uit verder

*Thanks bro!*

# Eigen algemene opmerkingen

- Ik zag pas na de deadline dat ik was vergeten aan te passen dat je meerdere aantekeningen tegelijkertijd kunt verwijderen. Dit is zonde, want ik had dezelfde code kunnen gebruiken die ik ook gebruik om meerdere woorden te selecteren om aantekeningen te maken.
- Ik wilde in eerste instantie dat je aantekeningen kon zien als je over een specifiek woord hoverde, maar eigenlijk vind ik dat juist onoverzichtelijk, vervelend en druk, dus alleen aantekeningen naast de tekst (als je dus op 'toon aantekeningen' hebt geklikt) voldoen prima.
- Het lukte niet om de Griekse teksten in de database te krijgen op de juiste manier. Ik heb hier ook best lang naar gekeken met een TA (Quinten) en hij kwam er ook niet uit. Het Grieks uit de teksten uit Perseus' database gebruikt een onbegrijpelijke encoding.
- In het algemeen had ik meer teksten willen hebben in de database. Ik heb er al best veel en daarom is bv. de pagina voor alle teksten erg langzaam. Ik wilde er toch niet veel verwijderen, omdat ik er redelijk lang over heb gedaan. De xml-files die ik heb gebruikt waren vaak inconsequent qua indeling. Daarom heb ik ook veel leuke teksten niet in mijn database.
- Aan mijn models had ik nog een soort tekst willen toevoegen. Ofwel proza, ofwel poëzie met het bijbehorende metrum. Dit zou makkelijker zijn om vorm te geven op de website, want nu heb ik handmatig aangepast in mijn HTML wanneer er na een couplet een witregel moet. Ik heb dit niet kunnen doen, omdat ik soms bv. in één keer 40 gedichten in mijn database zette, met gedichten die soms weer een ander metrum hadden.
- Ik had gewild dat bij lange teksten (zoals een willekeurig boek van Vergilius' Aeneis) de tekst geleidelijk werd geladen tijdens het scrollen. Naar de volgende pagina gaan voor meer tekst zou ook kunnen. Brian heeft zoiets gedaan in een college, maar het lukte mij niet.