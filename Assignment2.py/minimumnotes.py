Amount = int(input('Enter the Amount:'))

two_thousand = Amount // 2000
Amount = Amount % 2000

five_hundred = Amount // 500
Amount = Amount % 500

two_hundred = Amount // 200
Amount = Amount % 200

hundred = Amount // 100
Amount = Amount % 100

fifty = Amount // 50
Amount = Amount % 50

twenty = Amount // 20
Amount = Amount % 20

ten = Amount // 10
Amount = Amount % 10

print(f'minimum no. of notes of two_thousand:{two_thousand}, five_hundred:{five_hundred}, two_hundred:{two_hundred}, hundred:{hundred}, fifty:{fifty}, twenty:{twenty}, ten:{ten}')

