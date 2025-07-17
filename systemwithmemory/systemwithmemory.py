# a hot stone with heater, initial 100.0
# usage: python3 systemwithmemory.py 100.0

import sys

class Stone:
    """State class"""
    def __init__(self, inittemp):
        self.temp = inittemp

    def transition(self, heat):
        self.temp = 0.9 * self.temp + 0.1*(heat - self.temp)

def main(input):
    print( "system with memory")
    state = Stone(100.0)
    # --
    print ("x={:.2f}, input={:.2f}".format(state.temp, input))
    while True:
        state.transition(input)
        print ("x={:.2f}, input={:.2f}".format(state.temp, input))

# ------ main
args = sys.argv
input = float(args[1])

main(input)

