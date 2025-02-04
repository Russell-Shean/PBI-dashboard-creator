# PBI-dashboard-creator
This is a python module that can be used to automatically create PowerBI dashboards using the .pbir file type
[![pypi Version](https://img.shields.io/pypi/v/PBI-dashboard-creator.svg?style=flat-square&logo=pypi&logoColor=white)](https://pypi.org/project/PBI-dashboard-creator/)
[![PyPi downloads](https://static.pepy.tech/personalized-badge/PBI-dashboard-creator?period=total&units=international_system&left_color=grey&right_color=orange&left_text=pip%20downloads)](https://pypi.org/project/PBI-dashboard-creator/)
[![Codecov test coverage](https://codecov.io/gh/                 /branch/master/graph/badge.svg)](https://app.codecov.io/gh/        ?branch=master)

## prerequisites
1. python and pip installed and on path
2. git installed and on path
3. Power BI Desktop (You can create the dashboards without this, but not view them).      


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
