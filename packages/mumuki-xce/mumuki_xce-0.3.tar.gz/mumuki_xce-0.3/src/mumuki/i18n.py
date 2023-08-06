locales = {
  "en": {
    "could_not_load_exercise": "Could not access exercise {id}. Please visit {url} and verify the instructions",
    "magic_cell_missing": "Please ensure to mark you solution cell with %%solution",
    "no_ipython": "There is not ipython environment available. Make sure you are running from a Jupyter or Colab notebook"
  },
  "es": {
    "could_not_load_exercise": "No se pudo acceder al ejercicio {id}. Visitá {url} y verificá las instrucciones",
    "magic_cell_missing": "Asegurate de marcar tu celda de solución con %%solution",
    "no_ipython": "No hay un entorno de ipython disponible. Asegurate de estar en un cuaderno Jupyter o Colab"
  },
  "pt": {
    "could_not_load_exercise": "Não foi possível acessar o exercício {id}. Visite {url} e verifique as instruções",
    "magic_cell_missing": "Certifique-se de marcar sua célula de solução com %%solution",
    "no_ipython": "Não há ambiente ipython disponível. Verifique se você está executando em um caderno Jupyter ou Colab"
  }
}


class Locale:
  def __init__(self, code: str):
    if code not in locales:
      raise RuntimeError(f"Invalid locale {code}")

    self.code = code

  def translate(self, key: str, **kwargs) -> str:
    return locales[self.code][key].format(**kwargs)
