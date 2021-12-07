

#--การเข้าถึงข้อมูลภายใน Dictionary--
scores = {'james': 1828, 'thomas': 3628120312312023323323, 'danny': 9310, 'bobby': 4401}

# display data
print('james =>', scores['james'])
print('thomas =>', scores['thomas'])
print('danny =>', scores['danny'])
print('bobby =>', scores['bobby'])


# update data
scores['james'] = scores['james'] + 1000
scores['thomas'] = 100

print('james =>', scores['james'])
print('thomas =>', scores['thomas'])

#---การอ่านค่าใน Dictionary ด้วยคำสั่ง For loop---
countries = {'de': 'Germany', 'ua': 'Ukraine',
             'th': 'Thailand', 'nl': 'Netherlands'}

#---Python Dictionary methods---
countries = {'de': 'Germany', 'ua': 'Ukraine',
             'th': 'Thailand', 'nl': 'Netherlands'}

print(countries.popitem())
print(countries.popitem())

print(countries.items())




