def parse_line(line):
    """
    Incoming data format for logging sensor readings
    ph: post: 7.4
    ec: post: 600
    """
    data_list = line.split(":")
    if len(data_list) == 3:
        data = {"data":""}
        data_list = line.split(":")
        data["type"] = data_list.pop(0).strip().lower()
        data["request"] = data_list.pop(0).strip().lower()
        for item in data_list:
            data["data"] += item.strip().lower()
        return data
    return None