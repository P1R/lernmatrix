import numpy as np 

entradat = open("db.data", "r")
dbanimales = np.array([ map( int, linea.split() ) for linea in entradat ])
z = len(dbanimales) 
print z
entrada1 = open("xy1.data", "r")
xy1 = np.array([ map( int, linea.split() ) for linea in entrada1 ])

entrada2 = open("xy2.data", "r")
xy2 = np.array([ map( int, linea.split() ) for linea in entrada2 ])

entrada3 = open("xy3.data", "r")
xy3 = np.array([ map( int, linea.split() ) for linea in entrada3 ])

entrada4 = open("xy4.data", "r")
xy4 = np.array([ map( int, linea.split() ) for linea in entrada4 ])

entrada5 = open("xy5.data", "r")
xy5 = np.array([ map( int, linea.split() ) for linea in entrada5 ])

entrada6 = open("xy6.data", "r")
xy6 = np.array([ map( int, linea.split() ) for linea in entrada6 ])

entrada7 = open("xy7.data", "r")
xy7 = np.array([ map( int, linea.split() ) for linea in entrada7 ])

y1 = np.r_[1, 0, 0, 0, 0, 0, 0]
y2 = np.r_[0, 1, 0, 0, 0, 0, 0]
y3 = np.r_[0, 0, 1, 0, 0, 0, 0]
y4 = np.r_[0, 0, 0, 1, 0, 0, 0]
y5 = np.r_[0, 0, 0, 0, 1, 0, 0]
y6 = np.r_[0, 0, 0, 0, 0, 1, 0]
y7 = np.r_[0, 0, 0, 0, 0, 0, 1]

entradam = open("memoria.data", "r")
memoria = np.array([ map( int, linea.split() ) for linea in entradam ]) 
for i in xrange(0, 41):
 for j in xrange(0, 15): 
  if xy1[i][j] == 1: 
   memoria [0][j] = 1 + memoria [0][j]
  elif  xy1[i][j] == 0:
   memoria [0][j] = -1 + memoria [0][j]   
for i in xrange(0, 20):
 for j in xrange(0, 15): 
  if xy2[i][j] == 1: 
   memoria [1][j] = 1 + memoria [1][j]
  elif  xy2[i][j] == 0:
   memoria [1][j] = -1 + memoria [1][j]
for i in xrange(0, 5):
 for j in xrange(0, 15): 
  if xy3[i][j] == 1: 
   memoria [2][j] = 1 + memoria [2][j]
  elif  xy3[i][j] == 0:
   memoria [2][j] = -1 + memoria [2][j]
for i in xrange(0, 13):
 for j in xrange(0, 15): 
  if xy4[i][j] == 1: 
   memoria [3][j] = 1 + memoria [3][j]
  elif  xy4[i][j] == 0:
   memoria [3][j] = -1 + memoria [3][j]
for i in xrange(0, 4):
 for j in xrange(0, 15): 
  if xy5[i][j] == 1: 
   memoria [4][j] = 1 + memoria [4][j]
  elif  xy5[i][j] == 0:
   memoria [4][j] = -1 + memoria [4][j]
for i in xrange(0, 8):
 for j in xrange(0, 15): 
  if xy6[i][j] == 1: 
   memoria [5][j] = 1 + memoria [5][j]
  elif  xy6[i][j] == 0:
   memoria [5][j] = -1 + memoria [5][j]
for i in xrange(0, 10):
 for j in xrange(0, 15): 
  if xy7[i][j] == 1: 
   memoria [6][j] = 1 + memoria [6][j]
  elif  xy7[i][j] == 0:
   memoria [6][j] = -1 + memoria [6][j]
print memoria
cont = 0
cony1 = 0
cony2 = 0 
cony3 = 0
cony4 = 0
cony5 = 0
cony6 = 0
cony7 = 0
entradat = open("xy1.data", "r")  
for linea in entradat:
 db = np.array( [ map( int, linea.split() ) ] ) 
 db = db.transpose()
 clase = np.dot(memoria,db)
 aux= clase.max()
 for i in xrange(0, 7):
  if clase[i][0] == aux:
   clase [i][0] = 1
  elif clase[i][0] < aux:
   clase [i][0] = 0
 clase = clase.transpose()
 if np.all(clase == y1) == True:
  cont += 1
  cony1 += 1
