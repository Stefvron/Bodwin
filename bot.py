from re import T
from traceback import TracebackException
from twill.commands import *
from selenium import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import platform
import math
import random
import webdriver_manager.chrome
from PIL import Image
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import colormath
from colormath.color_objects import XYZColor, sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
import urllib.request
import ssl
from datetime import datetime
import validators
from selenium.webdriver.support.select import Select

ssl._create_default_https_context = ssl._create_unverified_context

TPP = 0.064922321438789365

x = 300
y = 200

wl = ["Ampel", "Apfelkuchen", "Sonnenaufgang", "Schwimmbad", "umarmen", "Raumschiff", "Armbanduhr", "Bier", "Regen", "Eselsohr", "Taco", "Sitzsack", "Clownfisch", "Diamant", "Qualle", "Pfeffer", "Orang-Utan", "Erdbeere", "Kiwi", "blau", "Staffelei", "Bademantel", "Sitzbank", "Hafen", "Horn", "Spaghettimonster", "Scooby Doo", "Ring", "Abfall", "Zeus", "schenken", "Feder", "Herz", "Pizza", "Kugelfisch", "Wolkenkratzer", "Sonne", "Zahnpasta", "Dirndl", "Lineal", "Daumen", "Auge", "Hagel", "Gladiator", "rasieren", "Felsen", "Bienenstich", "Schere", "High Five", "Nasenbluten", "Trompete", "Klobrille", "Boot", "Freitag", "Zug", "Explosion", "Bär", "Micky Maus", "Perle", "haarig", "Nemo", "kleiner Finger", "Afrika", "Computer", "Vogelscheuche", "Eisen", "Rubin", "Griechenland", "Handgelenk", "Seestern", "Teich", "Litschi", "Bob", "Black Friday", "Achteck", "Zyklop", "Schimmel", "Geburtstag", "Nachos", "Teufel", "Hammer", "Zombie", "Zahnlücke", "Kreuzotter", "Twitter", "Bestatter", "Mikrofon", "Baum", "Flaschendrehen", "Erde", "Cartoon", "Nordpol", "Tasche", "Seeigel", "Mercedes", "Mais", "Schwarm", "jung", "Superman", "geduldig", "Kreuzfahrt", "Zitteraal", "Ketchup", "Wasserfall", "Aprikose", "Wüste", "Luftschloss", "Krähe", "Einhorn", "Parade", "Antarktis", "Küste", "Muskelkater", "Bonbon", "Zirkus", "Meerjungfrau", "Weintrauben", "Patrick Star", "Bungee Jumping", "Klempner", "Mixer", "Oreo", "Korallenriff", "Mars", "Laubhaufen", "Luftmatratze", "Demonstration", "Krawatte", "Durst", "Meerschweinchen", "Tisch", "Schnurrbart", "Fass", "Bluterguss", "König", "Torpedo", "Hosenstall", "Spritze", "Stachelschwein", "Schreibschrift", "Muschel", "besuchen", "Popcorn", "Biene", "behindert", "Gesundheit", "Zwillinge", "Dschungel", "Echo", "goldenes Ei", "erschreckend", "Uniform", "Reh", "Spargel", "Kredithai", "Yin Yang", "Autoradio", "Maschine", "Donald Trump", "Galaxie", "Arzt", "Streichholzschachtel", "Richter", "schwarz", "Muttermal", "Charlie Chaplin", "Jo-Jo", "Chihuahua", "Blutspende", "Schaf", "Vatikan", "Teelicht", "Sombrero", "graben", "Silber", "Schlumpf", "schlecht", "Jagdziel", "Autogramm", "Angestellter", "Iron Man", "Kakao", "Einzelhandel", "Mikrowelle", "bauchpinseln", "Badeanzug", "Einsiedler", "Adidas", "Wohnzimmer", "Norden", "Rakete", "Limbo", "Raumanzug", "Marienkäfer", "Eiche", "LKW-Fahrer", "Kiefer", "Kleid", "Jeans", "Windows", "Tee", "Tunnel", "Eselsbrücke", "Kleeblatt", "Hunger", "Gießkanne", "Kaugummi", "Benzin", "Medaille", "positiv", "Monster", "Kühlschrank", "Pilot", "Postkarte", "Fliegenklatsche", "Känguru", "Kreuzung", "Peitsche", "niesen", "Vulkan", "Polarlicht", "Pfannkuchen", "Himmel", "Baguette", "kopieren", "Ballon", "Lunge", "Glühbirne", "Vogel", "Aubergine", "Ei", "Eichel", "Büroklammer", "Zeppelin", "Nilpferd", "Werbung", "studieren", "Feuerwehrmann", "Zahnfee", "Rapper", "Wattestäbchen", "mother", "Fassade", "Spiderman", "Minion", "Rollschuhe", "Kamel", "Rad", "Haarfarbe", "Party", "Glatze", "Giftzwerg", "heiß", "Museum", "Rechnung", "Hose", "Marmelade", "Tropfen", "Orange", "Eis", "Feuerwehrauto", "rülpsen", "Segelboot", "Falle", "Münze", "Ast", "schweben", "Erdkern", "Straßenbahn", "Piratenschiff", "Fisch", "Mäusefalle", "Zeitlupe", "Gepäckträger", "Badewanne", "Rücken", "Talentshow", "prallen", "schwimmen", "Glockenspiel", "Radio", "Spielzeug", "Wimper", "Holzfäller", "Schlitten", "Burrito", "Ampelmännchen", "Emoji", "eclipse", "Steinbock", "Terrasse", "Schach", "Bienenkönigin", "Segway", "Stuhlbein", "Hahn", "glücklich", "Portrait", "Geist", "Schleuder", "Rasierer", "lesen", "Tornado", "Zahn", "Croissant", "Koffer", "Fuchs", "Redner", "Person", "Limette", "Frieden", "Kobra", "Mutter", "Drillinge", "zupfen", "Säbel", "Strand", "Geige", "Türschloss", "Schnuller", "Hamburger", "Zahnbürste", "Möbel", "Besenstiel", "Tonleiter", "Bräutigam", "Slalom", "Webseite", "Figur", "Mumie", "Untersetzer", "Heuschrecke", "Mitternacht", "Dorf", "Löffel", "Lupe", "Harry Potter", "Ruder", "Dachboden", "Zucchini", "Ziegenbart", "Wespe", "Windmühle", "dünn", "Lotterie", "Joghurt", "Zelt", "Lasso", "Asteroid", "Sekunde", "Quadrat", "Welle", "Jacht", "Titanic", "Vollmond", "Totenkopf", "Hitze", "Paypal", "Pfeil", "Wasserpistole", "Huhn", "Hockey", "Eisverkäufer", "Stiefel", "Amor", "Donut", "Taschenlampe", "Anker", "Veganer", "Venus", "Wanderstock", "anzünden", "Barbecue", "Kamm", "Steckdose", "Westen", "Torte", "Streichholz", "Telefon", "Maske", "Ferrari", "Planet", "fliegendes Schwein", "Spinne", "Insel", "Verkehrskontrolle", "Klebestift", "Harfe", "untergewichtig", "Regenschirm", "Bauch", "Fotograf", "Goldfisch", "Tapete", "Apotheker", "Reddit", "Fanta", "Träne", "Wasserschildkröte", "blind", "Espresso", "Berlin", "Hawaiihemd", "gemütlich", "Hobbit", "Hosentasche", "Peperoni", "Silvester", "verletzt", "Gesicht", "Kaulquappe", "Chat", "Teddybär", "Düne", "Wörterbuch", "Donnerstag", "tennis", "axe", "Aussichtspunkt", "Hammerhai", "Gepäck", "Wind", "Pac-Man", "übergeben", "Biber", "mürrisch", "Truhe", "Feuerball", "Federball", "Morse Code", "Walnuss", "Tablette", "Briefträger", "Elefant", "Meme", "Osterhase", "Kneipe", "Batterie", "Kolosseum", "Gabel", "Keyboard", "Schlucht", "Karte", "Stereo", "Eltern", "Achterbahn", "Marke", "Kinn", "Krümelmonster", "Ente", "Tandem", "Fernseher", "Schädel", "read", "skull", "Zigarette", "Pyramide", "Nike", "Schwanz", "Motorrad", "Chamäleon", "Darsteller", "Nest", "Schneemann", "Discord", "Interview", "Chips", "Ukulele", "falten", "Kopftuch", "Werwolf", "Superkraft", "Spiegel", "Gazelle", "Evolution", "BMW", "fliegen", "Töne", "UFO", "Olive", "Playstation", "See", "Hula Hoop", "Violine", "Kohle", "Bettdecke", "Kappe", "Lampe", "Photosynthese", "Rohr", "Kakerlake", "Kennzeichen", "Aladdin", "Winter", "sneeze", "rice", "Rippe", "Ohr", "schwingen", "Saft", "Sattel", "Gebiss", "Duell", "Gemüse", "Südpol", "unendlich", "kauen", "rutschen", "Bomberman", "Grashüpfer", "Bombe", "Patronenhülse", "pink", "Mineralwasser", "Flöte", "Toilette", "Picknick", "Flügel", "Strumpfhose", "Milch", "Weltraum", "Melone", "Beatbox", "Weihnachten", "Bohnenstange", "Darts", "Knopf", "Textmarker", "palm tree", "Karotte", "Fallschirm", "Tür", "Bongo", "Netzwerk", "Pauke", "Drama", "Kleiderbügel", "Rose", "Vogelstrauß", "Fidget Spinner", "Wein", "ClickBait", "Höhle", "Welt", "Goldkette", "Polizei", "Kaktus", "Grafiktablett", "Creeper", "Geschenk", "Soldat", "beten", "Uranus", "Hexe", "Eisberg", "Panzerband", "Hölle", "Kirche", "rechnen", "Seilspringen", "Bart", "Seetang", "Luchs", "Ballett", "Park", "smell", "sunglasses", "Gänseblümchen", "Tausendfüßer", "Kontrabass", "Nachricht", "Grinch", "Kuckuck", "Avocado", "Gebrauchtwagenhändler", "Tabak", "Video", "Atmosphäre", "Wange", "Dämon", "Sanduhr", "Tor", "Funke", "Seite", "Minotaurus", "Hängebrücke", "Kanalisation", "Rennen", "Silo", "anzeigen", "Aufhänger", "Einrad", "Postbote", "frei schweben", "Weizen", "Ärmel", "zerreißen", "Leiche", "Risiko", "Arbeitszimmer", "Fischer", "Comicbuch", "Eimer", "Markt", "Bäckerei", "Haus", "Glitzer", "Brecheisen", "Regentropfen", "Sprühfarbe", "Ameise", "Inlineskates", "Pflaster", "Tschechien", "machomäßig", "Kanarienvogel", "Maskottchen", "ausruhen", "Rennauto", "pfeifen", "Teller", "Ziel", "Nacken", "Säge", "Fenster", "Italien", "Zeitung", "Kerze", "Hip Hop", "Haare", "wart", "cone", "Alkohol", "Gewürz", "Lippen", "aufwachen", "lächeln", "Spieß", "Schaumschläger", "Tank", "schnell", "Brennnessel", "Gitarre", "Hello Kitty", "Partnerlook", "Domino", "Handschuh", "Fliegenpilz", "Buntstift", "Elsa", "Spiegelei", "Laterne", "Grabstein", "Reißverschluss", "Handtuch", "Schornsteinfeger", "Küche", "Schimpanse", "Pegasus", "Blume", "Nasenring", "Ozean", "Hochzeitskutsche", "Schlüssel", "Süden", "Rochen", "Spitzmaus", "Stuhl", "Tiramisu", "Albtraum", "Euter", "Irokesenfrisur", "Temperatur", "Spaten", "Schnee", "Löwenzahn", "Gasse", "Hängematte", "Dinosaurier", "rückgängig", "Uhr", "Belgien", "Jesus", "Generator", "Zirkusdirektor", "Camping", "Feuerwerk", "Giraffe", "Fischernetz", "Taser", "waist", "compass", "flashlight", "Ohrenschmalz", "Samstag", "chemisch", "Poster", "Cola", "Dollar", "Ninja", "Kaugummikugel", "Abend", "Suppe", "stark", "Tastatur", "Windbeutel", "Karteikasten", "Seerose", "Einkaufswagen", "Abendessen", "lachen", "Herkules", "Stadion", "Korken", "Meerenge", "Schrank", "Elch", "Mafia", "Sherlock Holmes", "Idee", "Nussknacker", "Moskau", "schreiben", "Pause", "Taxi", "Wall-e", "Deutschland", "Weihnachtsmann", "Spaghetti", "Grinsen", "Heinzelmännchen", "Honig", "Sarg", "Skulptur", "Fleisch", "Zeh", "Ladebalken", "Rasensprenger", "Mantel", "Pferdeschwanz", "Magma", "Riese", "Corn Flakes", "Tasse", "Brezel", "Wasserkreislauf", "Keks", "Bücherregal", "Vampir", "Krebs", "Teppich", "Abonnement", "Becken", "Flutlicht", "Pistole", "Eiffelturm", "Balkon", "Gebäude", "Zebra", "Fliege", "sinken", "spülen", "Libelle", "Esel", "Champion", "Hulk", "Dampf", "Tattoo", "Ostern", "seekrank", "Mütze", "Asien", "Nudel", "Teleskop", "Excalibur", "Krankheit", "Russland", "Lüftung", "Panther", "Cello", "copy", "Chrome", "Sparschwein", "Bodybuilding", "Laptop", "Moskito", "Wunschliste", "Maurer", "Schneeflocke", "Cockpit", "Löwe", "Schnürsenkel", "sauber", "Verband", "Regenbogen", "Tetra Pak", "Bett", "Guillotine", "Kanister", "Feuerzeug", "Portugal", "Netz", "Lesezeichen", "Walross", "Seegurke", "Brieftaube", "Zahnarzt", "Wolf", "Falltür", "Vater", "Schneesturm", "Benachrichtigung", "Allergie", "Oper", "Obelix", "Jäger", "Brustkorb", "Morgan Freeman", "Gewitter", "Floh", "Saturn", "Passwort", "Gymnastik", "Bruch", "Glücksspiel", "Schornstein", "Mozart", "Großmutter", "Schwarzes Loch", "Geschäft", "Kronleuchter", "Nasenlöcher", "Laubsäge", "Thaddäus Tentakel", "Schwertfisch", "Salzwasser", "Amboss", "Zündschnur", "Moos", "Seifenblase", "Star Wars", "Spore", "Einkaufszentrum", "Flamingo", "Wunderlampe", "Bühne", "Airbag", "Pluto", "Ferse", "China", "Purzelbaum", "Natur", "Warze", "zelten", "Nuss", "Vogelhaus", "Delfin", "Oktopus", "traurig", "Voodoo", "Picasso", "Blasebalg", "Sternfrucht", "Arm", "einkaufen", "Warnweste", "Kegelrobbe", "Alufolie", "Lava", "Frühling", "Friedhof", "Leuchtstab", "Fingerspitze", "Marge Simpson", "Fleischbällchen", "googeln", "Kopfhörer", "Überschrift", "magersüchtig", "Snoopy", "Hausnummer", "kabellos", "Achsel", "Beförderung", "Pudding", "Fledermaus", "Entensuppe", "Audi", "Polizist", "depressiv", "Stirnband", "übersetzen", "Tukan", "Lilie", "grinsen", "Geologe", "Seelöwe", "Kettenkarussell", "Haltestelle", "Kopfende", "Magazin", "schwanger", "weiß", "Meteorologe", "Säule", "Tretmühle", "Kokosnuss", "Lichtschwert", "Schlüsselanhänger", "begrüßen", "Mörder", "Musik", "Konsole", "Böller", "Zirkel", "Kanada", "Observatorium", "Leiterbahn", "Ameisenbär", "Tannenbaum", "Barcode", "Chirurg", "Dreieck", "Verbrecher", "Schaltknüppel", "Blitz", "Götterspeise", "Weihnachtsbaum", "schlafen", "kratzen", "Morgen", "Schlafenszeit", "Supermarkt", "Gehirn", "funkeln", "König der Löwen", "Lego", "Hand", "Thron", "Unfall", "Kohlrübe", "Sonnenfinsternis", "Elektriker", "Radar", "Schaukelpferd", "Schatten", "Baumhaus", "Granate", "Deodorant", "Skyline", "Ferkel", "Arztkoffer", "Liane", "Zentaur", "Parkplatz", "Rührei", "Wippe", "Baumkuchen", "Leuchtreklame", "Anzug", "Sonnenblume", "Lautsprecher", "Zahnspange", "Florida", "Boris Becker", "Flipper", "Pfeife", "Trampolin", "Bürgermeister", "Einstein", "blood", "Bernstein", "Schnorchel", "Karate", "Poseidon", "Sprache", "Ober", "fahren", "Flughafen", "Hyäne", "Cyborg", "Lachs", "WhatsApp", "Labyrinth", "Urlaub", "Herbst", "Dach", "Mount Rushmore", "Sommer", "Kebab", "Klassenzimmer", "vertikal", "Dracula", "Waschbecken", "Nadelkissen", "Leidenschaft", "Zaubertrick", "Pflug", "Nashorn", "Motte", "Schweinestall", "Israel", "London Eye", "Bügeleisen", "Käse", "Architekt", "Basketball", "Velociraptor", "Pups", "Adler", "genau", "Zoowärter", "Döner", "Nähmaschine", "Ordner", "Hund", "Garnele", "Ohrhörer", "Rasseln", "parallel", "Gebäck", "James Bond", "Etagenbett", "weinen", "Xbox", "Beerdigung", "Amerika", "Maulwurf", "Teelöffel", "Nintendo", "Augenbraue", "herunterladen", "Anwalt", "Wal", "Wurst", "brünett", "Konfetti", "Essstäbchen", "Totem", "Roter Teppich", "Ende", "Weinglas", "Lebensmittel", "Lavalampe", "Roller", "Ingenieur", "Punkte", "CO2", "kochen", "Abgrund", "Pech", "Krankenschwester", "binden", "E-Gitarre", "Pelikan", "Muskete", "Diener", "Nutella", "DNS", "Orbit", "gebrochenes Herz", "Yoda", "Filmemacher", "sea", "Keksdose", "Glas", "Türstopper", "Edelstein", "Anime", "Lamm", "wachsen", "Schal", "arm", "Bauchnabel", "Handy", "Schüssel", "Mahlzeit", "Satellit", "Brust", "Boxer", "erröten", "Frisbee", "träumen", "Wunderland", "Ellbogen", "Dachfenster", "Hydrant", "Köder", "Gott", "Mr. Bean", "Pobacken", "Sudoku", "Sohn", "Jahrbuch", "Koralle", "Reinkarnation", "Hühnchen", "Braut", "Truthahn", "MTV", "Wunde", "Magier", "Kopf", "Marshmallow", "Tablet", "Patriot", "feiern", "Basis", "Nagel", "Hummer", "Alpaka", "Hieroglyphen", "schwitzen", "Helikopter", "Koch", "Straße", "Zickzack", "Reptil", "Messer", "Pfanne", "Radieschen", "Panda", "Intel", "Bahnschiene", "Traktor", "Barkeeper", "Papageientaucher", "Elfenbein", "Insekt", "Rotkehlchen", "Käsekuchen", "Pfannenwender", "Dexter", "Stein", "Eidechse", "Leiter", "Phineas und Ferb", "Pappe", "Navy", "tot", "Mülleimer", "Milchmann", "Rick", "Ehemann", "Diva", "Dieb", "Apple", "Rom", "Junge", "verdampfen", "Reise", "Seilrutsche", "Augenlid", "Himbeere", "älter", "Möhre", "stechen", "kurz", "zerren", "Tortenheber", "Korb", "Fernglas", "Nacht", "Überlebender", "Lemur", "Baseballschläger", "Alphorn", "Inuit", "Vin Diesel", "Vision", "zusammenzucken", "bekifft", "Fingernagel", "Ameisenhaufen", "Butter", "Ofen", "Bildschirm", "Brücke", "Samsung", "küssen", "Kartoffelbrei", "Didgeridoo", "Susan Wojcicki", "Bienenstock", "Bibliothekar", "Tablett", "Lisa Simpson", "Lanze", "Kuhglocke", "Curry", "Kroatien", "Fussel", "Blutegel", "trainieren", "Elektron", "Backenzahn", "Steve Jobs", "Bulle", "Volleyball", "Laboratorium", "Sonnenbrand", "Physalis", "Opfer", "Flasche", "Eistee", "Pokemon", "Gehirnwäsche", "Gesichtsbemalung", "Apfel", "Goofy", "Kaffee", "Revolver", "Glücksrad", "Strandkorb", "Schilf", "Bar", "Lama", "berühmt", "Kreide", "Monaco", "Gru", "Toaster", "Lasagne", "Himmelbett", "Maniküre", "insolvent", "Österreich", "Igel", "Fahrkarte", "Oboe", "Knöchel", "Schnecke", "Scheibenwischer", "Prüfung", "Monobraue", "Rückenschmerzen", "Wiesel", "Radioaktivität", "Werkzeugkasten", "tippen", "Überfall", "Tischdecke", "Schokolade", "Golfwagen", "Lakritz", "Erdnuss-flips", "Farbpalette", "Happy Meal", "Tannenzapfen", "Schleim", "Fluss", "Barbier", "Norwegen", "Kissen", "Geier", "Klebeband", "Tomate", "John Cena", "Gepard", "Pinsel", "Dusche", "Schoß", "Skateboardfahrer", "Wirbel", "Usain Bolt", "Limonade", "Teekanne", "Gleichgewicht", "Pfad", "Nagelfeile", "Bajonett", "Organ", "Rolltreppe", "Tweety", "New York", "Videospiel", "Jenga", "Schreibtisch", "Dompteur", "Mittwoch", "Niere", "Bandscheibenvorfall", "Sauna", "Schneeball", "Narwal", "salto schlagen", "Beziehung", "Gurke", "Zaun", "Krokodil", "The Rock", "Grab", "Tal", "Seuche", "Bambi", "Elon Musk", "Schaukel", "Maulkorb", "Bullauge", "Fossil", "Marionette", "Nasenhaar", "Kapitän", "winzig", "backen", "Schnauze", "Wildwasserbahn", "links", "Graffiti", "Käfer", "betrügen", "Absperrband", "stehen", "Kopie", "Bohne", "Speer", "Strahlung", "Oktoberfest", "kitzeln", "Pastete", "Muskel", "Rauch", "Silberbesteck", "königlich", "Bärenfalle", "Leichtsinn", "Einhornwal", "Pickel", "Handfläche", "jonglieren", "Versicherungskaufmann", "Elmo", "vollständig", "wütend", "Garage", "Papagei", "Daune", "Baumkrone", "Maibaum", "Lautstärke", "Dolch", "Beine", "niedrig", "Christbaumkugel", "Banjo", "Kasino", "Clown", "Thunfisch", "Hecht", "Spongebob", "Pfadfinder", "Matratze", "Xylofon", "Kranz", "High Score", "Hacker", "Weide", "Hirsch", "Eule", "Huf", "Jaguar", "Henne", "Youtuber", "Lagerfeuer", "Komet", "Maki", "Raupe", "rollen", "Umhang", "Vorhang", "Publikum", "Untergrund", "Socken", "Spule", "Medizin", "King Kong", "Gitter", "Bäcker", "Brot", "Xerox", "Drache", "Schweiß", "Kreditkarte", "Gras", "Punktestand", "Frucht", "Schweinchen Dick", "Hawaii", "schlagen", "Steinzeit", "Brett", "Indien", "Schiedsrichter", "Anhalter", "Puzzle", "Honigwabe", "Südafrika", "Augenbinde", "USB", "Grenze", "Muffin", "Wolle", "zurückspulen", "Garfield", "Schnellstraße", "Amsel", "feuerfest", "Tetris", "Klaviersaite", "beizen", "Birke", "Schweißer", "Reis", "Milchstraße", "Minute", "Darm", "Kröte", "Jahreszeit", "chaotisch", "Erkältung", "Wort", "Sechseck", "Skittles", "Sichel", "Granatapfel", "Bagger", "verschwinden", "Taxifahrer", "Anzeige", "Teig", "inkognito", "Erfrierung", "Kessel", "Telefonbuch", "Ravioli", "Billard", "detonieren", "undicht", "Fred Feuerstein", "Schulter", "Mark Zuckerberg", "Fensterbank", "Friseur", "schüchtern", "Pirat", "Argentinien", "Zehnagel", "Murmeln", "Waschlappen", "Desoxyribonukleinsäure", "W-LAN", "Föhn", "Cerberus", "Photoshop", "Hut", "Ecke", "Kathedrale", "Bettwanze", "Priester", "Bus", "Schaufensterpuppe", "Diplom", "Hamster", "Spender", "Detektiv", "Champagner", "Dose", "Trophäe", "Oase", "Oberteil", "Kissenschlacht", "Green Lantern", "Sumpf", "Luftkissenboot", "Achselhöhle", "Panzerfaust", "Hafenbecken", "Rüstung", "Euro", "KFC", "Dudelsack", "Vulkanologe", "Megafon", "Skorpion", "Marathon", "Konzert", "Bikini", "Krankenhaus", "Eiskaffee", "Auspuff", "Goldtopf", "Blut", "Kredit", "Höhlenmensch", "Logo", "Geröll", "Treibsand", "Zeitmaschine", "schminken", "kahl", "Deckenventilator", "Zement", "Veranda", "Katze", "biegen", "Saugglocke", "Lutscher", "Maler", "Tarzan", "Baumstumpf", "schneiden", "schauen", "Kirby", "umkehren", "Nagelschere", "singen", "Hampelmann", "Aschenbecher", "Teletubby", "Hase", "Schule", "Skalpell", "Paparazzi", "Virtual Reality", "Veröffentlichung", "Kleber", "Polo", "ernten", "pieksen", "Sweatshirt", "Taille", "Portal", "Stoppuhr", "epilieren", "Diskette", "Affe", "Spanien", "Luftschiff", "Türklinke", "stricken", "gähnen", "Luigi", "Regal", "Schwert", "Anhängerkupplung", "Waschbär", "Jimmy Neutron", "reparieren", "Aquarium", "Hähnchen", "Dänemark", "Zelle", "überwintern", "Puder", "riechen", "Pfund", "Blaubeere", "Kamera", "Manege", "Spieler", "Knie", "Wonder Woman", "Mel Gibson", "trinken", "vergessen", "Patenonkel", "Getränk", "Schaukelstuhl", "arbeiten", "Fußball", "Schlange", "Palast", "Essig", "föhnen", "Köcher", "Gorilla", "Rasierklinge", "Zügel", "Barack Obama", "Spartacus", "Kabel", "Wurm", "unsichtbar", "Lehm", "Erdnuss", "Miniclip", "Schnabel", "LKW", "Schicksal", "rauchen", "Kuh", "Waffel", "Waldbrand", "zertrümmern", "Freibad", "kriechen", "Grillen", "goldener Apfel", "Maisfeld", "Tauchgang", "Sonnenschirm", "Brieföffner", "Statue", "Robbe", "Gummi", "Tower Bridge", "Dalmatiner", "Gips", "Apfelsaft", "wiederholen", "Sandalen", "Atombombe", "England", "Rentier", "Zypresse", "Schnabeltier", "Vogelspinne", "Glocke", "Waschmaschine", "Tumor", "Wellensittich", "Röstaroma", "Sahne", "abstrakt", "Sau", "Mädchen", "Topf", "Brusthaare", "Karneval", "kiffen", "Birne", "Efeu", "Bauarbeiter", "Bingo", "Meeresfrüchte", "Kellner", "keuchen", "Bleiche", "Pony", "Nachbar", "Schutzhelm", "Mund", "Android", "Neptun", "Handschlag", "Wolke", "Widder", "Surfbrett", "tief", "warm", "Kartoffelpuffer", "Crash Bandicoot", "Fastfood", "Gottesanbeterin", "Junk Food", "verteidigen", "alt", "Mosaik", "Türsteher", "Cousin", "Schotter", "gestresst", "Trend", "Einschlag", "Tuba", "Safe", "Limousine", "Skateboard", "Berühmtheit", "Sport", "Schranke", "lustig", "Kernspintomografie", "vorspulen", "Zauberer", "bleichen", "Text", "Scheune", "rot", "Versteck", "Halbinsel", "Rutsche", "Mont Blanc", "Addition", "Haselnuss", "Kürbislaterne", "Popeye", "BMX", "Sattelschlepper", "Beule", "Mexiko", "Matrjoschka", "Regenmantel", "Peppa Pig", "Killerwal", "Kermit", "Helium", "Banane", "Vogelbad", "Wand", "Trittstufe", "Farbe", "Mario", "Nachtclub", "Bogen", "Fell", "übergewichtig", "Bambus", "beißen", "schütteln", "Florist", "Ananas", "Wrestler", "Axt", "Abraham Lincoln", "Periskop", "erbrechen", "Tunnelblick", "Papaya", "Astronaut", "Brasilien", "Garten", "Roboter", "Flaschenpost", "offen", "Knoten", "Psychologe", "Flammenwerfer", "Hotel", "Nussschale", "Kette", "Leuchtturm", "Raum", "Nagelpflege", "Mücke", "Schatz", "Diagonale", "Bürste", "Paris", "Donald Duck", "Gans", "Faultier", "Eichhörnchen", "Elektroauto", "Corn Dog", "Quelle", "Dachschaden", "Kung Fu", "Sicherheitsgurt", "erzählen", "Klingelton", "Held", "Groschen", "schreien", "Pantomime", "Küchentuch", "Rettungsring", "Schlafstörung", "Dreirad", "Ziege", "Leine", "Barbar", "Rucksack", "Abzug", "Deadpool", "Universum", "Stegosaurus", "Brownie", "Armleuchter", "falsche Zähne", "Eber", "Trüffel", "Baklava", "spannen", "Schweiz", "Jeep", "Sechserpack", "Kopfschmerzen", "Venusfliegenfalle", "Frost", "laden", "Otter", "Rentner", "Stacheldraht", "Papier", "Gong", "Tupperdose", "Eierbecher", "Windsack", "Brille", "Reinheit", "Malkasten", "Dienstag", "Vakuum", "Feierabend", "Lehrer", "Wetter", "Maßstab", "Skydiving", "Der Rosarote Panther", "Rettungsweste", "Gefängnis", "aufnehmen", "Yoshi", "Turban", "Steam", "Anubis", "Wasserfarbkasten", "Antilope", "Bart Simpson", "Verlies", "Pedal", "Mitfahrgelegenheit", "Meister", "Pfeffersalami", "Oberfläche", "Fahrbahn", "Dattel", "Stoßstange", "Wanze", "gehen", "Angelina Jolie", "Pavian", "Spitzhacke", "gelangweilt", "Mechaniker", "Bibel", "Ufer", "Sonnensystem", "Liebe", "Rune", "Google", "Trainer", "Armband", "Lady", "toter Winkel", "Linie", "reinigen", "The Beatles", "Dosenöffner", "Milchshake", "sabbern", "Prinz", "Heiligenschein", "Leck", "Rote Beete", "Bob Ross", "Orchester", "U-Bahn", "Vodka", "Olaf", "Doritos", "gehorchen", "Mischpult", "Ziegelstein", "Taube", "Wissenschaft", "Champagnersorbet", "Kaviar", "Salz", "Kojote", "iPad", "Leiterwagen", "Schalter", "Wildschwein", "Lampenschirm", "schwach", "Homer Simpson", "Sushi", "schmelzen", "Eintopf", "Rezeption", "Familie", "Flaschenöffner", "Nase", "Dürre", "applaudieren", "Tag", "Gier", "sterben", "versagen", "Geografie", "Pogo Stick", "Rasenmäher", "Schiefer Turm von Pisa", "Rechteck", "Akkordeon", "Pudel", "Zuckerstange", "Floß", "wählen", "Skelett", "Box", "Gärtner", "Regisseur", "Papiertüte", "Kondenswasser", "Makkaroni", "Wohnung", "Perücke", "Spinat", "Wolverine", "Gandalf", "Pi", "Stubenhocker", "Ass", "Strohhalm", "Miss Piggy", "Facebook", "Gipfelkreuz", "Hai", "Stoppschild", "Sprungturm", "Kendama", "Montag", "Brause", "krank", "Merkur", "Film", "Kind", "Gelee", "Feld", "Schauspieler", "Dynamit", "Zwischendecke", "Anakonda", "Mundharmonika", "Salami", "Pendel", "Wettervorhersage", "Läufer", "Creme", "schwindelig", "Holzscheit", "Shrek", "Stecknadel", "versöhnen", "Fitness Trainer", "Alligator", "Propeller", "hüpfen", "Schriftsteller", "Sommersprossen", "Kim Jong-Un", "Wecker", "Herde", "zeigen", "Injektion", "Tourist", "atmen", "Laser", "Frankenstein", "Kirsche", "Songtext", "Käfig", "Mr. Meeseeks", "Apokalypse", "Rasierschaum", "giftig", "Vitamin", "Bayern", "Cajon", "Safari", "klettern", "Rezeptionist", "Diät", "ABBA", "draußen", "Präsident", "Comic", "Fahnenstange", "Hotdog", "Strudel", "pflügen", "Traumfänger", "klingen", "Singapur", "Pfirsich", "Scherzkeks", "Schlachter", "Sauerstoff", "Windel", "Tennis", "Kindergarten", "befehlen", "Beute", "Bugs Bunny", "Federmäppchen", "Europa", "Jalapeno", "Riesenrad", "Social Media", "Atem", "Ahorn", "Shampoo", "Land", "Mona Lisa", "Bandnudel", "Haarschuppen", "Batman", "Lady Gaga", "Link", "Zucker", "Donner", "Schottland", "Personenschützer", "Flammkuchen", "Klippe", "vergrößern", "Gift", "Buch", "Mähdrescher", "Anglerfisch", "Dynamo", "Fahrer", "Yeti", "Panflöte", "Blumenkohl", "Sicherheitsdienst", "Spitzer", "Segelflieger", "glühen", "fernsehen", "Eingabestift", "Senf", "Armbrust", "Kehle", "stoßen", "Paralleluniversum", "Auster", "Luxemburg", "Weinrebe", "William Wallace", "Essiggurke", "Axolotl", "Kettensäge", "Lieferung", "klatschen", "sternhagelvoll", "Pilz", "High Heels", "Coffeeshop", "Schlauch", "Rapunzel", "Afrofrisur", "Aufkleber", "Pflaume", "Kalender", "Klarinette", "Schminke", "Stoff", "Bauer", "Kreis", "Narbe", "Seepferdchen", "Nahrung", "Katy Perry", "Ski", "Reisepass", "Katzenklo", "Röntgenstrahlung", "Gürteltier", "Freiheitsstatue", "Busch", "Besen", "Befehlshaber", "Sonic", "Seife", "Feldstecher", "Holz", "Allee", "verlassen", "Dora", "Fee", "niedlich", "kalt", "Festival", "London", "Schlagsahne", "McDonalds", "Presslufthammer", "Fingerhut", "Tierhandlung", "predigen", "Neuseeland", "Oscar", "Klimaanlage", "Minecraft", "Knast", "Kolibri", "Looping", "Hashtag", "Fässchen", "Rahmen", "Zwiebel", "Gewinner", "Bestrafung", "Religion", "Las Vegas", "tanzen", "Profi", "essen", "Vollkornbrot", "Landschaft", "Bratsche", "Tiegel", "Räucherstäbchen", "Finnland", "John Lennon", "Protest", "Kleinbus", "Japan", "Trauben", "Olivenöl", "Krug", "Decke", "Linse", "Band", "Versicherung", "Glut", "Sumo", "ringen", "Minze", "Krankenwagen", "Flagge", "Kompass", "Windsurfer", "Mistgabel", "Puppe", "Aktion", "Erfindung", "Origami", "Hügel", "Wissenschaftler", "Sand", "Omelett", "Mottenkugel", "Zaubertrank", "Stewardess", "Jupiter", "zoomen", "Kuba", "Briefkasten", "Reifen", "Kirschblüte", "Tintenpatrone", "Schwalbe", "Lagerhaus", "Mayonnaise", "Leonardo da Vinci", "Seiltänzer", "lernen", "Cheeseburger", "Liechtenstein", "fabelhaft", "Wrestling", "Armaturenbrett", "Schottenrock", "nichts", "Erdbeben", "Harz", "Nasa", "Bitcoin", "Virus", "Sandwich", "Stern", "Lidschatten", "Traum", "Schmerz", "Schneebesen", "Model", "stampfen", "Filmriss", "Zimmermann", "Blase", "Orgel", "Notenschlüssel", "Zugbrücke", "Studio", "Papst", "Kriegsschiff", "Puma", "Ferien", "Fernsehturm", "Vuvuzela", "Zikade", "Bulldozer", "Zuma", "Haut", "Freddie Faulig", "Bildhauer", "Chuck Norris", "Kameramann", "Pikachu", "Tauchen", "sitzen", "Viertel", "Schuhkarton", "Rumänien", "Pumba", "rechts", "provozieren", "Globus", "Planke", "bezaubernd", "Bücherei", "Traubensaft", "Querflöte", "Seehund", "Nordkorea", "Schlittschuh", "Hausmeister", "Heizungskessel", "Würfel", "Motor", "Katamaran", "Scheibenwelt", "Schlagzeug", "Büro", "Krabbe", "Frühlingsrolle", "Jacke", "Ladegerät", "obdachlos", "Halskette", "Flohmarkt", "Kastanie", "Kernkraftwerk", "Räuber", "Mönch", "Terminator", "Vogelbeere", "Youtube", "Degen", "Schlacht", "Professor", "Säure", "Specht", "Iron Giant", "Soße", "Litfaßsäule", "Rückgrat", "Cheerleader", "Gekritzel", "Karussell", "Hochzeit", "Einschränkung", "aufwerten", "Nachtisch", "Angebot", "Skilift", "Verlierer", "Halskrause", "Mikroskop", "Radiergummi", "Modedesigner", "Cocktail", "Farn", "AC/DC", "Bronze", "Atom", "Gas", "Feuerwache", "Rosine", "Koala", "Fußende", "Haarschnitt", "Brocken", "Chef", "iPhone", "Sicherung", "scharfe Soße", "Triangel", "Türkei", "Hürdenlauf", "Skrillex", "Eiszapfen", "Umweltverschmutzung", "Rindfleisch", "Rockstar", "Heckspoiler", "Schlüsselbund", "Paprika", "NASCAR", "Urknall", "Skispringen", "Sphinx", "Katastrophe", "Seifenoper", "Chinatown", "wackeln", "Bösewicht", "Goblin", "Thermometer", "Werbespot", "skribbl.io", "angreifen", "Katana", "Ringelblume", "Eis am Stiel", "Preisschild", "Jay Z", "Klaue", "Wahl", "Zahnstocher", "Stativ", "Gang", "Taschentuch", "Lockenwickler", "Plätzchen", "Chinesische Mauer", "Faustkampf", "denken", "Komödie", "dreckig", "Steigung", "Feueralarm", "Notch", "Süßholz raspeln", "Schock", "Kinderwagen", "Kuckucksuhr", "Hologramm", "Rollladen", "Dikdik", "Glanz", "Zahnseide", "Flugzeug", "doppelt", "Medusa", "Kartoffel", "Bürgersteig", "Trinkgeld", "Tacker", "Waschbrettbauch", "Schallplatte", "Reißverschlussverfahren", "Wasserhahn", "Robin Hood", "fleischfressend", "Tierfutter", "Kiste", "Halbleiter", "Schmied", "Lichtschalter", "melken", "differenzieren", "Rückspiegel", "Gnom", "Palme", "Bruce Lee", "Schacht", "Rübe", "Serviette", "Schubkarre", "Nebel", "Queue", "Hälfte", "Grippe", "Müller", "Vorschlaghammer", "Gummiwürmchen", "Wirbelsäule", "Eierschachtel", "Gold", "Königin", "Schamesröte", "Schuh", "Falte", "Chewbacca", "Cowboy", "Community", "Trommel", "Murmeltier", "Angry Birds", "zusammenbrechen", "Tentakel", "Sonnenbrille", "Lebkuchenhaus", "drehen", "Bagel", "Pfau", "Kontinent", "Bergkette", "Finger", "Haarspange", "Mopp", "Pinocchio", "Erdmännchen", "Gefahr", "Schleifpapier", "Vlogger", "Fächer", "Nerd", "Verkehr", "William Shakespeare", "abheben", "Fahrwerk", "Darwin", "Ratatouille", "Bank", "Finn und Jake", "Lexikon", "Server", "Tierarzt", "Cappuccino", "Lüfter", "Tischtennisschläger", "Toast", "Komiker", "Sandkasten", "voll", "Hackbraten", "Rechen", "Hippie", "Wasserpfeife", "Chinchilla", "Brunnen", "Anhänger", "Akne", "Hollywood", "Captain America", "Gummibärchen", "Beethoven", "Schleife", "Eigelb", "gut", "Fischgräte", "Blumenstrauß", "Öl", "Außerirdischer", "Zunge", "Schmetterling", "Daffy Duck", "Anführer", "Waschstraße", "Leonardo DiCaprio", "Patrone", "nähen", "Kruste", "Leder", "Frosch", "spielen", "Schwan", "Onkel", "Krake", "Kuchen", "Kristall", "Snowboard", "Distanz", "Kupfer", "Grotte", "Symphonie", "Kuppel", "Triebwerk", "Kastagnetten", "Pinguin", "Karaoke", "Windrad", "Fata Morgana", "Helm", "Hütte", "Tochter", "Küstenwache", "Nickel", "Spaghettieis", "Parkuhr", "Universität", "Magie", "Maus", "Rasiermesser", "Konversation", "Amsterdam", "taub", "Bill Gates", "Punker", "Thor", "hypnotisieren", "Nonne", "Pfote", "Kabine", "tropisch", "Diagramm", "Student", "Fackel", "Laktoseintoleranz", "suchen", "Brokkoli", "berühren", "Kurzschluss", "Blüte", "Odysseus", "Hundehütte", "Posaune", "Wäschespinne", "Gasmaske", "Aufzug", "Margarine", "asymmetrisch", "Skype", "Baby", "Pistazie", "Pinzette", "Klavier", "Sturz", "Würfelqualle", "Schwein", "Wetterfrosch", "Busfahrer", "Programmierer", "Stau", "Suezkanal", "Haarspray", "Island", "Zebrastreifen", "Gangster", "Gumball", "Tiger", "Journalist", "Albatros", "Hängebauchschwein", "Schwamm", "Mount Everest", "Wohlstand", "Bowling", "Animation", "Fechten", "Kunde", "Realität", "Asterix", "Tau", "schnorcheln", "grün", "Kaltwachsstreifen", "Gewalt", "Zauberstab", "Metall", "Rettich", "Sprudel", "Maikäfer", "Saxofon", "Bargeld", "Höhlenforscher", "Fahrrad", "spucken", "Kopflaus", "elektrisch", "saufen", "Fuß", "Artist", "schielen", "Keller", "Storch", "Orchidee", "Bauernhof", "Geschirrschrank", "Ohrring", "prokrastinieren", "erinnern", "Frankreich", "Geysir", "Bleistift", "Vault boy", "Oberarm", "dürr", "langsam", "Suppenkelle", "Spirale", "Vorstellungskraft", "Strauß", "Ikea", "Schublade", "brüllen", "Spiel", "Form", "Geldbeutel", "hart", "Schwerkraft", "Speck", "Lavendel", "Grubenarbeiter", "Abschleppwagen", "sanft", "Kokon", "Essen", "Ägypten", "Meteorit", "Glück", "Vene", "Schiffstaufe", "Schinken", "Harpune", "Abflussrohr", "Nagellack", "Dumbo", "Möwe", "Saftpresse", "Heiße Schokolade", "Slinky", "Family Guy", "Erbsen", "Berg", "Frühstück", "Mammut", "Lippenstift", "Cupcake", "Zoo", "Elster", "Reisender", "Zuckerwatte", "Kürbis", "Badekappe", "Scheidung", "Halbkreis", "geizig", "Zylinder", "Bedienung", "Grafik", "Parfüm", "Müllabfuhr", "Schneeballschlacht", "Korkenzieher", "Sandburg", "Fernbedienung", "Sandsturm", "Matsch", "Michael Jackson", "massieren", "Bock", "Hals", "Eminem", "Archäologe", "Katapult", "Tasmanischer Teufel", "Filter", "Kino", "gelb", "Poker", "Delle", "Baumwolle", "Punkt", "Tennisschläger", "Tragfläche", "Australien", "Straßensperre", "Glühwürmchen", "Biologie", "rutschig", "Smaragd", "Schraube", "Wald", "Fehler", "Scharfschütze", "Atlantis", "Unterschrift", "Mohn", "Tintenfisch", "Wachs", "Geschlecht", "Ruhe", "Kanone", "Villa", "Bushaltestelle", "Tischplatte", "Waffe", "Windschutzscheibe", "Grapefruit", "Wildnis", "Knallfrosch", "Regenwald", "Samen", "Kronkorken", "Einbahnstraße", "Locher", "Katalog", "Restaurant", "Internet", "Stephen Hawking", "knien", "Jazz", "Kamin", "Vermieter", "Nadel", "Notizbuch", "Salat", "Schaufel", "Stöpsel", "Zitrone", "Fritten", "Schweden", "Athlet", "U-Boot", "Zahnstein", "tauchen", "Pepsi", "Ringelschwanz", "Knoblauch", "Terrarium", "Äquator", "Zecke", "Simon and Garfunkel", "Vanille", "Emu", "Stempel", "Bumerang", "flüstern", "sperren", "Puppenhaus", "Jetski", "Lorbeeren", "Kegel", "Invasion", "klebrig", "Verpackung", "Bogenschütze", "Rampe", "Dessert", "Pfütze", "Atomuhr", "Altweibersommer", "drinnen", "Sprecher", "Anfänger", "Gandhi", "Kim Kardashian", "Lebkuchen", "Genie", "Zorro", "Kommunismus", "Ritter", "Hüpfkästchen", "Kerzenständer", "Telefonkabel", "Stachelrochen", "Doktor", "Stinktier", "Badezimmer", "Ehefrau", "Turmalin", "Zeuge", "Irland", "Fabrik", "Dachs", "Altglascontainer", "Stirn", "Quartal", "müde", "Gürtel", "Schleichwerbung", "Mond", "flach", "Big Ben", "Gefrierschrank", "Festung", "Aristokrat", "Cat Woman", "Haken", "Schreibfeder", "Fingerpuppe", "Kazoo", "Gully", "Brathering", "Winzer", "Niederlande", "Geld", "fallen", "Zuckerguss", "Schiffswrack", "Pringles", "Morty", "Osten", "Madagaskar", "Seekuh", "Vegetarier", "Roman", "Zimmerpflanze", "Prinzessin", "Motherboard", "Kätzchen", "Drucker", "Militär", "Pferd", "Narr", "Sturm", "Arbeiter", "Lederhose", "Apfelkern", "Wurzel", "Spion", "Sonntag", "Indianer", "Pasta", "Biotonne", "Operation", "Gentleman", "Äffchen", "verwirrt", "flüssig", "Pu der Bär", "Antivirus", "Golf", "Finn", "Ohrwurm", "Steuergerät", "Schlafanzug", "Ball", "farbenblind", "Staudamm", "Engel", "Zelda", "Blatt", "Asche", "Seewolf", "Minigolf", "Horizont", "Abschluss", "Nessie", "Widerstand", "Tyrannosaurus Rex", "Flash", "Keim", "Spielplatz", "Kerzenleuchter", "Speichel", "Ratte", "Grill", "Prisma", "Sandbank", "Johnny Bravo", "Alarm", "Bankier", "Opernhaus Sydney", "jagen", "Autor", "Reflexion", "Zweig", "Fühler", "Feuersalamander", "Gourmet", "Sieg", "Notizblock", "Pinienkerne", "Biss", "Kitesurfen", "Zwerg", "Paintball", "Oval", "Aufnahme", "Recycling", "Schraubenschlüssel", "Stangenbrot", "Lächeln", "book", "glass", "Sicherheitsnadel", "Mandel", "Bücherwurm", "erfrieren", "Tails", "Turm", "Grille", "Jesus Christ", "cell", "westlich", "Burgruine", "verrückt", "Orca", "Nachthemd", "Dreck", "laufen", "Tresorraum", "Nichtschwimmer", "Jackie Chan", "Experiment", "Spüllappen", "Magnet", "Eisbär", "Grabmal"]

