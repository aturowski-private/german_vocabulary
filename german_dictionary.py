
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

# ALT 0223 = ß
# ALT 0228 = ä
# ALT 0246 = ö
# ALT 0252 = ü
# ALT 0196 = Ä
# ALT 0214 = Ö
# ALT 0220 = Ü

# some helpful constants
ENG_IDX=0
GER_IDX=1

at_difficult_1 = {
    'name' : 'Adam difficult 1',
    'words' : [
        (('to remove'), ('entfernen')),
        (('the contibution'), ('der Beitrag')),
        (('to negotiate'), ('verhandeln')),
        (('the service'), ('die Dienstleistung')),
        (('the enterprise'), ('das Unternehmen')),
        (('the contract'), ('der Auftrag')),
        (('the expense'), ('die Ausgabe')),
        (('the need'), ('der Bedarf')),
        (('the business'), ('der Betrieb')),
        (('the difference'), ('der Unterschied')),
        (('the encouragement'), ('die Ermunterung')),
        (('the guide'), ('die Anleitung')),
        (('the selection'), ('die Auswahl')),
        (('the use'), ('der Gebrauch')),
        (('the usage'), ('die Verwendung')),
        (('the male spectator'), ('der Zuschauer')),
        (('dissappeared'), ('verschwunden')),
        (('wanted'), ('gewollt')),
        (('elected'), ('gew'+au+'hlt')),
        (('the experience'), ('die Erfahrung')),
    ]
}

at_difficult_2 = {
    'name' : 'Adam difficult 2',
    'words' : [
        (('v. favored'), ('bevorzugt')),
        (('v. guaranteed'), ('gewährleistet')),
        (('v. considered'), ('berücksichtigt')),
        (('the paradise'), ('das Paradies')),
        (('the agency'), ('die Behörde')),
        (('the law'), ('das Gesetz')),
        (('the administration'), ('die Verwaltung')),
        (('the regulation'), ('die Vorschrift')),
        (('the term'), ('die Bedingung')),
        (('the administration'), ('die Verwaltung')),
        (('the licence'), ('die Genehmigung')),
    ]
}

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
        (('some'), ('manche')),
        (('against'), ('gegen')),
        (('the disease'), ('die Krankheit')),
    ]
}
duolingo_directions = {
    'name' : 'Directions',
    'words' : [
        (('the library'), ('die Bibliothek')),
        (('the church'), ('die Kirche')),
        (('the market'), ('der Markt')),
        (('the museum'), ('das Museum')),
        (('excuse me'), ('entschuldigung')),
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
        (('the category'), ('die Kategorie')),
        (('to advise'), ('beraten')),
        (('been'), ('gewesen')),
        (('would have'), ('h'+au+'tten')),
        (('said'), ('gesagt')),
        (('would have been'), ('w'+au+'ren gewesen')),
        (('leave'), ('verlassen')),
        (('the experience'), ('die Erfahrung')),
        (('the improvement'), ('die Verbesserung')),
        (('the planning'), ('die Planung')),
        (('the height'), ('die H'+ou+'he')),
        (('the agriculture'), ('die Landwirtschaft')),
        (('the means'), ('das Mittel')),
        (('the recomendation'), ('der Vorschlag')),
        (('the length'), ('die L'+au+'nge')),
        (('to suffice'), ('reichen')),
        (('the ladder'), ('die Leiter')),
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
        (('the knowledge'), ('das Wissen')),

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
        (('the female spectator'), ('die Zuschauerin')),
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
        (('founded'), ('gegr'+uu+'ndet')),
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
        (('the hand'), ('die Hand')),
        (('the optical glasses'), ('die Brille')),
    ]
}
duolingo_the_arts = {
    'name' : 'The Arts',
    'words' : [
        (('the gallery'), ('die Galerie')),
        (('is located'), ('befindet sich')),
        (('the studio'), ('das Studio')),
        (('excited'), ('begeistert')),
        (('the guitar'), ('die Gitarre')),
        (('the art'), ('die Kunst')),
        (('the homeland'), ('die Heimat')),
        (('the exhibition'), ('die Ausstellung')),
        (('the musician'), ('der Musiker')),
        (('the instrument'), ('das Instrument')),
        (('the artist'), ('der K'+uu+'nstler')),
        (('the sculpture'), ('das Plastik')),
        (('the music'), ('die Musik')),
        (('the theater'), ('das Theater')),
        (('the culture'), ('die Kultur')),
        (('the start'), ('der Start')),
        (('ready'), ('bereit')),
        (('everything'), ('alles')),
        (('the director of the movie'), ('die Regie')),
        (('the draft'), ('der Entwurf')),
        (('the movie'), ('der Film')),
        (('the model'), ('das Modell')),
        (('the train'), ('der Zug')),
        (('to dance'), ('tanzen')),
        (('excellent'), ('ausgezeichnet')),
        (('the literature'), ('die Literatur')),
        (('the critique'), ('die Kritik')),
        (('open'), ('offen')),
        (('the corner'), ('die Ecke')),
        (('the design'), ('das Design')),
        (('the song'), ('das Lied')),
        (('the collection'), ('die Sammlung')),
        (('the shoe'), ('der Schuh')),
        (('the photography'), ('die Fotografie')),
        (('the recommendation'), ('die Empfehlung')),
        (('the concert'), ('das Konzert')),
        (('the castle'), ('das Schloss')),
        (('the jazz'), ('der Jazz')),
        (('the fashion'), ('die Mode')),
        (('the stage'), ('die B'+uu+'hne')),
        (('the style'), ('der Stil')),
        (('the frame'), ('der Rahmen')),
        (('the dance'), ('der Tanz')),
        (('all over again'), ('von vorne')),
        (('the picture'), ('das Bild')),
        (('the camera'), ('die Kamera')),
        (('the activitu'), ('die T'+au+'tigkeit')),
        (('satisfied'), ('zufrieden')),
        (('the documentiation'), ('die Dokumentation')),
        (('the male actor'), ('der Schauspieler')),
        (('the word'), ('das Wort')),
    ]
}

