import string

students = [
{"name": " Ana García ", "grade": "8", "status":"aprobado"},
{"name": "pedro lópez", "grade": "4", "status":"DESAPROBADO"},
{"name": "MARÍA FERNÁNDEZ", "grade": "10", "status":"Aprobado"},
{"name": "ana garcía", "grade": "9", "status":"aprobado"},
{"name": None, "grade": "7", "status": "aprobado"},
{"name": "Luis Martínez ", "grade": None, "status":"aprobado"},
{"name": " carlos RUIZ", "grade": "6", "status":"aprobado"},
{"name": "PEDRO LÓPEZ ", "grade": "3", "status":"desaprobado"},
{"name": " ", "grade": "5", "status": "aprobado"},
{"name": "María Fernández", "grade": "7", "status":"APROBADO"},
{"name": "Sofía Torres", "grade": "9", "status":"Aprobado"},
{"name": " sofía torres ", "grade": "8", "status":"aprobado"},
{"name": "Carlos Ruiz", "grade": "6", "status":"APROBADO"},
{"name": "Roberto Díaz", "grade": "absent", "status":"ausente"},
{"name": "roberto díaz", "grade": "", "status":"Ausente"},
{"name": None, "grade": None, "status": None},
{"name": "Laura Méndez", "grade": "7", "status":"aprobado"},
{"name": " laura méndez", "grade": "8", "status":"Aprobado"},
{"name": "GABRIELA RÍOS", "grade": "5", "status":"aprobado"},
{"name": "gabriela ríos ", "grade": "4", "status":"Desaprobado"},
]

students_clean = []
for student in students:
    name = student ["name"]
    grade = student ["grade"]
    if name != None and name.strip() != "" and grade != None and grade.isdigit():
        actualizo = False
        student_clean = {"name": name.strip().title(), "grade": grade, "status": student ["status"].strip().title()}
        for studentt in students_clean:
            if studentt ["name"] == student_clean ["name"]:
                if int (student_clean ["grade"]) > int (studentt ["grade"]):
                    studentt ["grade"] = student_clean ["grade"]
                actualizo = True
                break
        if not actualizo:
            students_clean.append(student_clean)

students_clean.sort(key=lambda x: x["name"])

print ("Registro limpio de alumnos:")
print ("-" * 50)
print (f"{'Nombre':19} {'Nota':9} {'Estado'}")
for student in students_clean:
    name = student ["name"]
    grade = student ["grade"]
    print (f"{name}{" " * (20 - len(name))}{grade}{" " * (10 - len(grade))}{student ['status']}")
