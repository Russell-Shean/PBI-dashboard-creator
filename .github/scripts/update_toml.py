import re





with open(pyprojects.toml, "r") as file:
  for line in file.readline():

    # look for the version line and extract version
    version_match = re.search('(?<=version: ").*(?=")', line )

    # if a version was found
    if version_match is not None:
      print(line)
      print(version_match.group()[0])

      # add one to the old version
      print(version_match.group()[0])
      ending_number = re.search("\d+",version_match.group()[0])
      print(ending_number)
      print(new_ending_number)
      new_ending_number = ending_number.group()[2] + 1
      

      line.replace("\d+$", new_ending_number)
      print(line)
