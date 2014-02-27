entrada = open("xy1.data", "r")
datos = [ map( float, linea.split() ) for linea in entrada ]
print datos(1)


Nclas = raw_input('Cuantas clases requiere: ')  
Nclas = int(Nclas)
y_i = np.array([])
a=1
for i in range(1, Nclas):
 
  for j in range(1, Nclas):
   if a == a: 
    y_i[j][1] = 1 
   else: 
    y_i[j][1] = 0
   a+=1




 
