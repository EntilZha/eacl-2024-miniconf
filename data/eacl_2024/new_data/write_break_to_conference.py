import json

# 读取break.json文件
with open('data/eacl_2024/new_data/break.json', 'r') as break_file:
    break_data = json.load(break_file)

# 读取conference.json文件
with open('data/eacl_2024/new_data/conference.json', 'r') as conference_file:
    conference_data = json.load(conference_file)

# 将break.json数据写入conference.json的events字段
for event_id, event_data in break_data.items():
    conference_data['events'][event_id] = event_data

# 将更新后的数据写入conference.json文件
with open('data/eacl_2024/new_data/conference.json', 'w') as conference_file:
    json.dump(conference_data, conference_file, indent=4)

print("数据已成功写入conference.json文件的events字段。")