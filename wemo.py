#!/usr/bin/env python3

from ouimeaux.environment import Environment

def on_switch(switch):
  print("Switch found!: " + switch.name)

def on_motion(motion):
  print("Motion found!: " + motion.name)


if __name__ == '__main__':
    env = Environment(on_switch, on_motion)
    env.start()
    env.discover(seconds=3)
    env.list_switches()
    switch = env.get_switch('WeMo')
    switch
    print(switch.get_state())
    switch.on()
    print(switch.get_state())
    print(switch.insight_params)
    print(switch.insight_params['currentpower'])
