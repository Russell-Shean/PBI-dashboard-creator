import os, re


import PBI_dashboard_creator.update_diagramLayout as PBI_DL
import PBI_dashboard_creator.update_model_file as PBI_model              # internal function to add data to model.tmdl



def add_custom_date_hr(dashboard_path, tmdl_file_path):
	
	'''



	'''

	# file paths


	# dateset_name ----------------------------------------------------------------------------------------
	# extract the dataset name from the tmdl file's path
	# extract bits of names for later
	path_end = os.path.basename(tmdl_file_path)
	split_end = os.path.splitext(path_end)

	dataset_name = split_end[0]
	print(dataset_name)


	# dateset_name -----------------------------------------------------------------------------------------------
	# read the whole table.tmdl file in andmake it a giant blob for regex
	file_content = ""

	with open(tmdl_file_path) as file: 

		# list comprehension
		# all lines have all the white spaces and \n and \t striped 
		# They're then joined together using the .join function and ~ as a seperator
		file_content = "~".join(re.sub('\t?', '', line).rstrip() for line in file)


	# pull out just the dataset_id using regex
	m = re.search("(?<=lineageTag: ).*?(?=~~column)", file_content )


	dataset_id = m.group(0)




	# update the diagramLayout file to include the new date table\
	#PBI_DL.update_diagramLayout(dashboard_path = dashboard_path, dateset_name = dataset_name, dataset_id = dataset_id)

	# update the model.tmdl file to include the new datetable



	# add the new tmdl file to the tables folder
	#PBI_model.update_model_file(dashboard_path = dashboard_path, dataset_name = dataset_name)





# add_custom_date_hr(dashboard_path = "C:/Users/rps1303/PBI_projects/blorg", tmdl_file_path = "C:/Users/rps1303/PBI_projects/test_dash/blorg/blorg.SemanticModel/definition/tables/DateTable.tmdl")