wl.sort(key=len)


d = webdriver.Chrome(ChromeDriverManager().install())
d.get("https://skribbl.io/")
d.set_window_size(1500, 1080)
d.set_window_position(0, 0)
d.find_element(By.ID, "inputName").send_keys("Bodwin")
Select(d.find_element(By.ID, "loginLanguage")).select_by_visible_text("German")

go = webdriver.Chrome(ChromeDriverManager().install())
go.get("https://google.com/")
go.set_window_size(1200, 800)
go.set_window_position(1500, 0)

farben = ["FFFFFF", "000000", "C1C1C1", "4C4C4C", "EF130B", "740B07", "FF7100", "C23800", "FFE400", "E8A200", "00CC00", "005510", "00B2FF", "00569E", "231FD3", "0E0865", "A300BA", "550069", "D37CAA", "A75574", "A0522D", "63300D"]

def nearest_color(pCol):
    pR = int(pCol[0:2], 16)
    pG = int(pCol[2:4], 16)
    pB = int(pCol[4:6], 16)
    prgb = sRGBColor(pR, pG, pB, True)
    pxyz = convert_color(prgb, XYZColor, target_illuminant='d50')
    plab = convert_color(pxyz, LabColor)
    diff = -1
    at = -1
    for i in range(len(farben)):
        r = int(farben[i][0:2], 16)
        g = int(farben[i][2:4], 16)
        b = int(farben[i][4:6], 16)
        rgb = sRGBColor(r, g, b, True)
        xyz = convert_color(rgb, XYZColor, target_illuminant='d50')
        lab = convert_color(xyz, LabColor)
        ak_diff = delta_e_cie2000(plab, lab)
        if diff == -1 or ak_diff < diff:
            diff = ak_diff
            at = i
    return at

