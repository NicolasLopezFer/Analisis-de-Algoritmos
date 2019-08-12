set terminal png size 1024,768

lin1(x)=(a1*x)+b1
sqr1(x)=(c1*(x**2))+(d1*x)+e1
cub1(x)=(f1*(x**3))+(g1*(x**2))+(h1*x)+i1

fit lin1(x) "experimento.txt" using 1:2 via a1,b1
fit sqr1(x) "experimento.txt" using 1:2 via c1,d1,e1
fit cub1(x) "experimento.txt" using 1:2 via f1,g1,h1,i1

lin2(x)=(a2*x)+b2
sqr2(x)=(c2*(x**2))+(d2*x)+e2
cub2(x)=(f2*(x**3))+(g2*(x**2))+(h2*x)+i2

fit lin2(x) "experimento.txt" using 1:3 via a2,b2
fit sqr2(x) "experimento.txt" using 1:3 via c2,d2,e2
fit cub2(x) "experimento.txt" using 1:3 via f2,g2,h2,i2

plot \
  "experimento.txt" using 1:2 with lines title "Bubble", \
  "experimento.txt" using 1:3 with lines title "Insertion", \
  lin1(x) linewidth 3, \
  sqr1(x) linewidth 3, \
  cub1(x) linewidth 3, \
  lin2(x) linewidth 3, \
  sqr2(x) linewidth 3, \
  cub2(x) linewidth 3

## eof
