posts = [   
    "Arrancando el lunes con energía #Motivación #NuevaSemana",
    "Terminé mi primer proyecto en Python #Python #Programación #OrgullosoDeMi",
    "No puedo creer el final de la serie #SinSpoilers #SerieAdicta",
    "Nuevo video en el canal sobre #InteligenciaArtificial y #Python",
    "Entrenamiento de hoy completado #Fitness #Motivación #NoPainNoGain",
    "Leyendo sobre #InteligenciaArtificial y el futuro del trabajo #Tecnología",
    "Arranqué a estudiar #Programación por mi cuenta #Python #Autodidacta",
    "Finde de lluvia, maratón de series #SerieAdicta #Relax",
    "Workshop de #InteligenciaArtificial en la universidad #Tecnología #Programación"


]
hashtags = []
for post in posts:
    for word in post.split():
        if word.startswith("#"):
            hashtags.append(word)


ya_mencionados = []
print ("Hashtags trending (Mas de una aparicion): ")
for hashtag in hashtags:
    if not ya_mencionados.__contains__(hashtag):
        ya_mencionados.append(hashtag)
        if hashtags.count(hashtag) > 1:
            print (f"   {hashtag}: {hashtags.count(hashtag)}")
print ()
print (f"Total de hashtags unicos: {len(ya_mencionados)}")