duolingo_passiv_2 = {
    'name' : 'The Arts',
    'words' : [
        (('v. favored'), ('bevorzugt')),
        (('v. guaranteed'), ('gewährleistet')),
        (('seldom'), ('selten')),
        (('v. eaten'), ('gegessen')),
        (('v. used'), ('genutzt')),
        (('v. changed'), ('geändert')),
        (('v. written'), ('geschrieben')),
        (('v. published'), ('veröffentlicht')),
        (('v. considered'), ('berücksichtigt')),
        (('the application'), ('die Bewerbung')),
        (('v. stolen'), ('gestohlen')),
        (('v. assessed'), ('bewertet')),
    ]
}

duolingo_religion = {
    'name' : 'Religion',
    'words' : [
        (('the religion'), ('die Religion')),
        (('the death'), ('der Tod')),
        (('the God'), ('der Gott')),
        (('the priest'), ('der Priester')),
        (('the belief'), ('der Glaube')),
        (('v. pray'), ('beten')),
        (('v. earn'), ('verdienen')),
        (('the prayer'), ('das Gebet')),
        (('the paradise'), ('das Paradies')),
        (('the islam'), ('der Islam')),
        (('holy'), ('heilig')),
        (('the atheist'), ('der Atheist')),
        (('the buddism'), ('der Buddhismus')),
        (('the christian'), ('der Christ')),
        (('the muslim'), ('der Moslem')),
        (('the jew'), ('der Jude')),
        (('the muslims'), ('die Muslime')),
        (('the christians'), ('die Christen')),
        (('the monk'), ('der Mönch')),
        (('the monks'), ('die Mönche')),
        (('the temple'), ('der Tempel')),
        (('the temples'), ('die Tempel')),
        (('the church'), ('die Kirche')),
        (('the churches'), ('die Kirchen')),
        (('v. meditate'), ('meditieren')),
        (('the mosque'), ('die Moschee')),
        (('the synagogue'), ('die Synagoge')),
        (('the Gods'), ('die Götter')),
        (('the religions'), ('die Religionen')),
        (('v. believe in'), ('glauben an')),
    ]
}

