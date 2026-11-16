def sq():
    import sqlite3 as sql
    with sql.connect("mF.db") as a:
        return a