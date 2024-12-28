class vehicle:
    def __init__(self, max_speed ,milege):
     self.max_speed = max_speed
     self.milege = milege


modelx = vehicle(240,18)
print("model max speed:",modelx.max_speed)
print("model milege:",modelx.milege)