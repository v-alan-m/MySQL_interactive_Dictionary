import mysql.connector as msc

con = msc.connect(
# Enter credentials for database access
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

# Create a cursor object to navigate through the database
cursor = con.cursor()

# Request a word from the user
word = input("Enter a word: ")

# Locate the data and define the format and value of the search word, from stdin
query = cursor.execute("SELECT * FROM Dictionary WHERE expression = '%s'" % word)
# Fetch the data
results = cursor.fetchall()
# If results are present (in case the search has no results)
if results:
# Print the defintions. Multiple definitions have been found in the form of tuples:
    for result in results:
        print(results)
# Message to user in case no words are found
else:
    print ("Word can not be found. Please enter in another word")