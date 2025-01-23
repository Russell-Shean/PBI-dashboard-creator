
import os, json


# , chart_type

def add_chart(dashboard_path,
              page_id, 
              chart_id, 
              chart_type,
              data_source, 
              chart_title,
              x_axis_title,
              y_axis_title,
              x_axis_var, 
              y_axis_var, 
              y_axis_var_aggregation_type, 
              x_position, 
              y_position, 
              height, 
              width ):


  '''
  This function adds a new chart to a page in a power BI dashboard report. 

  :param str chart_type: The type of chart to build on the page. Known available types include: ["columnChart","barChart", "clusteredBarChart", ]
  :param str dashboard_path: 




  :param str recipient: The recipient of the message
  :param str message_body: The body of the message
  :param priority: The priority of the message, can be a number 1-5
  :type priority: integer or None
  :return: the message id
  :rtype: int
  :raises ValueError: if the message_body exceeds 160 characters
  :raises TypeError: if the message_body is not a basestring
  
  '''

  # file paths -------------------------------
  report_name = os.path.basename(dashboard_path)

  pages_folder = os.path.join(dashboard_path, f'{report_name}.Report/definition/pages')
  page_folder_path = os.path.join(pages_folder, page_id)

  visuals_folder = os.path.join(page_folder_path, "visuals")
  new_visual_folder = os.path.join(visuals_folder, chart_id)
  visual_json_path = os.path.join(new_visual_folder, "visual.json")







	# checks ---------------------------------------------------------

	# page exists? 
	if os.path.isdir(page_folder_path) is not True:
		raise NameError(f"Couldn't find the page folder at {page_folder_path}")

	# chart id unique? 
	if os.path.isdir(new_visual_folder) is True:
		raise ValueError(f'A visual with that chart_id already exists! Try using a different chart_id')

	else: 
		os.makedirs(new_visual_folder)





	#glob.glob(dashboard_path)



	# define the json for the new chart
	chart_json = {
  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/1.3.0/schema.json",
  "name": chart_id,
  "position": {
    "x": x_position,
    "y": y_position,
    "z": 0,
    "height": height,
    "width": width,
    "tabOrder": 0
  },
  "visual": {
    "visualType": chart_type,
    "query": {
      "queryState": {
        "Category": {
          "projections": [
            {
              "field": {
                "Column": {
                  "Expression": {
                    "SourceRef": {
                      "Entity": data_source
                    }
                  },
                  "Property": x_axis_var
                }
              },
              "queryRef": f"{data_source}.{x_axis_var}",
              "nativeQueryRef": x_axis_var,
              "active": True
            }
          ]
        },
        "Y": {
          "projections": [
            {
              "field": {
                "Aggregation": {
                  "Expression": {
                    "Column": {
                      "Expression": {
                        "SourceRef": {
                          "Entity": data_source
                        }
                      },
                      "Property": y_axis_var
                    }
                  },
                  "Function": 0
                }
              },
              "queryRef": f"{y_axis_var_aggregation_type}({data_source}.{y_axis_var})",
              "nativeQueryRef": f"{y_axis_var_aggregation_type} of {y_axis_var}"
            }
          ]
        }
      },
      "sortDefinition": {
        "sort": [
          {
            "field": {
              "Aggregation": {
                "Expression": {
                  "Column": {
                    "Expression": {
                      "SourceRef": {
                        "Entity": data_source
                      }
                    },
                    "Property": y_axis_var
                  }
                },
                "Function": 0
              }
            },
            "direction": "Descending"
          }
        ],
        "isDefaultSort": True
      }
    },
    "objects": {
      "categoryAxis": [
        {
          "properties": {
            "titleText": {
              "expr": {
                "Literal": {
                  "Value": f"'{x_axis_title}'"
                }
              }
            }
          }
        }
      ],
      "valueAxis": [
        {
          "properties": {
            "titleText": {
              "expr": {
                "Literal": {
                  "Value": f"'{y_axis_title}'"
                }
              }
            }
          }
        }
      ]
    },
    "visualContainerObjects": {
      "title": [
        {
          "properties": {
            "text": {
              "expr": {
                "Literal": {
                  "Value": f"'{chart_title}'"
                }
              }
            }
          }
        }
      ]
    },
    "drillFilterOtherVisuals": True
  }
}

	# Write out the new json 
	with open(visual_json_path, "w") as file:
		json.dump(chart_json, file, indent = 2)


