import threading
class OddEvenMonitor(threading.Condition):
    ODD_TURN = True
    EVEN_TURN = False

    def __init__(self):
        super().__init__()
        # would always start with an odd number
        self.turn = self.ODD_TURN

    def wait_turn(self, waited_turn):
        with self:
            while self.turn != waited_turn:
                self.wait()

    def toggle_turn(self):
        with self:
            self.turn ^= True
            self.notify()

class OddThread(threading.Thread):
    def __init__(self, monitor):
        super().__init__()
        # so the monitor is shared?
        self.monitor = monitor

    def run(self):
        for i in range(1, 101, 2):
            self.monitor.wait_turn(OddEvenMonitor.ODD_TURN)
            print(i)
            self.monitor.toggle_turn()

class EvenThread(threading.Thread):
    def __init__(self, monitor):
        super().__init__()
        self.monitor = monitor

    def run(self):
        for i in range(2, 101, 2):
            self.monitor.wait_turn(OddEvenMonitor.EVEN_TURN)
            print(i)
            self.monitor.toggle_turn()

monitor = OddEvenMonitor()
t1 = EvenThread(monitor)
t2 = OddThread(monitor)

t1.start()
t2.start()

