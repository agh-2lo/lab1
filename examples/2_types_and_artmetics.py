# Bedziemy pracowac na dwoch typach danych
# - calkowite (int)
# - zmiennoprzecinkowe (float)

print 3, -2, 3.14159, -2.9

# Typ mozna sprawdzic przy pomocy funkcji type()
# print type(3), type(-2), type(3.14159), type(-2.9)

# Mozna dokonywac konwersji miedzy typami.
# print int(3.14159), int(-2.8)
# print float(3), float(-1)

# Typ float (zmiennoprzecinkowy) ma ograniczona dokladnosc.
# Dokladnie 15 miejsc po przecinku. Maksymalna dokladnosc liczby Pi wynosi:

# print 3.1415926535897932384626433832795028841971

# Chcac dokonywac operacji na tego typu liczbach trzeba pamietac
# ze podnoszac wartosc pi^2 (do kwadratu) uzyskamy jedynie wartosc przyblizona
# nie dokladna.


# Dostepne operacje artmetyczne:
# + dodawanie
# - odejmowanie
# * mnozenie
# / dzielenie
# ** potegowanie

# Przy okazji operacji artmetycznych nalezy pamietac na jakich typach danych operujemy
'''
print type( 1 + 3 ) # int
print type( 1 - 3 ) # int
print type( 1 + 3 ) # int
print type( 1 / 3 ) # int, ale zwraca zaokraglenie w dol 
print type( 1 ** 3 ) # int
'''

'''
print type( 1 + 3.1 ) # float
print type( 1 - 3.1 ) # float
print type( 1 + 3.1 ) # float
print type( 1 / 3.1 ) # float
print type( 1 ** 3.1 ) # float
'''

# Podobnie mozemy wypisac wiele operacji oddzielajac je przecinkiem.
# print 1 + 2 * 3, 6 / 3 * 2, 1**0

# Oraz grupowac je nawiasami
# print (1 + 2) * 3, 6 / (3 * 2), 1**0

# Dzielenie przez zero jak zawsze konczy sie koncem swiata
# print 1 / 0



# 
