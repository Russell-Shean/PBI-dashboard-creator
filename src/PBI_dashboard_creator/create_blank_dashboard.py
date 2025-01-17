# Create a new blank .pbir dashboard
import os
from pathlib import Path
import uuid
from importlib import resources
import shutil



def create_new_dashboard(parent_dir, report_name):


	#create a new logical id field
	# see this for explanation of what a UUID is: https://stackoverflow.com/a/534847 
	logical_id = str(uuid.uuid4())

	# define page name
	page1_name = "page1"


	# Outer level directory --------------------------------------------------------------------------------
	project_folder_path = os.path.join(parent_dir, report_name)




	# check to make sure parent directory exists
	if not os.path.exists(parent_dir):
		raise ValueError("The parent directory doesn't exist! Please create it and try again!")


	# make sure a report folder doesn't already exist
	if os.path.exists(project_folder_path):
		raise ValueError("Sorry a report with that name already exists! Please use a different report name or parent directory and try again")





	traversable = resources.files("PBI-dashboard-creator.dashboard_resources")
	with resources.as_file(traversable) as path:
    	shutil.copytree(path, project_folder_path)







