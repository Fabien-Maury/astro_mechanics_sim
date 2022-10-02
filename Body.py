class Body:
  def __init__(self, name, mass, position, speed, acceleration):
    self.name = name
    self.mass = mass
    self.position = [position]
    self.speed = [speed]
    self.acceleration = [acceleration]
  
  def setName(self, name):
    try:
      self.name = name
      status = True
    except Exception as e:
      print("Error (setName) : " + str(e))
      status = False
    return(status)

  def setMass(self, mass):
    try:
      self.mass = mass
      status = True
    except Exception as e:
      print("Error (setMass) : " + str(e))
      status = False
    return(status)

  def setPosition(self, position):
    try:
      self.position.append(position)
      status = True
    except Exception as e:
      print("Error (setPosition) : " + str(e))
      status = False
    return(status)
  
  def setSpeed(self, speed):
    try:
      self.speed.append(speed)
      status = True
    except Exception as e:
      print("Error (setSpeed) : " + str(e))
      status = False
    return(status)

  def setAcceleration(self, acceleration):
    try:
      self.acceleration.append(acceleration)
      status = True
    except Exception as e:
      print("Error (setAcceleration) : " + str(e))
      status = False
    return(status)

  def getPosition(self):
    try:
      r = self.position[-1]
    except Exception as e:
      print("Error (getPosition) : " + str(e))
      r = False
    return(r)

  def getSpeed(self):
    try:
      r = self.speed[-1]
    except Exception as e:
      print("Error (getSpeed) : " + str(e))
      r = False
    return(r)

  def getAcceleration(self):
    try:
      r = self.acceleration[-1]
    except Exception as e:
      print("Error (getAcceleration) : " + str(e))
      r = False
    return(r)
