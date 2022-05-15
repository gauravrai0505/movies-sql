import sqlite3
c= sqlite3.connect('movie.db')
print(c) 
c.cursor()

c.execute("INSERT INTO MoviesINFO VALUES('kashmir files','anupam kher','2022','Vivek Agnihotri')")
c.execute("INSERT INTO MoviesINFO VALUES('Turning red','meilin','2022','Domee Shi')")
c.execute("INSERT INTO MoviesINFO VALUES('Kgf 2','Yash','2022','Prashant neil')")
c.execute("INSERT INTO MoviesINFO VALUES('Inception','Leonardo DiCaprio','2022','Christopher Nolan')")

c.commit()
c.close()