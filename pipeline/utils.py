def parse_line(line):
    """
    Incoming data format for logging sensor readings
    ph: post: 7.4
    ec: post: 600
    For task logs
    task: post: 6000: ec
    task: post: 4000: ph
    """
    data_list = line.split(":")
    data = {}
    if len(data_list) in (3, 4):
        data_list = [item.strip().lower() for item in data_list]
        data["type"] = data_list[0]
        data["request"] = data_list[1]
        data["data"] = data_list[2]
    else:
        return None
    if len(data_list) == 4:
        # Task log
        data["data"] = {}
        data["data"]["data"] = data_list[2]
        data["data"]["task_type"] = data_list[3]
    return data