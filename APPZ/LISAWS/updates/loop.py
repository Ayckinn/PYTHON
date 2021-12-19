# ==========================
# = LOOP MODULE MANAGEMENT =
# ==========================

class LoopStation:

    def __init__(self):
        self.loop_value = 0

    def loop_increase(self):
        self.loop_value += 1

    def get_loop_value(self):
        return self.loop_value