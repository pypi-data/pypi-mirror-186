class Scheduler:
    def __init__(self, scanner):
        self.scanner = scanner

    def submit(self, d):
        node = self.scanner.pop()
        address = node.save(d)
        return address

if __name__ == "__main__":
    pass
    # scanner = LanScanner()

    # x0 = scheduler.submit({"a": 1})
    # x1 = scheduler.submit({"b": 1})
    # x2 = scheduler.submit({"c": 1})
    # print(x0, x1, x2)
    # scanner.set_release()
    # scanner.join()