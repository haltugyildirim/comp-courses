from numpy import * #array kullanmak icin cagirdik
a=[1,2,3,4,5]
print a[2]
a.append(6) #sonuna eleman ekliyor
a.insert(0,7) #insert komutu sadece iki parametreyle calisiyor
print "liste:", a
print "liste uzunlugu:", len(a)
print "liste carpimi:", 2*a
m=[[1,2,3],[4,5,6],[7,8,9]] #array icinde array tanimlayinca matris gibi oluyor.
print "listeyle matris tanimi:", m
print "eleman sayisi:", len(m)
print "Ilk elemani:", m[1]
print "Liste icindeki listenin elemani ya da matrisin ilk elemani:", m[1][1]
b=array([[1.,2.,3.],[4.,5.,6.],[7.,8.,9.]]) #numpy kutuphanesinde array fonksiyonunu kullanma
print "Array fonksiyonuyla tanimlanmis array b:", b
print "Dimension veriyor(b icin) bizim kullanacagimiz seyler(vektorler) hep iki boyutlu:",ndim(b)
print "Shape b arrayi icin", shape(b)
