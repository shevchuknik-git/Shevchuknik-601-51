def decode_secret_message():
    secret_message = [
        'квевтфппбщЗстмзалтнмаршг65длгуча',
        'дьсеыблц2бане4т64ь463ущея6втщл6б',
        'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
        'ьд5фму3ежородт9г686буиимыкучшсал',
        'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
    ]

    print(
        secret_message[0][3],
        secret_message[1][9:13],
        secret_message[2][5:15:2],
        secret_message[3][7:13][::-1],
        secret_message[4][16:21][::-1],
        sep=' '
    )

if __name__ == '__main__':
    decode_secret_message()