class int(int):
    def __init__(self, value=None) -> None:
        super().__init__()
        self.value = value

    def __lshift__(self, var):
        print(var, end="")
        return str(self.value + str(var))