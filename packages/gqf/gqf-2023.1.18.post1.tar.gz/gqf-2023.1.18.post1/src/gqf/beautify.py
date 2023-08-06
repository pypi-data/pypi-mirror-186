def separator():
    """
    分隔线
    """
    print('-' * 100)


def hum_convert(value):
    """
    将单位转为人类可读
    """
    units = ["B", "KB", "MB", "GB", "TB", "PB"]
    size = 1024.0
    for i in range(len(units)):
        if (value / size) < 1:
            return f"{value:.2f}{units[i]}"
        value = value / size
