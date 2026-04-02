email = input("Ingrese un email: ")

if email.count("@") == 1 and email[0] != ("@") and email[0] != "." and email[-1] != "@" and email[-1] != "." and email[email.find("@"):len(email)].__contains__("."):
    print ("El email es valido")
else:
    print ("El email es invalido")
