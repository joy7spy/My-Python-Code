class Bike :
  name = ""
  model = "MT 15"
  company = "Yamaha"
  def __init__(self , name):
    self.name = name 

  def display (self):
    print ("Bike name = " + self.name) 
    print ("Bike model = " + self.model)
    print ("Bike company = " + self.company)

a = Bike ("AB69")
a.display()