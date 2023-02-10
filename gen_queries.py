# Use this function to generate a query that needs to be performed on multiple columns, and can't be executed in the same SELECT

def generate_queries(cols, query):
	queries = []
	first_letter = query[0]
	for col in cols:
		formatted_query = query.replace('col_name', col).replace('"', '')
		queries.append(formatted_query)
	queries = ', '.join(queries)
	# Replace quotes with empty strings and add newlines between the queries for readability
	queries = queries.replace('"', '').replace(f', {first_letter}', f'\n{first_letter}')
	return queries
