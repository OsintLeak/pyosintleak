# pyosintleak

pyosintleak is a Python library designed to leverage the capabilities of the osintleak API, streamlining the integration and automation of open-source intelligence (OSINT) operations.

## Installation

You can install pyosintleak using pip:

```bash
pip install pyosintleak
```

Alternatively, you can clone the repository from GitHub:

```bash
git clone https://github.com/osintleak/pyosintleak.git
cd pyosintleak
pip install .
```

## Usage

### Command Line Interface (CLI)

pyosintleak also comes with a command line interface (CLI) tool to interact with the API conveniently.

#### Setting API Key

Before using the CLI tool, you need to set your API key. This key is essential for accessing the osintleak API. You can set or update the API key using the following command:

```bash
osintleak --key <your_api_key>
```

#### CLI Options

- **-q, --query**: Set search query (e.g., `-q osintleak.com`)
- **-r, --result_id**: Fetch recent search by ID (e.g., `-r <ID>`)
- **-t, --type**: Set search type (e.g., `-t url`). Default is 'username'
- **-d, --datasets**: Set datasets (e.g., `-d SL,DB,D2`). Default is ''
- **--ss, --similar**: Enable similar search
- **-p, --page**: Set page number (e.g., `-p 1`). Default is 1
- **--ps, --page_size**: Set page size (e.g., `-p 20`). Default is 20
- **-o, --output**: Specify output file (optional)
- **-s, --silent**: Enable silent mode (optional)
- **--key**: Change API key (optional)

#### Example Usage

```bash
# Set API key
osintleak --key <your_api_key>

# Perform a search
osintleak -q ahmed

# Fetch recent search results by ID
osintleak -r <result_id> -p 2

# Save output to a file
osintleak -q example.com -t url -o output.txt
```

Feel free to explore more options and functionalities by checking the help:

```bash
osintleak --help
```

## Contributing

If you encounter any issues or have suggestions for improvements, please feel free to contribute by opening an issue or submitting a pull request on [GitHub](https://github.com/osintleak/pyosintleak). Your feedback is highly appreciated!