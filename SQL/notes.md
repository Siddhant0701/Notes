## Manipulations 


- Relational Databses are databases that organize information in rows and columns.
<br/>

- Commands for manipulating data:
  - `CREATE TABLE <name> (column_1 data_type,column_2 data_type,column_3 data_type)` will create a table.
  - `INSERT INTO <name> (column_1,...) VALUES (value_1,...)` inserts new values into the table.
  - `SELECT column FROM <name>` selects the columns from a table.
  - `ALTER TABLE <name> ADD COLUMN column_name data_type` adds a column to the table. All other rows get this value set to NULL. 
  - `UPDATE <name> SET col_name = value WHERE ...` updates a value in the table.
  - `DELETE FROM <name> WHERE ...` deletes a value.
  
<br/>

- Constraints can be set on the columns when creating the table:
  - `PRIMARY KEY` is the unique identifier for each row.
  - `UNIQUE` is the same as PRIMARY KEY except each table can have multiple UNIQUE columns.
  - `NOT NULL` means it must have a value.
  - `DEFAULT <value>` sets a default for the column.

<br/>

## Queries

- `SELECT` is the clause we use every time we want to query information from a database.
- `AS` renames a column or table.
- `DISTINCT` return unique values.
- `WHERE` is a popular command that lets you filter the results of the query based on conditions that you specify.
- `LIKE` and `BETWEEN` are special operators.
- `AND` and `OR` combines multiple conditions.
- `ORDER BY` sorts the result.
- `LIMIT` specifies the maximum number of rows that the query will return.
- `CASE` creates different outputs.

<br/>

## Aggregate Functions

- `COUNT()`: count the number of rows
- `SUM()`: the sum of the values in a column
- `MAX()/MIN()`: the largest/smallest value
- `AVG()`: the average of the values in a column
- `ROUND()`: round the values in the column
- `GROUP BY` is a clause used with aggregate functions to combine data from one or more columns.
- `HAVING` limit the results of a query based on an aggregate property.

<br/>

## Multiple Tables

- `JOIN` will combine rows from different tables if the join condition is true.
- `LEFT JOIN` will return every row in the left table, and if the join condition is not met, NULL values are used to fill in the columns from the right table.
- Primary key is a column that serves a unique identifier for the rows in the table.
- Foreign key is a column that contains the primary key to another table.
- `CROSS JOIN` lets us combine all rows of one table with all rows of another table.
- `UNION` stacks one dataset on top of another.
- `WITH` allows us to define one or more temporary tables that can be used in the final query.

