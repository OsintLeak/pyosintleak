from optparse import OptionParser
import pkg_resources
import json
from colorama import Fore, Style
from pyosintleak import osintleak

def handel_response(response):
    if response["status"] == "success":
        meta_data = response["meta_data"]
        global meta_dict
        meta_dict = {str(list(item.keys())[0]): list(item.values())[0]['name'] for item in meta_data}
        for result in response["results"]:
            print_record(result)
        
        max_length = max(len(str(response['page'])), len(str(response['total_page'])), len(response['result_id']), len(str(response['count'])))
        box_width = max_length + 17
        
        print(f"{Fore.YELLOW}+{'-' * box_width}+{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}| Current Page:  {Fore.BLUE}{str(response['page']).rjust(max_length)}{Fore.YELLOW} |{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}| Total Pages:   {Fore.BLUE}{str(response['total_page']).rjust(max_length)}{Fore.YELLOW} |{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}| Result ID:     {Fore.BLUE}{str(response['result_id']).rjust(max_length)}{Fore.YELLOW} |{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}| Result Count:  {Fore.BLUE}{str(response['count']).rjust(max_length)}{Fore.YELLOW} |{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}+{'-' * box_width}+{Style.RESET_ALL}")

        if options.output:
            with open(options.output, 'w') as f:
                json.dump(response, f)
        if response['total_page'] > response['page']:
            print(f"{Fore.YELLOW}[i] Use '{Fore.WHITE}osintleak -r {response['result_id']} --ps {options.page_size} -p {response['page']+1}{Fore.YELLOW}' to fetch the next page{Style.RESET_ALL}")

    elif response["status"] == "error":
        print(f"{Fore.RED}{response['message']}{Style.RESET_ALL}")

def print_record(record):
    if 'leak_id' in record:
        print(f"{Fore.BLUE}+{'=' * 53}+{Style.RESET_ALL}")
        print(f"{Fore.BLUE}| Source: {Fore.WHITE}{record['leak_id']} - {meta_dict.get(str(record['leak_id']), 'Unknown')}{Style.RESET_ALL}")
        for key, value in record.items():
            if key != "leak_id":
                print(f"{Fore.BLUE}| {key}: {Fore.WHITE}{value}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}+{'=' * 53}+{Style.RESET_ALL}")
        print("")
    elif 'source' in record:
        print(f"{Fore.CYAN}+{'=' * 53}+{Style.RESET_ALL}")
        print(f"{Fore.CYAN}| Source: {Fore.WHITE}{record['source']} - {meta_dict.get(str(record['source']), 'Unknown')}{Style.RESET_ALL}")
        for key, value in record.items():
            if key != "source":
                print(f"{Fore.CYAN}| {key}: {Fore.WHITE}{value}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}+{'=' * 53}+{Style.RESET_ALL}")
        print("")
    else:
        print(f"{Fore.GREEN}+{'=' * 53}+{Style.RESET_ALL}")
        if 'log_name' in record:
            print(f"{Fore.GREEN}| Log Name: {Fore.WHITE}{record['log_name']}{Style.RESET_ALL}")
        if 'email' in record:
            print(f"{Fore.GREEN}| Email: {Fore.WHITE}{record['email']}{Style.RESET_ALL}")
        if 'username' in record:
            print(f"{Fore.GREEN}| Username: {Fore.WHITE}{record['username']}{Style.RESET_ALL}")
        if 'password' in record:
            print(f"{Fore.GREEN}| Password: {Fore.WHITE}{record['password']}{Style.RESET_ALL}")
        if 'ip' in record:
            print(f"{Fore.GREEN}| IP: {Fore.WHITE}{record['ip']}{Style.RESET_ALL}")
        if 'insertion_timestamp' in record:
            print(f"{Fore.GREEN}| Insertion Timestamp: {Fore.WHITE}{record['insertion_timestamp']}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}+{'=' * 53}+{Style.RESET_ALL}")
        print("")

