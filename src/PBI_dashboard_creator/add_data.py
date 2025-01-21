import pandas as pd
import os, uuid, json

# Import a custom function to create the date heirarchies
import PBI_dashboard_creator.create_date_hrcy as PBI_date_hr


def add_csv(dashboard_path, data_path):

  # generate a random id for the data set
	dataset_id = str(uuid.uuid4())


	# extract bits of names for later
	path_end = os.path.basename(data_path)
	split_end = os.path.splitext(path_end)

	dataset_name = split_end[0]
	dataset_extension =split_end[1]


	report_name = os.path.basename(dashboard_path)

  # Reverse slash directions bc windows is stooooooopid
	data_path_reversed = data_path.replace('/', '\\')
	


	# file paths
	semantic_model_folder = os.path.join(dashboard_path, f'{report_name}.SemanticModel' )
	definitions_folder = os.path.join(semantic_model_folder, "definition")
	model_path = os.path.join(definitions_folder, 'model.tmdl')
	relationships_path = os.path.join(definitions_folder, "relationships.tmdl")
	diagram_layout_path = os.path.join(semantic_model_folder, 'diagramLayout.json')

	tables_folder = os.path.join(definitions_folder, 'tables')
	dataset_file_path = os.path.join(tables_folder, f'{dataset_name}.tmdl')

	# create a tables folder if it doesn't already exist
	if not os.path.exists(tables_folder):
		os.makedirs(tables_folder)


	# load dataset using pandas
	dataset = pd.read_csv(data_path)





		# add dataset to diagramLayout file ---------------------------------------------------------------------
	with open(diagram_layout_path,'r') as file:
		diagram_layout = json.load(file)


	# add all this junk to describe the table's "nodes"
	diagram_layout["diagrams"][0]["nodes"].append( 
        {
          "location": {
            "x": 0,
            "y": 0
          },
          "nodeIndex": "colony",
          "nodeLineageTag": dataset_id,
          "size": {
            "height": 300,
            "width": 234
          },
          "zIndex": 0
        }
      )

   
	# write to file
	with open(diagram_layout_path,'w') as file:
		json.dump(diagram_layout, file, indent = 2)





	# modify model.tdml file -------------------------------------------------------------------------------------
	with open(model_path, 'a') as file:
		file.write(f'annotation PBI_QueryOrder = [{dataset_name}]\n\nref table {dataset_name}')



	# Data model file --------------------------------------------------------------------------
    
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
				print(f"{col}: This column is probably a date!")

				# change the data type in the panda dataframe
				dataset[col] = pd.to_datetime(dataset[col], format = "%Y-%m-%d")

				# create a date heirarchy table
				file_id = create_date_hr(col_name = col,
				 dataset_name = dataset_name,
				  report_name = report_name, 
				  dashboard_path = dashboard_path )
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
				print(f"{col}: This column is probably a date!")

				# change the data type in the panda dataframe
				dataset[col] = pd.to_datetime(dataset[col], format = "%Y-%m-%d")

				# create a date heirarchy table
				file_id = create_date_hr(col_name = col, 
					dataset_name = dataset_name, 
					report_name = report_name,
					 dashboard_path = dashboard_path )
				break

		# add the column's name to a set for later
		col_names.append(col)

		# record more details in a different set

		col_id = str(uuid.uuid4())

		if dataset[col].dtype == "int64" or dataset[col].dtype == "float64":

			# record more details in a different set
			col_deets.append(f'{{"{col}", Int64.Type}}')


			with open(dataset_file_path, 'a') as file:
				file.write(f'\tcolumn {col}\n')
				file.write('\t\tdataType: int64\n')
				file.write('\t\tformatString: 0\n')
				file.write(f'\t\tlineageTag: {col_id}\n')
				file.write('\t\tsummarizeBy: sum\n')
				file.write(f'\t\tsourceColumn: {col}\n\n')
				file.write('\t\tannotation SummarizationSetBy = Automatic\n\n')

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
				file.write(f'\t\tvariation Variation\n')
				file.write('\t\t\tisDefault\n')
				file.write(f'\t\t\trelationship: {relationship_id}\n')
				file.write(f"\t\t\tdefaultHierarchy: LocalDateTable_{file_id}.'Date Hierarchy'\n\n")
				file.write('\t\tannotation SummarizationSetBy = Automatic\n\n')
				file.write('\t\tannotation UnderlyingDateTimeDataType = Date\n\n')


			# create a new file to define the relationship
			with open(relationships_path, "a") as file:
				file.write(f'relationship {relationship_id}\n')
				file.write(f'\tjoinOnDateBehavior: datePartOnly\n')
				file.write(f'\tfromColumn: {dataset_name}.{col}\n')
				file.write(f'\ttoColumn: LocalDateTable_{file_id}.Date\n\n')






	# write out M code 
	# bc we're stilllllllll not done.....
	with open(dataset_file_path, 'a') as file:
		file.write(f'\tpartition {dataset_name} = m\n')
		file.write('\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n')
		file.write(f'\t\t\t\t\tSource = Csv.Document(File.Contents("{data_path_reversed}"),[Delimiter=",", Columns=10, Encoding=1252, QuoteStyle=QuoteStyle.None]),\n')
		file.write('\t\t\t\t\t#"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),\n')
		file.write(f'\t\t\t\t\t#"Replaced Value" = Table.ReplaceValue(#"Promoted Headers","NA",null,Replacer.ReplaceValue,{{\"{'", "'.join(col_names)}\"}}),\n')
		file.write(f'\t\t\t\t\t#"Changed Type" = Table.TransformColumnTypes(#"Replaced Value",{{{', '.join(map(str, col_deets))}}})\n')
		file.write('\t\t\t\tin\n\t\t\t\t\t#"Changed Type"\n\n')
		file.write('\tannotation PBI_ResultType = Table\n\n\tannotation PBI_NavigationStepName = Navigation\n\n')














