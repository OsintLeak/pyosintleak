from pyosintleak import osintleak

ol = osintleak("API_KEY_HERE")
response = ol.search(query="example.com", type="url")
if response["status"] == "success":
    print(response["results"])
else:
    print(response["message"])