#background_image
import os, shutil

def add_background_img(dashboard_path, page_id, img_path, alpha):

	'''



	'''

	# file paths
	report_name = os.path.basename(dashboard_path)
	img_name = os.path.basename(img_name)

	report_folder_path = os.path.join(project_folder_path, f'{report_name}.Report')
	definitions_folder = os.path.join(semantic_model_folder, "definition")

	page_json = os.path.join(definitions_folder, f"pages/{page_id}/page.json")
	report_json_path = os.path.join(definitions_folder, "report.json")


	registered_resources_folder = os.path.join(report_folder_path, "StaticResources/RegisteredResources")

	# This is the location of the image within the dashboard
	registered_img_path = os.path.join(registered_resources_folder, img_name)


	# Upload image to report -------------------------------------------------------------------------

	# create registered resources folder if it doesn't exist
	if not os.path.exists(registered_resources_folder):
		os.mkdirs(registered_resources_folder)

	# move image to registered resources folder
	shutil.copy(img_path, registered_img_path)


	# add new registered resource (the image) to report.json ----------------------------------------------
	with open(report_json_path,'r') as file:
		report_json = json.load(file)


	# add the image as an item to the registered resources items list
	for dict in report_json["resourcePackages"]:
		if dict["name"] == "RegisteredResources":
			dict["items"].append(
				                  {
                                    "name": img_name,
                                    "path": img_name,
                                    "type": "Image"
                                   }   
        	                    )



	print(report_json)
	quit()

	

   
	# write to file
	with open(report_json_path,'w') as file:
		json.dump(report_json_path, file, indent = 2)




	# Add image to page -------------------------------------------------------------------------------




	#blorg/blorg.Report/StaticResources/RegisteredResources/Taipei_skyline_at_sunset_201506895591283012392.jpg




report_name = "blorg"
report_location = f"C:/Users/rps1303/PBI_projects"

dashboard_path = f"{report_location}/{report_name}"

add_background_img(dashboard_path = dashboard_path, page_id = "page2", img_path = "C:/Users/rps1303/Downloads/Taipei_skyline_at_sunset_20150607.jpg")
