# PBI-dashboard-creator
This is a python module that can be used to automatically create PowerBI dashboards using the .pbir file type

## prerequisites
1. python and pip installed and on path
2. git installed and on path
3. Power BI Desktop (You can create the dashboards without this, but not view them).      


# Run the example
This example assumes you are on windows.      

1. Create a new folder to store all the files you'll need.    
In command prompt enter the following:
```batchfile
:: create a new folder
mkdir automatic_PBI_dashboards_example

:: move into the new folder
cd automatic_PBI_dashboards_example
```
2. Clone the files from github.    
In command prompt enter the following:
```batchfile
git clone https://github.com/Russell-Shean/PBI_dashboard_creator
```
3. Activate venv.    
The following is taken from this <a href="https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/">tutorial<a>. We'll use venv to install the python package in an isolated environemnt.     
In command prompt enter the following:    
```batchfile
:: create a virtual environment
py -m venv .venv

:: activate the virtual environment
.venv\Scripts\activate

:: For extra credit, verify that venv is working
where python

```

4. Make sure pip is installed and up-to-date.    
Pip is the tool we'll use to install the package. In command prompt run the following:    
```batchfile
:: install and/or upgrade pip
py -m pip install --upgrade pip

:: check version number (and confirm it's working)
py -m pip --version

```   
   
5. Install the package.    
We'll install from a wheel stored in the package we cloned from github in step 2. In command prompt run the following:    
```batchfile
py -m pip install PBI_dashboard_creator/dist/pbi_dashboard_creator-1.0.65-py3-none-any.whl

```     

6. Create the example dashboard.    
We'll run an example script to generate an example dashboard. In command prompt run the following:    
```batchfile

py PBI_dashboard_creator/examples/create_example_dashboard.py

```     
    
7. Open the dashboard.      
Let's open the dashboard to confirm everything worked. 
In command prompt enter the following:
```
start test_dashboard/test_dashboard.pbip
```

8. Refresh data models   
After Power BI opens, you'll see a banner that looks like this:    


Click `Refresh now`
