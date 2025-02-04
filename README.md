# Power Bpy
Do you wish you could build dashboard with python or R, but can't because the client specifically asked for Power BI or your employer only supports publishing Power BI? Do you love love love Power BI, but wish there was a way to automatically generate parts of your dashboard to speed up your development process?          

Introducing Power Bpy, a python package that lets you create Power BI dashboards using functions 💪 instead of the point-and-click interface 🥹. Dashboards created using these functions can be opened, edited and saved normally in Power BI desktop.       

This package uses the new .pbip/.pbir format with TMDL enabled. This stores dashboards as directories of text files instead of binary files letting you version control your dashboards! 🥳 These features are still preview features, so use this with caution until there's more clarity from microsoft about what they're going to do with .pbir and tmdl.       

[![pypi Version](https://img.shields.io/pypi/v/PBI-dashboard-creator.svg?style=flat-square&logo=pypi&logoColor=white)](https://pypi.org/project/PBI-dashboard-creator/)
[![PyPI Downloads](https://static.pepy.tech/badge/pbi-dashboard-creator)](https://pepy.tech/projects/pbi-dashboard-creator)
[![Codecov test coverage](https://codecov.io/gh/Russell-Shean/PBI-dashboard-creator/branch/master/graph/badge.svg)](https://app.codecov.io/gh/Russell-Shean/PBI-dashboard-creator?branch=master)

           
# Features      
Currently the package has functions that let you *automatically* 🥳 do the following:     
- Create a new dashboard
- Import data from
  - csv file stored locally 
  - csv file stored in Azure Data Lake Storage (ADLS)
  - Power BI table stored as a Tabular Model Definition Language (TMDL) file
- Add a page
- Add background images to a page
- Add visuals to a page
  - charts
  - slicers
  - cards
  - maps
  - text boxes
  - buttons

## Dependencies    
Before you can start to build power BI dashboards using this package's functions you'll need the following: 
1. python and pip installed and on path
2. git installed and on path
3. Power BI Desktop (You can create the dashboards without this, but not view them).

Power BI settings:      
You'll need to enable some preview features in Power BI Desktop. Navigate to `File` > `Options and Settings` > `Options` > `Preview features` and enable the following options:
1. Shape map visual
2. Power BI Project (.pbip) save option
2. A. Store Semantic Model using TMDL format
2. B. Store reports using enhanced metadata format (PBIR)


# Run the example
This example assumes you are on windows. All the code below should be entered in command prompt or put in a batch script.      

1. Create a new folder to store all the files you'll need.    
```batchfile
:: create a new folder
mkdir automatic_PBI_dashboards_example

:: move into the new folder
cd automatic_PBI_dashboards_example
```
2. Clone the files from github.    
```batchfile
git clone https://github.com/Russell-Shean/PBI_dashboard_creator
```
3. Activate venv.    
The following is taken from this <a href="https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/">tutorial</a>. We'll use venv to install the python package in an isolated environemnt.   
```batchfile
:: create a virtual environment
py -m venv .venv

:: activate the virtual environment
.venv\Scripts\activate

:: For extra credit, verify that venv is working
where python

```

4. Make sure pip is installed and up-to-date.    
Pip is the tool we'll use to install the package.  
```batchfile
:: install and/or upgrade pip
py -m pip install --upgrade pip

:: check version number (and confirm it's working)
py -m pip --version

```   
   
5. Install the package.
Install the package from pypi.     
```batchfile
py -m pip install PBI_dashboard_creator

```     

6. Create the example dashboard.
Run an example script to generate an example dashboard.
```batchfile

py PBI_dashboard_creator/examples/create_example_dashboard.py

```     
    
7. Open the dashboard.      
Open the dashboard to confirm everything worked. 
```
start test_dashboard/test_dashboard.pbip
```

8. Refresh data models   
After Power BI opens, you'll see a banner that looks like this:    


Click `Refresh now`