def header():
    print(f'''{Fore.GREEN}
   ____       _       __  __               __  
  / __ \\_____(_)___  / /_/ /   ___  ____ _/ /__
 / / / / ___/ / __ \\/ __/ /   / _ \\/ __ `/ //_/
/ /_/ (__  ) / / / / /_/ /___/  __/ /_/ / ,<   
\\____/____/_/_/ /_/\\__/_____/\\___/\\__,_/_/|_|  
{Style.RESET_ALL}
                                     
Version : {Fore.RED}{__import__('pyosintleak').__version__}{Style.RESET_ALL}

''')

def main():
    if not options.silent:
        header()

    configPath = pkg_resources.resource_filename('pyosintleak', 'config.json')
    try:
        configFile = open(configPath, "r+")
    except FileNotFoundError:
        configFile = open(configPath, "w+")
    if configFile.read() == "":
        configData = {"API_KEY": ""}
    else:
        configFile.seek(0)
        configData = json.load(configFile)
    if options.key:
        configData["API_KEY"] = options.key
        configFile = open(configPath, "w+")
        json.dump(configData, configFile)
        print(f"{Fore.GREEN}[i] API_KEY updated successfully{Style.RESET_ALL}")
    else:
        if not configData["API_KEY"]:
            print(f"{Fore.RED}[!] API_KEY is not set in config{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}[!] Please set your API_KEY in config using --key option{Style.RESET_ALL}")
            exit()
    configFile.close()

    ol = osintleak(configData["API_KEY"])

    if options.query:
        if options.type not in ol.AVAILABLE_SEARCH_TYPES:
            print(f"{Fore.RED}[!] Invalid type{Style.RESET_ALL}")
            print(f"[!] Available types are: {', '.join(ol.AVAILABLE_SEARCH_TYPES)}")
            exit()
        response = ol.search(query=options.query, type=options.type, datasets=options.datasets, similar_search=options.similar, page_size=options.page_size, page=options.page)
        handel_response(response)
    elif options.result_id:
        response = ol.get_results(result_id=options.result_id, page_size=options.page_size, page=options.page)
        handel_response(response)
    else:
        print(f"{Fore.RED}[!] Please provide -q query or -r result_id{Style.RESET_ALL}")
        exit()

parser = OptionParser(usage=f"{Fore.YELLOW}%prog: [options]{Style.RESET_ALL}")
parser.add_option( "-q", dest="query", help=f"{Fore.WHITE}Set search query (e.g., '-q osintleak.com'){Style.RESET_ALL}")
parser.add_option( "-r", dest="result_id", help=f"{Fore.WHITE}Fetch recent search by ID (e.g., '-r <ID>'){Style.RESET_ALL}")
parser.add_option( "-t", dest="type", help=f"{Fore.WHITE}Set search type (e.g., '-t url'). Default is 'username'{Style.RESET_ALL}", default="username")
parser.add_option( "-d", dest="datasets", help=f"{Fore.WHITE}Set datasets (e.g., '-d SL,DB,D2'). Default is ''{Style.RESET_ALL}", default="SL,DB,D2")
parser.add_option("--ss", dest="similar", action="store_true", help="Enable similar search")
parser.add_option( "-p", dest="page", type=int, help=f"{Fore.WHITE}Set page number (e.g., '-p 1'). Default is 1{Style.RESET_ALL}", default=1)
parser.add_option( "--ps", dest="page_size", type=int, help=f"{Fore.WHITE}Set page size (e.g., '-p 20'). Default is 20{Style.RESET_ALL}", default=20)
parser.add_option( "-o", dest="output", help=f"{Fore.WHITE}Specify output file (optional){Style.RESET_ALL}")
parser.add_option( "-s", dest="silent", action='store_true', help=f"{Fore.WHITE}Enable silent mode (optional){Style.RESET_ALL}")
parser.add_option( "--key", dest="key", default=False, help=f"{Fore.WHITE}Change API key (optional){Style.RESET_ALL}")


(options, args) = parser.parse_args()
options.datasets = options.datasets.split(',')

meta_dict = {}

if __name__ == "__main__":
    main()