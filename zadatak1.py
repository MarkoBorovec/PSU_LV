def total_euro(brojRadnihSati,RadniSati):
    return brojRadnihSati * RadniSati

brojRadnihSati= int(input(' Unesite broj radnih sati '))
RadniSat= float(input('Unesite iznos za jedan radni sat '))

print(f'Radni sati : {brojRadnihSati}')
print(f'eura/h : {RadniSat}')

ukupno = total_euro(brojRadnihSati,RadniSat)

print(f'ukupno:{ukupno} ')