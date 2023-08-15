
from translate import Translator

translator = Translator(to_lang='zh')

try:
  with open('./bozo.txt', mode='r') as my_file:
      text = my_file.read()
      translation = translator.translate(text)
      with open('./japan.txt', mode='w') as your_file:
        your_file.write(translation)
      
except FileNotFoundError as err:
  print('file not found') 
  


