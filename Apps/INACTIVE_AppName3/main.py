import importlib

Name = "AppName3"
Page = importlib.import_module("Apps." + Name + ".DashboardLayout").layout
Callbacks = importlib.import_module("Apps." + Name + ".callbacks")
