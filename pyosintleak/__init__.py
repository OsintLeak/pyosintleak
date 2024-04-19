import requests

__version__ = '1.0.1'

class osintleak:
    BASE_URL = "https://osintleak.com/api/v1"
    API_KEY = None
    HEADERS = None
    USER_AGENT = f"OL-Python/{__version__}"
    AVAILABLE_SEARCH_TYPES = ['name', 'first_name', 'last_name', 'email', 'username', 'password', 'logname', 'phone', 'idcard', 'cc_holder', 'cc_number', 'ftp', 'ip', 'url']
    DATASETS = ['SL', 'DB', 'D2']

    def __init__(self, key):
        self.API_KEY = key
        self.HEADERS = {
            "User-Agent": self.USER_AGENT
        }

    def search(self, query, type, datasets=DATASETS, similar_search=False, from_date=None, to_date=None, page=1, page_size=20, meta='true'):
        if type not in self.AVAILABLE_SEARCH_TYPES:
            return {"status": "error", "message": f"Invalid search type. Available types are: {', '.join(self.AVAILABLE_SEARCH_TYPES)}"}
        
        stealerlogs = 'false'
        dbleaks = 'false'
        dbleaks2 = 'false'
        if "SL" in datasets:
            stealerlogs = 'true'
        if "DB" in datasets:
            dbleaks = 'true'
        if "D2" in datasets:
            dbleaks2 = 'true'
            
        if similar_search:
            similar_search = 'true'
            quick_search = 'false'
        else:
            similar_search = 'false'
            quick_search = 'true'

        try:
            PARAMS = {
                "api_key": self.API_KEY,
                "query": query,
                "type": type,
                "stealerlogs": stealerlogs,
                "dbleaks": dbleaks,
                "dbleaks2": dbleaks2,
                "quick_search": quick_search,
                "similar_search": similar_search,
                "from_date": from_date,
                "to_date": to_date,
                "page": page,
                "page_size": page_size,
                "meta": meta
            }
            rep = requests.get(f"{self.BASE_URL}/search_api/", headers=self.HEADERS, params=PARAMS)
            if rep.status_code == 200:
                return rep.json()
            elif rep.status_code == 404:
                return {"status": "error", "message": "Result not found"}
            elif rep.status_code == 403:
                return {"status": "error", "message": rep.json()["message"]}
            else:
                return {"status": "error", "message": f"{rep.status_code} Error fetching data"}
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def get_results(self, result_id, page=1, page_size=20, meta='true'):
        try:
            PARAMS = {
                "api_key": self.API_KEY,
                "result_id": result_id,
                "page": page,
                "page_size": page_size,
                "meta": meta
            }
            rep = requests.get(f"{self.BASE_URL}/search_api/", headers=self.HEADERS, params=PARAMS)
            if rep.status_code == 200:
                return rep.json()
            elif rep.status_code == 404:
                return {"message": "Result not found"}
            elif rep.status_code == 403:
                return {"message": rep.json()["message"]}
            else:
                return {"status": "error", "message": f"{rep.status_code} Error fetching data"}
        except Exception as e:
            return {"status": "error", "message": str(e)}