def findeErstes(wla, bu=0, bo=len(wl) - 1):
    if bu <= bo:
        mid = (bu + bo) // 2
        if len(wl[mid]) > wla:
            return findeErstes(wla, bu, mid - 1)
        elif len(wl[mid]) < wla:
            return findeErstes(wla, mid + 1, bo)
        elif len(wl[mid]) == wla:
            res = mid
            while(len(wl[res]) == wla):
                res -= 1
            return res + 1
    else:
        return bu

def findeErstesMit(st, lett, wla):
    print(bs)
    inx = st
    while len(wl[inx]) == wla and inx < len(wl):
        print(wl[inx])
        match = True
        for elem in lett:
            if wl[inx][elem[1]] != elem[0]:
                match = False
        if match == True:
            return inx
        inx += 1
    return -1




def search_google(num=0):

    images_url = ""

    # open browser and begin search
    elements = go.find_elements(By.CLASS_NAME, 'rg_i')

    e = elements[num]
    
    # get images source url
    e.click()
    time.sleep(0.2)
    element = go.find_elements(By.CLASS_NAME, 'v4dQwb')

    # Google image web site logic
    if num == 0:
        big_img = element[0].find_element(By.CLASS_NAME, 'n3VNCb')
    else:
        big_img = element[1].find_element(By.CLASS_NAME, 'n3VNCb')

    images_url = str(big_img.get_attribute("src"))

    return images_url


