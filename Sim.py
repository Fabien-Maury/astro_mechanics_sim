import math

class Sim:
  def __init__(self, start, end, step, bodies, g):
    self.start = start
    self.end = end
    self.step = step
    self.bodies = bodies
    self.g = g
    self.time = [i for i in range(start, end + step, step)]
    self.bodies_position = [body.position for body in bodies]
    self.bodies_position = dict(zip(bodies, self.bodies_position))
    self.bodies_speed = [body.speed for body in bodies]
    self.bodies_speed = dict(zip(bodies, self.bodies_speed))
    self.bodies_acceleration = [body.acceleration for body in bodies]
    self.bodies_acceleration = dict(zip(bodies, self.bodies_acceleration))

  def distance(self, pos1, pos2):
    d = 0
    for i in range(len(pos1)):
      d += (pos2[i] - pos1[i])**2
    return(math.sqrt(d))
    
  def update_acceleration(self, body):
    current_body = body
    current_acceleration = current_body.getAcceleration()
    current_position = current_body.getPosition()
    total_update = [0,0,0]
    try:
      for body in self.bodies:
        if body != current_body:
          r = self.distance(current_position, body.getPosition())
          intensity = (self.g * current_body.mass * body.mass) / r**2
          update = [intensity * (body.getPosition()[i] - current_position[i]) / r for i in range(len(current_position))]
          total_update = [total_update[i] + update[i] for i in range(len(current_position))]
      new_acceleration = [current_acceleration[i] + total_update[i] for i in range(len(current_acceleration))]
      current_body.setAcceleration(new_acceleration)
      status = True
    except Exception as e:
      print("Error (update_acceleration) : " + str(e))
      status = False
    return(status)

  def update_speed(self, body):
    current_body = body
    current_acceleration = current_body.getAcceleration()
    current_speed = current_body.getSpeed()
    try:
      update = [current_acceleration[i] * self.step for i in range(len(current_acceleration))]
      new_speed = [current_speed[i] + update[i] for i in range(len(current_speed))]
      current_body.setSpeed(new_speed)
      status = True
    except Exception as e:
      print("Error (update_speed) : " + str(e))
      status = False
    return(status)
  
  def update_position(self, body):
    current_body = body
    current_speed = current_body.getSpeed()
    current_position = current_body.getPosition()
    try:
      update = [current_speed[i] * self.step for i in range(len(current_speed))]
      new_position = [current_position[i] + update[i] for i in range(len(current_position))]
      current_body.setPosition(new_position)
      status = True
    except Exception as e:
      print("Error (update_speed) : " + str(e))
      status = False
    return(status)

  def update_log(self):
    try:
      bodies = self.bodies
      self.bodies_position = [body.position for body in bodies]
      self.bodies_position = dict(zip(bodies, self.bodies_position))
      self.bodies_speed = [body.speed for body in bodies]
      self.bodies_speed = dict(zip(bodies, self.bodies_speed))
      self.bodies_acceleration = [body.acceleration for body in bodies]
      self.bodies_acceleration = dict(zip(bodies, self.bodies_acceleration))
      status = True
    except Exception as e:
      print("Error (update_logs) : " + str(e))
      status = False
    return(status)
  
  def run(self):
    for i in self.time:
      for body in self.bodies:
        try:
          status1 = self.update_acceleration(body)
          status2 = self.update_speed(body)
          status3 = self.update_position(body)
          status = status1 and status2 and status3
        except Exception as e:
          print("Error (run) : " + str(e))
          status = False
      status4 = self.update_log()
      status = status and status4
    print("Done")

    #testing
    print(self.bodies_acceleration[star1])
    print("-----------")
    print(self.bodies_speed[star1])
    print("-----------")
    print(self.bodies_position[star1])
    print(len(self.bodies_position[star1]))
    # end test 
    return(status)
