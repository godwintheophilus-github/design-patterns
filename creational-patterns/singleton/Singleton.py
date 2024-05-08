class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            cls._instance = super(Singleton, cls).__new__(cls, *args, *kwargs)
        return cls._instance

    def __init__(self):
        self.value = None

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    s1.setValue("Singleton")
    print(s2.getValue())
