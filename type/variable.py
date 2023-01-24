class variable:
    def __init__(self, value = None) -> None:
        self.value = value

    def __str__(self) -> str:
        return self.value

    def __int__(self) -> int:
        return len(self.value)

    def __bool__(self) -> bool:
        return len(self.value) != 0