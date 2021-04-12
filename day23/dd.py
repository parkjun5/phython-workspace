record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

lists = []


for cords in record:
    
    info = { 'Id': '',
            'nickname' : '',
            'act' : ''}
    cord = cords.split(" ")
    if cord[0] == "Enter" :

        for list_info in lists:
            if list_info['Id'] == cord[1]:
                list_info['nickname'] = cord[2]

        info['Id'] = cord[1]
        info['nickname'] = cord[2]
        info['act']  = "들어왔습니다."
        lists.append(info)

    elif cord[0] == "Leave" :

        info['Id'] = cord[1]
        for list_info in lists:
            if list_info['Id'] == cord[1]:
                info['nickname'] = list_info['nickname']
                break
        info['act']  = "나갔습니다."
       
        lists.append(info)
        

    elif cord[0] == "Change" :
        lists[cord[1]] = cord[2]
    
answer = []
for message in lists:
    answer.append("{0}님이 {1}".format(message['nickname'], message['act']))

