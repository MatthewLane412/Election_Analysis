# Open the data file.
# Write down the names of all the candidates.
# Add a vote count for each candidate.
# Get the total votes for each candidate.
# Get the total votes cast for the election.


import os
from typing import cast


# The data we need to retrieve.



# 1. The total number of voes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.



# # Import the datetime class from the datetime module.
# import datetime as dt
# # Use the now() attribute on the datetime class to get the present time.
# now = dt.datetime.now()
# # Print the present time.
# print("The time right now is ", now)



# # Open the election results and read the file.
# with open('Resources/election_results.csv') as election_data:

#     # To do: perform analysis.
#     print(election_data)



# # Open the election results and read the file.
# import csv
# import os
# # Assign a variable for the file to load and the path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Open the election results and read the file.
# with open(file_to_load) as election_data:

#     # Print the file object.
#      print(election_data)





# import os

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Using the open() function with the "w" mode we will write data to the file.
# open(file_to_save, "w")





# #Create a filename variable to a direct or indriect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# #Using the with statement to open the file as a text file.
# outfile = open(file_to_save, "w")
# #write some data to the file.
# outfile.write("Hello World")

# #Close the file
# outfile.close()





# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# #Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     #Write some data to the file.
#     txt_file.write("Hello World")





# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# #Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     #Write some data to the file.
#     txt_file.write("Arapahoe, Denver, Jefferson")
    






# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# #Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     #Write some data to the file.
#     txt_file.write("Arapahoe\nDenver\nJefferson")






# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# #Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     #Write some data to the file.
#     txt_file.write("Counties in the Election\n ----------------------\nArapahoe\nDenver\nJefferson")





# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.

    #to do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

# # Print each row in the CSV file.
#     for row in file_reader:
#         print(row)

# Print the header row.
    headers = next(file_reader)
    print(headers)