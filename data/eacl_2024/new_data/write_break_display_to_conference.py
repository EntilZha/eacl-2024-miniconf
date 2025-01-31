import json

# 读取break.json文件
with open('data/eacl_2024/new_data/break_display.json', 'r') as break_display_file:
    break_display_data = json.load(break_display_file)

# 读取conference.json文件
with open('data/eacl_2024/new_data/conference.json', 'r') as conference_file:
    conference_data = json.load(conference_file)

# 将break.json数据写入conference.json的events字段
for event_id, event_data in break_display_data.items():
    conference_data['sessions'][event_id] = event_data

# 将更新后的数据写入conference.json文件
with open('data/eacl_2024/new_data/conference.json', 'w') as conference_file:
    json.dump(conference_data, conference_file, indent=4)

print("数据已成功写入conference.json文件的sessions字段。")