print("8.6 City names")
def city_country(city, country):
    print(city+', '+ country)
city_country("Quito", "Ecuador")
city_country("Bogota", "Colombia")
city_country("Lima", "Peru")

print("\n8.7 Album")
def make_album(artist_name, album_title, number_tracks = ''): 
    music_album = {} 
    music_album = {'artist': artist_name, 'album': album_title}
    music_album['tracks'] = number_tracks
    return music_album

while True: 
    print("Your can quit whenever you want: q")
    nombre_artista = input("ingrese el nombre del artista")
    if nombre_artista == 'q':
        break
    nombre_album = input("ingrese el nombre del album")
    if nombre_album == 'q':
        break
    numero_tracks = input("ingrese el numero de tracks del album")
    if numero_tracks == 'q':
        break
    
    print(make_album(nombre_artista, nombre_album, numero_tracks))
    