entradat = open("xy2.data", "r")  
for linea in entradat:
 db = np.array( [ map( int, linea.split() ) ] ) 
 db = db.transpose()
 clase = np.dot(memoria,db)
 aux= clase.max()
 for i in xrange(0, 7):
  if clase[i][0] == aux:
   clase [i][0] = 1
  elif clase[i][0] < aux:
   clase [i][0] = 0
 clase = clase.transpose()
 if np.all(clase == y2) == True:
  cont += 1
  cony2 += 1
entradat = open("xy3.data", "r")  
for linea in entradat:
 db = np.array( [ map( int, linea.split() ) ] ) 
 db = db.transpose()
 clase = np.dot(memoria,db)
 aux= clase.max()
 for i in xrange(0, 7):
  if clase[i][0] == aux:
   clase [i][0] = 1
  elif clase[i][0] < aux:
   clase [i][0] = 0
 clase = clase.transpose()
 if np.all(clase == y3) == True:
  cont += 1
  cony3 += 1
entradat = open("xy4.data", "r")  
for linea in entradat:
 db = np.array( [ map( int, linea.split() ) ] ) 
 db = db.transpose()
 clase = np.dot(memoria,db)
 aux= clase.max()
 for i in xrange(0, 7):
  if clase[i][0] == aux:
   clase [i][0] = 1
  elif clase[i][0] < aux:
   clase [i][0] = 0
 clase = clase.transpose()
 if np.all(clase == y4) == True:
  cont += 1
  cony4 += 1  
entradat = open("xy5.data", "r")  
for linea in entradat:
 db = np.array( [ map( int, linea.split() ) ] ) 
 db = db.transpose()
 clase = np.dot(memoria,db)
 aux= clase.max()
 for i in xrange(0, 7):
  if clase[i][0] == aux:
   clase [i][0] = 1
  elif clase[i][0] < aux:
   clase [i][0] = 0
 clase = clase.transpose()
 if np.all(clase == y5) == True:
  cont += 1
  cony5 += 1
entradat = open("xy6.data", "r")  
for linea in entradat:
 db = np.array( [ map( int, linea.split() ) ] ) 
 db = db.transpose()
 clase = np.dot(memoria,db)
 aux= clase.max()
 for i in xrange(0, 7):
  if clase[i][0] == aux:
   clase [i][0] = 1
  elif clase[i][0] < aux:
   clase [i][0] = 0
 clase = clase.transpose()
 if np.all(clase == y6) == True:
  cont += 1
  cony6 += 1
entradat = open("xy5.data", "r")  
for linea in entradat:
 db = np.array( [ map( int, linea.split() ) ] ) 
 db = db.transpose()
 clase = np.dot(memoria,db)
 aux= clase.max()
 for i in xrange(0, 7):
  if clase[i][0] == aux:
   clase [i][0] = 1
  elif clase[i][0] < aux:
   clase [i][0] = 0
 clase = clase.transpose()
 if np.all(clase == y7) == True:
  cont += 1
  cony7 += 1  
print cont, cony1, cony2, cony3, cony4, cony5, cony6, cony7

x = raw_input('Da los parametros de un animal: ')
x = np.array([ map ( int, x.split() ) ])
x = x.transpose()
clase = np.dot(memoria,x)
aux= clase.max()
for i in xrange(0, 7):
 if clase[i][0] == aux:
  clase [i][0] = 1
 elif clase[i][0] < aux:
  clase [i][0] = 0
clase = clase.transpose()
if np.all(clase == y7) == True:
 print "pertenece a la clase 7"
elif np.all(clase == y6) == True:
 print "pertenece a la clase 6"
elif np.all(clase == y5) == True:
 print "pertenece a la clase 5"
elif np.all(clase == y4) == True:
 print "pertenece a la clase 4"
elif np.all(clase == y3) == True:
 print "pertenece a la clase 3"
elif np.all(clase == y2) == True:
 print "pertenece a la clase 2"
elif np.all(clase == y1) == True:
 print "pertenece a la clase 1"	


 


















