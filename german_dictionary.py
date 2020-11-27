
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
GEN_IDX=1
GER_IDX=2

duolingo_abstract_2 = {
    'name' : 'Abstract 2',
    'words' : [
        (('deployment', 'dedication'), ('der', 'Einsatz')),
        (('implementation'), ('die', 'Umsetzung')),
        (('circle'), ('der', 'Kreis')),
        (('overview'), ('der', Uu + 'berblick'))
    ]
}

vocabulary = [
    duolingo_abstract_2
]
