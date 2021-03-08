# DashMultiPageExample
An example of a multipage dash app with individual folders and separated layouts/callbacks/data folders.


General structure seen in multipage examples (see https://dash.plotly.com/urls)
![alt text](https://user-images.githubusercontent.com/53160568/110267088-19820600-7f8d-11eb-9a0c-7c18729086d6.png)

This structure, importing the apps from the Apps folder and using the structured if/elif layout selector in the index.py file works, but is hard to scale. For every dashboard you add to your server, you need to add that to the import list and add a new elif to select the layout from the URL. As I have scaled to 10+ dashboards, the index file and Apps folder get very busy. Also, if a dashboard has an issue, the server will not load. Ideally, I would like to be able to drop a new app into the Apps folder and run the server. 

This repository example tries to clean up the organization of the folder structure and simplifies the index.py structure:

![alt text](https://user-images.githubusercontent.com/53160568/110267097-1d158d00-7f8d-11eb-9b3c-17c327654162.png)

One drops new app folders into the apps folder. A script runs (from the Global Methods folder) that builds a list of apps to load into the index file, and also creates a dictionary for layout handling. 
