class gui_callback:
    """
    author:mrtang
    date:2017.7
    version:1.0
    email:mrtang@nudt.edu.cn

    It is used to return value in callback functions.
    """
    def __init__(self):
        self.args = None
        self.res = None
        self.func = None
    def call(self):
        self.res = self.func(self.args)