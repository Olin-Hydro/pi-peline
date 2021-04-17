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
    data = {"data":""}
    if len(data_list) in [3, 4]:
        data["type"] = data_list.pop(0).strip().lower()
        data["request"] = data_list.pop(0).strip().lower()
        if len(data_list) == 4:
            data["task_type"] = data_list.pop(1).strip.lower()
    else:
        return None
    for item in data_list:
        data["data"] += item.strip().lower()
    return data