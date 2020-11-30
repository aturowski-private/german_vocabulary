
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
        (('billig'), ('cheap')),
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

vocabulary = [
    duolingo_hobbies,
    duolingo_directions,
    duolingo_questions,
    duolingo_abstract,
    duolingo_abstract_2
]
