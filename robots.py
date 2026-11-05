from components import Components
class Robot:
    def __init__(self,  code: str, model: str, application: str, max_weigth_components_kg: float, state: str) -> None:
        self.code=code
        self.model=model
        self.aplication=application
        self.max_weigth_components_kg=max_weigth_components_kg
        self.state=state
        self.components=[]
    def add_component(self,component:Components):
        
        for comp in self.components:
            if comp.code==component.code:
                return (f"Code already present in the robot")
            if component.weigth_kg + self.components_weigth() > self.max_weigth_components_kg:
                raise ValueError
        
        self.components.append(component)
        
        
    def components_weigth(self):
        tot_w=0.0
        for comp in self.components:
            tot_w+=comp.weigth_kg
        
        return tot_w
    
    def search_component(self,code:str):
         for comp in self.components:
            if comp.code==code:
                return comp
        
         return None
    
    def remove_component(self,code:str):
        if self.search_component(code)==None: return None
        
        for comp in self.comonents:
            if comp.code==component.code:
                temp=comp
                self.components.remove(comp)
                return comp
            
    def underweigth_components(self,max_weigth:float):
        temp=[]
        for comp in self.components:
            if comp.weigth_kt < max_weigth:
                temp.append(comp)
                
        return comp
        