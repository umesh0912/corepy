from urllib.parse import urlencode

# Sample list of IDs
ids = [1, 2, 3, 4, 5]

# Creating the query parameter string
query_param_string = urlencode({'id': ids}, doseq=True)

# Printing the query parameter string
print(query_param_string)