import importlib
import DashboardLayout
import os

Name = os.path.dirname(os.path.realpath(__file__)).partition("Apps\\")[-1]
print("Loading " + Name)
Page = importlib.import_module("Apps." + Name + ".DashboardLayout").layout
Callbacks = importlib.import_module("Apps." + Name + ".callbacks")

