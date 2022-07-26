class JointDrive:
    def __init__(self, id = -1):
        self.id = id
        self.angle = -1
        self.speed = -1

    def set_angle(self, angle):
        self.angle = angle
    def get_angle(self):
        return self.angle

    def set_speed(self, speed):
        self.speed = speed
    def get_speed(self):
        return self.speed
