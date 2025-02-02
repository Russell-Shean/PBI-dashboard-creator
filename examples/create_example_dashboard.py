import PBI_dashboard_creator.create_blank_dashboard as PBI_dash
import PBI_dashboard_creator.add_local_csv as PBI_local_csv
import PBI_dashboard_creator.add_tmdl as PBI_tmdl

import PBI_dashboard_creator.create_date_hrcy as PBI_date_hr
import PBI_dashboard_creator.create_new_page as PBI_pages
import PBI_dashboard_creator.create_new_chart as PBI_charts
import PBI_dashboard_creator.add_background_image as PBI_bg_img
import PBI_dashboard_creator.add_ADLS_csv as PBI_blob_csv
import PBI_dashboard_creator.add_text_box as PBI_text_box
import PBI_dashboard_creator.add_button as PBI_button
import PBI_dashboard_creator.add_shape_map as PBI_map

import os

# Define file paths -----------------------------------------------------------------------------------------
report_name = "test_dashboard"
report_location = os.getcwd()

dashboard_path = os.path.join(report_location, report_name)



# Create a new dashboard -----------------------------------------------------------------------------------------
PBI_dash.create_new_dashboard(report_location, report_name)


# add data -------------------------------------------------------------------------------------------------------
# add locally stored csv files to the new dashboard
PBI_local_csv.add_csv(dashboard_path, os.path.join(report_location, "PBI_dashboard_creator/examples/data/colony.csv" ))
PBI_local_csv.add_csv(dashboard_path, os.path.join(report_location, "PBI_dashboard_creator/examples/data/wa_bigfoot_by_county.csv" ))

# add the default DateTable to the dashboard 
PBI_tmdl.add_tmdl_dataset(dashboard_path = dashboard_path, data_path = None, add_default_datetable = True)

# add a csv file stored in ADLS

try:
	PBI_blob_csv.add_csv_from_blob(dashboard_path, 
	                           account_url = "https://sadohpowerbi.blob.core.windows.net",  
	                           blob_name = "test",
	                           data_path = "wa_wolfs.csv",
	                           tenant_id = "11d0e217-264e-400a-8ba0-57dcc127d72d",
	                           use_saved_storage_key = False)

except:
	print("Uh oh! Looks like you don't hav access to this azure tenant or something else went wrong. Skipping the add data from azure step!")


# add new page -----------------------------------------------------------------------------------------------------

## page 2 ---------------------------------------------------------------------------------------------------------
# create a new page
PBI_pages.add_new_page(dashboard_path, 
	                   page_name = "Bee Colonies",
	                   title= "The bees are in Trouble!",
	                   subtitle = "We're losing bee colonies"
	)

# add background image
PBI_bg_img.add_background_img(dashboard_path = dashboard_path, 
	               page_id = "page2", 
	               img_path = "./PBI_dashboard_creator/examples/data/Taipei_skyline_at_sunset_20150607.jpg", 
	               alpha = 51,
	               scaling_method = "Fit")

## page 3 ------------------------------------------------------------------------------------------------------
PBI_pages.add_new_page(dashboard_path, 
	                   page_name = "Bigfoot Map",
	                   title= "Bigfoot sightings",
	                   subtitle = "By Washington Counties"
	)





# Add visual elements ---------------------------------------------------------------------------------------------------

# add a new column chart on the second page
PBI_charts.add_chart(dashboard_path = dashboard_path, 
	      page_id = "page2", 
	      chart_id = "colonies_lost_by_year", 
	      chart_type = "columnChart",
	      data_source = "colony",
	      chart_title = "Number of Bee Colonies Lost per Year",
	      x_axis_title = "Year",
	      y_axis_title = "Number of Colonies",
	      x_axis_var = "year",
	      y_axis_var = "colony_lost",
	      y_axis_var_aggregation_type = "Sum",
	      x_position = 23,
	      y_position = 158,
	      height = 524,
	      width = 603)

# add a text box to the second page
PBI_text_box.add_text_box(text = "Explanatory text in the bottom right corner",
             dashboard_path= dashboard_path,
               page_id = "page2",
                 text_box_id = "page2_explain_box", 
                 height = 200,
                   width= 300,
                     x_position = 1000, 
                     y_position = 600, 
                     font_size = 15)

# add buttons

# download data button (a link to an internet address)
PBI_button.add_button(label = "Download Data",
  dashboard_path = dashboard_path,
  page_id = "page2",
  button_id = "page2_download_button",
  height = 40,
  width = 131,
  x_position = 1000,
  y_position = 540,
  url_link = "https://doh.wa.gov/data-and-statistical-reports/washington-tracking-network-wtn/opioids/overdose-dashboard#downloads")

# navigate back to page 1 button
PBI_button.add_button(label = "Back to page 1",
  dashboard_path = dashboard_path,
  page_id = "page2",
  button_id = "page2_back_to_page1_button",
  height = 40,
  width = 131,
  x_position = 1000,
  y_position = 490,
  page_navigation_link = "page1")


## Add a map to page 3 ----------------------------------------------------------------------

PBI_map.add_shape_map(dashboard_path = dashboard_path, 
              page_id = "page3",
              map_id = "bigfoots_by_county_map",
              data_source = "wa_bigfoot_by_county",
              shape_file_path = "./PBI_dashboard_creator/examples/data/2019_53_WA_Counties9467365124727016.json",
              map_title = "Washington State Bigfoot Sightings by County",
              location_var = "county",
              color_var = "count",
              color_breaks = [0, 15.4, 30.8, 46.2, 61.6, 77.0],
              color_palette = ["#a1343c", "#de6a73", "#e68f96", "#efb5b9", "#6b2328"],
              height = 534,
              width = 816,
              x_position = 75,
              y_position = 132

              )






