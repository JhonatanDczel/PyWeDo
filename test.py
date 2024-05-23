import wedo

wd = wedo.WeDo()


wd.motor_b = 0

while True:
  print(wd.distance)
  input()

