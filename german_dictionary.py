
# German letters
Au = "\u00c4"   # A umlaut
au = "\u00e4"   # a umlaut
Ea = "\u00c9"   # E acute
ea = "\u00e9"   # e acute
Ou = "\u00d6"   # O umlaut
ou = "\u00f6"   # o umlaut
Uu = "\u00dc"   # U umlaut
uu = "\u00fc"   # u umlaut
Ss = "\u00df"   # s ligature

# some helpful constants
ENG_IDX=0
GER_IDX=1

duolingo_hobbies = {
    'name' : 'Hobbies',
    'words' : [
        (('to swim'), ('schwimmen')),
        (('sometimes'), ('manchmal')),
        (('to cook'), ('kochen')),
        (('the mother'), ('die Mutter')),
        (('the father'), ('der Vater')),
        (('never'), ('nie')),
        (('the chess'), ('das Schach')),
        (('to paint'), ('malen')),
        (('the piano'), ('das Klavier')),
        (('the cat'), ('die Katze')),
        (('the owl'), ('die Eule')),
        (('the brother'), ('der Bruder')),
    ]
}
duolingo_directions = {
    'name' : 'Directions',
    'words' : [
        (('the library'), ('die Bibliothek')),
        (('the church'), ('die Kirche')),
        (('the market'), ('der Markt')),
        (('the museum'), ('das Museum')),
        (('excuse me'), ('Entschuldigung')),
        (('where'), ('wo')),
        (('the park'), ('der Park')),
        (('the cinema'), ('das Kino')),
        (('on the right'), ('rechts')),
        (('on the left'), ('links')),
        (('beautiful'), ('sch'+ou+'n')),
        (('the ATM'), ('der Geldautomat')),
        (('the university'), ('die Universit'+au+'t')),
        (('big'), ('gro'+Ss)),
        (('the coffee shop'), ('das Caf'+ea)),
        (('the proximity'), ('die N'+au+'he')),
        (('the coffee'), ('der Kaffee')),
        (('cheap'), ('billig')),
        (('the hotel'), ('das Hotel')),
        (('the supermarket'), ('der Supermarkt')),
        (('the restaurant'), ('das Restaurant')),
    ]
}
duolingo_questions = {
    'name' : 'Questions',
    'words' : [
        (('the male police officer'), ('der Polizist')),
        (('the male lawyer'), ('der Anwalt')),
        (('the female lawyer'), ('die Anw'+au+'ltin')),
        (('Germany'), ('Deutschland')),
        (('Canada'), ('Kanada')),
        (('to speak'), ('sprechen')),
        (('Russia'), ('Russland')),
        (('the male professor'), ('der Professor')),
        (('the female professor'), ('die Professorin')),
        (('the male doctor'), ('der Arzt')),
        (('the female doctor'), ('die '+Au+'rztin')),
        (('France'), ('Frankreich')),
        (('Switzerland'), ('die Schweiz')),
        (('Sweden'), ('Schweden')),
        (('the male pupil'), ('der Sch'+uu+'ler')),
        (('the female pupil'), ('die Sch'+uu+'lerin')),
    ]
}
duolingo_market = {
    'name' : 'Market',
    'words' : [
        (('the pizza'), ('die Pizza')),
        (('to cost'), ('kosten')),
        (('for free'), ('kostenlos')),
        (('the strawberry'), ('die Erdbeere')),
        (('Thank you very much'), ('vielen Dank')),
        (('zero'), ('null')),
        (('one'), ('eins')),
        (('two'), ('zwei')),
        (('three'), ('drei')),
        (('four'), ('vier')),
        (('five'), ('f'+uu+'nf')),
        (('six'), ('sechs')),
        (('seven'), ('sieben')),
        (('eight'), ('acht')),
        (('nine'), ('neun')),
        (('ten'), ('zehn')),
        (('eleven'), ('elf')),
        (('twelve'), ('zw'+ou+'lf')),
        (('you are welcome'), ('gern geschehen')),
        (('the orange'), ('die Orange')),
        (('please'), ('bitte')),
        (('the potato'), ('die Kartoffel')),
        (('the doner'), ('der D'+ou+'ner')),
        (('the beer'), ('das Bier')),
        (('really'), ('wirklich')),
        (('the market place'), ('der Marktplatz')),
    ]
}
duolingo_weather = {
    'name' : 'Weather',
    'words' : [
        (('sunny'),('sonnig')),
        (('today'),('heute')),
        (('the weather'),('das Wetter')),
        (('the umbrella'),('der Regenschirm')),
        (('to trek'),('wandern')),
        (('often'),('oft')),
        (('the water bottle'),('die Wasserflasche')),
        (('small'),('klein')),
        (('the summer'),('der Sommer')),
        (('the spring'),('der Fr'+uu+'hling')),
        (('the winter'),('der Winter')),
        (('the autumn'),('der Herbst')),
        (('the sun cream'),('die Sonnencreme')),
        (('always'),('immer')),
        (('foggy'),('neblig')),
        (('to rain'),('regnen')),
        (('windy'),('windig')),
        (('bad'),('schlecht')),
    ]
}
duolingo_family_2 = {
    'name' : 'Family 2',
    'words' : [
        (('the uncle'),('der Onkel')),
        (('the snail'),('die Schnecke')),
        (('the dog'),('der Hund')),
        (('to love'),('lieben')),
        (('the male partner'),('der Partner')),
        (('the aunt'),('die Tante')),
        (('the fish'),('der Fisch')),
        (('but'),('aber')),
        (('the daughter'),('die Tochter')),
        (('the son'),('der Sohn')),
        (('the girl'),('das M'+au+'dchen')),
        (('the boy'),('der Junge')),
        (('the grandma'),('die Oma')),
        (('the grandpa'),('der Opa')),
        (('the male roommate'),('der Mitbewohner')),
        (('the female roommate'),('die Mitbewohnerin')),
        (('nice'),('nett')),
        (('the male friend'),('der Freund')),
        (('the female friend'),('die Freundin')),
    ]
}
duolingo_abstract = {
    'name' : 'Abstract',
    'words' : [
        (('the opportunity'), ('die Gelegenheit')),
        (('the change'), ('die '+Au+'nderung')),
        (('the note'), ('der Hinweis')),
        (('the selection'), ('die Auswahl')),
        (('valuable'), ('wertvoll')),
        (('the position'), ('die Lage')),
        (('the attempt'), ('der Versuch')),
        (('the gold'), ('das Gold')),
        (('the way'), ('die Weise')),
        (('different'), ('anders')),
        (('the use'), ('der Gebrauch')),
        (('the letter'), ('der Brief')),
    ]
}
duolingo_abstract_2 = {
    'name' : 'Abstract 2',
    'words' : [
        (('the process'), ('der Verlauf')),
        (('the party'), ('die Party')),
        (('the access'), ('der Zugang')),
        (('the field'), ('das Feld')),
        (('the induction'), ('die Einf'+uu+'hrung')),
        (('the reference'), ('die Referenze')),
        (('the role'), ('die Rolle')),
        (('the effect'), ('die Wirkung')),
        (('the page'), ('die Spalte')),
        (('the step'), ('die Stufe')),
        (('the guide'), ('die Anleitung')),
        (('the usage'), ('die Vervendung')),
        (('the background'), ('der Hintergrund')),
        (('the detail'), ('die Einzelheit')),
        (('the weight'), ('das Gewicht')),
        (('the deployment', 'the dedication'), ('der Einsatz')),
        (('the implementation'), ('die Umsetzung')),
        (('the circle'), ('der Kreis')),
        (('the overview'), ('der '+Uu+'berblick')),
        (('the condition'), ('der Zustand')),
        (('the combination'), ('die Kombination')),
        (('the difference'), ('der Unterschied')),
        (('the regulation'), ('die Bestimmung')),
        (('the encouragement'), ('die Ermunterung')),
        (('the force'), ('die Kraft')),
        (('the category'), ('die Kategorie'))
    ]
}
duolingo_business_2 = {
    'name' : 'Business 2',
    'words' : [
        (('the firm'), ('die Firma')),
        (('young'), ('jung')),
        (('the house'), ('das Haus')),
        (('the sale'), ('der Verkauf')),
        (('the delivery'), ('die Lieferung')),
        (('the city'), ('die Stadt')),
        (('now'), ('jetzt')),
        (('more'), ('mehr')),
        (('the industry'), ('die Industrie')),
        (('high'), ('hoch')),
        (('up'), ('oben')),
        (('the chart'), ('die Tabelle')),
        (('the citizen'), ('der B'+uu+'rger')),
        (('the goods'), ('die Ware')),
        (('the insurance'), ('die Versicherung')),
        (('expensive'), ('teuer')),
        (('the island'), ('die Insel')),
        (('probably'), ('wahrscheinlich')),
        (('whom'), ('wen')),
        (('to pay'), ('zahlen')),
        (('the enterprise'), ('das Unternehmen')),
        (('the contract'), ('der Auftrag')),
        (('to modify'), ('ver'+au+'ndern')),
        (('the trade fair'), ('die Messe')),
        (('the deal'), ('das Angebot')),
        (('the warranty'), ('die Garantie')),
        (('the advertisement'), ('die Anzeige')),
        (('the newspaper'), ('die Zeitung')),
        (('the chance'), ('die Chance')),
        (('the warehouse'), ('das Lager')),
        (('the brand'), ('die Marke')),
        (('the payment'), ('die Bezahlung')),
        (('the service'), ('die Dienstleistung')),
        (('the rating'), ('die Bewertung')),
        (('the benefit'), ('die Leistung')),
        (('the customer service'), ('der Kundenservice')),
        (('the expense'), ('die Ausgabe')),
        (('the country'), ('das Land')),
        (('the production'), ('die Produktion')),
        (('the stock exchange'), ('die B'+ou+'rse')),
        (('the job offer'), ('das Stellenangebot')),
        (('between'), ('zwischen')),
        (('the foundation'), ('die Gr'+uu+'ndung')),
        (('the industry branch'), ('die Branche')),
        (('the logistics'), ('die Logistik')),
        (('the retail'), ('der Einzelhandel')),
        (('the business'), ('der Betrieb')),
        (('to run'), ('laufen')),
        (('the need'), ('der Bedarf')),
        (('to calculate'), ('berechnen')),
        (('to negotiate'), ('verhandeln')),
        (('the price'), ('der Preis')),
        (('various'), ('verschieden')),
        (('the male customer'), ('der Kunde')),
        (('the female customer'), ('die Kundin')),
    ]
}
duolingo_verbs_7 = {
    'name' : 'Verbs 7',
    'words' : [
        (('to select'), ('ausw'+au+'hlen')),
        (('the window'), ('das Fenster')),
        (('to hear'), ('h'+ou+'ren')),
        (('the wind'), ('der Wind')),
        (('simple'), ('einfach')),
        (('to open'), (ou+'ffnen')),
        (('the bottle'), ('die Flasche')),
        (('the wine'), ('der Wein')),
        (('make possible'), ('erm'+ou+'glichen')),
        (('to use'), ('benutzen')),
        (('to improve'), ('verbessern')),
        (('the article'), ('der Artikel')),
        (('the contibution'), ('der Beitrag')),
        (('to determine'), ('festlegen')),
        (('the date'), ('das Datum')),
        (('the scissor'), ('die Schere')),
        (('tomorrow'), ('morgen')),
        (('soon'), ('bald')),
        (('the nutrition'), ('die Ern'+au+'hrung')),
        (('nobody'), ('niemand')),
        (('to achieve'), ('leisten')),
        (('to participate'), ('mitmachen')),
        (('to avoid'), ('vermeiden')),
        (('to bring'), ('bringen')),
        (('the hospital'), ('das Krankenhaus')),
        (('the street'), ('die Stra'+Ss+'e')),
        (('to fulfill'), ('erf'+uu+'llen')),
        (('the wish'), ('der Wunsch')),
        (('to look at'), ('ansehen')),
        (('to take over'), (uu+'bernehmen')),
        (('to remove'), ('entfernen')),
        (('to have to'), ('m'+uu+'ssen')),
        (('afterwards'), ('danach')),
        (('to work'), ('arbeiten')),
        (('to find'), ('finden')),
        (('the tree'), ('der Baum')),
        (('to care'), ('sorgen')),
        (('to inform'), ('informieren')),
        (('to make a phone call'), ('telefonieren')),
        (('to go'), ('gehen')),
        (('the train station'), ('der Bahnhof')),
        (('the computer'), ('der Computer')),
        (('to learn'), ('lernen')),
        (('french'), ('franz'+ou+'sisch')),
        (('to make'), ('machen')),
        (('broken'), ('kaputt')),
        (('to read'), ('lesen')),
        (('the newspaper'), ('die Zeitung')),
        (('the mirror'), ('der Spiegel')),
        (('to play'), ('spielen')),
        (('outside'), ('drau'+Ss+'en')),
        (('the child'), ('das Kind')),
        (('to report to the authorities'), ('anzeigen')),
        (('to win'), ('gewinnen')),
        (('barely'), ('knapp')),
        (('the books'), ('die B'+uu+'cher')),
    ]
}
duolingo_sport = {
    'name' : 'Sport',
    'words' : [
        (('the team'), ('das Team')),
        (('the ball'), ('der Ball')),
        (('the sport'), ('der Sport')),
        (('to like'), ('m'+ou+'gen')),
        (('the hobby'), ('das Hobby')),
        (('to collect'), ('sammeln')),
        (('the post stamp'), ('die Briefmarke')),
        (('the football'), ('der Fu'+Ss+'ball')),
        (('the tennis'), ('das Tennis')),
        (('found'), ('gefunden')),
        (('the activity'), ('die Aktivit'+au+'t')),
        (('healthy'), ('gesund')),
        (('the male patient'), ('der Patient')),
        (('the female patient'), ('die Patientin')),
        (('round'), ('rund')),
        (('to meet'), ('treffen')),
        (('the luck'), ('das Gl'+uu+'ck')),
        (('the league'), ('die Liga')),
        (('the German football league'), ('die Bundesliga')),
        (('the participation'), ('die Teilnahme')),
        (('free of cost'), ('gratis')),
        (('the male spectator'), ('der Zuschauer')),
        (('the female spectator'), ('der Zuschauerin')),
        (('back'), ('zur'+uu+'ck')),
        (('the male player'), ('der Spieler')),
        (('the female player'), ('die Spielerin')),
        (('the crew'), ('die Mannschaft')),
        (('the victory'), ('der Sieg')),
        (('the career'), ('die Karriere')),
        (('the game'), ('das Spiel')),
        (('seen'), ('gesehen')),
        (('to watch television'), ('fernsehen')),
        (('TV'), ('das Fernsehen')),
        (('complete'), ('komplett')),
        (('the ski'), ('der Ski')),
        (('the free time'), ('die Freizeit')),
        (('it applies to'), ('es gilt f'+uu+'r')),
        (('the swimming pool'), ('das Schwimmbad')),
        (('the wager'), ('die Wette')),
        (('strange'), ('komisch')),
        (('the movement'), ('die Bewegung')),
        (('slow'), ('langsam')),
        (('calm'), ('ruhig')),
        (('as long as'), ('solange')),
        (('as soon as'), ('sobald')),
        (('responsible'), ('z'+uu+'standig')),
        (('went'), ('ging')),
        (('accomplish'), ('geschafft')),
        (('happened'), ('passiert')),
        (('yesterday'), ('gestern')),
        (('understood'), ('verstanden')),
        (('led'), ('gef'+uu+'hrt')),
        (('thought'), ('gedacht')),
        (('the accident'), ('der Unfall')),
        (('had'), ('hatten')),
        (('founded'), ('gegr'+uu+'nded')),
        (('already'), ('schon')),
        (('brought'), ('gebracht')),
        (('own'), ('eigen')),
        (('the community'), ('die Gemeinde')),
        (('tested'), ('gepr'+uu+'ft')),
        (('known'), ('gewusst')),
        (('told'), ('genannt')),
        (('the cup'), ('die Tasse')),
        (('to fly'), ('fliegen')),
        (('the fly'), ('die Fliege')),
        (('the room'), ('das Zimmer')),
        (('the car'), ('das Auto')),
        (('the club'), ('der Verein')),
        (('dissappeared'), ('verschwunden')),
        (('wanted'), ('gewollt')),
        (('the silver'), ('das Silber')),
        (('held'), ('gehalten')),
        (('fulfilled'), ('erf'+uu+'llt')),
        (('forgiven'), ('vergeben')),
        (('elected'), ('gew'+au+'hlt')),
        (('the mayor'), ('der B'+uu+'rgermeister')),
        (('the hand'), ('die Hande')),
        (('the optical glasses'), ('die Brille')),
    ]
}

vocabulary = [
    duolingo_hobbies,
    duolingo_directions,
    duolingo_questions,
    duolingo_market,
    duolingo_weather,
    duolingo_family_2,
    duolingo_abstract,
    duolingo_abstract_2,
    duolingo_business_2,
    duolingo_verbs_7,
    duolingo_sport,
]
