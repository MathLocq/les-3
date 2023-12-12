import webbrowser

keuze = str(input("wil je zoeken op personnage of seizoen? "))

if keuze == "personnage":
    character = str(input("Welk personnage zoek je? "))
    link = "https://rickandmortyapi.com/api/character/?name=" + character
  

if keuze == "seizoen":
    seizoen = int(input("naar welk seizoen bent u op zoek? (antwoord met nummer) "))
    if seizoen < 10:
        converted_seizoen = str(seizoen)
        link = "https://rickandmortyapi.com/api/episode/?episode=S0" + converted_seizoen
    if seizoen > 10:
        converted_seizoen = str(seizoen)
        link = "https://rickandmortyapi.com/api/episode/?episode=S" + converted_seizoen
    else:
        print("Er werd een ongeldig nummer opgegeven")     

webbrowser.open(link)

