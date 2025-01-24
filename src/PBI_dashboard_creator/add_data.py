import pandas as pd
import os, uuid, json, re, shutil

# Import a custom function to create the date heirarchies
import PBI_dashboard_creator.create_date_hrcy as PBI_date_hr

# Import function to update the model.tmdl file
import PBI_dashboard_creator.update_model_file as PBI_model              # internal function to add data to model.tmdl
import PBI_dashboard_creator.update_diagramLayout as PBI_DL
import PBI_dashboard_creator.create_tmdl as PBI_TMDL

def add_csv(dashboard_path, data_path):

  # generate a random id for the data set
	dataset_id = str(uuid.uuid4())


	# extract bits of names for later
	path_end = os.path.basename(data_path)
	split_end = os.path.splitext(path_end)

	dataset_name = split_end[0]
	dataset_extension = split_end[1]


	report_name = os.path.basename(dashboard_path)

  # Reverse slash directions bc windows is stooooooopid
	data_path_reversed = data_path.replace('/', '\\')
	


	# file paths
	semantic_model_folder = os.path.join(dashboard_path, f'{report_name}.SemanticModel' )
	definitions_folder = os.path.join(semantic_model_folder, "definition")
	model_path = os.path.join(definitions_folder, 'model.tmdl')
	temp_model_path = os.path.join(dashboard_path, 'model2.tmdl')

	relationships_path = os.path.join(definitions_folder, "relationships.tmdl")
	diagram_layout_path = os.path.join(semantic_model_folder, 'diagramLayout.json')

	tables_folder = os.path.join(definitions_folder, 'tables')
	dataset_file_path = os.path.join(tables_folder, f'{dataset_name}.tmdl')

	# create a tables folder if it doesn't already exist
	if not os.path.exists(tables_folder):
		os.makedirs(tables_folder)


	# load dataset using pandas
	dataset = pd.read_csv(data_path)

	# remove unnamed columns
	dataset = dataset.loc[:, ~dataset.columns.str.contains('^Unnamed')]



	# add dataset to diagramLayout file ---------------------------------------------------------------------
	PBI_DL.update_diagramLayout(dashboard_path = dashboard_path, dataset_name = dataset_name, dataset_id = dataset_id)


  # Call a function to update the model file with the dataset
	PBI_model.update_model_file(dashboard_path = dashboard_path, dataset_name = dataset_name)


	# Data model file --------------------------------------------------------------------------
	col_attributes = PBI_TMDL.create_tmdl(dashboard_path = dashboard_path, dataset_name = dataset_name, dataset_id = dataset_id, dataset = dataset)



	# write out M code 
	# bc we're stilllllllll not done.....
	with open(dataset_file_path, 'a') as file:
		file.write(f'\tpartition {dataset_name} = m\n')
		file.write('\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n')
		file.write(f'\t\t\t\t\tSource = Csv.Document(File.Contents("{data_path_reversed}"),[Delimiter=",", Columns={len(dataset.columns)}, Encoding=1252, QuoteStyle=QuoteStyle.None]),\n')
		file.write('\t\t\t\t\t#"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),\n')
		file.write(f'\t\t\t\t\t#"Replaced Value" = Table.ReplaceValue(#"Promoted Headers","NA",null,Replacer.ReplaceValue,{{\"{'", "'.join(col_attributes["col_names"])}\"}}),\n')
		file.write(f'\t\t\t\t\t#"Changed Type" = Table.TransformColumnTypes(#"Replaced Value",{{{', '.join(map(str, col_attributes["col_deets"]))}}})\n')
		file.write('\t\t\t\tin\n\t\t\t\t\t#"Changed Type"\n\n')
		file.write('\tannotation PBI_ResultType = Table\n\n\tannotation PBI_NavigationStepName = Navigation\n\n')







