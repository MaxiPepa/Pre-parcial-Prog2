def list_compare(list1, list2):
    common_elements = 0
    for element in list1:
        for index in range(len(list2)):
            if element == list2[index]:
                common_elements += 1
    
    if common_elements >= 2:
        return print("Parecidas")
    else:
        return print("No coinciden")

# Prueba listas parecidas

listaNombres1 = ["Marcos", "Emilio", "Ramiro", "Juana"]
listaNombres2 = ["Emilio", "Juan", "Roberta","Elvira","Marcos"]

list_compare(listaNombres1, listaNombres2)

# Prueba listas que no coinciden

listaApellidos1 = ["Pepa", "López", "Ramirez"]
listaApellidos2 = ["Romero", "Pepa", "Ordóñez", "Miralles"]

list_compare(listaApellidos1, listaApellidos2)