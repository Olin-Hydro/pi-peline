
def parse_line(line):

    data_list = line.split(":")
    data = {}
    if len(data_list) not in (3, 4):
        return None
    data_list = [item.strip().lower() for item in data_list]
    data["type"] = data_list[0]
    data["request"] = data_list[1]
    data["data"] = data_list[2]
        
    if len(data_list) == 4:
        # Task log
        data["data"] = {}
        data["data"]["data"] = data_list[2]
        data["data"]["task_type"] = data_list[3]
    return data
