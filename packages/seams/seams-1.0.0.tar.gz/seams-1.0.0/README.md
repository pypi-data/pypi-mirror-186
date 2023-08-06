# Seams SDK

## Importing Seams
The Seams SDK can be integrated into any Python file by simply calling an import statement and then initializing a new Seams class.

```python
from seams import Seams

seams = Seams()
```

## Set Pythonpath for testing
You must set the pythonpath to the Seams SDK if you wish to run the test files

```bash
set PYTHONPATH=%PYTHONPATH%,C:\Users\{user}\repos\seams-sdk\seams
```

## Connecting to the Seams API
To connect to the Seams API just run the connect() function and pass in the secret, app id, and tenant id, which all should have been given to you by an RJLG employee. The connect() function will not return anything. Once you call the connect() function you can then call seams.bearer to get the bearer token if desired. The bearer token is recorded in the Seams() class and used for each connection behind the scenes.

```python
seams.connect(APP_SECRET, APP_ID, TENANT_ID)
print(seams.bearer)
```

## Seams connection information
After you run seams.connect() you'll be able to run seams.whoami() which will return a JSON formatted string of everything that makes up the seams API connection, including: bearer token, API URL, connection status, and the secret, app id, and tenant id that you provided during the connection. Note: if whoami() is run without running connect() first then it will only return the URL and the connected status of False.

```python
seams.whoami()
```

Returns:
```json
"{'bearer': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYwNmYyYzgwYTcwZjAzN2JlNGYyZmJkZiIsImlhdCI6MTY0ODU4MTk0MywiZXhwIjoxNjQ4NjY4MzQzfQ.U1r4UZgt8MihfKGyHDwkVdFb9_X4-SlM_kvM-JVb3AU', 'url': 'http://localhost:4010/api', 'connected': True, 'secret': '1234567890abcdefghijklmnopqrstuvwxyz', 'app_id': '123456-7891-0123-4567-hgsfdhsd897', 'tenant_id': 'hgsfdhsd897-321-521-7895-asd;ghsad6565'}"
```

## Verifying Connection
To verify that you are connected you can call the me() function which currently returns a giant blob of JSON that represents the graph DB for all the tenants.

```python
response = seams.me()
```

## Disconnecting from Seams
To disconnect from the Seams SDK call the disconnect() method. This is not required as there are no active connections open, but it is still best practice. 
```python
seams.disconnect()
```

# Vertex Methods

## Vertex test file
The vertex test file is located at /Seams/seams/tests/test_vertices.py

## Getting vertex by ID
To get a vertex by the vertex ID you can call the get_vertex_by_id(tenantId, id) function. You'll need the tenant id and vertex id to be able to call this function. 

```python
vertex = seams.get_vertex_by_id('61a5008ba5d83d6a3931594b', '704480ce-4e18-47b5-ae41-24cc9c61c075')
```

## Getting vertices by label
To get all vertices under the same label you can call the get_vertices_by_label(tenantId, label). You'll need the tenant id and the label name to be able to call this function. 

```python
label = seams.get_vertices_by_label('61a5008ba5d83d6a3931594b', "Chamber")
```

## Updating a vertex
To update a vertex call the update_vertex method with 3 required arguments: Tenant Id, Vertex Id, and Vertex Label. The last, optional parameter, is a dictionary of key/value pairs that will represent the data fields of the vertex.

```python
attributes = {
    'type':'Manganin', 
    'location':'upper right corner', 
    'description': 'This is a test vertex created from the sdk'
}

update = seams.update_vertex(tenants['tenant_id'], 'de7f9c4b-748e-4887-a066-8dc1ba8eec4f', 'Manganin Sensor', attributes)
```

## Upserting a vertex
The upsert_vertex() function can be used to first check to see if a vertex with the given label exists, if it does exist then it will update the vertex with the given attributes, if it doesn't exist it will create the vertex. upsert_vertex() has 3 required arguments, tenant_id, vertex_label, and vertex_name; these are all strings. The last, optional parameter, is a dictionary of key/value pairs that will represent the data fields of the vertex.

```python
print("calling upsert_vertex")
upsert = seams.upsert_vertex(tenants["Digital Twin"], "Subject","Test Subject 1", attributes)
print(upsert)
```

## Creating a vertex
To create a vertex call the create_vertex method with 3 required arguments: Tenant Id, Vertex Label, and Vertex Name. The last, optional parameter, is a dictionary of key/value pairs that will represent the data fields of the vertex.

