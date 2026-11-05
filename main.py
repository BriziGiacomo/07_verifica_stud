from components import Components
from robots import Robot
 
if __name__=="__main__":
    comp1=Components("IOI","Ruota meccanica", 11.2)
    comp2=Components("AAI","Bulone", 0.4)
    comp3=Components("YYI","Ruota meccanica", 13.2)
    
    robot1=Robot("AAA", "RS232", "WAR", 30.0, "ACTIVE")
    robot1.add_component(comp1)
    robot1.add_component(comp2)
    print(robot1.components_weigth())
    robot1.remove_component(comp1)