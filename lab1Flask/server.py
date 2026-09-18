from flask import Flask, make_response, request
app = Flask(__name__)

data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]

# Define a route for the root URL ("/")
@app.route('/')
def index():
    return "hello World."

@app.route('/no_content')
def no_content():
    """return 'No content found' json response with a status of 204

    Returns:
        string: No content found
	    status code: 204
    """
    return ({'message': 'No content found'}, 204)

@app.route('/exp')
def index_explicit():
    """Return 'Helloooo' message with a status code of 200.

    Returns:
        response: A response object containing the message and status code 200.
    """
    resp = make_response({"message": "Helloooo"})
    resp.status_code = 200
    return resp

@app.route("/data")
def get_data():
    try:
        # Check if 'data' exists and has a length greater than 0
        if (data and len(data) > 0):
            # Return a JSON response with a message indicating the length of the data
            return {"message": f"Data of length {len(data)} found"}
        else:
            # If 'data' is empty, return a JSON response with a 500 Internal Server Error status code
            return ({"message": "Data is empty"}, 500)
    except NameError:
        # Handle the case where 'data' is not defined
        # Return a JSON response with a 404 Not Found status code
        return ({"message": "Data not found"}, 404)

@app.route("/name_search")
def name_search():
    query = request.args.get('q')

    if (query is None):
        return ({'error_message': 'Input parameter "q" is missing'}, 400)
    
    elif ((query.strip() == "") or query.isdigit()):
        return ({'error_message': 'Invalid input parameter'}, 422)
    
    else:
        for dict_item in data:
            if (dict_item["first_name"].lower() == query.lower()):
                return (dict_item, 200)
            
        return ({'error_message': 'Person not found'}, 404)

@app.route("/count"):
def count():
    try:
        # Attempt to return a JSON response with the count of items in 'data'
        # Replace {insert code to find length of data} with len(data) to get the length of the 'data' collection
        return ({"Number of data entries": len(data)}, 200)
    except NameError:
        # If 'data' is not defined and raises a NameError
        # Return a JSON response with a message and a 500 Internal Server Error status code
        return ({"error_message": "data not defined"}, 500)

@app.route(/person/<uuid:id>)
def find_by_uuid(id):
    # Iterate through the 'data' list to search for a person with a matching ID
    for dict_item in data:
        # Check if the 'id' field of the person matches the 'id' parameter
        if dict_item["id"] == str(id):
            # Return the matching person as a JSON response with a 200 OK status code
            return dict_item
    # If no matching person is found, return a JSON response with a message and a 404 Not Found status code
    return ({"message": "person not found"}, 404)

@app.route("/person/<uuid:id>", methods=['DELETE'])
def delete_by_uuid(id):
    # Iterate through the 'data' list to search for a person with a matching ID
    for dict_item in data:
        # Check if the 'id' field of the person matches the 'id' parameter
        if dict_item["id"] == str(id):
            # Remove the person from the 'data' list
            data.remove(dict_item)
            # Return a JSON response with a message confirming deletion and a 200 OK status code
            return ({"message": f"Person with ID {id} deleted"}, 200)
    # If no matching person is found, return a JSON response with a message and a 404 Not Found status code
    return ({"message": "person not found"}, 404)
