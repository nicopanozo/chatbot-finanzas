from SPARQLWrapper import SPARQLWrapper, JSON
import requests

class anzofraph_connection:
    def __init__(self, endpoint_url, username, password):
        self.endpoint_url = endpoint_url
        self.username = username
        self.password = password
        self.sparql = SPARQLWrapper(self.endpoint_url)
        self.sparql.setCredentials(self.username, self.password)

    def connect(self):
        try:
            # Attempt to connect by fetching the AnzoGraph service description
            self.sparql.setQuery("SELECT * WHERE { ?s ?p ?o } LIMIT 1")
            self.sparql.setReturnFormat(JSON)
            
            # Execute the query and fetch results
            results = self.sparql.query().convert()
            
            # If there are results, the connection is successful
            if results and "results" in results:
                return True
            else:
                return False
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while connecting to AnzoGraph: {e}")

# Uso:
# endpoint_url = "http://localhost:80/sparql"
# username = "admin"
# password = "Passw0rd1"
# anzo_conn = Anzo_conn(endpoint_url, username, password)
# if anzo_conn.connect():
#     print("Connected to AnzoGraph")
# else:
#     print("Failed to connect to AnzoGraph")
