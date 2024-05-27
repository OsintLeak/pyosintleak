# osintleak.com API Documentation

The `osintleak.com` API provides functionalities to search various types of data across multiple datasets.

## Dataset and Search Type Compatibility

### 1. Stealer Logs (`stealerlogs`)
- **Compatible Search Types**: `username`, `email`, `password`, `ip`, `logname`, `url`, `ftp`, `cc_number`, `cc_holder`, `subdomain`
- **Incompatible Search Types**: `phone`, `idcard`, `name`, `first_name`, `last_name`
- **Additional Features**:
  - Allows for country-specific filtering and date range selections.
  - Supports Sorting: This dataset allows results to be sorted in ascending (`asc`) or descending (`desc`) order, providing additional flexibility in data presentation.
  - Supports both quick searches & similar searches.

### 2. Database Leaks (`dbleaks`)
- **Compatible Search Types**: `username`, `email`
- **Incompatible Search Types**: `url`, `logname`, `ftp`, `cc_number`, `cc_holder`, `idcard`, `ip`, `password`, `name`, `first_name`, `last_name`, `phone`, `subdomain`
- **Operational Constraints**:
  - Facilitates only quick searches; similar searches are not available.
  - Country-specific and date range filters are not available.

### 3. Database Leaks 2 (`dbleaks2`)
- **Compatible Search Types**: `username`, `email`, `password`, `ip`, `idcard`, `phone`, `name`, `first_name`, `last_name`
- **Incompatible Search Types**: `url`, `logname`, `ftp`, `cc_number`, `cc_holder`, `subdomain`
- **Operational Constraints**:
  - Supports only quick searches; similar searches are not available.
  - Country-specific and date range filters are not available.

## Base URL
`https://osintleak.com/api/v1`

## Authentication
- **API Key**: Required for all API requests. The API key should be included in the query parameters under the key `api_key`.

## Endpoints

### Search API
- **Endpoint**: `/search_api/`
- **Method**: `GET`
- **Description**: Performs a search across specified datasets for a given query and type.
- **Complete URL Example**:
  ```
  https://osintleak.com/api/v1/search_api/?api_key=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&query=ahmed&type=username&stealerlogs=true&dbleaks=true&dbleaks2=true&quick_search=true&similar_search=false&from_date=2024-01-01&to_date=2024-05-01&country=US&page=1&page_size=20&meta=true
  ```
- **Query Parameters**:
  - `api_key` (string): Your API key for authentication.
  - `query` (string): The search term or value.
  - `type` (string): The type of search to perform. Valid options include: `name`, `first_name`, `last_name`, `email`, `username`, `password`, `logname`, `phone`, `idcard`, `cc_holder`, `cc_number`, `ftp`, `ip`, `url`.
  - `stealerlogs` (boolean): Whether to include 'Stealer Logs' dataset in the search (`true` or `false`).
  - `dbleaks` (boolean): Whether to include 'Database Leaks' dataset in the search (`true` or `false`).
  - `dbleaks2` (boolean): Whether to include 'Database Leaks 2' dataset in the search (`true` or `false`).
  - `quick_search` (boolean): Perform a quick search (`true` or `false`).
  - `similar_search` (boolean): Perform a similar search (`true` or `false`).
  - `from_date` (string): Start date for the search in `YYYY-MM-DD` format.
  - `to_date` (string): End date for the search in `YYYY-MM-DD` format.
  - `country` (string): Filter results by country. Support country code like (`US`, `IN`, `RU`).
  - `page` (integer): Page number of the results.
  - `page_size` (integer): Number of results per page (Max 100).
  - `sort` (string): Sort order of the results by idate (`asc` for ascending or `desc` for descending).
  - `meta` (string): Include metadata in the response (`true` or `false`).
- **Responses**:
  - `200`: Search successful. Returns JSON data.
  - `404`: No results found.
  - `403`: Authentication failure or insufficient permissions.
  - Other codes indicate various errors with message explanations.

### Get Results API
- **Endpoint**: `/search_api/`
- **Method**: `GET`
- **Description**: Fetches results from a previous search using a result ID.
- **Complete URL Example**:
  ```
  https://osintleak.com/api/v1/search_api/?api_key=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&result_id=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx&page=2&page_size=20&meta=false
  ```
- **Query Parameters**:
  - `api_key` (string): Your API key for authentication.
  - `result_id` (string): ID of the result to fetch more details.
  - `page` (integer): Page number of the results.
  - `page_size` (integer): Number of results per page (Max 100).
  - `meta` (string): Include metadata in the response (`true` or `false`).
- **Responses**:
  - `200`: Results retrieval successful. Returns JSON data.
  - `404`: No results found with the given ID.
  - `403`: Authentication failure or insufficient permissions.
  - Other codes indicate various errors with message explanations.

## Error Handling
Responses with error status codes will include a JSON object with the key `message` providing details about the error.