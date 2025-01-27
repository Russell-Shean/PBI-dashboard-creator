import os, json

def add_new_page(dashboard_path, page_name):

	'''Create a new blank dashboard page

	:param str dashboard_path: The path where the dashboard files are stored. (This is the top level directory containing the .pbip file and Report and SemanticModel folders). 
	:param str page_name: The display name for the page you just created. This is differnt from the page_id which is only used internally. 

	:returns: new_page_id: The unique id for the page you just created. If you used this function it will be in the format page1, page2, page3, page4, etc. If you manually create a page it will be a randomly generated UUID. To find a page's page id, consult the report > definition> pages > page.json file and look in the page order list. 
  
	'''

	# file paths
	report_name = os.path.basename(dashboard_path)
	pages_folder = os.path.join(dashboard_path, f'{report_name}.Report/definition/pages' )
	pages_json_path = os.path.join(pages_folder, "pages.json")

	# determine number of pages
	with open(pages_json_path,'r') as file:
		pages_list = json.load(file)

		# determine number of pages
		n_pages = len(pages_list["pageOrder"])

		# create a new page id based on existing number of pages
		new_page_id = f"page{n_pages + 1}"

		# add the new page id to the pageOrder list
		pages_list["pageOrder"].append(new_page_id)
    
  
	# write to file
	with open(pages_json_path,'w') as file:
		json.dump(pages_list, file, indent = 2)

	
	# create a folder for the new page
	new_page_folder = os.path.join(pages_folder, new_page_id)
	new_page_json_path = os.path.join(new_page_folder, "page.json")
	os.makedirs(new_page_folder)

	# create a new json file for the new page
	new_page_json = {"$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/1.2.0/schema.json",
	                  "name": new_page_id,
	                  "displayName": page_name,
	                  "displayOption": "FitToPage",
	                  "height": 720,
	                  "width": 1280,
					  "objects":{}}

	# write to file
	with open(new_page_json_path, "w") as file:
		json.dump(new_page_json, file, indent = 2)


	return new_page_id

