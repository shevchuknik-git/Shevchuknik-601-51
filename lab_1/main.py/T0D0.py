from math import *

def get_distances():
    sites = {
        'Moscow': (550, 370),
        'London': (510, 510),
        'Peris': (480, 480),
    }
    distance = {}

    cities = list(sites.keys())

    for i in range (len(cities)):
        for j in range (i + 1, len(cities)):
            city_1 = cities[i]
            city_2 = cities[j]

            x1, y1 = (sites[city_1])
            x2, y2 = (sites[city_2])

            dist =  sqrt((x1 - x2)**2 +  (y1 - y2)**2)
            distance[(city_1, city_2)] = dist

    return distance

if __name__ == '__main__':
    print(get_distances())