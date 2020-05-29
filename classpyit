# @jsmatias
# email: smatias.jean@gmail.com

class ClassPyIt:
  '''Make an instanced object from dictionary
  dObj = ClassPyIt({'a': 1}
  dObj.a
  1
  '''
  def __init__(self, dicty):
    for k, v in dicty.items():
      k = f'N{k}' if type(k) == int else k.replace(' ', '')
      setattr(self, str(k).strip(), v)
