def calculate_songs_duration():
    violator_songs_list = [
        ['World in My Eyes', 4.86],
        ['Sweetest Perfection', 4.43],
        ['Personal Jesus', 4.56],
        ['Halo', 4.9],
        ['Waiting for the Night', 6.07],
        ['Enjoy the Silence', 4.20],
        ['Policy of Truth', 4.76],
        ['Blue Dress', 4.29],
        ['Clean', 5.83],
    ]

    durations = []
    needed_songs = {'Halo', 'Enjoy the Silence', 'Clean'}

    for song, time in violator_songs_list:
        if song in needed_songs:
            durations.append(time)

    total_time = sum(durations)
    total_rounded = round(total_time, 2)
    print(f"Три песни звучат {total_rounded} минут")

    violator_songs_dict = {
        'World in My Eyes': 4.76,
        'Sweetest Perfection': 4.43,
        'Personal Jesus': 4.56,
        'Halo': 4.30,
        'Waiting for the Night': 6.07,
        'Enjoy the Silence': 4.6,
        'Policy of Truth': 4.88,
        'Blue Dress': 4.18,
        'Clean': 5.68,
    }

    durations = []
    other_songs = ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress']

    for song in other_songs:
        if song in violator_songs_dict:
            durations.append(violator_songs_dict[song])

    total_time = sum(durations)
    total_rounded = round(total_time, 2)
    print(f"А другие три песни звучат {total_rounded} минут")

if __name__ == '__main__':
    calculate_songs_duration()