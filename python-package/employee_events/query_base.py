# Import any dependencies needed to execute sql queries
# YOUR CODE HERE
from sqlite3 import connect
from pathlib import Path

# Define a class called QueryBase
# Use inheritance to add methods
# for querying the employee_events database.
# YOUR CODE HERE
class QueryBase(QueryMixin):
    # Create a class attribute called `name`
    # set the attribute to an empty string
    # YOUR CODE HERE
    name: str = ""

    # Define a `names` method that receives
    # no passed arguments
    # YOUR CODE HERE
    def names(self):        
        # Return an empty list
        # YOUR CODE HERE
        return []


    # Define an `event_counts` method
    # that receives an `id` argument
    # This method should return a pandas dataframe
    # YOUR CODE HERE
    def event_counts(self, id):

        # QUERY 1
        # Write an SQL query that groups by `event_date`
        # and sums the number of positive and negative events
        # Use f-string formatting to set the FROM {table}
        # to the `name` class attribute
        # Use f-string formatting to set the name
        # of id columns used for joining
        # order by the event_date column
        # YOUR CODE HERE
        sql_query = f"""
        SELECT 
            event_date,
            SUM(CASE WHEN event_type = 'positive' THEN 1 ELSE 0 END) AS positive_events,
            SUM(CASE WHEN event_type = 'negative' THEN 1 ELSE 0 END) AS negative_events
        FROM {self.name}
        WHERE {self.name}_id = {id}
        GROUP BY event_date
        ORDER BY event_date;
        """

        return self.pandas_query(sql_query)
            
    

    # Define a `notes` method that receives an id argument
    # This function should return a pandas dataframe
    # YOUR CODE HERE
    def notes(self, id):
        # QUERY 2
        # Write an SQL query that returns `note_date`, and `note`
        # from the `notes` table
        # Set the joined table names and id columns
        # with f-string formatting
        # so the query returns the notes
        # for the table name in the `name` class attribute
        # YOUR CODE HERE
        sql_query = f"""
        SELECT 
            note_date,
            note
        FROM {self.name}
        """

