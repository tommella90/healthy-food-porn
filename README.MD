# CREATE DB - POSTGRES
Start postgres
```
brew install postgresql
brew services start postgresql
psql -U tommella90 -d postgres
CREATE DATABASE recipes_db
```

Now connect to pgadmin and create new server ("register")
- Host name/address: Enter "localhost" 
- By default, PostgreSQL uses port 5432
- Maintenance database: Enter the name of the database you want to connect to. In your case, it's "recipes_db
- Username: Enter the username you want to use to connect to the database. You can use "tommella90