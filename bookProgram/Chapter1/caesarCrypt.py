def caesarCrypt(type: str, movement:int, content: str):

    crypt_1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
               'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    crypt_2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
               'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    if type == 'E' and movement >= 0:
        crypt_target1 = crypt_1[movement:] + crypt_1[:movement]
        crypt_target2 = crypt_2[movement:] + crypt_2[:movement]
    elif type == 'D' and movement >= 0:
        crypt_target1 = crypt_1[-movement:] + crypt_1[:-movement]
        crypt_target2 = crypt_2[-movement:] + crypt_2[:-movement]
    else:
        return None

    crypy_dic = {}
    for i in range(len(crypt_2)):
        crypy_dic[crypt_1[i]] = crypt_target1[i]
    for i in range(len(crypt_1)):
        crypy_dic[crypt_2[i]] = crypt_target2[i]

    result = []
    for i in content:
        if i in crypy_dic.keys():
            result.append(crypy_dic[i])
        else:
            result.append(i)
    return ''.join(result)


result = caesarCrypt('D', 2, 'BC bc')
print(result)


