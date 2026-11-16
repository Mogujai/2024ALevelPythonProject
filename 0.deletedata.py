import sql_call as sql

c = sql.sq()
cursor = c.cursor()
cursor.execute("""
               DELETE FROM accounts WHERE accessLevel = 2;
               """,
               )
c.commit()
cursor.close()