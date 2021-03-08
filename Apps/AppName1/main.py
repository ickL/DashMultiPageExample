import importlib

Name = "AppName1"
print("Loading " + Name)
Page = importlib.import_module("Apps." + Name + ".DashboardLayout").layout
Callbacks = importlib.import_module("Apps." + Name + ".callbacks")