```python
attributes = {
    'type':'Manganin', 
    'location':'upper right corner', 
    'description': 'This is a test vertex created from the sdk'
}

create = seams.create_vertex(tenants['tenant_id'], 'Manganin Sensor', 'Manganin Sensor 1', attributes)
```

## Deleting a vertex
To delete a vertex call the delete_vertex method with 2 required arguments: Tenant Id and Vertex Id

```python
delete = seams.delete_vertex(tenants['tenant_id'], create['id'])
```

## Finding the edges on a vertex
To find the edges in a specific direction on a vertex use the get_edges_on_vertex method. This method has 4 required arguments: Tenant Id, Vertex Id, Vertex Label and direction.

```python
edges_out = seams.get_edges_on_vertex(tenants['tenant_id'], '9e2e8dcd-1b68-4b06-ab41-045d78f62e38', "Test Conducted", "out")
edges_in = seams.get_edges_on_vertex(tenants['tenant_id'], '9e2e8dcd-1b68-4b06-ab41-045d78f62e38', "Test Conducted", "in")
```


# Edge Methods

## Edge test file
The edge test file is located at /Seams/seams/tests/test_edges.py

## Attaching edges to a vertex
To attach an edge to a vertex call the attach_edges method with 4 required arguments: Tenant Id, Vertex Id, Vertex Label and a list of edges that you want to attach to the vertex.

```python
vertex_1 = seams.create_vertex(tenants['tenant_id'], 'Manganin Sensor', 
                    type="Manganin", location='upper right corner', description="This is a test vertex created from the sdk")
vertex_2 = seams.create_vertex(tenants['tenant_id'], 'Manganin Sensor', 
                    type="Manganin", location='bottom left corner', description="This is a test vertex created from the sdk")
vertex_3 = seams.create_vertex(tenants['tenant_id'], 'Manganin Sensor', 
                    type="Manganin", location='middle center', description="This is a test vertex created from the sdk")

vertex_list = []
vertex_list.append(vertex_1['id'])
vertex_list.append(vertex_2['id'])
vertex_list.append(vertex_3['id'])

set_edges = seams.attach_edges(tenants['tenant_id'], "9e2e8dcd-1b68-4b06-ab41-045d78f62e38", "Manganin Sensor", vertex_list)
```

## Attaching a label TO an edge
To attach a label to an edge call the attach_label_to_edge method with 4 required arguments: Tenant Id, Parent Vertex Label, Edge Label and Vertex Id.

```python
set_label_to = seams.attach_label_to_edge(tenants['tenant_id'], "Manganin Sensor", "Manganin Sensor", vertex_1['id'])
```

## Attaching a label FROM an edge
To attach a label from an edge call the attach_label_from_edge method with 4 required arguments: Tenant Id, Parent Vertex Id, Edge Name and Child Label.

```python
set_label_from = seams.attach_label_from_edge(tenants['tenant_id'], vertex_2['id'], "Manganin Sensor", "Manganin Sensor")
```


# File Methods

## File test file
The file test file is located at /Seams/seams/tests/test_files.py

## Bulk upload files
To upload multiple files call the upload_files method which has 1 required argument, Tenant Id, followed by any number of filenames the user wishes to upload.

```python
file1 = open('file-To-Upload.txt', 'w')
file1.write("This is a test text file that is being uploaded and downloaded from the Python SDK.")
file1.close()
file2 = open('secondFileToUpload.txt', 'w')
file2.write("This is a second test text file that is being uploaded and downloaded from the Python SDK.")
file2.close()

upload = seams.upload_files(tenants['tenant_id'], 'file-To-Upload.txt', 'secondFileToUpload.txt')
```

## Bulk download files
To download multiple files call the download_files method which has 1 required argument, Tenant Id, followed by any number of Vertex Id's the user wishes to download. 

```python
download = seams.download_files(tenants['tenant_id'], upload[0]['id'], upload[1]['id'])
for item in download:
    file3 = open(item, 'w')
    file3.write(download[item])
    file3.close()
    print("filename: ", item)
    with open(item, 'r') as f:
        print(f.read())
```
This method will return a JSON formatted object like:
```json
{
   "file-To-Upload.txt":"This is a test text file that is being uploaded and downloaded from the Python SDK.",
   "secondFileToUpload.txt":"This is a second test text file that is being uploaded and downloaded from the Python SDK."
}
```