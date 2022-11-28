n = 5
name = ["Harry","Berry","Tina","Akriti","Harsh"]
score = [37.21,37.21,37.2,41,39]

b = []
for i in range(n):
        a = []
        a.append(name[i])
        a.append(score[i])
        b.append(a)
b = sorted(b)
min = 100;
c = 0
for i in range(n):
     if min > b[i][1] :

         if c <=2 :
             if c == 0:
                 c =c+1
             else:
                 print(b[i][0])
                 c = c+ 1
     else:
         exit()