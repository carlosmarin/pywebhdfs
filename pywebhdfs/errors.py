class PyWebHdfsException(Exception):
    def __init__(self, msg=str()):
        self.msg = msg
        super(PyWebHdfsException, self).__init__(self.msg)
