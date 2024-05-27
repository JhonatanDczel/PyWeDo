import wedo

wd = wedo.WeDo()


wd.motor_b = 0

while True:
  level = input()
  wd.motor_b = int(level)

