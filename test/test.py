import json

with open('7th-round.json', 'r', encoding='utf-8') as data:
    aaa = json.load(data)
    empty_tid = []
    for item in aaa:
        if item['tid'] == '39':
            print(item)
        if len(item['different']) == 0:
            empty_tid.append(item['tid'])
    with open('empty_tid.txt', 'w', encoding='utf-8') as file:
        file.write(json.dumps(empty_tid, ensure_ascii=False))
    # print(empty_tid)
