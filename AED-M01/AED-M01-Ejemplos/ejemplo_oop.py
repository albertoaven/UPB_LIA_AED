class ModeloIA: 
  def __init__(self, nombre, tasa_aprendizaje): 
    self.nombre = nombre 
    self.tasa_aprendizaje = tasa_aprendizaje 
    self.entrenado = False 
  
  def entrenar(self, datos): 
    print(f"Entrenando {self.nombre}...") 
    self.entrenado = True 
    
  def predecir(self, entrada): 
    if not self.entrenado: 
      raise ValueError("Modelo no entrenado") 
    
    return "Predicción realizada" 
  
class ModeloDeep(ModeloIA): 
  def __init__(self, nombre, tasa_aprendizaje, capas): 
    super().__init__(nombre, tasa_aprendizaje) 

    self.capas = capas 
    
  def entrenar(self, datos): 
    # Override 
    print(f"Entrenamiento Deep Learning con {self.capas} capas...") 

    super().entrenar(datos)