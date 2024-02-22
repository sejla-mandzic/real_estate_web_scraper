# active-specific variables
APARTMENTS_URL = "https://olx.ba/pretraga?attr=373031322850726f64616a6129&attr_encoded=1&category_id=23"
HOUSES_URL = "https://olx.ba/pretraga?attr=373032312850726f64616a6129&attr_encoded=1&category_id=24"

# closed-specific variables
PAGES_NUM = 25
FINISHED_URL = "https://everestagencija.olx.ba/api/users/2702074/listings/finished?page="



APARTMENTS_MAPPING = [
    {"canton" : 1, "pages" : 2},
    {"canton" : 2, "pages" : 1},
    {"canton" : 3, "pages" : 12},
    {"canton" : 4, "pages" : 5},
    {"canton" : 5, "pages" : 1},
    {"canton" : 6, "pages" : 3},
    {"canton" : 7, "pages" : 4},
    {"canton" : 8, "pages" : 1},
    {"canton" : 9, "pages" : 50},
    {"canton" : 10, "pages" : 1},
    {"canton" : 11, "pages" : 26},
    {"canton" : 12, "pages" : 8},
    {"canton" : 13, "pages" : 10},
    {"canton" : 14, "pages" : 2},
    {"canton" : 15, "pages" : 10},
]


HOUSES_MAPPING = [
    {"canton" : 1, "pages" : 7},
    {"canton" : 2, "pages" : 1},
    {"canton" : 3, "pages" : 14},
    {"canton" : 4, "pages" : 16},
    {"canton" : 5, "pages" : 1},
    {"canton" : 6, "pages" : 8},
    {"canton" : 7, "pages" : 9},
    {"canton" : 8, "pages" : 1},
    {"canton" : 9, "pages" : 43},
    {"canton" : 10, "pages" : 1},
    {"canton" : 11, "pages" : 24},
    {"canton" : 12, "pages" : 11},
    {"canton" : 13, "pages" : 7},
    {"canton" : 14, "pages" : 2},
    {"canton" : 15, "pages" : 10},
]


CANTONS = [
    "Unsko-sanski kanton",
    "Posavski kanton",
    "Tuzlanski kanton",
    "Zenicko-dobojski kanton",
    "Bosansko-podrinjski kanton",
    "Srednjobosanski kanton",
    "Hercegovacko-neretvanski kanton",
    "Zapadnohercegovacki kanton",
    "Kanton Sarajevo",
    "Kanton 10",
    "Banjalucka regija",
    "Dobojsko-Bijeljinska regija",
    "Sarajevsko-Zvornicka regija",
    "Trebinjsko-Focanska regija",
    "Brcko distrikt",
]


CITIES = [
    {"id": 1, "cities": ["Bihać", "Bosanska Krupa", "Bosanski Petrovac", "Bužim", "Cazin", "Ključ", "Sanski Most", "Velika Kladuša"]},
    {"id": 2, "cities": ["Domaljevac-Šamac", "Odžak", "Orašje"]},
    {"id": 3, "cities": ["Banovići", "Čelić", "Doboj Istok", "Gračanica", "Gradačac", "Kalesija", "Kladanj", "Lukavac", "Sapna", "Srebrenik", "Teočak", "Tuzla", "Živinice"]},
    {"id": 4, "cities": ["Breza", "Doboj Jug", "Kakanj", "Maglaj", "Olovo", "Tešanj", "Usora", "Vareš", "Visoko", "Zavidovići", "Zenica", "Žepče"]},
    {"id": 5, "cities": ["Goražde", "Ustikolina"]},
    {"id": 6, "cities": ["Bugojno", "Busovača", "Dobretići", "Donji Vakuf", "Fojnica", "Gornji Vakuf-Uskoplje", "Jajce", "Kiseljak", "Kreševo", "Novi Travnik", "Travnik", "Vitez"]},
    {"id": 7, "cities": ["Čapljina", "Čitluk", "Jablanica", "Konjic", "Mostar", "Neum", "Prozor", "Ravno", "Stolac"]},
    {"id": 8, "cities": ["Grude", "Ljubuški", "Posušje",  "Široki Brijeg"]},
    {"id": 9, "cities": ["Hadžići", "Ilidža", "Ilijaš", "Sarajevo - Centar", "Sarajevo - Novi Grad", "Sarajevo - Novo Sarajevo", "Sarajevo - Stari Grad", "Trnovo", "Vogošća"]},
    {"id": 10, "cities": ["Bosansko Grahovo", "Drvar", "Glamoč", "Kupres", "Livno", "Tomislavgrad"]},
    {"id": 11, "cities": ["Banja Luka", "Čelinac", "Gradiška", "Jezero", "Kneževo", "Kostajnica", "Kotor Varoš", "Kozarska Dubica", "Krupa na Uni", "Laktaši", "Mrkonjić Grad", "Novi Grad", "Oštra Luka", "Prijedor", "Prnjavor", "Ribnik", "Šipovo", "Srbac"]},
    {"id": 12, "cities": ["Bijeljina", "Brod", "Derventa", "Doboj", "Donji Žabar", "Lopare", "Modriča", "Pelagićevo", "Petrovo", "Šamac", "Stanari", "Teslić", "Ugljevik", "Vukosavlje"]},
    {"id": 13, "cities": ["Bratunac", "Han Pijesak", "Istočna Ilidža", "Istočni Stari Grad", "Istočno Sarajevo", "Milići", "Novo Goražde", "Osmaci", "Pale", "Rogatica", "Rudo", "Šekovići", "Sokolac", "Srebrenica", "Višegrad", "Vlasenica", "Zvornik"]},
    {"id": 14, "cities": ["Berkovići", "Bileća", "Čajniče", "Foča", "Gacko", "Istočni Mostar", "Kalinovik", "Ljubinje", "Nevesinje", "Trebinje"]},
    {"id": 15, "cities": ["Brčko"]}
]