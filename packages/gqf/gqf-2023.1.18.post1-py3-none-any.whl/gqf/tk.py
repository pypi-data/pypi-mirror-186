import ctypes

def tk_adjust_high_DPI(win):
    """
    @描述：tk 适配高分屏
    @参数：窗口 win
    @返回：无
    """
    # 告诉操作系统使用程序自身的dpi适配
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    # 获取屏幕的缩放因子
    scale_factor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
    # 设置程序缩放
    win.tk.call('tk', 'scaling', scale_factor / 75)