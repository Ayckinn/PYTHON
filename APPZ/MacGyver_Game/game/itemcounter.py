# =======================================
# = Module for items counter management =
# =======================================

class ItemCounter:

    def __init__(self):
        self.counter_value = 3

    # ------------------------------------------------------------------------
    def decrease(self):
        self.counter_value -= 1

    # ------------------------------------------------------------------------
    def get_counter_value(self):
        return self.counter_value