duolingo_politics_1a = {
    'name' : 'Politics 1a',
    'words' : [
        (('the politics'), ('die Politik')),
        (('the peace'), ('der Frieden')),
        (('the power'), ('die Macht')),
        (('the political party'), ('die Partei')),
        (('the vote'), ('die Stimme')),
        (('the president'), ('der Präsident')),
        (('v. support'), ('fördern')),
        (('v. belong'), ('gehören')),
        (('the republic'), ('die Republik')),
        (('the people'), ('das Volk')),
        (('the male politician'), ('der Politiker')),
        (('the female politician'), ('die Politikerin')),
        (('the success'), ('der Erfolg')),
        (('the contract'), ('der Vertrag')),
        (('the contracts'), ('die Verträge')),
        (('the queen'), ('die Königin')),
        (('the state'), ('der Staat')),
        (('the election'), ('die Wahl')),
        (('the agency'), ('die Behörde')),
        (('the agencies'), ('die Behörden')),
    ]
}

duolingo_politics_1b = {
    'name' : 'Politics 1b',
    'words' : [
        (('the king'), ('der König')),
        (('the law'), ('das Gesetz')),
        (('the administration'), ('die Verwaltung')),
        (('the licence'), ('die Genehmigung')),
        (('the government'), ('die Regierung')),
        (('the war'), ('der Krieg')),
        (('the ministry'), ('das Ministerium')),
        (('the right'), ('das Recht')),
        (('the rights'), ('die Rechte')),
        (('the fight'), ('der Kampf')),
        (('the regulation'), ('die Vorschrift')),
        (('the city hall'), ('das Rathaus')),
        (('the influence'), ('der Einfluss')),
        (('v. vote'), ('wählen')),
        (('the princess'), ('die Prinzessin')),
        (('the rule'), ('die Regel')),
        (('v. apply to'), ('betreffen')),
        (('the prince'), ('der Prinz')),
        (('the control'), ('die Kontrolle')),
        (('the term'), ('die Bedingung')),
        (('the decision'), ('die Entscheidung')),
        (('the legal trial'), ('der Prozess')),
        (('the procedure'), ('das Verfahren')),
        (('the interest in'), ('das Interesse')),
        (('successful'), ('erfolgreich')),
    ]
}

duolingo_adverbs_2 = {
    'name' : 'Adverbs 2a',
    'words' : [
        (('just'), ('soeben')),
        (('at any time'), ('jederzeit')),
        (('the jewelry'), ('der Schmuck')),
        (('in addition'), ('hinzu')),
        (('as well'), ('ebenfalls')),
        (('finally'), ('schließlich')),
        (('that is why'), ('deswegen')),
        (('on the other hand'), ('hingegen')),
        (('for this'), ('hierzu')),
        (('nevertheless'), ('denoch')),
        (('with this'), ('hiermit')),
        (('again'), ('nochmals')),
        (('particularly'), ('insbesondere')),
        (('currently'), ('derzeit')),
        (('still'), ('weiterhin')),
    ]
}

duolingo_abstract_3a = {
    'name' : 'Abstract 3a',
    'words' : [
        (('the comparison'), ('der Vergleich')),
        (('the facility'), ('die Anlage')),
        (('the section'), ('die Rubrik')),
        (('the criteria'), ('die Kriterien')),
        (('the support'), ('die Förderung')),
        (('the system'), ('das System')),
        (('the application'), ('die Anwendung')),
        (('the development'), ('die Entwiklung')),
        (('the example'), ('das Beispiel')),
        (('the admission'), ('der Eintritt')),
        (('the content'), ('der Inhalt')),
        (('the opening'), ('die Eröffnung')),
        (('the average'), ('der Durchschnitt')),
    ]
}

duolingo_abstract_3b = {
    'name' : 'Abstract 3b',
    'words' : [
        (('the part'), ('der Abschnitt')),
        (('the loss'), ('der Verlust')),
        (('the requirement'), ('die Auflage')),
        (('the remainder'), ('der rest')),
        (('the supply'), ('die Versorgung')),
        (('the share'), ('der Anteil')),
        (('the repair'), ('die Reparatur')),
        (('the event'), ('das Ereignis')),
        (('the events'), ('die Ereignisse')),
        (('the speed'), ('die Geschwindigkeit')),
        (('the idea'), ('die Vorstellung')),
        (('the agency'), ('die Agentur')),
        (('the tradition'), ('die Tradition')),
    ]
}

