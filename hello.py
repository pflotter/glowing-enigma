keys = ['userLimit', 'serviceLimit', 'duration']
values = input().split()
data = dict(zip(keys, values))


users = {}
users['reqN'] = ['-1'] * int(data['serviceLimit'])

while True:
    req = input().split()

    if '-1' not in users['reqN'] and (int(req[0]) - int(users['reqN'][0])) < int(data['duration']):
        if req[0] == '-1':
            break
        print(503)
        continue
    if req[0] == '-1':
        break
    elif req[1] not in users:
        users[req[1]] = ['-1'] * int(data['userLimit'])
        users[req[1]][0] = req[0]

        if '-1' in users['reqN']:
            for i in range(len(users['reqN'])):
                if users['reqN'][i] == '-1':
                    users['reqN'][i] = req[0]
                    break
        else:
            users['reqN'][len(users['reqN']) - 2], users['reqN'][len(users['reqN']) - 1] = users['reqN'][len(users['reqN']) - 1], req[0]
        print(200)

    elif req[1] in users:
        if '-1' in users[req[1]]:
            for i in range(len(users[req[1]])):
                if users[req[1]][i] == '-1':
                    users[req[1]][i] = req[0]


            if '-1' in users['reqN']:
                for i in range(len(users['reqN'])):
                    if users['reqN'][i] == '-1':
                        users['reqN'][i] = req[0]
                        break
            else:
                users['reqN'][len(users['reqN']) - 2], users['reqN'][len(users['reqN']) - 1] = users['reqN'][len(users['reqN']) - 1], req[0]


            print(200)
        else:
            if int(req[0]) - int(users[req[1]][0]) <= int(data['duration']):
                print(429)
            else:
                users[req[1]][0], users[req[1]][1] = users[req[1]][1], req[0]


                if '-1' in users['reqN']:
                    for i in range(len(users['reqN'])):
                        if users['reqN'][i] == '-1':
                            users['reqN'][i] = req[0]
                            break
                else:
                    users['reqN'][len(users['reqN']) - 2], users['reqN'][len(users['reqN']) - 1] = users['reqN'][len(users['reqN']) - 1], req[0]
                print(200)
