import win32com.client


def proc_exist(process_name: str):
    """
    判断进程是否存在
    """
    flag = False
    wmi = win32com.client.GetObject('winmgmts:')
    processCodeCov = wmi.ExecQuery(f'select * from Win32_Process where name=\"{process_name}\"')
    if len(processCodeCov) > 0:
        flag = True
    return flag