def draw():
    webdriver.ActionChains(d, duration=0).move_by_offset(x, y).click().perform()
    webdriver.ActionChains(d, duration=0).move_by_offset(-x, -y).perform()
def down():
    global y
    y += 8
def up():
    global y
    y -= 8
def left():
    global x
    x -= 8
def right():
    global x
    x += 8
def color(n):
    if n % 2 == 0:
        d.find_element(By.XPATH, "//*[@id=\"containerBoard\"]/div[2]/div[2]/div[1]/div[" + str(n / 2 + 1) + "]").click()
    else:
        d.find_element(By.XPATH, "//*[@id=\"containerBoard\"]/div[2]/div[2]/div[2]/div[" + str((n - 1) / 2 + 1) + "]").click()

while True:
    x = 300
    y = 200
    try:
        if len(d.find_element(By.ID, "currentWord").text) != len(word):
            stelle = -1
    except Exception as e:
        stelle = -1
    try:
        word = d.find_element(By.ID, "currentWord").text
    except Exception as e:
        word = ""

    url = ""
    if "_" not in word and word != "":
        nv = True
        url = ""
        count = 0
        search_url = f"https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&q={word}+clipart+png"
        go.get(search_url)
        flag = True
        while count < 30 and flag == True:
            try:
                url = search_google(count)
                urllib.request.urlretrieve(url, "source.png")
                im = Image.open("source.png")
                gr = max(im.size[0], im.size[1])
                bIm = Image.new("RGBA", (gr, gr), "white")
                bIm.paste(im, (int((gr - im.size[0]) / 2), int((gr - im.size[1]) / 2)))
                bIm.save("source.png")
                im = Image.open("source.png")
                sq = 50
                reIm = im.resize((sq, sq))
                reIm.save("source.png")
                reIm.save("output.png")
                flag = False
            except Exception as e:
                print(e)
            if not validators.url(url):
                flag = True
            count += 1
        
        if not validators.url(url):
            im = Image.open("error.png")
            im.save("source.png")
            im.save("output.png")
            continue

        i = Image.open("source.png")
        p = i.load()

        i2 = Image.open("output.png")
        p2 = i2.load()
        
        h = i.height
        w = i.width

        print("Vermutliche Dauer: " + str(int(50 ** 2 * TPP)) + " Sekunden")
        try:
            d.find_element(By.ID, "buttonClearCanvas").click()
            for i in range(h):
                for j in range(w):
                    print("Vermutliche Restdauer: " + str(int(50 ** 2 * TPP) - (i * w + j) * TPP + 1) + " Sekunden")
                    try:
                        if (p[j, i][0], p[j, i][1], p[j, i][2]) != (255, 255, 255) and (len(p[j, i]) == 3 or p[j, i][3] > 0):
                            r = hex(p[j, i][0]).replace("0x", "")
                            g = hex(p[j, i][1]).replace("0x", "")
                            b = hex(p[j, i][2]).replace("0x", "")
                            if len(r) == 1:
                                r = "0" + str(r)
                            if len(g) == 1:
                                g = "0" + str(g)
                            if len(b) == 1:
                                b = "0" + str(b)
                            nc = nearest_color("".join([r, g, b]))
                            p2[j, i] = (int(farben[nc][0:2], 16), int(farben[nc][2:4], 16), int(farben[nc][4:6], 16), 255)
                            if nc > 0:
                                try:
                                    color(nc)
                                    draw()
                                except Exception as e:
                                    print(e)
                                    break
                    except Exception as e:
                        print(p[j, i])
                    right()
                down()
                for j in range(50):
                    left()
                i2.save("output.png")
            time.sleep(15)
        except Exception as e:
            print("Ne")
    elif word != "":
        l = len(word)
        bs = []
        if word != "_" * l:
            for i in range(l):
                if word[i] != "_":
                    obj = (word[i], i)
                    bs.append(obj)
        if stelle == -1:
            stelle = findeErstes(l)
            print(str(stelle))
        stelle = findeErstesMit(stelle, bs, l)
        print(str(stelle))
        if stelle != -1:
            d.find_element(By.ID, "inputChat").send_keys(wl[stelle])
            d.find_element(By.ID, "inputChat").send_keys(Keys.RETURN)
        stelle += 1
        time.sleep(1.5)