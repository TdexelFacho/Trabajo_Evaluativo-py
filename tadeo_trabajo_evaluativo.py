lista = []
while True:
 print("ESCOJA UNA DE ESTAS OPCIÓNES")
 print("1) AGREGAR ELEMENTO")
 print("2) BUSCAR ELEMENTO")
 print("3) ORDENAR LISTA ALFABETICAMENTE")
 print("4) ELIMINAR ELEMENTO")
 print("5) SALIR DE LA APP")
 selec_opc = int(input("INGRESE UN NÚMERO: "))
 if selec_opc == 1:
  nom_element = input("INGRESE LO QUE QUIERA: ")
  lista.append(nom_element)
  print(lista)
  print("LISTA SUBIDA")
 elif selec_opc== 2:
    selec_element = input("INGRESE EL ELEMENTO: ")
    if selec_element in lista:
      print("ESTA EN LA LISTA")
    else:
      print("NO ESTÁ EN LA LISTA")
 elif selec_opc == 3:
  lista.sort()
  print(lista)
 elif selec_opc == 4:
  print(lista)
  elim_element = input("INGRESE EL NOMBRE DEL ELEMENTO QUE DESEA ELIMINAR: ")
  lista.remove(elim_element)
  print(lista)
 elif selec_opc == 5:
  print("GRACIAS POR USAR OVANDLIST")
  break
 
 #En este trabajo lo que hice fue crear una lista que agregue tareas, busque y borre los elementos que aparecen en ella.
 #Primero puse el WHILE para hacer un bucle y que se repitan las opciones para qeu se ejecute el programa.
 #Segundo ponemos las opciones y un INPUT para que despues podamos poner el IF para que si se el INPUT es igual a las opcioes se puedea ejecutar
 #Tercero puse que si la opcion es 1 pase al INPUT de nombre nom_element se encarga de ingresar el nombre para que el.append lo pueda agregar a la lista
 #cuarto puse que si la opcion es 2 pase al INPUT de nombre select_element que se encarga de ingresar el el nombre del elemento que esta en la lista y con el IN va a buscar si lo que ingresamos esta o no en la lisa y manda un mensaje si está o no.
 #Quinto puse que si la opcion es 3 con el .sort() ordene la lista alfabeticamente (A-Z)
 #Sexto puse que si la opcion es 4 pase al INPUT de nombre elim_element que se encarga de ingresar el nombre del elemento y con el.remove saca el elemnto que seleccionamos de la lista.
 #Septimo puse que si la opcion es 5 se termine el programa y cierre el bucle de WHILE para que no halla errores en el programa.
