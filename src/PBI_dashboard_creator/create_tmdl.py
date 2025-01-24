import os, re, uuid
import pandas as pd

def create_tmdl(dashboard_path, dataset_name, dataset_id, dataset):


	# file paths ---------------------------------------------------------------------------
	report_name = os.path.basename(dashboard_path)


	semantic_model_folder = os.path.join(dashboard_path, f'{report_name}.SemanticModel' )
	definitions_folder = os.path.join(semantic_model_folder, "definition")

	tables_folder = os.path.join(definitions_folder, 'tables')
	dataset_file_path = os.path.join(tables_folder, f'{dataset_name}.tmdl')

	# create a tables folder if it doesn't already exist
	if not os.path.exists(tables_folder):
		os.makedirs(tables_folder)


	# remove unnamed columns from dataset
	dataset = dataset.loc[:, ~dataset.columns.str.contains('^Unnamed')]



	# sink inital header stuff about dataset
	with open(dataset_file_path, 'w') as file:
		file.write(f'table {dataset_name}\n\tlineageTag: {dataset_id}\n\n')

    # read in the dataset
    # compare how pandas manages to do this in a single line 
    # and Power BI requires 40 lines of code and modifying multiple files to do the same thing
    # in case you needed evidence of how dummmmmmmbbb Power BI, Power querry and M are.....



	for col in dataset:

		# Loop through the dataset and find dates
		for value in dataset[col][0:100]:
			m = re.search("^\d{4}-\d{2}-\d{2}$", str(value))

			if m is not None:
				#print(f"{col}: This column is probably a date!")

				# change the data type in the panda dataframe
				dataset[col] = pd.to_datetime(dataset[col], format = "%Y-%m-%d")

				# create a date heirarchy table
				#file_id = PBI_date_hr.create_date_hr(col_name = col,
				 #dataset_name = dataset_name,
				  #report_name = report_name, 
				  #dashboard_path = dashboard_path )
				break


	col_names = []
	col_deets = []


  # loop through columns and write specs out to model file
	for col in dataset:

		# loop through the values in a column to see if it contains dates
		# Loop through the dataset and find dates
		for value in dataset[col][0:100]:
			m = re.search("^\d{4}-\d{2}-\d{2}$", str(value))

			if m is not None:
				#print(f"{col}: This column is probably a date!")

				# change the data type in the panda dataframe
				dataset[col] = pd.to_datetime(dataset[col], format = "%Y-%m-%d")

				# create a date heirarchy table
				#file_id = create_date_hr(col_name = col, 
				#	dataset_name = dataset_name, 
				#	report_name = report_name,
			#		 dashboard_path = dashboard_path )
			#	break

		# add the column's name to a set for later
		col_names.append(col)

		# record more details in a different set

		col_id = str(uuid.uuid4())


    # For numbers, we're not distinguishing between integers (int64)
    # and numbers (double)
		if dataset[col].dtype == "int64" or dataset[col].dtype == "float64":

			# record more details in a different set
			col_deets.append(f'{{"{col}", type number}}')


			with open(dataset_file_path, 'a') as file:
				file.write(f'\tcolumn {col}\n')
				file.write('\t\tdataType: double\n')
				#file.write('\t\tformatString: 0\n')
				file.write(f'\t\tlineageTag: {col_id}\n')
				file.write('\t\tsummarizeBy: sum\n')
				file.write(f'\t\tsourceColumn: {col}\n\n')
				file.write('\t\tannotation SummarizationSetBy = Automatic\n\n')
				file.write('\t\tannotation PBI_FormatHint = {"isGeneralNumber":true}\n\n')


    # strings ------------------------------------------------
		if dataset[col].dtype == "object":

			# record more details in a different set
			col_deets.append(f'{{"{col}", type text}}')

			with open(dataset_file_path, 'a') as file:
				file.write(f'\tcolumn {col}\n')
				file.write('\t\tdataType: string\n')
				file.write(f'\t\tlineageTag: {col_id}\n')
				file.write('\t\tsummarizeBy: none\n')
				file.write(f'\t\tsourceColumn: {col}\n\n')
				file.write('\t\tannotation SummarizationSetBy = Automatic\n\n')

 
 		# dates ----------------------------------------------
		if dataset[col].dtype == "datetime64[ns]":

			# create a relationship id
			relationship_id = str(uuid.uuid4())

			# record more details in a different set
			col_deets.append(f'{{"{col}", type date}}')

			with open(dataset_file_path, 'a') as file:
				file.write(f'\tcolumn {col}\n')
				file.write(f'\t\tdataType: dateTime\n')
				file.write(f'\t\tformatString: Long Date\n')
				file.write(f'\t\tlineageTag: {col_id}\n')
				file.write('\t\tsummarizeBy: none\n')
				file.write(f'\t\tsourceColumn: {col}\n\n')

				# this is only needed if you want automatic date heirarchies
				# at some point I may add that as an option to the create dashboard function.....
				#file.write(f'\t\tvariation Variation\n')
				#file.write('\t\t\tisDefault\n')
				#file.write(f'\t\t\trelationship: {relationship_id}\n')
				#file.write(f"\t\t\tdefaultHierarchy: LocalDateTable_{file_id}.'Date Hierarchy'\n\n")
				file.write('\t\tannotation SummarizationSetBy = Automatic\n\n')
				file.write('\t\tannotation UnderlyingDateTimeDataType = Date\n\n')


			# create a new file to define the relationship
			#with open(relationships_path, "a") as file:
			#	file.write(f'relationship {relationship_id}\n')
			#	file.write(f'\tjoinOnDateBehavior: datePartOnly\n')
			#	file.write(f'\tfromColumn: {dataset_name}.{col}\n')
			#	file.write(f'\ttoColumn: LocalDateTable_{file_id}.Date\n\n')

			# Append the date table to the model.tmdl file
			#with open(model_path, "a") as file:
			#	file.write(f'\nref table LocalDateTable_{file_id}')

	# create a dictionary containing col_deets and col_names
	col_attributes = {"col_deets":col_deets, "col_names": col_names}

			
	return col_attributes