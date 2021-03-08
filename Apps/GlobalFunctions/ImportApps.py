import importlib
import os
import sys

def AllApps(defaultApp):
       dictionaryOfApps = {}
       for i in os.scandir( "Apps\\"):
              directory = i.name
                                  
              if directory != "GlobalFunctions" and "INACTIVE" not in directory.upper():
                 try:
                     main = "main"
                     sys.path.insert(1, "Apps\\" + directory)
                     j = importlib.import_module("Apps." + directory +"." +main)
                     dictionaryOfApps[directory] = j
                     if directory == defaultApp:
                           dictionaryOfApps["Default"] = j 
                 except:
                     print(str(i.name) + " - Had issues Loading")
                     #logLoadError(str(i) + " - fail to load App!" ##maybe feed in type of error that occured
       return dictionaryOfApps
