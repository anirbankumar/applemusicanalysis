import csv
import datetime

user_year = int(input('What year do you want data for: '))

Singers = {}

print('searching...')

#put full path to csv file here

with open('/Users/anirban/Desktop/playing_activity.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    extracted = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    line_count = 0

    for row in csv_reader :
        if line_count == 0:
            line_count += 1
        else:
            time = row[13]

            if user_year == int(time[0:4]):
                try:
                    Singers[str(row[2])]
                except:
                    Singers[str(row[2])] = 0
                finally:
                    Singers[str(row[2])] = (Singers[str(row[2])] + 1)
            else:
                continue
            line_count += 1

singer_name = ""
listens = 0
while singer_name != str(-1):
    singer_name = input('Enter a singer\'s name (enter -1 to view everyone): ')
    try:
        listens = Singers[singer_name]
        print('You listened to ' + singer_name + ', ' + str(listens) + ' times')
    except:
        listens = 0
        if singer_name != str(-1):
            print('You either haven\'t listened to ' + singer_name + ' or misspelled the artist\'s name')
    #finally:
print("here is breakdown of everyone in the yesr " + str(user_year))


for k,v in Singers.items():
    print(k, '->', v)

