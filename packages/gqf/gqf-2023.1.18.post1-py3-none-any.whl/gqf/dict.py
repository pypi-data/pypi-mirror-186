def get_values_of_key(_dict: dict, _key: str):
    """
    获取字典中某个键的全部值
    示例
    students = {'kelvin': {'age': 18},'vicky': {'age': 19}}
    print(get_values_of_key(students, 'age'))
    # [18, 19]
    """
    queue = [_dict]
    result = []
    while len(queue) > 0:
        data = queue.pop()
        for key, value in data.items():
            if key == _key:
                result.append(value)
            elif isinstance(value, dict):
                queue.append(value)
    return sorted(result)