duolingo_abstract_3c = {
    'name' : 'Abstract 3c',
    'words' : [
        (('the circumference'), ('der Umfang')),
        (('the surface'), ('die Oberfläche')),
        (('the level'), ('das Niveau')),
        (('the obligation'), ('die Verpflichtung')),
        (('the qualification'), ('die Qualifikation')),
        (('the danger'), ('die Gefahr')),
        (('the violence'), ('die Gewalt')),
        (('the character'), ('der Charakter')),
        (('the lecture'), ('der Vortrag')),
        (('the material'), ('das Material')),
        (('the materials'), ('die Materialien')),
        (('the cover'), ('der Bezug')),
        (('the leather'), ('das Leder')),
        (('the round'), ('die Runde')),
        (('the mailbox'), ('der Briefkasten')),
        (('the entrance'), ('der Eingang')),
    ]
}

duolingo_abstract_3d = {
    'name' : 'Abstract 3d',
    'words' : [
        (('the degree'), ('der Abschluss')),
        (('the interaction'), ('der Umgang')),
        (('sincere'), ('herzlich')),
        (('the approach'), ('der Ansatz')),
        (('the reception'), ('der Empfang')),
        (('the attitude'), ('die Einstellung')),
        (('the ticket'), ('die Karte')),
        (('v. finished'), ('beendet')),
        (('the mediation'), ('die Vermittlung')),
        (('the symbol'), ('das Symbol')),
        (('the show'), ('die Schau')),
        (('the cooperation'), ('die Kooperation')),
        (('the phrase'), ('der Satz')),
        (('the case'), ('der Fall')),
        (('the cases'), ('die Fälle')),
    ]
}

duolingo_verbs_8a = {
    'name' : 'Verbs 8a',
    'words' : [
        (('v. send'), ('schicken')),
        (('v. compare'), ('vergleichen')),
        (('v. hike'), ('wandern')),
        (('v. explain'), ('erklären')),
        (('v. jump'), ('springen')),
        (('v. use'), ('verwenden')),
        (('v. give up'), ('abgeben')),
        (('v. collect'), ('sammeln')),
        (('v. save'), ('sparen')),
        (('v. be enough'), ('reichen')),
        (('v. cost'), ('kosten')),
        (('v. share'), ('teilen')),
        (('v. protect'), ('schützen')),
    ]
}

duolingo_verbs_8b = {
    'name' : 'Verbs 8b',
    'words' : [
        (('v. test'), ('testen')),
        (('v. notice'), ('merken')),
        (('v. avoid'), ('vermeiden')),
        (('v. search through'), ('durchsuchen')),
        (('v. publish'), ('veröffentlichen')),
        (('v. update'), ('aktualisieren')),
        (('v. love'), ('lieben')),
        (('v. book'), ('buchen')),
        (('the competition'), ('der Wettbewerb')),
        (('the flight'), ('der Flug')),
        (('v. achieve'), ('leisten')),
        (('the plan'), ('der Plan')),
        (('v. inquire'), ('nachfragen')),
        (('v. suggest'), ('vorschlagen')),
        (('daily'), ('taglisch')),
        (('v. surrender'), ('aufgeben')),
    ]
}

duolingo_verbs_8c = {
    'name' : 'Verbs 8c',
    'words' : [
        (('v. watch'), ('beachten')),
        (('v. belong'), ('gehören')),
        (('v. terminate'), ('abbrechen')),
        (('v. ask'), ('bitten')),
        (('v. respond to'), ('beantworten')),
        (('v. secure'), ('sichern')),
        (('v. reside'), ('wohnen')),
        (('v. stand'), ('stehen')),
        (('v. quote'), ('zitieren')),
        (('v. believe'), ('glauben')),
        (('v. wish'), ('wünschen')),
        (('v. appear'), ('erscheinen')),
    ]
}

