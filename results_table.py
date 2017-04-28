import sqlite3

connect = sqlite3.connect('FractionSolver.db')

results_info = connect.cursor()

#Create table to store grocery information
results_info.execute('''CREATE TABLE IF NOT EXISTS results (score real, operator varchar(1))''') # Creates Table for results info

#Insert base data
results_info.execute('''INSERT INTO results (score, correct) VALUES(2.1,"/")''')
#results_info.execute('''INSERT INTO results (score, correct) VALUES(?,?)''', (score, correct))


for row in results_info.execute('SELECT * FROM results ORDER BY score'):
	print (row)

#Save Changes
connect.commit()
connect.close()