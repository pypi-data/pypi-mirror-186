__version__ = '0.1.1'
import time
import os
working = False
class functions:
  #-----------------------------------------#   #--------------REPLACE LINE FUNCTION------------#  
    def line_replace(self, file_name: str, lineindex: str, text: str, msg: bool):

      base = open(file_name, "r")
      ####
      lines = base.read()
      keys = lines.split("\n")
      ####
      for line in keys:
        try:
          global loc
          loc = keys.index(str(lineindex))
        except ValueError:
          pass
        try:
          keys[loc] = str(keys[loc])
          if keys[loc] != text:
            keys[loc] = str(text)
          with open(file_name, "w") as f:
            f.write("\n".join(keys))
            f.close()
        except NameError:
          linename = lineindex
          raise NameError(f'Input Incorrect. No matches: "{linename}" ')
      if msg == True:
        print("Line Replaced")
      elif msg == False:
        pass
      
      
      
    #-----------------------------------------#   #--------------NEW LINE FUNCTION------------#  
          
    def new_file(self, name: str, msg: bool):
      try:
        w = open(name, "w")
        working=True
        w.close()
      except:
        working=False
  
      if working == True:
        if msg == True:
          print("New File created")
        elif msg == False:
          pass
      elif working == False:
        raise FileExistsError("This file is an existing file. Please do not use this function if file already has been created. Sometimes this function can clear data stored.")

    #-----------------------------------------#   #------------- ADD LINE FUNCTION ------------#
        
    def add(self, file_name: str, text: str):
      f = open(file_name, "a")
      f.write(text+"\n")
      print("Line added")
    #-----------------------------------------#   #--------------WAIT FUNCTION------------#  
      
    def wait(self, num: int):
      time.sleep(num)
    #-----------------------------------------#   #--------------DELETE LINE FUNCTION------------#  
    def delete_line(self, file_name: str, lineindex: str, linenum: int, string: bool):
      new = []
      if string == True:
        r = open(file_name, "r")
        read = r.read()
        re = read.split("\n")
        for line in read:
          
          try:
            re[loc] = str(re[loc])
            re[loc] = ""
            w = open(file_name, "w")
            w.write("\n".join(re))
            w.close()
          except NameError:
            linename = lineindex
            raise NameError(f"Incorrect Input. No matches: {linename}")

   #-----------------------------------------#   #--------------CHECK LINE/DATA FUNCTION------------# 
    def check_line(self, file_name: str, lineindex: str, linenum: int, string: bool):
      if string == True:
        with open(file_name, "r") as file:
          check = file.read()
        for line in check:
          if line.startswith(lineindex):
            print(line+"\n")
            print("-----------------")
        return
          