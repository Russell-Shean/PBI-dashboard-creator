import re, shutil


with open("./pyproject3.toml", "w") as tmp:
  with open("./pyproject.toml", "r") as file:
    for line in file.readlines():
      
      # look for the version line and extract version
      version_match = re.search('(?<=version = ").*(?=")', line )

      #print(line)

      # if a version was found
      if version_match is not None:
        print(line)
        print(version_match.group(0))

        # add one to the old version
        print(version_match.group(0))
        ending_number = re.search("\\d+$" , version_match.group(0))
        print(ending_number.group(0))
      
        new_ending_number = int(ending_number.group(0)) + 1
        print(new_ending_number)
      

        line = re.sub('\\d+"$', str(new_ending_number) + '"', line)
        print(line)


      tmp.write(line)

shutil.move("./pyproject3.toml", "./pyproject.toml")

    