duolingo_verbs_8d = {
    'name' : 'Verbs 8d',
    'words' : [
        (('v. offer'), ('bieten')),
        (('v. shop'), ('einkaufen')),
        (('v. pay'), ('zahlen')),
        (('v. own'), ('besitzen')),
        (('v. follow'), ('folgen')),
        (('v. turn around'), ('wenden')),
        (('v. wait'), ('warten')),
        (('v. report'), ('melden')),
        (('v. portray'), ('darstellen')),
        (('v. move'), ('bewegen')),
        (('v. discuss'), ('diskutieren')),
    ]
}

duolingo_verbs_8e = {
    'name' : 'Verbs 8e',
    'words' : [
        (('v. call'), ('rufen')),
        (('v. be happy'), ('freuen')),
        (('v. need'), ('benötigen')),
        (('v. deserve'), ('verdienen')),
        (('v. press'), ('drucken')),
        (('v. know'), ('wissen')),
        (('v. acquire'), ('erwerben')),
        (('careful'), ('vorsichtig')),
    ]
}

duolingo_philosophy_1a = {
    'name' : 'Philosophy 1a',
    'words' : [
        (('the reality'), ('die Wirklichkeit')),
        (('the philosophy'), ('die Philosophie')),
        (('the consciousness'), ('das Bewusstsein')),
        (('true'), ('wahr')),
   ]
}

duolingo_verbs_9a = {
    'name' : 'Verbs 9a',
    'words' : [
        (('v. demand'), ('fordern')),
        (('v. lead'), ('führen')),
        (('v. affect'), ('aufwirken')),
        (('v. arise'), ('entstehen')),
        (('v. accomplish'), ('schaffen')),
        (('finally'), ('endlich')),
        (('v. leave'), ('verlassen')),
        (('v. sit'), ('setzen')),
        (('v. own'), ('verfügen über')),
        (('v. set down'), ('absetzen')),
        (('v. result in'), ('ergeben')),
        (('v. remove'), ('entfernen')),
        (('v. represent'), ('vertreten')),
        (('v. deal'), ('handeln')),
   ]
}

duolingo_verbs_9b = {
    'name' : 'Verbs 9b',
    'words' : [
        (('v. form'), ('bilden')),
        (('v. hang'), ('hängen')),
        (('v. forgive'), ('vergeben')),
        (('v. deliver'), ('liefern')),
        (('the lesson'), ('der Unterricht')),
        (('v. achieve'), ('leisten')),
        (('v. communicate'), ('vermitteln')),
        (('v. edited'), ('bearbeitet')),
        (('v. treat'), ('behandeln')),
        (('v. confirm'), ('bestätigen')),
        (('v. authorize'), ('berechitigen')),
        (('v. consist'), ('besteht')),
   ]
}


# duolingo_verbs_8a = {
#     'name' : 'Verbs 8a',
#     'words' : [
#         ((''), ('')),
#         ((''), ('')),
#         ((''), ('')),
#         ((''), ('')),
#         ((''), ('')),
#         ((''), ('')),
#         ((''), ('')),
#         ((''), ('')),
#         ((''), ('')),
#    ]
# }


vocabulary = [
    at_difficult_1,         # 0
    at_difficult_2,         # 1
    duolingo_hobbies,       # 2
    duolingo_directions,    # 3
    duolingo_questions,     # 4
    duolingo_market,        # 5
    duolingo_weather,       # 6
    duolingo_family_2,      # 7
    duolingo_abstract,      # 8
    duolingo_abstract_2,    # 9
    duolingo_business_2,    # 10
    duolingo_verbs_7,       # 11
    duolingo_sport,         # 12
    duolingo_the_arts,      # 13
    duolingo_passiv_2,      # 14
    duolingo_religion,      # 15
    duolingo_politics_1a,   # 16
    duolingo_politics_1b,   # 17
    duolingo_adverbs_2,     # 18
    duolingo_abstract_3a,   # 19
    duolingo_abstract_3b,   # 20
    duolingo_abstract_3c,   # 21
    duolingo_abstract_3d,   # 22
    duolingo_verbs_8a,      # 23
    duolingo_verbs_8b,      # 24
    duolingo_verbs_8c,      # 25
    duolingo_verbs_8d,      # 26
    duolingo_verbs_8e,      # 27
    duolingo_philosophy_1a, # 28
    duolingo_verbs_9a,      # 29
    duolingo_verbs_9b,      # 30
]
