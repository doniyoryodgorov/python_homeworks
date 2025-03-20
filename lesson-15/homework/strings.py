#Review Exercises
#Task 1
#Create a new database with a table named Roster that has three fields: Name, Species, and Age. 
#The Name and Species columns should be text fields, and the Age column should be an integer field.

import sqlite3

create_table = """Create table Roster
(Name TEXT, Species TEXT, Age INT);
"""
con = sqlite3.connect('test.db')
cursor = con.cursor() 
cursor.execute(create_table)
con.commit()
con.close()

#Task 2 Populate your new table with the following values:

insert_table=""" into Roster (Name, Species, Age) 
values
('Benjamin Sisko', 'Human', 40),
('Jadzia Dax', 'Trill', 300),
('Kira Nerys', 'Bajoran', 29);
"""
#Task 3 Update the Name of Jadzia Dax to be Ezri Dax
update_table = """
Update Roster
Set Name = 'Ezri Dax'
Where Name = 'Jadzia Dax'
"""
# Task Display the Name and Age of everyone in the table classified as Bajoran.
select_table = """
Select Name, Age
From Roster
Where Species = 'Bajoran'
"""    
  
