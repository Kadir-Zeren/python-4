fruit = "Orange"

print("Word:",fruit)

print("First Letter:",fruit[0])

print(fruit[1:4])

print(fruit[:])

print(fruit[:5])


text = "abcdefghi"


print(text[1:8])

print(text[1:8:2])

print(text[1::3])

print(text[::2])

print(text[5:1:-1])

print(text[::-1])

print("python candi"[2:10:2])

text= "kayak"

print(text == text[::-1])

text = "abcdefghi"

print(text[-1])

print(text[-3:-1])

print(text[-1]==text[8])

print(text[::-1])

print(text[-3::-1])

text = "istanbul"

new_text = text[:4] + "n" + text[5:]

print(new_text)

print(len(text))

new_t = text[0] + text[len(text) // 2]+ text[-1]

print(new_t)

print(text, "kelimesinin uzunluğu", len(text))

print(* text)


name = "ahmet"

print("mehrba, %s" %name)

age = 43
meslek = "contect creator"

print("merhabai ismin %s yaşın %d meslegin ise %s" %(name,age,meslek))

age = 43.5
print("merhabai ismin %s yaşın %f meslegin ise %s" %(name,age,meslek))

name = "ahmet"
age = 43
meslek = "contect creator"

print("merhaba ismin {} yaşın {} meslegin ise {}" .format(name,age,meslek))

print("merhaba ismin {2} yaşın {0} meslegin ise {1}" .format(age,meslek,name))

print("merhaba ismin {a} yaşın {b} meslegin s ise {c}" .format(b=age,c=meslek,a=name))

print("merhaba ismin {} yaşın {b} meslegin s ise {c}" .format(name,b=age,c=meslek))

print("merhaba ismin {} yaşın {b} meslegin s ise {c}" .format(name,c=meslek,b=age))

taban = 6
yukseklik = 4
print("hesaplama {}".format(taban*yukseklik/2))


name = "ahmet"
age = 43
meslek = "contect creator"

print(f"merhaba benim adim {name} yasim {age} mesleğim {meslek}")

print(f"hesaplama {taban*yukseklik/2}")

name = "MARIAM"
print(f"My name is {name.capitalize()}")

print(f"saga hizlama {name:>20}")

print(f"saga hizlama {name:<20}")

print(f"saga hizlama {name:^20}")

print(f"saga hizlama {name:*^20}")

name = "susan"
age = "young"
gender = "lady"
print(F"{name} {gender} {age}")
