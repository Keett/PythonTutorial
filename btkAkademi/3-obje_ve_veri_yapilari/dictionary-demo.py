ogrenciler = {}

ogrenciler = {
    '120': {
        'ad': 'Ali',
        'soyad': 'Yılmaz',
        'telefon': '532 000 00 01'
    },
    '125': {
        'ad': 'Can',
        'soyad': 'Korkmaz',
        'telefon': '532 000 00 02'
    },
    '128': {
        'ad': 'Volkan',
        'soyad': 'Yükselen',
        'telefon': '532 000 00 03'
    },
}

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")

# ogrenciler[number] = {
#     'ad': name,
#     'soyad': surname,
#     'telefon': phone
# }

ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon':phone 
    }
})
"""
number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")

ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon':phone 
    }
})

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")

ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon':phone 
    }
})
"""
print('*'*50)
print(ogrenciler)

ogrNo = input('öğrenci no: ')
ogrenci = ogrenciler[ogrNo]
print(ogrenci)

print(f"Aradığınız {ogrNo} nolu öğrencinin adı: {ogrenci['ad']} soyadı: {ogrenci['soyad']} ve telefonu ise {ogrenci['telefon']}")