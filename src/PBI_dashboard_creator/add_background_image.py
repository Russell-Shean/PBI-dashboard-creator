#background_image
import os, shutil, json

def add_background_img(dashboard_path, page_id, img_path, alpha, scaling_method = "Fit"):

	'''



	'''

	if typ(alpha) is not int:
		raise TypeError("alpha (the transparency value) must be an integer between 1-100")

	if alpha is > 100 or < 0:
		raise ValueError("alpha (the transparency value) must be an integer between 1-100")

	# file paths
	report_name = os.path.basename(dashboard_path)
	img_name = os.path.basename(img_path)

	report_folder = os.path.join(dashboard_path, f'{report_name}.Report')
	definitions_folder = os.path.join(report_folder, "definition")

	page_json_path = os.path.join(definitions_folder, f"pages/{page_id}/page.json")
	report_json_path = os.path.join(definitions_folder, "report.json")


	registered_resources_folder = os.path.join(report_folder, "StaticResources/RegisteredResources")

	# This is the location of the image within the dashboard
	registered_img_path = os.path.join(registered_resources_folder, img_name)


	# Upload image to dashboard's registered resources ---------------------------------------------------

	# create registered resources folder if it doesn't exist
	if not os.path.exists(registered_resources_folder):
		os.makedirs(registered_resources_folder)

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



	#print(report_json)

   
	# write to file
	with open(report_json_path,'w') as file:
		json.dump(report_json, file, indent = 2)




	# Add image to page -------------------------------------------------------------------------------
	with open(page_json_path,'r') as file:
		page_json = json.load(file)


	# add the image to the page's json
	page_json["objects"].update(

		    "background": [
      {
        "properties": {
          "image": {
            "image": {
              "name": {
                "expr": {
                  "Literal": {
                    "Value": f"'{img_name}'"
                  }
                }
              },
              "url": {
                "expr": {
                  "ResourcePackageItem": {
                    "PackageName": "RegisteredResources",
                    "PackageType": 1,
                    "ItemName": img_name
                  }
                }
              },
              "scaling": {
                "expr": {
                  "Literal": {
                    "Value": f"'{scaling_method}'"
                  }
                }
              }
            }
          },
          "transparency": {
            "expr": {
              "Literal": {
                "Value": f"{alpha}D"
              }
            }
          }
        }
      }
    ]


		)
	

	

   
	# write to file
	with open(page_json_path,'w') as file:
		json.dump(page_json, file, indent = 2)






	#blorg/blorg.Report/StaticResources/RegisteredResources/Taipei_skyline_at_sunset_201506895591283012392.jpg




report_name = "blorg"
report_location = f"C:/Users/rps1303/PBI_projects"

dashboard_path = f"{report_location}/{report_name}"

add_background_img(dashboard_path = dashboard_path, page_id = "page2", img_path = "C:/Users/rps1303/Downloads/Taipei_skyline_at_sunset_20150607.jpg", alpha = 100)
