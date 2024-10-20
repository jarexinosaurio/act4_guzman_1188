("")
("guzman guzman")
("")
#diccionario con palabras
traductor = {
#las palabras
"garcias":"thank you",
"dinosaurio":"dinosaur",
"cafe":"coffe"

}
p=input("introduce una palabra en español:").strip().lower()#pide la palabra
if p in traductor:
    t=traductor[p]
#imprime en pantalla
    print("introdusca la trauccion de la palabra",p,"es",t,"en ingles")
else:#sino
    print("esa apalbara no se encuentra")#error si la palabra no se encuentra





