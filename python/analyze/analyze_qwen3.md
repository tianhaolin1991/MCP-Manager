# BAD CASE 0
## TASK
Update the file "src/utils/helpers.js" in the project with ID "project-123" by adding a new utility function for formatting dates. The commit message should be "Add date formatting utility" and the changes should be pushed to the "feature/date-utils" branch.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | GitLab | Terminal-Control |
| TOOL | create_or_update_file | update_file_content |
| DESC | Create or update a single file in a project | Update content at specific row(s) in a file. |
| PARAMETERS | project_id: (string) Project ID or URL-encoded path<br>file_path: (string) Path where to create/update the file<br>content: (string) Content of the file<br>commit_message: (string) Commit message<br>branch: (string) Branch to create/update the file in<br>previous_path: (Optional, string) Path of the file to move/rename | path: (string) Path to the file<br>content: (string) New content to place at the specified row(s)<br>row: (Optional, int) Row number to update (0-based)<br>rows: (Optional, list) List of row numbers to update (0-based) |
| SCORES(SERVER/TOOL/FINAL) | 0.325/0.353/0.040 | 0.417/0.555/0.129 |
| RANKS(SERVER/TOOL/FINAL) | 25/372/301 | 2/1/1 |
## ANALYSIS

# BAD CASE 1
## TASK
Run the provided Python code snippet that calculates the factorial of 5 and save it to a file named "factorial_calculation.py".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | code-executor | Data Exploration |
| TOOL | execute_code | run-script |
| DESC | Executes Python code in the configured environment. | Executes a Python script. |
| PARAMETERS | code: (string) The Python code to execute<br>filename: (string) The filename to store the generated code | script: (string, required) The script to execute |
| SCORES(SERVER/TOOL/FINAL) | 0.277/0.546/0.083 | 0.387/0.592/0.136 |
| RANKS(SERVER/TOOL/FINAL) | 44/2/6 | 3/1/1 |
## ANALYSIS

# BAD CASE 2
## TASK
Retrieve the current connection URL and API key status for the Meilisearch instance.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Meilisearch | Unstructured |
| TOOL | get-connection-settings | get_source_info |
| DESC | View current Meilisearch connection URL and API key status | Get detailed information about a specific source connector. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.517/0.571/0.169 | 0.630/0.711/0.319 |
| RANKS(SERVER/TOOL/FINAL) | 6/210/50 | 1/2/1 |
## ANALYSIS

# BAD CASE 3
## TASK
Update the connection settings to a new Meilisearch instance with the URL "https://search.example.com" and the API key "abc123xyz".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Meilisearch | Unstructured |
| TOOL | update-connection-settings | update_source_connector |
| DESC | Update URL and/or API key to connect to a different instance | Update an existing source connector by params. |
| PARAMETERS | url: (string) New Meilisearch instance URL<br>api_key: (string) New Meilisearch API key |  |
| SCORES(SERVER/TOOL/FINAL) | 0.413/0.478/0.094 | 0.560/0.680/0.259 |
| RANKS(SERVER/TOOL/FINAL) | 19/310/153 | 1/2/1 |
## ANALYSIS

# BAD CASE 4
## TASK
Create a new index with the unique identifier "user_profiles" and set "user_id" as the primary key.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Meilisearch | DBHub |
| TOOL | create-index | explain_db |
| DESC | Create a new index with optional primary key | Explains database elements such as tables, indexes, and procedures. |
| PARAMETERS | uid: (string) Unique identifier for the index<br>primaryKey: (Optional, string) Primary key for the index | element_type: (string) The type of database element to explain (e.g., 'table', 'index', 'procedure').<br>element_name: (string) The name of the database element to explain. |
| SCORES(SERVER/TOOL/FINAL) | 0.335/0.556/0.104 | 0.456/0.579/0.153 |
| RANKS(SERVER/TOOL/FINAL) | 53/12/21 | 3/7/1 |
## ANALYSIS

# BAD CASE 5
## TASK
List all available indexes in the current database.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Meilisearch | ClickHouse |
| TOOL | list-indexes | list_tables |
| DESC | List all available indexes | List all tables in a database. |
| PARAMETERS |  | database: (string) The name of the database. |
| SCORES(SERVER/TOOL/FINAL) | 0.445/0.571/0.145 | 0.463/0.756/0.264 |
| RANKS(SERVER/TOOL/FINAL) | 20/100/63 | 14/5/1 |
## ANALYSIS

# BAD CASE 6
## TASK
Search for the top 5 AI agents related to natural language processing with a timeout of 10 seconds.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | AI Agent Marketplace Index | OpenAI WebSearch MCP |
| TOOL | search_ai_agent | web_search |
| DESC | General search of AI Agents for information, websites, content, and metric statistics of web traffic, etc. | Call OpenAI websearch as a tool. |
| PARAMETERS | q: (str) Query string for searching AI agents<br>limit: (Optional, int) Maximum number of results to return (default is 100)<br>timeout: (Optional, int) Timeout for the search request in seconds (default is 5) | type: (string) web_search_preview<br>search_context_size: (string) High level guidance for the amount of context window space to use for the search. One of low, medium, or high. medium is the default.<br>user_location: (object or null) User location details, including type, city, country, region, and timezone. |
| SCORES(SERVER/TOOL/FINAL) | 0.334/0.725/0.175 | 0.587/0.756/0.335 |
| RANKS(SERVER/TOOL/FINAL) | 149/17/85 | 6/3/1 |
## ANALYSIS

# BAD CASE 7
## TASK
Retrieve the execution details for the DAG with the ID "customer_data_pipeline".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Airflow | n8n |
| TOOL | Get DAG Details | execution_get |
| DESC | Gets details of a specific DAG. | Gets details of a specific execution. |
| PARAMETERS | dag_id: (string) The ID of the DAG. | id: (string) The ID of the execution |
| SCORES(SERVER/TOOL/FINAL) | 0.497/0.831/0.344 | 0.618/0.868/0.466 |
| RANKS(SERVER/TOOL/FINAL) | 6/3/3 | 1/2/1 |
## ANALYSIS

# BAD CASE 8
## TASK
List all available data sources in the current Tinybird workspace.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Tinybird | Unstructured |
| TOOL | list-data-sources | list_sources |
| DESC | Lists all Data Sources in the Tinybird Workspace | Lists available sources from the Unstructured API. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.461/0.538/0.134 | 0.606/0.807/0.395 |
| RANKS(SERVER/TOOL/FINAL) | 30/377/260 | 2/1/1 |
## ANALYSIS

# BAD CASE 9
## TASK
List all available Pipe Endpoints in the current Tinybird Workspace.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Tinybird | Unstructured |
| TOOL | list-pipes | list_workflows_with_finished_jobs |
| DESC | Lists all Pipe Endpoints in the Tinybird Workspace | Lists all workflows that have any completed job, together with information about source and destination details. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.434/0.563/0.137 | 0.592/0.700/0.290 |
| RANKS(SERVER/TOOL/FINAL) | 27/274/191 | 2/4/1 |
## ANALYSIS

# BAD CASE 10
## TASK
Retrieve the schema and details of the Data Source named "Customer_Orders".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Tinybird | Unstructured |
| TOOL | get-data-source | get_source_info |
| DESC | Gets the information of a Data Source given its name, including the schema | Get detailed information about a specific source connector. |
| PARAMETERS | name: (string) The name of the Data Source |  |
| SCORES(SERVER/TOOL/FINAL) | 0.413/0.500/0.103 | 0.561/0.747/0.313 |
| RANKS(SERVER/TOOL/FINAL) | 67/408/383 | 4/3/1 |
## ANALYSIS

# BAD CASE 11
## TASK
Retrieve the nodes and SQL transformation details for the Pipe Endpoint named "customer_data_pipeline".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Tinybird | Heroku |
| TOOL | get-pipe | pipelines_info |
| DESC | Gets the information of a Pipe Endpoint given its name, including its nodes and SQL transformation | Get detailed pipeline information. |
| PARAMETERS | name: (string) The name of the Pipe Endpoint |  |
| SCORES(SERVER/TOOL/FINAL) | 0.423/0.565/0.135 | 0.518/0.785/0.319 |
| RANKS(SERVER/TOOL/FINAL) | 55/164/171 | 6/1/1 |
## ANALYSIS

# BAD CASE 12
## TASK
Retrieve the last 30 days of sales data from the 'monthly-sales' endpoint, filtering by the 'region' parameter set to 'North America'.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Tinybird | Aranet4 |
| TOOL | request-pipe-data | get_data_by_timerange |
| DESC | Requests data from a Pipe Endpoint via an HTTP request. Pipe endpoints can have parameters to filter the analytical data | Get data within a specific time range from the local database. Can specify the number of measurements. |
| PARAMETERS | name: (string) The name of the Pipe Endpoint<br>parameters: (Optional, object) Parameters to filter the data | start_time: (str) Start time of the range.<br>end_time: (str) End time of the range.<br>measurements: (Optional, int) Number of measurements to retrieve. |
| SCORES(SERVER/TOOL/FINAL) | 0.318/0.489/0.076 | 0.476/0.646/0.199 |
| RANKS(SERVER/TOOL/FINAL) | 131/227/371 | 2/2/1 |
## ANALYSIS

# BAD CASE 13
## TASK
Run a select query to retrieve the top 10 highest-selling products from the sales database for Q1 2024.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Tinybird | dune-analytics-mcp |
| TOOL | run-select-query | get_latest_result |
| DESC | Allows to run a select query over a Data Source to extract insights | Retrieves the latest results of a specified Dune query. |
| PARAMETERS | query: (string) The SQL select query | query_id: (int) The ID of the Dune query. |
| SCORES(SERVER/TOOL/FINAL) | 0.221/0.342/0.026 | 0.417/0.512/0.110 |
| RANKS(SERVER/TOOL/FINAL) | 183/581/712 | 2/7/1 |
## ANALYSIS

# BAD CASE 14
## TASK
Add a new business insight about the recent increase in customer retention rates to the memo resource.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Tinybird | Sqlite |
| TOOL | append-insight | append_insight |
| DESC | Adds a new business insight to the memo resource | Add new business insights to the memo resource |
| PARAMETERS | insight: (string) The business insight to add | insight: (string) Business insight discovered from data analysis |
| SCORES(SERVER/TOOL/FINAL) | 0.350/0.746/0.195 | 0.723/0.764/0.423 |
| RANKS(SERVER/TOOL/FINAL) | 127/5/5 | 1/3/1 |
## ANALYSIS

# BAD CASE 15
## TASK
Retrieve a list of all available collections stored in the database.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Astra DB | Outline |
| TOOL | GetCollections | List Collections |
| DESC | Get all collections in the database | List all available collections. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.336/0.633/0.135 | 0.409/0.911/0.340 |
| RANKS(SERVER/TOOL/FINAL) | 56/25/32 | 13/1/1 |
## ANALYSIS

# BAD CASE 16
## TASK
Update the existing collection in the database with the latest data entries.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Astra DB | MongoDB Lens |
| TOOL | UpdateCollection | rename-collection |
| DESC | Update an existing collection in the database | Rename existing collections (requires confirmation when dropping targets) |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.334/0.635/0.135 | 0.420/0.662/0.184 |
| RANKS(SERVER/TOOL/FINAL) | 54/6/18 | 9/2/1 |
## ANALYSIS

# BAD CASE 17
## TASK
Delete the specified collection from the connected database.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Astra DB | Graphlit |
| TOOL | DeleteCollection | Delete Collection(s) |
| DESC | Delete a collection from the database | Deletes one or more collections from the knowledge base. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.297/0.702/0.146 | 0.351/0.858/0.258 |
| RANKS(SERVER/TOOL/FINAL) | 63/6/20 | 23/1/1 |
## ANALYSIS

# BAD CASE 18
## TASK
List all records from the 'customers' collection in the database.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Astra DB | Chroma |
| TOOL | ListRecords | chroma_list_collections |
| DESC | List records from a collection in the database | List all collections with pagination support |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.370/0.574/0.122 | 0.609/0.514/0.191 |
| RANKS(SERVER/TOOL/FINAL) | 42/45/39 | 1/159/1 |
## ANALYSIS

# BAD CASE 19
## TASK
Retrieve the record with ID "12345" from the specified collection.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Astra DB | Couchbase |
| TOOL | GetRecord | get_document_by_id |
| DESC | Get a specific record from a collection by ID | Get a document by ID from a specified scope and collection. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.328/0.509/0.085 | 0.396/0.741/0.217 |
| RANKS(SERVER/TOOL/FINAL) | 68/104/108 | 9/1/1 |
## ANALYSIS

# BAD CASE 20
## TASK
Create a new record in the specified collection with the provided data fields.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Astra DB | Fibery |
| TOOL | CreateRecord | create_entities_batch |
| DESC | Create a new record in a collection | Creates multiple new entities in your Fibery workspace with specified field values. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.337/0.496/0.083 | 0.457/0.711/0.231 |
| RANKS(SERVER/TOOL/FINAL) | 27/77/58 | 2/1/1 |
## ANALYSIS

# BAD CASE 21
## TASK
Update the existing record with ID '12345' in the specified collection.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Astra DB | Couchbase |
| TOOL | UpdateRecord | upsert_document_by_id |
| DESC | Update an existing record in a collection | Upsert a document by ID to a specified scope and collection. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.311/0.528/0.087 | 0.364/0.748/0.203 |
| RANKS(SERVER/TOOL/FINAL) | 50/55/65 | 18/1/1 |
## ANALYSIS

# BAD CASE 22
## TASK
Convert the provided text content into an audio file using ElevenLabs' text-to-speech service.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Graphlit | Qwen_Max |
| TOOL | Publish as Audio (ElevenLabs Audio) | qwen_max |
| DESC | Publishes content as audio using ElevenLabs. | Generates text using the Qwen Max language model. |
| PARAMETERS |  | prompt: (string) The input prompt for the model.<br>max_tokens: (number) The maximum number of tokens to generate in the output.<br>temperature: (number) Controls the randomness of the model's output. |
| SCORES(SERVER/TOOL/FINAL) | 0.242/0.904/0.197 | 0.490/0.688/0.232 |
| RANKS(SERVER/TOOL/FINAL) | 134/1/6 | 5/4/1 |
## ANALYSIS

# BAD CASE 23
## TASK
Retrieve the top 5 products matching the search term "wireless headphones" from the product catalog.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Shopify | Productboard |
| TOOL | get-products | get_product_detail |
| DESC | Get all products or search by title | Retrieves detailed information about a specific product. |
| PARAMETERS | searchTitle: (optional string) Filter products by title<br>limit: (number) Maximum number of products to return |  |
| SCORES(SERVER/TOOL/FINAL) | 0.378/0.460/0.080 | 0.520/0.744/0.288 |
| RANKS(SERVER/TOOL/FINAL) | 38/444/318 | 2/1/1 |
## ANALYSIS

# BAD CASE 24
## TASK
Retrieve the product details for the item with ID "PRD-2024-0456".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Shopify | Productboard |
| TOOL | get-product-by-id | get_product_detail |
| DESC | Get a specific product by ID | Retrieves detailed information about a specific product. |
| PARAMETERS | productId: (string) ID of the product to retrieve |  |
| SCORES(SERVER/TOOL/FINAL) | 0.476/0.504/0.121 | 0.598/0.844/0.426 |
| RANKS(SERVER/TOOL/FINAL) | 6/345/96 | 1/1/1 |
## ANALYSIS

# BAD CASE 25
## TASK
Retrieve the first 15 customers whose names or emails contain the keyword "tech".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Shopify | Intercom |
| TOOL | get-customers | search_tickets_by_customer |
| DESC | Get customers or search by name/email | Finds tickets associated with a specific customer. |
| PARAMETERS | searchQuery: (optional string) Filter customers by name or email<br>limit: (optional number, default: 10) Maximum number of customers to return | customerIdentifier: (string) Customer email or Intercom ID (required)<br>startDate: (Optional, DD/MM/YYYY) Optional start date<br>endDate: (Optional, DD/MM/YYYY) Optional end date |
| SCORES(SERVER/TOOL/FINAL) | 0.368/0.485/0.087 | 0.481/0.676/0.220 |
| RANKS(SERVER/TOOL/FINAL) | 56/303/230 | 5/2/1 |
## ANALYSIS

# BAD CASE 26
## TASK
Retrieve the latest 5 orders for the Shopify customer with ID "6276879810626".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Shopify | Stripe |
| TOOL | get-customer-orders | listProducts |
| DESC | Get orders for a specific customer | Lists all products in Stripe. |
| PARAMETERS | customerId: (string, required) Shopify customer ID (numeric ID only, like "6276879810626")<br>limit: (optional number, default: 10) Maximum number of orders to return |  |
| SCORES(SERVER/TOOL/FINAL) | 0.542/0.486/0.143 | 0.409/0.729/0.217 |
| RANKS(SERVER/TOOL/FINAL) | 2/412/46 | 24/1/1 |
## ANALYSIS

# BAD CASE 27
## TASK
Retrieve the latest 5 orders with a status of "shipped" from the order database.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Shopify | DBHub |
| TOOL | get-orders | execute_sql |
| DESC | Get orders with optional filtering | Executes SQL queries on the connected database. |
| PARAMETERS | status: (optional string) Filter by order status<br>limit: (optional number, default: 10) Maximum number of orders to return | dsn: (string) The database connection string.<br>sql: (string) The SQL query to execute. |
| SCORES(SERVER/TOOL/FINAL) | 0.468/0.410/0.090 | 0.453/0.532/0.128 |
| RANKS(SERVER/TOOL/FINAL) | 1/245/28 | 3/8/1 |
## ANALYSIS

# BAD CASE 28
## TASK
Retrieve the order details for the Shopify order with ID "gid://shopify/Order/6090960994370".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Shopify | Productboard |
| TOOL | get-order-by-id | get_product_detail |
| DESC | Get a specific order by ID | Retrieves detailed information about a specific product. |
| PARAMETERS | orderId: (string, required) Full Shopify order ID (e.g., "gid://shopify/Order/6090960994370") |  |
| SCORES(SERVER/TOOL/FINAL) | 0.568/0.466/0.151 | 0.544/0.726/0.286 |
| RANKS(SERVER/TOOL/FINAL) | 2/473/22 | 3/1/1 |
## ANALYSIS

# BAD CASE 29
## TASK
Retrieve all customer records from the Hologres database where the registration date is after January 1, 2023.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Hologres | Intercom |
| TOOL | execute_select_sql | search_tickets_by_customer |
| DESC | Execute a SELECT SQL query on the Hologres server | Finds tickets associated with a specific customer. |
| PARAMETERS |  | customerIdentifier: (string) Customer email or Intercom ID (required)<br>startDate: (Optional, DD/MM/YYYY) Optional start date<br>endDate: (Optional, DD/MM/YYYY) Optional end date |
| SCORES(SERVER/TOOL/FINAL) | 0.000/0.000/0.000 | 0.433/0.685/0.203 |
| RANKS(SERVER/TOOL/FINAL) | -1/-1/-1 | 3/2/1 |
## ANALYSIS

# BAD CASE 30
## TASK
Update the customer records in the Hologres database to set the 'status' field to 'inactive' for all customers who have not made a purchase in the last 12 months.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Hologres | Intercom |
| TOOL | execute_dml_sql | search_tickets_by_customer |
| DESC | Execute a DML (INSERT, UPDATE, DELETE) SQL query on the Hologres server | Finds tickets associated with a specific customer. |
| PARAMETERS |  | customerIdentifier: (string) Customer email or Intercom ID (required)<br>startDate: (Optional, DD/MM/YYYY) Optional start date<br>endDate: (Optional, DD/MM/YYYY) Optional end date |
| SCORES(SERVER/TOOL/FINAL) | 0.000/0.000/0.000 | 0.390/0.548/0.117 |
| RANKS(SERVER/TOOL/FINAL) | -1/-1/-1 | 10/2/1 |
## ANALYSIS

# BAD CASE 31
## TASK
Create a new table named 'customer_orders' with columns for customer_id (integer), order_date (date), and total_amount (decimal) in the Hologres database.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Hologres | Snowflake |
| TOOL | execute_ddl_sql | create_table |
| DESC | Execute a DDL (CREATE, ALTER, DROP) SQL query on the Hologres server | Create new tables in the database. |
| PARAMETERS |  | query: (string) CREATE TABLE SQL statement |
| SCORES(SERVER/TOOL/FINAL) | 0.373/0.412/0.063 | 0.452/0.660/0.197 |
| RANKS(SERVER/TOOL/FINAL) | 27/213/179 | 6/1/1 |
## ANALYSIS

# BAD CASE 32
## TASK
Retrieve the primary hours of operation for the DevHub location with ID 'LOC123'.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | DevHub | DevHub |
| TOOL | get_hours_of_operation | get_hours_of_operation |
| DESC | Gets the hours of operation for a specific DevHub location. Returns a structured list of time ranges for each day of the week. | Gets the hours of operation for a specific DevHub location. Returns a structured list of time ranges for each day of the week. |
| PARAMETERS | location_id: (string) The ID of the location.<br>hours_type: (Optional, string) The type of hours to retrieve, default is 'primary'. | location_id: (string) The ID of the location.<br>hours_type: (Optional, string) The type of hours to retrieve, default is 'primary'. |
| SCORES(SERVER/TOOL/FINAL) | 0.284/0.850/0.205 | 0.284/0.850/0.205 |
| RANKS(SERVER/TOOL/FINAL) | 193/1/1 | 193/1/1 |
## ANALYSIS

# BAD CASE 33
## TASK
List all available apps sorted by creation date, starting from the app with the slug "example-app" and limit the results to 20 per page.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Bitrise | Heroku |
| TOOL | list_apps | get_app_info |
| DESC | List all the apps available for the authenticated account | Get detailed information about an app, including its configuration, dynos, and add-ons. |
| PARAMETERS | sort_by: (Optional, string) Order of the apps: last_build_at (default) or created_at<br>next: (Optional, string) Slug of the first app in the response<br>limit: (Optional, integer) Max number of elements per page (default: 50) |  |
| SCORES(SERVER/TOOL/FINAL) | 0.484/0.515/0.128 | 0.519/0.822/0.351 |
| RANKS(SERVER/TOOL/FINAL) | 7/257/65 | 4/1/1 |
## ANALYSIS

# BAD CASE 34
## TASK
Swap 100 USDC for ETH on the Balmy platform.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | GOAT | GOAT |
| TOOL | Swap tokens on Balmy | Swap tokens on Uniswap |
| DESC | Allows token swapping on the Balmy platform. | Facilitates token swapping on Uniswap. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.650/0.700/0.318 | 0.650/0.787/0.403 |
| RANKS(SERVER/TOOL/FINAL) | 1/10/7 | 1/1/1 |
## ANALYSIS

# BAD CASE 35
## TASK
Retrieve the latest insights for the top 5 trending tokens in the market.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | GOAT | GOAT |
| TOOL | Get token insights using BirdEye API | Get token insights using BMX API |
| DESC | Provides token insights using the BirdEye API. | Fetches token insights using the BMX API. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.553/0.754/0.314 | 0.553/0.776/0.333 |
| RANKS(SERVER/TOOL/FINAL) | 3/3/2 | 3/2/1 |
## ANALYSIS

# BAD CASE 36
## TASK
Retrieve the latest market data for Bitcoin using the CoinGecko API.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | GOAT | coin_api_mcp |
| TOOL | Get coin information using CoinGecko API | get-coin-quotes |
| DESC | Retrieves coin information using the CoinGecko API. | Fetches the latest market quotes for one or more cryptocurrencies. |
| PARAMETERS |  | id: (string, optional) One or more comma-separated cryptocurrency CoinMarketCap IDs.<br>slug: (string, optional) A comma-separated list of cryptocurrency slugs.<br>symbol: (string, optional) One or more comma-separated cryptocurrency symbols. |
| SCORES(SERVER/TOOL/FINAL) | 0.490/0.731/0.261 | 0.630/0.833/0.437 |
| RANKS(SERVER/TOOL/FINAL) | 4/6/10 | 2/1/1 |
## ANALYSIS

# BAD CASE 37
## TASK
Retrieve the latest market data for the top 10 cryptocurrencies by market capitalization.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | GOAT | coin_api_mcp |
| TOOL | Get coin information using Coinmarketcap API | get-coin-quotes |
| DESC | Fetches coin information using the Coinmarketcap API. | Fetches the latest market quotes for one or more cryptocurrencies. |
| PARAMETERS |  | id: (string, optional) One or more comma-separated cryptocurrency CoinMarketCap IDs.<br>slug: (string, optional) A comma-separated list of cryptocurrency slugs.<br>symbol: (string, optional) One or more comma-separated cryptocurrency symbols. |
| SCORES(SERVER/TOOL/FINAL) | 0.520/0.696/0.252 | 0.684/0.861/0.507 |
| RANKS(SERVER/TOOL/FINAL) | 5/10/14 | 2/1/1 |
## ANALYSIS

# BAD CASE 38
## TASK
Transfer 100 ATOM tokens from one Cosmos wallet address to another.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | GOAT | GOAT |
| TOOL | Interact with Cosmos tokens | Create a wallet, mint tokens and get test tokens on any chain using Crossmint |
| DESC | Enables interaction with Cosmos tokens. | Facilitates the creation of wallets, minting of tokens, and retrieval of test tokens on any supported chain using Crossmint. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.689/0.765/0.403 | 0.689/0.776/0.414 |
| RANKS(SERVER/TOOL/FINAL) | 1/6/5 | 1/2/1 |
## ANALYSIS

# BAD CASE 39
## TASK
Retrieve the latest price and trading volume data for the top 5 trending tokens on the Ethereum network.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | GOAT | Financial Datasets |
| TOOL | Get token information using Dexscreener API | get_current_crypto_price |
| DESC | Provides token information using the Dexscreener API. | Get the current / latest price of a crypto currency. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.559/0.661/0.244 | 0.723/0.790/0.451 |
| RANKS(SERVER/TOOL/FINAL) | 4/24/21 | 1/3/1 |
## ANALYSIS

# BAD CASE 44
## TASK
Retrieve the detailed metrics for the index with the unique identifier "IDX-2024-001".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Meilisearch | Aiven |
| TOOL | get-index-metrics | get_service_details |
| DESC | Get detailed metrics for a specific index | Get the detail of your service in a specific Aiven project. |
| PARAMETERS | uid: (string) Unique identifier for the index |  |
| SCORES(SERVER/TOOL/FINAL) | 0.522/0.487/0.132 | 0.521/0.666/0.231 |
| RANKS(SERVER/TOOL/FINAL) | 6/594/145 | 7/9/1 |
## ANALYSIS

# BAD CASE 45
## TASK
Retrieve the first 15 documents from the index with the unique identifier "customer_reviews".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Meilisearch | lucene-mcp-server |
| TOOL | get-documents | GET /mcp/v1/list |
| DESC | Retrieve documents from an index with pagination | Lists documents from the Lucene index. |
| PARAMETERS | indexUid: (string) Unique identifier for the index<br>offset: (Optional, integer) Number of results to skip (default: 0)<br>limit: (Optional, integer) Maximum number of results to return (default: 20) | ids: (array) An array of document IDs to list. |
| SCORES(SERVER/TOOL/FINAL) | 0.426/0.576/0.141 | 0.561/0.711/0.284 |
| RANKS(SERVER/TOOL/FINAL) | 55/135/145 | 4/3/1 |
## ANALYSIS

# BAD CASE 46
## TASK
Add or update 5 product documents in the index with the unique identifier "products_2024". The documents should include fields for product ID, name, price, and category.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Meilisearch | Productboard |
| TOOL | add-documents | get_product_detail |
| DESC | Add or update documents in an index | Retrieves detailed information about a specific product. |
| PARAMETERS | indexUid: (string) Unique identifier for the index<br>documents: (array of objects) Documents to add or update |  |
| SCORES(SERVER/TOOL/FINAL) | 0.381/0.484/0.089 | 0.527/0.645/0.219 |
| RANKS(SERVER/TOOL/FINAL) | 55/225/253 | 3/4/1 |
## ANALYSIS

# BAD CASE 47
## TASK
Search for documents containing the keyword "machine learning" across all indices, limiting the results to 15 per index and sorting them by publication date in descending order.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Meilisearch | DPLP |
| TOOL | search | search |
| DESC | Flexible search across single or multiple indices with filtering and sorting options | Search DBLP for publications using boolean queries. |
| PARAMETERS | query: (string) The search query (required)<br>indexUid: (Optional, string) Specific index to search in<br>limit: (Optional, integer) Maximum number of results per index (default: 20)<br>offset: (Optional, integer) Number of results to skip (default: 0)<br>filter: (Optional, string) Filter expression<br>sort: (Optional, array of strings) Sorting rules | query: (string, required) A query string that may include boolean operators 'and' and 'or' (case-insensitive)<br>max_results: (number, optional) Maximum number of publications to return. Default is 10<br>year_from: (number, optional) Lower bound for publication year<br>year_to: (number, optional) Upper bound for publication year<br>venue_filter: (string, optional) Case-insensitive substring filter for publication venues (e.g., 'iclr')<br>include_bibtex: (boolean, optional) Whether to include BibTeX entries in the results. Default is false |
| SCORES(SERVER/TOOL/FINAL) | 0.362/0.510/0.094 | 0.491/0.845/0.351 |
| RANKS(SERVER/TOOL/FINAL) | 63/184/197 | 7/1/1 |
## ANALYSIS

# BAD CASE 48
## TASK
Retrieve the current configuration details for the index with the unique identifier "IDX12345".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Meilisearch | Keboola |
| TOOL | get-settings | get_component_details |
| DESC | View current settings for an index | Gets detailed information about a specific Keboola component configuration given component/transformation ID and configuration ID. |
| PARAMETERS | uid: (string) Unique identifier for the index |  |
| SCORES(SERVER/TOOL/FINAL) | 0.473/0.429/0.096 | 0.439/0.783/0.269 |
| RANKS(SERVER/TOOL/FINAL) | 8/900/302 | 18/2/1 |
## ANALYSIS

# BAD CASE 49
## TASK
Update the ranking and faceting settings for the index with the unique identifier 'IDX12345' to optimize search performance.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Meilisearch | Pinecone |
| TOOL | update-settings | rerank-documents |
| DESC | Update index settings (ranking, faceting, etc.) | Reranks a collection of records or text documents using a specialized reranking model. |
| PARAMETERS | uid: (string) Unique identifier for the index<br>settings: (object) New settings to apply |  |
| SCORES(SERVER/TOOL/FINAL) | 0.391/0.733/0.210 | 0.510/0.646/0.213 |
| RANKS(SERVER/TOOL/FINAL) | 17/1/2 | 1/3/1 |
## ANALYSIS

# BAD CASE 50
## TASK
List all available API keys stored in the system.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Meilisearch | GOAT |
| TOOL | get-keys | Get token insights using BirdEye API |
| DESC | List all API keys | Provides token insights using the BirdEye API. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.414/0.657/0.179 | 0.514/0.659/0.223 |
| RANKS(SERVER/TOOL/FINAL) | 36/25/30 | 5/23/1 |
## ANALYSIS

# BAD CASE 51
## TASK
Generate a new API key with permissions to read and write data on the "customers" and "orders" indexes, set to expire on 2025-12-31. The key should allow actions for document creation and deletion.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Meilisearch | GOAT |
| TOOL | create-key | Swap tokens on KIM |
| DESC | Create new API key with specific permissions | Allows token swapping on the KIM platform. |
| PARAMETERS | description: (string) Description for the API key<br>actions: (array of strings) Actions allowed for the API key<br>indexes: (array of strings) Indexes the API key can access<br>expiresAt: (Optional, string) Expiration date and time for the API key |  |
| SCORES(SERVER/TOOL/FINAL) | 0.413/0.544/0.122 | 0.536/0.593/0.188 |
| RANKS(SERVER/TOOL/FINAL) | 47/92/139 | 4/16/1 |
## ANALYSIS

# BAD CASE 52
## TASK
Delete the API key with the identifier "XYZ12345".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Meilisearch | Unstructured |
| TOOL | delete-key | cancel_job |
| DESC | Delete an existing API key | Delete a specific job by id. |
| PARAMETERS | key: (string) API key to delete |  |
| SCORES(SERVER/TOOL/FINAL) | 0.317/0.606/0.117 | 0.471/0.690/0.224 |
| RANKS(SERVER/TOOL/FINAL) | 87/27/71 | 3/3/1 |
## ANALYSIS

# BAD CASE 53
## TASK
Retrieve the details of the task with the unique identifier "TASK-12345".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Meilisearch | Airflow |
| TOOL | get-task | Get Task Details |
| DESC | Get information about a specific task | Gets details of a specific task. |
| PARAMETERS | uid: (string) Unique identifier for the task | dag_id: (string) The ID of the DAG.<br>task_id: (string) The ID of the task. |
| SCORES(SERVER/TOOL/FINAL) | 0.404/0.591/0.141 | 0.393/0.930/0.339 |
| RANKS(SERVER/TOOL/FINAL) | 38/86/107 | 53/1/1 |
## ANALYSIS

# BAD CASE 54
## TASK
Retrieve the first 20 tasks that were enqueued after 2024-05-01 and have a status of "completed", sorted in reverse chronological order.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Meilisearch | Todoist |
| TOOL | get-tasks | todoist_get_tasks |
| DESC | List tasks with optional filters | Retrieve and filter tasks. |
| PARAMETERS | limit: (Optional, integer) Maximum number of tasks to return<br>from: (Optional, integer) Number of tasks to skip<br>reverse: (Optional, boolean) Sort order of tasks<br>batchUids: (Optional, array of strings) Filter by batch UIDs<br>uids: (Optional, array of strings) Filter by task UIDs<br>canceledBy: (Optional, string) Filter by cancellation source<br>types: (Optional, array of strings) Filter by task types<br>statuses: (Optional, array of strings) Filter by task statuses<br>indexUids: (Optional, array of strings) Filter by index UIDs<br>afterEnqueuedAt: (Optional, string) Filter by enqueue time<br>beforeEnqueuedAt: (Optional, string) Filter by enqueue time<br>afterStartedAt: (Optional, string) Filter by start time<br>beforeStartedAt: (Optional, string) Filter by start time<br>afterFinishedAt: (Optional, string) Filter by finish time<br>beforeFinishedAt: (Optional, string) Filter by finish time | due date: (Optional, string) filter by due date<br>priority: (Optional, number) filter by priority<br>project: (Optional, string) filter by project<br>result limit: (Optional, number) limit the number of results |
| SCORES(SERVER/TOOL/FINAL) | 0.363/0.428/0.066 | 0.573/0.771/0.341 |
| RANKS(SERVER/TOOL/FINAL) | 80/892/678 | 3/1/1 |
## ANALYSIS

# BAD CASE 55
## TASK
Cancel all pending tasks with the status "enqueued" for the index with UID "documents".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Meilisearch | Todoist |
| TOOL | cancel-tasks | todoist_delete_task |
| DESC | Cancel pending or enqueued tasks | Remove tasks using natural language search. |
| PARAMETERS | uids: (array of strings) Task UIDs to cancel<br>batchUids: (Optional, array of strings) Batch UIDs to filter tasks<br>types: (Optional, array of strings) Task types to filter tasks<br>statuses: (Optional, array of strings) Task statuses to filter tasks<br>indexUids: (Optional, array of strings) Index UIDs to filter tasks<br>canceledBy: (Optional, string) Cancellation source | task name: (string) partial name match to find the task |
| SCORES(SERVER/TOOL/FINAL) | 0.348/0.563/0.110 | 0.528/0.733/0.284 |
| RANKS(SERVER/TOOL/FINAL) | 102/84/159 | 5/1/1 |
## ANALYSIS

# BAD CASE 56
## TASK
Delete all completed tasks with the status "finished" that belong to the "data_processing" type and were canceled by the "system" source.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Meilisearch | Todoist |
| TOOL | delete-tasks | todoist_delete_task |
| DESC | Delete completed tasks | Remove tasks using natural language search. |
| PARAMETERS | uids: (array of strings) Task UIDs to delete<br>batchUids: (Optional, array of strings) Batch UIDs to filter tasks<br>types: (Optional, array of strings) Task types to filter tasks<br>statuses: (Optional, array of strings) Task statuses to filter tasks<br>indexUids: (Optional, array of strings) Index UIDs to filter tasks<br>canceledBy: (Optional, string) Cancellation source | task name: (string) partial name match to find the task |
| SCORES(SERVER/TOOL/FINAL) | 0.348/0.655/0.149 | 0.565/0.713/0.288 |
| RANKS(SERVER/TOOL/FINAL) | 88/11/61 | 3/1/1 |
## ANALYSIS

# BAD CASE 57
## TASK
Perform a basic health check on the system to ensure all essential services are running properly.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Meilisearch | Airflow |
| TOOL | health-check | Get Health |
| DESC | Basic health check | Gets the health status of the server. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.428/0.597/0.153 | 0.505/0.617/0.192 |
| RANKS(SERVER/TOOL/FINAL) | 9/7/6 | 2/4/1 |
## ANALYSIS

# BAD CASE 58
## TASK
Check the comprehensive health status of the system.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Meilisearch | consul-mcp |
| TOOL | get-health-status | Get system health service information |
| DESC | Comprehensive health status | Retrieves system health service information. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.486/0.487/0.115 | 0.437/0.775/0.263 |
| RANKS(SERVER/TOOL/FINAL) | 8/361/145 | 22/1/1 |
## ANALYSIS

# BAD CASE 59
## TASK
Retrieve the current version details of the Meilisearch instance.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Meilisearch | Aiven |
| TOOL | get-version | get_service_details |
| DESC | Get Meilisearch version information | Get the detail of your service in a specific Aiven project. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.542/0.635/0.219 | 0.515/0.711/0.260 |
| RANKS(SERVER/TOOL/FINAL) | 4/27/4 | 8/2/1 |
## ANALYSIS

# BAD CASE 60
## TASK
Retrieve the current Kubernetes configuration in YAML format, ensuring the output is minified.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Kubernetes and OpenShift | code-executor |
| TOOL | configuration_view | get_environment_config |
| DESC | Get the current Kubernetes configuration content as a kubeconfig YAML | Gets the current environment configuration. |
| PARAMETERS | minified: (Optional, boolean) Return a minified version of the configuration. Default is true. |  |
| SCORES(SERVER/TOOL/FINAL) | 0.462/0.568/0.149 | 0.435/0.597/0.155 |
| RANKS(SERVER/TOOL/FINAL) | 3/7/2 | 5/2/1 |
## ANALYSIS

# BAD CASE 61
## TASK
List all Kubernetes events in the current cluster, including those from all namespaces.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Kubernetes and OpenShift | mcp-k8s-go |
| TOOL | events_list | Get Kubernetes events |
| DESC | List all the Kubernetes events in the current cluster from all namespaces | Retrieves Kubernetes events. |
| PARAMETERS | namespace: (Optional, string) Namespace to retrieve the events from. If not provided, will list events from all namespaces. |  |
| SCORES(SERVER/TOOL/FINAL) | 0.732/0.478/0.256 | 0.402/0.928/0.346 |
| RANKS(SERVER/TOOL/FINAL) | 1/361/4 | 21/1/1 |
## ANALYSIS

# BAD CASE 62
## TASK
Retrieve the details of the Pod named "web-app" from the "production" namespace in the Kubernetes cluster.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Kubernetes and OpenShift | mcp-k8s-go |
| TOOL | pods_get | List Kubernetes pods |
| DESC | Get a Kubernetes Pod in the current or provided namespace with the provided name | Lists available Kubernetes pods. |
| PARAMETERS | name: (Required, string) Name of the Pod<br>namespace: (Required, string) Namespace to get the Pod from |  |
| SCORES(SERVER/TOOL/FINAL) | 0.637/0.454/0.184 | 0.471/0.818/0.315 |
| RANKS(SERVER/TOOL/FINAL) | 1/471/16 | 4/1/1 |
## ANALYSIS

# BAD CASE 63
## TASK
List all Kubernetes pods across all namespaces in the current cluster.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Kubernetes and OpenShift | mcp-k8s-go |
| TOOL | pods_list | List Kubernetes pods |
| DESC | List all the Kubernetes pods in the current cluster from all namespaces | Lists available Kubernetes pods. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.719/0.478/0.247 | 0.476/0.948/0.428 |
| RANKS(SERVER/TOOL/FINAL) | 1/322/12 | 3/1/1 |
## ANALYSIS

# BAD CASE 64
## TASK
List all the Kubernetes pods in the "production" namespace of the current cluster.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Kubernetes and OpenShift | mcp-k8s-go |
| TOOL | pods_list_in_namespace | List Kubernetes pods |
| DESC | List all the Kubernetes pods in the specified namespace in the current cluster | Lists available Kubernetes pods. |
| PARAMETERS | namespace: (Required, string) Namespace to list pods from |  |
| SCORES(SERVER/TOOL/FINAL) | 0.685/0.542/0.254 | 0.470/0.918/0.395 |
| RANKS(SERVER/TOOL/FINAL) | 1/111/7 | 4/1/1 |
## ANALYSIS

# BAD CASE 65
## TASK
Retrieve the logs from the container named "app-server" in the Pod "web-service" within the "production" namespace.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Kubernetes and OpenShift | mcp-k8s-go |
| TOOL | pods_log | Get Kubernetes pod logs |
| DESC | Get the logs of a Kubernetes Pod in the current or provided namespace with the provided name | Retrieves logs from a specified Kubernetes pod. |
| PARAMETERS | name: (Required, string) Name of the Pod to get logs from<br>namespace: (Required, string) Namespace to get the Pod logs from<br>container: (Optional, string) Name of the Pod container to get logs from |  |
| SCORES(SERVER/TOOL/FINAL) | 0.580/0.500/0.168 | 0.447/0.915/0.375 |
| RANKS(SERVER/TOOL/FINAL) | 1/195/12 | 9/1/1 |
## ANALYSIS

# BAD CASE 66
## TASK
List all the projects available in the current OpenShift cluster.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Kubernetes and OpenShift | Aiven |
| TOOL | projects_list | list_projects |
| DESC | List all the OpenShift projects in the current cluster | List all projects on your Aiven account. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.679/0.601/0.277 | 0.520/0.845/0.371 |
| RANKS(SERVER/TOOL/FINAL) | 1/76/5 | 5/1/1 |
## ANALYSIS

# BAD CASE 67
## TASK
Search for documents containing the keyword "machine learning" in the "research_papers" collection, focusing on the "title" and "abstract" fields, and return a maximum of 20 results sorted by publication date in descending order.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Typesense | DPLP |
| TOOL | typesense_query | search |
| DESC | Search for documents in Typesense collections with powerful filtering | Search DBLP for publications using boolean queries. |
| PARAMETERS | query_text: (string) The query text to search for<br>collection_name: (string) The name of the collection to search<br>search_fields: (array) Fields to search within<br>filters: (object, optional) Filters to apply to the search<br>sort_options: (object, optional) Options for sorting results<br>limit: (number, optional) Maximum number of results to return | query: (string, required) A query string that may include boolean operators 'and' and 'or' (case-insensitive)<br>max_results: (number, optional) Maximum number of publications to return. Default is 10<br>year_from: (number, optional) Lower bound for publication year<br>year_to: (number, optional) Upper bound for publication year<br>venue_filter: (string, optional) Case-insensitive substring filter for publication venues (e.g., 'iclr')<br>include_bibtex: (boolean, optional) Whether to include BibTeX entries in the results. Default is false |
| SCORES(SERVER/TOOL/FINAL) | 0.430/0.414/0.076 | 0.481/0.842/0.341 |
| RANKS(SERVER/TOOL/FINAL) | 16/454/234 | 6/1/1 |
## ANALYSIS

# BAD CASE 68
## TASK
Retrieve the document with ID "user123" from the "customers" collection.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Typesense | Couchbase |
| TOOL | typesense_get_document | get_document_by_id |
| DESC | Retrieve specific documents by ID from collections | Get a document by ID from a specified scope and collection. |
| PARAMETERS | collection_name: (string) The name of the collection<br>document_id: (string) The ID of the document to retrieve |  |
| SCORES(SERVER/TOOL/FINAL) | 0.307/0.508/0.079 | 0.495/0.781/0.302 |
| RANKS(SERVER/TOOL/FINAL) | 134/141/276 | 4/1/1 |
## ANALYSIS

# BAD CASE 69
## TASK
Retrieve the total number of documents and average document size for the "products" collection in Typesense.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Typesense | Chroma |
| TOOL | typesense_collection_stats | chroma_get_collection_count |
| DESC | Get statistics about a Typesense collection | Get the number of documents in a collection |
| PARAMETERS | collection_name: (string) The name of the collection |  |
| SCORES(SERVER/TOOL/FINAL) | 0.476/0.577/0.158 | 0.695/0.556/0.269 |
| RANKS(SERVER/TOOL/FINAL) | 16/64/42 | 1/114/1 |
## ANALYSIS

# BAD CASE 70
## TASK
Analyze the structure and contents of the "customer_data" collection.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Typesense | Chroma |
| TOOL | analyze_collection | chroma_get_collection_count |
| DESC | Analyze collection structure and contents | Get the number of documents in a collection |
| PARAMETERS | collection_name: (string) The name of the collection |  |
| SCORES(SERVER/TOOL/FINAL) | 0.369/0.536/0.106 | 0.725/0.556/0.292 |
| RANKS(SERVER/TOOL/FINAL) | 93/130/239 | 1/82/1 |
## ANALYSIS

# BAD CASE 71
## TASK
Manage the list of available prompts by updating outdated entries and removing unused ones.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Comet Opik | GreptimeDB |
| TOOL | Prompts Management | list_prompts |
| DESC | Create, list, update, and delete prompts | Lists available prompts. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.311/0.487/0.074 | 0.456/0.834/0.317 |
| RANKS(SERVER/TOOL/FINAL) | 109/83/178 | 4/1/1 |
## ANALYSIS

# BAD CASE 72
## TASK
Organize all active projects into categorized workspaces based on their current status and priority levels.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Comet Opik | Unstructured |
| TOOL | Projects/Workspaces Management | list_workflows_with_finished_jobs |
| DESC | Organize and manage projects | Lists all workflows that have any completed job, together with information about source and destination details. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.323/0.476/0.073 | 0.517/0.677/0.237 |
| RANKS(SERVER/TOOL/FINAL) | 105/306/443 | 6/3/1 |
## ANALYSIS

# BAD CASE 73
## TASK
Analyze the trace data collected over the past 24 hours to identify any anomalies or performance bottlenecks.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Comet Opik | Heroku |
| TOOL | Traces | pg_outliers |
| DESC | Track and analyze trace data | Identify resource-intensive queries. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.428/0.483/0.100 | 0.354/0.632/0.141 |
| RANKS(SERVER/TOOL/FINAL) | 6/42/15 | 24/2/1 |
## ANALYSIS

# BAD CASE 74
## TASK
Gather and analyze the latest system performance metrics over the past 24 hours.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Comet Opik | Heroku |
| TOOL | Metrics | pg_outliers |
| DESC | Gather and query metrics data | Identify resource-intensive queries. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.454/0.426/0.088 | 0.404/0.631/0.161 |
| RANKS(SERVER/TOOL/FINAL) | 7/462/98 | 18/1/1 |
## ANALYSIS

# BAD CASE 75
## TASK
Read the contents of the files located at `/var/log/app.log`, `/var/log/db.log`, and `/var/log/error.log` simultaneously.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Golang Filesystem Server | Terminal-Control |
| TOOL | read_multiple_files | read_file |
| DESC | Read multiple files simultaneously | Read content from a file with optional row selection. |
| PARAMETERS | paths: (string[]) Array of file paths | path: (string) Path to the file<br>start_row: (Optional, int) Starting row to read from (0-based)<br>end_row: (Optional, int) Ending row to read to (0-based, inclusive) |
| SCORES(SERVER/TOOL/FINAL) | 0.260/0.667/0.116 | 0.484/0.573/0.159 |
| RANKS(SERVER/TOOL/FINAL) | 143/1/12 | 1/14/1 |
## ANALYSIS

# BAD CASE 76
## TASK
Upload a PDF document to the knowledge base for future reference and retrieval.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Graphlit | Box |
| TOOL | Files | box_docgen_create_batch_tool |
| DESC | Ingests files into the knowledge base. | Generate documents using a Box Doc Gen template and a local JSON file. |
| PARAMETERS |  | file_id: (str) Template file ID<br>destination_folder_id: (str) Folder ID where generated documents should be stored<br>user_input_file_path: (str) Path to a JSON file with input data<br>output_type: (str, optional) Output format (default is 'pdf') |
| SCORES(SERVER/TOOL/FINAL) | 0.374/0.651/0.158 | 0.405/0.772/0.241 |
| RANKS(SERVER/TOOL/FINAL) | 87/23/65 | 60/1/1 |
## ANALYSIS

# BAD CASE 77
## TASK
Ingest the latest 50 unread emails from the primary inbox into the knowledge base.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Graphlit | Graphlit |
| TOOL | Emails | Emails |
| DESC | Ingests emails into the knowledge base. | Ingests emails into the knowledge base. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.453/0.907/0.373 | 0.453/0.907/0.373 |
| RANKS(SERVER/TOOL/FINAL) | 35/1/1 | 35/1/1 |
## ANALYSIS

# BAD CASE 78
## TASK
Retrieve the latest 10 unread emails from the primary inbox in Google Mail.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Graphlit | Gmail |
| TOOL | Google Mail | search_emails |
| DESC | Connects to Google Mail to ingest emails. | Searches for emails using Gmail search syntax. |
| PARAMETERS |  | query: (string) Gmail search query<br>maxResults: (Optional, integer) Maximum number of results to return |
| SCORES(SERVER/TOOL/FINAL) | 0.418/0.777/0.252 | 0.716/0.814/0.474 |
| RANKS(SERVER/TOOL/FINAL) | 29/3/15 | 1/2/1 |
## ANALYSIS

# BAD CASE 79
## TASK
Fetch all active issues from the connected Linear workspace.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Graphlit | Linear (Go) |
| TOOL | Linear | linear_get_user_issues |
| DESC | Connects to Linear to ingest data. | Retrieves issues assigned to a specific user or the authenticated user. |
| PARAMETERS |  | userId: (Optional) Optional user ID. If not provided, returns authenticated user's issues<br>includeArchived: Include archived issues in results<br>limit: Maximum number of issues to return (default: 50) |
| SCORES(SERVER/TOOL/FINAL) | 0.466/0.558/0.145 | 0.597/0.843/0.424 |
| RANKS(SERVER/TOOL/FINAL) | 12/198/98 | 3/1/1 |
## ANALYSIS

# BAD CASE 80
## TASK
Retrieve all open issues assigned to the "Development" team from the Jira project "Web Platform" created in the last 30 days.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Graphlit | Linear (Go) |
| TOOL | Jira | linear_get_user_issues |
| DESC | Connects to Jira to ingest data. | Retrieves issues assigned to a specific user or the authenticated user. |
| PARAMETERS |  | userId: (Optional) Optional user ID. If not provided, returns authenticated user's issues<br>includeArchived: Include archived issues in results<br>limit: Maximum number of issues to return (default: 50) |
| SCORES(SERVER/TOOL/FINAL) | 0.420/0.568/0.135 | 0.580/0.831/0.401 |
| RANKS(SERVER/TOOL/FINAL) | 20/55/51 | 2/1/1 |
## ANALYSIS

# BAD CASE 81
## TASK
Upload a PDF document to the connected cloud storage service.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Graphlit | Cloudinary |
| TOOL | Google Drive | upload |
| DESC | Connects to Google Drive to ingest files. | Upload images and videos to Cloudinary. |
| PARAMETERS |  | file: (required) Path to file, URL, or base64 data URI to upload<br>resource_type: (optional) Type of resource ('image', 'video', or 'raw')<br>public_id: (optional) Custom public ID for the uploaded asset<br>overwrite: (optional) Whether to overwrite existing assets with the same public ID<br>tags: (optional) Array of tags to assign to the uploaded asset |
| SCORES(SERVER/TOOL/FINAL) | 0.318/0.721/0.165 | 0.473/0.704/0.234 |
| RANKS(SERVER/TOOL/FINAL) | 99/4/13 | 8/7/1 |
## ANALYSIS

# BAD CASE 82
## TASK
Upload a document from the local machine to the connected cloud storage service.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Graphlit | Cloudinary |
| TOOL | OneDrive | upload |
| DESC | Connects to OneDrive to ingest files. | Upload images and videos to Cloudinary. |
| PARAMETERS |  | file: (required) Path to file, URL, or base64 data URI to upload<br>resource_type: (optional) Type of resource ('image', 'video', or 'raw')<br>public_id: (optional) Custom public ID for the uploaded asset<br>overwrite: (optional) Whether to overwrite existing assets with the same public ID<br>tags: (optional) Array of tags to assign to the uploaded asset |
| SCORES(SERVER/TOOL/FINAL) | 0.297/0.803/0.192 | 0.472/0.723/0.247 |
| RANKS(SERVER/TOOL/FINAL) | 122/3/5 | 6/8/1 |
## ANALYSIS

# BAD CASE 83
## TASK
Upload a PDF document to the connected cloud storage service.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Graphlit | Cloudinary |
| TOOL | Dropbox | upload |
| DESC | Connects to Dropbox to ingest files. | Upload images and videos to Cloudinary. |
| PARAMETERS |  | file: (required) Path to file, URL, or base64 data URI to upload<br>resource_type: (optional) Type of resource ('image', 'video', or 'raw')<br>public_id: (optional) Custom public ID for the uploaded asset<br>overwrite: (optional) Whether to overwrite existing assets with the same public ID<br>tags: (optional) Array of tags to assign to the uploaded asset |
| SCORES(SERVER/TOOL/FINAL) | 0.318/0.702/0.156 | 0.473/0.704/0.234 |
| RANKS(SERVER/TOOL/FINAL) | 99/8/20 | 8/7/1 |
## ANALYSIS

# BAD CASE 84
## TASK
Extract the formatted content including text and images from the homepage of a specified website.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Hyperbrowser | Google Custom Search |
| TOOL | scrape_webpage | read_webpage |
| DESC | Extract formatted (markdown, screenshot etc) content from any webpage | Extract content from any webpage. |
| PARAMETERS |  | url: (string) the URL of the webpage to extract content from |
| SCORES(SERVER/TOOL/FINAL) | 0.364/0.616/0.138 | 0.604/0.842/0.429 |
| RANKS(SERVER/TOOL/FINAL) | 73/41/70 | 2/1/1 |
## ANALYSIS

# BAD CASE 85
## TASK
Crawl and extract formatted content from all linked pages starting from the homepage of a specified website.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Hyperbrowser | Google Custom Search |
| TOOL | crawl_webpages | read_webpage |
| DESC | Navigate through multiple linked pages and extract LLM-friendly formatted content | Extract content from any webpage. |
| PARAMETERS |  | url: (string) the URL of the webpage to extract content from |
| SCORES(SERVER/TOOL/FINAL) | 0.349/0.527/0.097 | 0.560/0.841/0.396 |
| RANKS(SERVER/TOOL/FINAL) | 59/131/141 | 2/1/1 |
## ANALYSIS

# BAD CASE 86
## TASK
Search for the latest news articles about renewable energy advancements.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Hyperbrowser | Octagon |
| TOOL | search_with_bing | octagon-deep-research-agent |
| DESC | Query the web and get results with Bing search | Perform comprehensive research on any topic. |
| PARAMETERS |  | prompt: (string) A natural language query specifying the topic to research. |
| SCORES(SERVER/TOOL/FINAL) | 0.275/0.409/0.046 | 0.477/0.714/0.243 |
| RANKS(SERVER/TOOL/FINAL) | 137/417/506 | 3/2/1 |
## ANALYSIS

# BAD CASE 87
## TASK
Automate the process of organizing and categorizing a collection of 100 research papers into relevant topics using OpenAI's CUA model.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Hyperbrowser | Unstructured |
| TOOL | openai_computer_use_agent | invoke_firecrawl_llmtxt |
| DESC | General-purpose automation using OpenAI’s CUA model | Generates LLM-optimized text from crawled pages. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.285/0.534/0.081 | 0.624/0.672/0.282 |
| RANKS(SERVER/TOOL/FINAL) | 173/141/279 | 1/5/1 |
## ANALYSIS

# BAD CASE 88
## TASK
Perform a complex browser task involving automated form filling and submission on a specified website using Claude's capabilities.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Hyperbrowser | Unstructured |
| TOOL | claude_computer_use_agent | invoke_firecrawl_llmtxt |
| DESC | Complex browser tasks using Claude computer use | Generates LLM-optimized text from crawled pages. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.415/0.520/0.112 | 0.658/0.624/0.270 |
| RANKS(SERVER/TOOL/FINAL) | 30/167/150 | 1/21/1 |
## ANALYSIS

# BAD CASE 89
## TASK
Create a wrapped token on the Ethereum Mainnet for the original token at address 0x123... using Wormhole.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Solana Agent Kit | GOAT |
| TOOL | createWrappedToken | Swap tokens on Starknet |
| DESC | Creates a wrapped token on a target chain using Wormhole. | Enables token swapping on the Starknet network. |
| PARAMETERS | destinationChain: (string) Target chain<br>tokenAddress: (string) Original token address<br>network: (string) Network type (Testnet or Mainnet) |  |
| SCORES(SERVER/TOOL/FINAL) | 0.426/0.950/0.384 | 0.696/0.810/0.457 |
| RANKS(SERVER/TOOL/FINAL) | 12/1/9 | 1/2/1 |
## ANALYSIS

# BAD CASE 90
## TASK
Convert the provided text "Hello, welcome to our service. How can I assist you today?" into an audio file using default voice settings.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ElevenLabs | Qwen_Max |
| TOOL | generate_audio_simple | qwen_max |
| DESC | Generate audio from plain text using default voice settings | Generates text using the Qwen Max language model. |
| PARAMETERS |  | prompt: (string) The input prompt for the model.<br>max_tokens: (number) The maximum number of tokens to generate in the output.<br>temperature: (number) Controls the randomness of the model's output. |
| SCORES(SERVER/TOOL/FINAL) | 0.444/0.659/0.193 | 0.522/0.692/0.250 |
| RANKS(SERVER/TOOL/FINAL) | 12/5/6 | 3/4/1 |
## ANALYSIS

# BAD CASE 91
## TASK
Delete the job with ID 'JOB12345'.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ElevenLabs | Unstructured |
| TOOL | delete_job | cancel_job |
| DESC | Delete a job by its ID | Delete a specific job by id. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.365/0.531/0.103 | 0.465/0.909/0.385 |
| RANKS(SERVER/TOOL/FINAL) | 21/82/74 | 3/1/1 |
## ANALYSIS

# BAD CASE 92
## TASK
List all available voice options for text-to-speech conversion.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ElevenLabs | Deepseek_R1 |
| TOOL | list_voices | deepseek_r1 |
| DESC | List all available voices | Generates advanced text using the Deepseek R1 model with configurable parameters. |
| PARAMETERS |  | prompt: (string) The input prompt for text generation<br>max_tokens: (number) Maximum tokens to generate<br>temperature: (number) Controls randomness, default is 0.2 |
| SCORES(SERVER/TOOL/FINAL) | 0.467/0.633/0.187 | 0.456/0.696/0.221 |
| RANKS(SERVER/TOOL/FINAL) | 10/13/9 | 13/3/1 |
## ANALYSIS

# BAD CASE 93
## TASK
Set up a notification workflow in the Dynatrace Automation Engine to alert the team when specific system events occur.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Dynatrace | n8n |
| TOOL | set_up_notification_workflow | run_webhook |
| DESC | Sets up notification workflows using the Dynatrace Automation Engine. | Triggers a workflow via a webhook, passing the workflow name and optional data. |
| PARAMETERS |  | workflowName: (string) The name of the workflow to trigger<br>data: (Optional, object) Additional data to pass to the webhook |
| SCORES(SERVER/TOOL/FINAL) | 0.312/0.888/0.246 | 0.619/0.694/0.298 |
| RANKS(SERVER/TOOL/FINAL) | 117/1/2 | 1/2/1 |
## ANALYSIS

# BAD CASE 94
## TASK
Retrieve the latest product listings from the specified e-commerce API endpoint, including query parameters for category "electronics" and a limit of 20 items per page.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Rquest | Productboard |
| TOOL | http_get | get_product_detail |
| DESC | Perform GET requests with optional parameters | Retrieves detailed information about a specific product. |
| PARAMETERS | url: (string) The URL to send the GET request to<br>headers: (Optional, dict) Additional headers to include in the request<br>cookies: (Optional, dict) Cookies to include in the request<br>params: (Optional, dict) Query parameters to include in the request |  |
| SCORES(SERVER/TOOL/FINAL) | 0.000/0.000/0.000 | 0.510/0.785/0.315 |
| RANKS(SERVER/TOOL/FINAL) | -1/-1/-1 | 3/1/1 |
## ANALYSIS

# BAD CASE 95
## TASK
Update the user profile with the new email address "user@example.com" by sending a PUT request to the API endpoint "/api/users/123". Include the necessary authentication headers and ensure the request body is formatted as JSON.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Rquest | Ghost |
| TOOL | http_put | Edit User |
| DESC | Update resources with PUT requests | Update user details. |
| PARAMETERS | url: (string) The URL to send the PUT request to<br>data: (Optional, dict or string) Data to send in the body of the request<br>json: (Optional, dict) JSON data to send in the body of the request<br>headers: (Optional, dict) Additional headers to include in the request<br>cookies: (Optional, dict) Cookies to include in the request<br>files: (Optional, dict) Files to send in the body of the request |  |
| SCORES(SERVER/TOOL/FINAL) | 0.322/0.443/0.063 | 0.383/0.765/0.224 |
| RANKS(SERVER/TOOL/FINAL) | 30/130/119 | 8/1/1 |
## ANALYSIS

# BAD CASE 96
## TASK
Update the user profile with the new email address "user@example.com" by sending a PATCH request to the API endpoint "/users/123". Include the necessary authentication headers and send the data in JSON format.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Rquest | Ghost |
| TOOL | http_patch | Edit User |
| DESC | Partially update resources | Update user details. |
| PARAMETERS | url: (string) The URL to send the PATCH request to<br>data: (Optional, dict or string) Data to send in the body of the request<br>json: (Optional, dict) JSON data to send in the body of the request<br>headers: (Optional, dict) Additional headers to include in the request<br>cookies: (Optional, dict) Cookies to include in the request<br>files: (Optional, dict) Files to send in the body of the request |  |
| SCORES(SERVER/TOOL/FINAL) | 0.339/0.397/0.053 | 0.390/0.777/0.236 |
| RANKS(SERVER/TOOL/FINAL) | 31/313/310 | 8/1/1 |
## ANALYSIS

# BAD CASE 97
## TASK
Retrieve the available HTTP methods for the resource located at "https://api.example.com/v1/users" including custom headers for authentication.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Rquest | OpenAPI AnyApi |
| TOOL | http_options | {prefix}_api_request_schema |
| DESC | Retrieve options for a resource | Get API endpoint schemas that match your intent. Returns endpoint details including path, method, parameters, and response formats. |
| PARAMETERS | url: (string) The URL to send the OPTIONS request to<br>headers: (Optional, dict) Additional headers to include in the request<br>cookies: (Optional, dict) Cookies to include in the request | query: (string) Describe what you want to do with the API (e.g., 'Get user profile information', 'Create a new job posting') |
| SCORES(SERVER/TOOL/FINAL) | 0.322/0.403/0.052 | 0.538/0.699/0.263 |
| RANKS(SERVER/TOOL/FINAL) | 70/892/728 | 2/1/1 |
## ANALYSIS

# BAD CASE 98
## TASK
Retrieve lines 50 to 100 from the stored response with ID "RESP12345".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Rquest | Unstructured |
| TOOL | get_stored_response | list_workflows |
| DESC | Retrieve stored large responses, optionally by line range | Lists workflows from the Unstructured API. |
| PARAMETERS | response_id: (string) The ID of the stored response<br>start_line: (Optional, int) The starting line number to retrieve<br>end_line: (Optional, int) The ending line number to retrieve |  |
| SCORES(SERVER/TOOL/FINAL) | 0.467/0.520/0.126 | 0.616/0.598/0.227 |
| RANKS(SERVER/TOOL/FINAL) | 11/473/167 | 1/69/1 |
## ANALYSIS

# BAD CASE 99
## TASK
Store the configuration settings for the production environment in the key-value store.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | consul-mcp | Azure |
| TOOL | Put values in KV store | Manage key-value pairs |
| DESC | Adds or updates values in the Consul key-value store. | Manages key-value pairs within an App Configuration store. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.306/0.685/0.143 | 0.297/0.746/0.165 |
| RANKS(SERVER/TOOL/FINAL) | 58/3/4 | 68/1/1 |
## ANALYSIS

# BAD CASE 101
## TASK
Deploy a new NFT collection named "Digital Dreams" with the metadata URI "ipfs://QmXyZ123", set the royalty to 500 basis points, and assign two creators with their respective shares.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Solana Agent Kit | GOAT |
| TOOL | deployCollection | Get NFT information using Solana NFTs API |
| DESC | Deploys a new NFT collection. | Provides NFT information using the Solana NFTs API. |
| PARAMETERS | name: (string) Name of the collection<br>uri: (string) URI for the collection metadata<br>royaltyBasisPoints: (number) Royalty basis points<br>creators: (Creator[]) Array of creator objects |  |
| SCORES(SERVER/TOOL/FINAL) | 0.419/0.843/0.298 | 0.661/0.702/0.326 |
| RANKS(SERVER/TOOL/FINAL) | 12/1/4 | 1/4/1 |
## ANALYSIS

# BAD CASE 102
## TASK
Send a compressed airdrop of 100 tokens per recipient to 50 specified wallet addresses with a priority fee of 500 lamports.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Solana Agent Kit | GOAT |
| TOOL | sendCompressedAirdrop | Create a wallet, mint tokens and get test tokens on any chain using Crossmint |
| DESC | Sends a compressed airdrop using ZK compression. | Facilitates the creation of wallets, minting of tokens, and retrieval of test tokens on any supported chain using Crossmint. |
| PARAMETERS | mint: (PublicKey) Token mint<br>amountPerRecipient: (number) Amount per recipient<br>recipients: (PublicKey[]) Array of recipient public keys<br>priorityFee: (number) Priority fee in lamports |  |
| SCORES(SERVER/TOOL/FINAL) | 0.416/0.865/0.312 | 0.633/0.706/0.315 |
| RANKS(SERVER/TOOL/FINAL) | 12/1/3 | 1/3/1 |
## ANALYSIS

# BAD CASE 103
## TASK
Create a new vault with the following specifications:  
- Name: "AlphaFund"  
- Market: "ETH/USD"  
- Redemption period: 30 days  
- Maximum tokens: 10,000  
- Minimum deposit amount: 0.1 ETH  
- Management fee: 2%  
- Profit share: 20%  
- Hurdle rate: 10%  
- Permissioned: true
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Solana Agent Kit | GOAT |
| TOOL | createDriftVault | Create liquidity pools on Meteora |
| DESC | Creates a new Drift vault. | Enables the creation of liquidity pools on Meteora. |
| PARAMETERS | name: (string) Name of the vault<br>marketName: (string) Market name<br>redeemPeriod: (number) Redemption period in days<br>maxTokens: (number) Maximum tokens<br>minDepositAmount: (number) Minimum deposit amount<br>managementFee: (number) Management fee in percentage<br>profitShare: (number) Profit share in percentage<br>hurdleRate: (number) Hurdle rate in percentage<br>permissioned: (boolean) Whether the vault is permissioned |  |
| SCORES(SERVER/TOOL/FINAL) | 0.416/0.525/0.115 | 0.531/0.512/0.145 |
| RANKS(SERVER/TOOL/FINAL) | 30/1/36 | 1/3/1 |
## ANALYSIS

# BAD CASE 104
## TASK
Retrieve the current details of the active Drift user account.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Solana Agent Kit | Solana Agent Kit |
| TOOL | driftUserAccountInfo | driftUserAccountInfo |
| DESC | Gets information about the Drift user account. | Gets information about the Drift user account. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.262/0.923/0.224 | 0.262/0.923/0.224 |
| RANKS(SERVER/TOOL/FINAL) | 214/1/1 | 214/1/1 |
## ANALYSIS

# BAD CASE 105
## TASK
Update the parameters of a Drift vault named "AlphaFund" to set a 30-day redemption period, a maximum of 10,000 tokens, a minimum deposit amount of 100 tokens, a 2% management fee, a 20% profit share, a 5% hurdle rate, and make it permissioned.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Solana Agent Kit | Solana Agent Kit |
| TOOL | updateDriftVault | updateDriftVault |
| DESC | Updates the parameters of a Drift vault. | Updates the parameters of a Drift vault. |
| PARAMETERS | name: (string) Name of the vault<br>marketName: (string) Market name<br>redeemPeriod: (number) Redemption period in days<br>maxTokens: (number) Maximum tokens<br>minDepositAmount: (number) Minimum deposit amount<br>managementFee: (number) Management fee in percentage<br>profitShare: (number) Profit share in percentage<br>hurdleRate: (number) Hurdle rate in percentage<br>permissioned: (boolean) Whether the vault is permissioned | name: (string) Name of the vault<br>marketName: (string) Market name<br>redeemPeriod: (number) Redemption period in days<br>maxTokens: (number) Maximum tokens<br>minDepositAmount: (number) Minimum deposit amount<br>managementFee: (number) Management fee in percentage<br>profitShare: (number) Profit share in percentage<br>hurdleRate: (number) Hurdle rate in percentage<br>permissioned: (boolean) Whether the vault is permissioned |
| SCORES(SERVER/TOOL/FINAL) | 0.364/0.884/0.285 | 0.364/0.884/0.285 |
| RANKS(SERVER/TOOL/FINAL) | 23/1/1 | 23/1/1 |
## ANALYSIS

# BAD CASE 106
## TASK
Retrieve the current position values and total asset value for the Voltr vault at address 0x1234abcd5678ef90.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Solana Agent Kit | Solana Agent Kit |
| TOOL | voltrGetPositionValues | voltrGetPositionValues |
| DESC | Gets the current position values and total value of assets in a Voltr vault. | Gets the current position values and total value of assets in a Voltr vault. |
| PARAMETERS | vaultAddress: (string) Vault address | vaultAddress: (string) Vault address |
| SCORES(SERVER/TOOL/FINAL) | 0.416/0.945/0.372 | 0.416/0.945/0.372 |
| RANKS(SERVER/TOOL/FINAL) | 13/1/1 | 13/1/1 |
## ANALYSIS

# BAD CASE 107
## TASK
Retrieve the details of the Solana asset with the ID "ABC123XYZ456".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Solana Agent Kit | Solana Agent Kit |
| TOOL | getAsset | getAsset |
| DESC | Gets a Solana asset by its ID. | Gets a Solana asset by its ID. |
| PARAMETERS | assetId: (string) Asset ID | assetId: (string) Asset ID |
| SCORES(SERVER/TOOL/FINAL) | 0.403/0.899/0.326 | 0.403/0.899/0.326 |
| RANKS(SERVER/TOOL/FINAL) | 11/1/1 | 11/1/1 |
## ANALYSIS

# BAD CASE 108
## TASK
List all available topics from the Allora platform.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Solana Agent Kit | Unstructured |
| TOOL | getAllTopics | list_sources |
| DESC | Lists all topics from Allora. | Lists available sources from the Unstructured API. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.242/0.965/0.225 | 0.587/0.692/0.281 |
| RANKS(SERVER/TOOL/FINAL) | 274/1/8 | 2/8/1 |
## ANALYSIS

# BAD CASE 109
## TASK
Retrieve the details of the USDC token on the Ethereum chain using deBridge.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Solana Agent Kit | GOAT |
| TOOL | getDebridgeTokensInfo | Bridge tokens on DeBridge |
| DESC | Gets information about tokens on a specific chain using deBridge. | Enables token bridging on the DeBridge network. |
| PARAMETERS | chainId: (string) Chain ID<br>token: (string) Token symbol |  |
| SCORES(SERVER/TOOL/FINAL) | 0.445/0.851/0.322 | 0.657/0.767/0.386 |
| RANKS(SERVER/TOOL/FINAL) | 12/1/15 | 1/2/1 |
## ANALYSIS

# BAD CASE 110
## TASK
Retrieve details about the currently highlighted or selected item.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Talk To Figma | Productboard |
| TOOL | get_selection | get_component_detail |
| DESC | Get information about the current selection | Retrieves detailed information about a specific component. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.389/0.549/0.117 | 0.482/0.679/0.222 |
| RANKS(SERVER/TOOL/FINAL) | 92/147/175 | 7/1/1 |
## ANALYSIS

# BAD CASE 111
## TASK
Retrieve detailed information for the nodes with IDs [101, 102, 103, 104].
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Talk To Figma | consul-mcp |
| TOOL | get_nodes_info | Get current peers |
| DESC | Get detailed information about multiple nodes by providing an array of node IDs | Retrieves the current peer nodes in the Consul cluster. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.000/0.000/0.000 | 0.513/0.693/0.246 |
| RANKS(SERVER/TOOL/FINAL) | -1/-1/-1 | 5/6/1 |
## ANALYSIS

# BAD CASE 112
## TASK
Batch create or update 10 annotations for a dataset with unique identifiers and labels.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Talk To Figma | Fibery |
| TOOL | set_multiple_annotations | create_entities_batch |
| DESC | Batch create/update multiple annotations efficiently | Creates multiple new entities in your Fibery workspace with specified field values. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.282/0.658/0.122 | 0.429/0.667/0.191 |
| RANKS(SERVER/TOOL/FINAL) | 193/4/28 | 14/2/1 |
## ANALYSIS

# BAD CASE 113
## TASK
Create a new rectangle positioned at coordinates (100, 200) with a width of 300 pixels and a height of 150 pixels, and label it "Container".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Talk To Figma | Docker |
| TOOL | create_rectangle | create_container |
| DESC | Create a new rectangle with position, size, and optional name | Creates a new container. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.333/0.438/0.064 | 0.372/0.595/0.132 |
| RANKS(SERVER/TOOL/FINAL) | 35/68/63 | 6/1/1 |
## ANALYSIS

# BAD CASE 114
## TASK
Scan and intelligently chunk text nodes from a large design file for efficient processing.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Talk To Figma | Unstructured |
| TOOL | scan_text_nodes | invoke_firecrawl_llmtxt |
| DESC | Scan text nodes with intelligent chunking for large designs | Generates LLM-optimized text from crawled pages. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.355/0.552/0.108 | 0.700/0.696/0.341 |
| RANKS(SERVER/TOOL/FINAL) | 105/143/201 | 1/7/1 |
## ANALYSIS

# BAD CASE 115
## TASK
Set the layout mode of the current frame to vertical with wrapping enabled.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Talk To Figma | Talk To Figma |
| TOOL | set_layout_mode | set_layout_mode |
| DESC | Set the layout mode and wrap behavior of a frame (NONE, HORIZONTAL, VERTICAL) | Set the layout mode and wrap behavior of a frame (NONE, HORIZONTAL, VERTICAL) |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.264/0.797/0.168 | 0.264/0.797/0.168 |
| RANKS(SERVER/TOOL/FINAL) | 58/1/1 | 58/1/1 |
## ANALYSIS

# BAD CASE 116
## TASK
Adjust the horizontal and vertical sizing modes of the selected auto-layout frame to HUG for both dimensions.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Talk To Figma | Talk To Figma |
| TOOL | set_layout_sizing | set_layout_sizing |
| DESC | Set horizontal and vertical sizing modes for auto-layout frames (FIXED, HUG, FILL) | Set horizontal and vertical sizing modes for auto-layout frames (FIXED, HUG, FILL) |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.286/0.776/0.172 | 0.286/0.776/0.172 |
| RANKS(SERVER/TOOL/FINAL) | 75/1/1 | 75/1/1 |
## ANALYSIS

# BAD CASE 117
## TASK
Set the stroke color to red and the stroke weight to 3 pixels for the selected node.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Talk To Figma | Neovim |
| TOOL | set_stroke_color | vim_visual |
| DESC | Set the stroke color and weight of a node | Creates a visual selection in the VIM editor. |
| PARAMETERS |  | startLine: (number) Start line of the selection<br>startColumn: (number) Start column of the selection<br>endLine: (number) End line of the selection<br>endColumn: (number) End column of the selection |
| SCORES(SERVER/TOOL/FINAL) | 0.283/0.575/0.094 | 0.429/0.574/0.141 |
| RANKS(SERVER/TOOL/FINAL) | 57/2/6 | 1/3/1 |
## ANALYSIS

# BAD CASE 118
## TASK
Terminate all active sessions for the current user account.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | consul-mcp | Heroku |
| TOOL | Destroy sessions | pg_kill |
| DESC | Destroys specified sessions. | Terminate specific database processes. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.243/0.766/0.142 | 0.381/0.650/0.161 |
| RANKS(SERVER/TOOL/FINAL) | 159/1/2 | 7/3/1 |
## ANALYSIS

# BAD CASE 119
## TASK
Save a table named "2024_Sales_Summary" containing aggregated monthly sales data for later visualization. The data should include columns for month, total sales, and average order value.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Vega-Lite | Vega-Lite |
| TOOL | save_data | save_data |
| DESC | Save a table of data aggregations to the server for later visualization. | Save a table of data aggregations to the server for later visualization. |
| PARAMETERS | name: (string) Name of the data table to be saved<br>data: (array) Array of objects representing the data table | name: (string) Name of the data table to be saved<br>data: (array) Array of objects representing the data table |
| SCORES(SERVER/TOOL/FINAL) | 0.256/0.710/0.129 | 0.256/0.710/0.129 |
| RANKS(SERVER/TOOL/FINAL) | 140/1/1 | 140/1/1 |
## ANALYSIS

# BAD CASE 120
## TASK
Retrieve the full list of contacts from the Xero accounting platform.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Xero | Unstructured |
| TOOL | list-contacts | list_workflows |
| DESC | Retrieve a list of contacts from Xero | Lists workflows from the Unstructured API. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.398/0.586/0.136 | 0.558/0.649/0.235 |
| RANKS(SERVER/TOOL/FINAL) | 44/144/138 | 2/26/1 |
## ANALYSIS

# BAD CASE 121
## TASK
List all available items in the current inventory.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Xero | GreptimeDB |
| TOOL | list-items | list_tools |
| DESC | Retrieve a list of items | Lists available tools. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.251/0.499/0.062 | 0.399/0.713/0.202 |
| RANKS(SERVER/TOOL/FINAL) | 228/282/565 | 18/2/1 |
## ANALYSIS

# BAD CASE 122
## TASK
Retrieve the current list of all available tax rates.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Xero | Ramp |
| TOOL | list-tax-rates | get_ramp_categories |
| DESC | Retrieve a list of tax rates | Fetches Ramp categories. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.328/0.611/0.122 | 0.395/0.625/0.155 |
| RANKS(SERVER/TOOL/FINAL) | 76/4/12 | 9/2/1 |
## ANALYSIS

# BAD CASE 123
## TASK
Retrieve the list of all employees currently enrolled in the payroll system.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Xero | HDW LinkedIn |
| TOOL | list-payroll-employees | get_linkedin_company_employees |
| DESC | Retrieve a list of Payroll Employees | Retrieve employees of a LinkedIn company. |
| PARAMETERS |  | companies: (required) Array of company URNs.<br>keywords: (optional)<br>first_name: (optional)<br>last_name: (optional)<br>count: (optional, default: 10)<br>timeout: (optional, default: 300) |
| SCORES(SERVER/TOOL/FINAL) | 0.408/0.552/0.124 | 0.525/0.721/0.273 |
| RANKS(SERVER/TOOL/FINAL) | 17/147/75 | 2/1/1 |
## ANALYSIS

# BAD CASE 124
## TASK
Retrieve the aged payables for the specified contact within the last 90 days.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Xero | Intercom |
| TOOL | list-aged-payables-by-contact | search_tickets_by_customer |
| DESC | Retrieves aged payables for a contact | Finds tickets associated with a specific customer. |
| PARAMETERS |  | customerIdentifier: (string) Customer email or Intercom ID (required)<br>startDate: (Optional, DD/MM/YYYY) Optional start date<br>endDate: (Optional, DD/MM/YYYY) Optional end date |
| SCORES(SERVER/TOOL/FINAL) | 0.449/0.517/0.120 | 0.481/0.624/0.187 |
| RANKS(SERVER/TOOL/FINAL) | 7/170/58 | 2/5/1 |
## ANALYSIS

# BAD CASE 125
## TASK
Generate a new invoice for the latest completed project, including all relevant details such as client name, project description, and total amount due.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Xero | Stripe |
| TOOL | create-invoice | createInvoice |
| DESC | Create a new invoice | Creates a new invoice in Stripe. |
| PARAMETERS |  | customer: (string) The ID of the customer to create the invoice for.<br>lines: (array) An array of line items to include in the invoice. |
| SCORES(SERVER/TOOL/FINAL) | 0.434/0.649/0.183 | 0.386/0.801/0.248 |
| RANKS(SERVER/TOOL/FINAL) | 14/4/3 | 30/1/1 |
## ANALYSIS

# BAD CASE 126
## TASK
Update the contact details for 'John Doe' in the address book, including their new phone number and email address.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Xero | Ghost |
| TOOL | update-contact | Edit User |
| DESC | Update an existing contact | Update user details. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.412/0.592/0.144 | 0.385/0.744/0.213 |
| RANKS(SERVER/TOOL/FINAL) | 9/27/12 | 18/2/1 |
## ANALYSIS

# BAD CASE 127
## TASK
Upload a text file containing "Project Report 2024" to the "reports" directory in Firebase Storage.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Firebase | Cloudinary |
| TOOL | storage_upload | upload |
| DESC | Upload files from text, base64 content, or local file paths | Upload images and videos to Cloudinary. |
| PARAMETERS | filePath: (string) The path where the file will be stored in Firebase Storage<br>content: (string) The content of the file to upload, can be a local file path, base64 data URL, or plain text | file: (required) Path to file, URL, or base64 data URI to upload<br>resource_type: (optional) Type of resource ('image', 'video', or 'raw')<br>public_id: (optional) Custom public ID for the uploaded asset<br>overwrite: (optional) Whether to overwrite existing assets with the same public ID<br>tags: (optional) Array of tags to assign to the uploaded asset |
| SCORES(SERVER/TOOL/FINAL) | 0.283/0.433/0.053 | 0.489/0.676/0.224 |
| RANKS(SERVER/TOOL/FINAL) | 146/440/558 | 4/5/1 |
## ANALYSIS

# BAD CASE 128
## TASK
List all documents in the 'user_profiles' collection with filtering applied.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Firebase | Chroma |
| TOOL | firestore_list_documents | chroma_list_collections |
| DESC | List documents with filtering | List all collections with pagination support |
| PARAMETERS | collection: (string) The name of the collection |  |
| SCORES(SERVER/TOOL/FINAL) | 0.367/0.585/0.126 | 0.624/0.554/0.216 |
| RANKS(SERVER/TOOL/FINAL) | 61/36/55 | 1/80/1 |
## ANALYSIS

# BAD CASE 129
## TASK
List all root collections in the Firestore database.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Firebase | Outline |
| TOOL | firestore_list_collections | List Collections |
| DESC | List root collections | List all available collections. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.349/0.550/0.105 | 0.467/0.810/0.306 |
| RANKS(SERVER/TOOL/FINAL) | 65/104/129 | 4/1/1 |
## ANALYSIS

# BAD CASE 132
## TASK
Create a new newsletter with the latest company updates and upcoming events.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Ghost | Gmail |
| TOOL | Add Newsletter | send_email |
| DESC | Create a new newsletter. | Sends a new email immediately. |
| PARAMETERS |  | to: (array) List of recipient email addresses<br>subject: (string) Subject of the email<br>body: (string) Body content of the email<br>cc: (Optional, array) List of CC recipient email addresses<br>bcc: (Optional, array) List of BCC recipient email addresses |
| SCORES(SERVER/TOOL/FINAL) | 0.365/0.875/0.280 | 0.562/0.707/0.281 |
| RANKS(SERVER/TOOL/FINAL) | 43/1/2 | 1/4/1 |
## ANALYSIS

# BAD CASE 133
## TASK
Retrieve the details of the offer with ID 'OFF12345'.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Ghost | Ghost |
| TOOL | Read Offer | Read Offer |
| DESC | Retrieve an offer by ID. | Retrieve an offer by ID. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.297/0.914/0.248 | 0.297/0.914/0.248 |
| RANKS(SERVER/TOOL/FINAL) | 171/1/1 | 171/1/1 |
## ANALYSIS

# BAD CASE 134
## TASK
Retrieve the details of the tier with ID '12345'.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Ghost | Ghost |
| TOOL | Read Tier | Read Tier |
| DESC | Retrieve a tier by ID. | Retrieve a tier by ID. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.331/0.892/0.263 | 0.331/0.892/0.263 |
| RANKS(SERVER/TOOL/FINAL) | 108/1/1 | 108/1/1 |
## ANALYSIS

# BAD CASE 135
## TASK
Create a new entry in the system with the following details: title "Project Kickoff", description "Initial meeting to discuss project goals and timelines", and due date "2024-07-15".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Contentful-mcp | Apple Calendar |
| TOOL | create_entry | Event Creation |
| DESC | Create new entries | Creates calendar events based on natural language input. |
| PARAMETERS |  | calendar: (Optional, string) The calendar to add the event to.<br>location: (Optional, string) The location of the event.<br>notes: (Optional, string) Additional notes for the event.<br>reminder: (Optional, string) Reminder settings for the event.<br>recurring: (Optional, string) Recurrence pattern for the event. |
| SCORES(SERVER/TOOL/FINAL) | 0.326/0.466/0.071 | 0.497/0.691/0.238 |
| RANKS(SERVER/TOOL/FINAL) | 131/241/385 | 6/1/1 |
## ANALYSIS

# BAD CASE 136
## TASK
Publish the latest blog entry to the website.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Contentful-mcp | DevHub |
| TOOL | publish_entry | update_blog_post |
| DESC | Publish entries | Updates an existing blog post's title and/or content. |
| PARAMETERS |  | post_id: (string) The ID of the blog post.<br>title: (Optional, string) The new title of the blog post.<br>content: (Optional, string) The new HTML content of the blog post. |
| SCORES(SERVER/TOOL/FINAL) | 0.368/0.458/0.077 | 0.375/0.709/0.189 |
| RANKS(SERVER/TOOL/FINAL) | 16/141/89 | 12/1/1 |
## ANALYSIS

# BAD CASE 137
## TASK
Update the metadata and associated files for the latest version of the digital asset in the repository.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Contentful-mcp | Fibery |
| TOOL | update_asset | update_entity |
| DESC | Update asset metadata and files | Updates existing entities in your Fibery workspace with new field values. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.378/0.514/0.100 | 0.385/0.618/0.147 |
| RANKS(SERVER/TOOL/FINAL) | 21/56/31 | 16/2/1 |
## ANALYSIS

# BAD CASE 138
## TASK
Retrieve a list of all available accounts in the system.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Xero | Azure |
| TOOL | list-accounts | List Cosmos DB accounts |
| DESC | Retrieve a list of accounts | Lists all Cosmos DB accounts. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.272/0.593/0.096 | 0.326/0.863/0.243 |
| RANKS(SERVER/TOOL/FINAL) | 197/136/318 | 98/1/1 |
## ANALYSIS

# BAD CASE 139
## TASK
Retrieve the details of the current organization, including its name, address, and contact information.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Xero | Dynatrace |
| TOOL | list-organisation-details | get_ownership |
| DESC | Retrieve details about an organisation | Retrieves ownership information of an entity. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.379/0.550/0.115 | 0.509/0.767/0.299 |
| RANKS(SERVER/TOOL/FINAL) | 94/332/393 | 11/1/1 |
## ANALYSIS

# BAD CASE 140
## TASK
Retrieve the most recent 10 payments processed in the system.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Xero | Stripe |
| TOOL | list-payments | listProducts |
| DESC | Retrieve a list of payments | Lists all products in Stripe. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.403/0.512/0.106 | 0.449/0.681/0.208 |
| RANKS(SERVER/TOOL/FINAL) | 28/237/120 | 7/3/1 |
## ANALYSIS

# BAD CASE 141
## TASK
Create a new contact entry with the following details: full name, email address, and phone number.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Xero | Telegram |
| TOOL | create-contact | add_contact |
| DESC | Create a new contact | Add a contact. |
| PARAMETERS |  | phone: (str) Phone number of the contact<br>first_name: (str) First name of the contact<br>last_name: (Optional, str) Last name of the contact |
| SCORES(SERVER/TOOL/FINAL) | 0.405/0.577/0.135 | 0.312/0.879/0.241 |
| RANKS(SERVER/TOOL/FINAL) | 22/60/34 | 138/1/1 |
## ANALYSIS

# BAD CASE 142
## TASK
Generate a motivational quote about perseverance and success.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Xero | Sequential Thinking |
| TOOL | create-quote | sequential_thinking |
| DESC | Create a new quote | Facilitates a detailed, step-by-step thinking process for problem-solving and analysis. |
| PARAMETERS |  | thought: (string) The current thinking step<br>nextThoughtNeeded: (boolean) Whether another thought step is needed<br>thoughtNumber: (integer) Current thought number<br>totalThoughts: (integer) Estimated total thoughts needed<br>isRevision: (boolean, optional) Whether this revises previous thinking<br>revisesThought: (integer, optional) Which thought is being reconsidered<br>branchFromThought: (integer, optional) Branching point thought number<br>branchId: (string, optional) Branch identifier<br>needsMoreThoughts: (boolean, optional) If more thoughts are needed |
| SCORES(SERVER/TOOL/FINAL) | 0.000/0.000/0.000 | 0.318/0.491/0.077 |
| RANKS(SERVER/TOOL/FINAL) | -1/-1/-1 | 15/1/1 |
## ANALYSIS

# BAD CASE 143
## TASK
Delete the existing payroll timesheet for the current month.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Xero | n8n |
| TOOL | delete-payroll-timesheet | workflow_delete |
| DESC | Delete an existing Payroll Timesheet | Deletes a workflow. |
| PARAMETERS |  | id: (string) The ID of the workflow to delete |
| SCORES(SERVER/TOOL/FINAL) | 0.431/0.545/0.128 | 0.431/0.608/0.159 |
| RANKS(SERVER/TOOL/FINAL) | 3/30/11 | 4/4/1 |
## ANALYSIS

# BAD CASE 144
## TASK
Browse all available model collections to review their details.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Replicate | Chroma |
| TOOL | list_collections | chroma_list_collections |
| DESC | Browse model collections | List all collections with pagination support |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.399/0.619/0.153 | 0.748/0.537/0.300 |
| RANKS(SERVER/TOOL/FINAL) | 63/33/67 | 1/295/1 |
## ANALYSIS

# BAD CASE 145
## TASK
List the most recent predictions made in the system.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Replicate | GOAT |
| TOOL | list_predictions | Get price predictions using Allora API |
| DESC | See your recent predictions | Fetches price predictions using the Allora API. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.355/0.642/0.146 | 0.462/0.756/0.264 |
| RANKS(SERVER/TOOL/FINAL) | 113/15/87 | 15/1/1 |
## ANALYSIS

# BAD CASE 146
## TASK
List all currently configured payment methods for the account.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Redis Cloud API | Stripe |
| TOOL | get_current_payment_methods | listProducts |
| DESC | List all payment methods configured for your account | Lists all products in Stripe. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.417/0.677/0.191 | 0.404/0.753/0.229 |
| RANKS(SERVER/TOOL/FINAL) | 15/8/9 | 19/1/1 |
## ANALYSIS

# BAD CASE 147
## TASK
Retrieve the detailed information for the Essential subscription with the ID "ESS12345".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Redis Cloud API | Redis Cloud API |
| TOOL | get_essential_subscription_by_id | get_essentials_plans |
| DESC | Get detailed information about a specific Essential subscription | List available Essential subscription plans (paginated) |
| PARAMETERS | subscription_id: (string) ID of the Essential subscription |  |
| SCORES(SERVER/TOOL/FINAL) | 0.437/0.642/0.180 | 0.437/0.843/0.311 |
| RANKS(SERVER/TOOL/FINAL) | 16/13/7 | 16/1/1 |
## ANALYSIS

# BAD CASE 148
## TASK
Update the values in the range B2:D5 of the "Sales" sheet in the specified spreadsheet with the provided 2D array of sales data.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Google Sheets | Google Sheets |
| TOOL | update_cells | get_sheet_data |
| DESC | Writes data to a specific range. Overwrites existing data. | Reads data from a range in a sheet. |
| PARAMETERS | spreadsheet_id: (string)<br>sheet: (string)<br>range: (string) A1 notation.<br>data: (2D array) Values to write. | spreadsheet_id: (string)<br>sheet: (string) Name of the sheet.<br>range: (Optional, string) A1 notation (e.g., 'A1:C10', 'Sheet1!B2:D'). If omitted, reads the whole sheet. |
| SCORES(SERVER/TOOL/FINAL) | 0.362/0.587/0.125 | 0.362/0.710/0.182 |
| RANKS(SERVER/TOOL/FINAL) | 8/6/6 | 8/1/1 |
## ANALYSIS

# BAD CASE 149
## TASK
Retrieve 5 messages before and after the message with ID 123 in chat ID 456 to understand the conversation context.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Telegram | Membase |
| TOOL | get_message_context | get_messages |
| DESC | Get context around a message. | Get the last n messages from the current conversation. |
| PARAMETERS | chat_id: (int) ID of the chat<br>message_id: (int) ID of the message<br>context_size: (int) Number of messages before and after the message |  |
| SCORES(SERVER/TOOL/FINAL) | 0.363/0.615/0.137 | 0.566/0.784/0.348 |
| RANKS(SERVER/TOOL/FINAL) | 59/64/75 | 2/7/1 |
## ANALYSIS

# BAD CASE 150
## TASK
Search for contacts with the name "John Smith" in the address book.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Telegram | Intercom |
| TOOL | search_contacts | search_conversations_by_customer |
| DESC | Search contacts. | Finds conversations for a specific customer. |
| PARAMETERS | query: (str) Search query | customerIdentifier: (string) Customer email or Intercom ID (required)<br>startDate: (Optional, DD/MM/YYYY) Optional start date<br>endDate: (Optional, DD/MM/YYYY) Optional end date<br>keywords: (array) Optional keywords to filter by content |
| SCORES(SERVER/TOOL/FINAL) | 0.275/0.844/0.196 | 0.516/0.655/0.221 |
| RANKS(SERVER/TOOL/FINAL) | 194/1/3 | 3/12/1 |
## ANALYSIS

# BAD CASE 151
## TASK
Export all contacts in JSON format.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Telegram | Telegram |
| TOOL | export_contacts | export_contacts |
| DESC | Export all contacts as JSON. | Export all contacts as JSON. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.290/0.976/0.277 | 0.290/0.976/0.277 |
| RANKS(SERVER/TOOL/FINAL) | 158/1/1 | 158/1/1 |
## ANALYSIS

# BAD CASE 152
## TASK
Retrieve your personal user information from the system.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Telegram | EduBase |
| TOOL | get_me | edubase_get_user |
| DESC | Get your user info. | Retrieves user information from the EduBase platform. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.322/0.798/0.205 | 0.536/0.759/0.309 |
| RANKS(SERVER/TOOL/FINAL) | 139/1/3 | 1/3/1 |
## ANALYSIS

# BAD CASE 153
## TASK
Discover all available Amazon Bedrock Knowledge Bases along with their associated data sources.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | AWS | AWS KB Retrieval |
| TOOL | Discover Knowledge Bases | retrieve_from_aws_kb |
| DESC | Discover Amazon Bedrock Knowledge Bases and their data sources. | Perform retrieval operations using the AWS Knowledge Base. |
| PARAMETERS |  | query: (string) The search query for retrieval.<br>knowledgeBaseId: (string) The ID of the AWS Knowledge Base.<br>n: (number, optional) Number of results to retrieve (default: 3). |
| SCORES(SERVER/TOOL/FINAL) | 0.376/0.947/0.337 | 0.600/0.806/0.390 |
| RANKS(SERVER/TOOL/FINAL) | 125/1/3 | 3/3/1 |
## ANALYSIS

# BAD CASE 154
## TASK
Provide a set of best practices for implementing infrastructure as code in a cloud environment.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | AWS | AWS |
| TOOL | Infrastructure as Code Best Practices | Infrastructure as Code Best Practices |
| DESC | Provide best practices for infrastructure as code. | Provide best practices for infrastructure as code. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.265/0.898/0.214 | 0.265/0.898/0.214 |
| RANKS(SERVER/TOOL/FINAL) | 101/1/1 | 101/1/1 |
## ANALYSIS

# BAD CASE 155
## TASK
Generate an image using a color palette consisting of shades of blue and green.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | AWS | Placid.app |
| TOOL | Color-Guided Image Generation | placid_generate_image |
| DESC | Generate images with specific color palettes. | Generate static images by combining Placid templates with dynamic content like text and images. |
| PARAMETERS |  | template_id: (string) UUID of the template to use<br>layers: (object) Object containing dynamic content for template layers |
| SCORES(SERVER/TOOL/FINAL) | 0.228/0.828/0.156 | 0.479/0.600/0.173 |
| RANKS(SERVER/TOOL/FINAL) | 227/1/3 | 2/10/1 |
## ANALYSIS

# BAD CASE 156
## TASK
Implement a security-first development workflow for a new web application project, ensuring secure coding practices, regular security reviews, and automated vulnerability scanning are integrated into the development lifecycle.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | AWS | AWS |
| TOOL | Security-First Development Workflow | Security-First Development Workflow |
| DESC | Implement a security-first development workflow. | Implement a security-first development workflow. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.193/0.840/0.136 | 0.193/0.840/0.136 |
| RANKS(SERVER/TOOL/FINAL) | 102/1/1 | 102/1/1 |
## ANALYSIS

# BAD CASE 157
## TASK
Retrieve the latest 10 unread emails from the inbox folder in Microsoft Outlook.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Graphlit | Gmail |
| TOOL | Microsoft Outlook email | search_emails |
| DESC | Connects to Microsoft Outlook to ingest emails. | Searches for emails using Gmail search syntax. |
| PARAMETERS |  | query: (string) Gmail search query<br>maxResults: (Optional, integer) Maximum number of results to return |
| SCORES(SERVER/TOOL/FINAL) | 0.399/0.800/0.255 | 0.719/0.776/0.432 |
| RANKS(SERVER/TOOL/FINAL) | 29/1/14 | 1/3/1 |
## ANALYSIS

# BAD CASE 158
## TASK
Search for the latest podcast episodes discussing advancements in artificial intelligence.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Graphlit | FireCrawl |
| TOOL | Web Search (including Podcast Search) | firecrawl_deep_research |
| DESC | Performs web searches and ingests the results. | Conduct deep web research on a query using intelligent crawling, search, and LLM analysis. |
| PARAMETERS |  | query: (string, required) The research question or topic to explore.<br>maxDepth: (number, optional) Maximum recursive depth for crawling/search (default: 3).<br>timeLimit: (number, optional) Time limit in seconds for the research session (default: 120).<br>maxUrls: (number, optional) Maximum number of URLs to analyze (default: 50). |
| SCORES(SERVER/TOOL/FINAL) | 0.350/0.546/0.105 | 0.404/0.684/0.189 |
| RANKS(SERVER/TOOL/FINAL) | 42/52/54 | 17/2/1 |
## ANALYSIS

# BAD CASE 159
## TASK
Select 10 files from the current directory for inclusion in the project.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | llm-context | Terminal-Control |
| TOOL | lc-sel-files | list_directory |
| DESC | Select files for inclusion | List files and subdirectories in the specified directory. |
| PARAMETERS |  | path: (Optional, string) Directory path to list contents (default: current directory) |
| SCORES(SERVER/TOOL/FINAL) | 0.518/0.547/0.155 | 0.544/0.633/0.218 |
| RANKS(SERVER/TOOL/FINAL) | 3/65/11 | 1/6/1 |
## ANALYSIS

# BAD CASE 160
## TASK
Retrieve the contents of the "src/utils" directory from the "main" branch of the "example-repo" repository owned by "github-user".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | GitHub | Gitee |
| TOOL | get_file_contents | list_repo_pulls |
| DESC | Get contents of a file or directory | List pull requests in a repository |
| PARAMETERS | owner: (string) Repository owner<br>repo: (string) Repository name<br>path: (string) Path to file/directory<br>branch: (optional string) Branch to get contents from |  |
| SCORES(SERVER/TOOL/FINAL) | 0.416/0.415/0.072 | 0.672/0.602/0.272 |
| RANKS(SERVER/TOOL/FINAL) | 19/760/402 | 1/18/1 |
## ANALYSIS

# BAD CASE 161
## TASK
Add a comment with the text "This issue has been resolved in the latest update" to issue number 45 in the repository owned by "example-org".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | GitHub | Linear |
| TOOL | add_issue_comment | linear_add_comment |
| DESC | Add a comment to an issue | Add a comment to a Linear issue. |
| PARAMETERS | owner: (string) Repository owner<br>repo: (string) Repository name<br>issue_number: (number) Issue number to comment on<br>body: (string) Comment text | issueId: (string) Issue ID to comment on<br>body: (string) Comment text (markdown supported)<br>createAsUser: (Optional, string) Custom username<br>displayIconUrl: (Optional, string) Custom avatar URL |
| SCORES(SERVER/TOOL/FINAL) | 0.451/0.652/0.192 | 0.500/0.869/0.378 |
| RANKS(SERVER/TOOL/FINAL) | 11/10/16 | 4/1/1 |
## ANALYSIS

# BAD CASE 162
## TASK
Retrieve the details of pull request #42 from the repository named "sample-project" owned by "example-org".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | GitHub | Codacy |
| TOOL | get_pull_request | codacy_get_repository_pull_request |
| DESC | Get details of a specific pull request | Get detailed information about a specific pull request. |
| PARAMETERS | owner: (string) Repository owner<br>repo: (string) Repository name<br>pull_number: (number) Pull request number |  |
| SCORES(SERVER/TOOL/FINAL) | 0.497/0.650/0.210 | 0.422/0.937/0.371 |
| RANKS(SERVER/TOOL/FINAL) | 12/32/32 | 38/1/1 |
## ANALYSIS

# BAD CASE 163
## TASK
List all MongoDB Atlas organizations currently available in the system.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | MongoDB | Kong Konnect |
| TOOL | atlas-list-orgs | List Control Planes |
| DESC | Lists MongoDB Atlas organizations | List all control planes in your organization. |
| PARAMETERS |  | pageSize: (number) Number of control planes per page<br>pageNumber: (number) Page number to retrieve<br>filterName: (string) Filter control planes by name<br>filterClusterType: (string) Filter by cluster type<br>filterCloudGateway: (boolean) Filter by cloud gateway capability<br>labels: (array) Filter by labels<br>sort: (string) Sort field and direction |
| SCORES(SERVER/TOOL/FINAL) | 0.396/0.663/0.174 | 0.457/0.684/0.214 |
| RANKS(SERVER/TOOL/FINAL) | 36/22/26 | 12/10/1 |
## ANALYSIS

# BAD CASE 164
## TASK
Connect to the MongoDB Atlas cluster named "ProductionCluster" and verify the connection status.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | MongoDB | Airflow |
| TOOL | atlas-connect-cluster | Test Connection |
| DESC | Connects to MongoDB Atlas cluster | Tests a specific connection. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.445/0.590/0.155 | 0.468/0.659/0.203 |
| RANKS(SERVER/TOOL/FINAL) | 15/17/11 | 6/3/1 |
## ANALYSIS

# BAD CASE 165
## TASK
Aggregate the total sales amount from the MongoDB collection for the first quarter of 2024.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | MongoDB | Aranet4 |
| TOOL | aggregate | get_recent_data |
| DESC | Run an aggregation against a MongoDB collection | Get recent data from the local database. Can specify the number of measurements. |
| PARAMETERS |  | measurements: (Optional, int) Number of recent measurements to retrieve. |
| SCORES(SERVER/TOOL/FINAL) | 0.423/0.467/0.092 | 0.415/0.560/0.130 |
| RANKS(SERVER/TOOL/FINAL) | 4/28/7 | 5/1/1 |
## ANALYSIS

# BAD CASE 166
## TASK
Retrieve the current document details from the active Figma project.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Talk To Figma | Aiven |
| TOOL | get_document_info | get_service_details |
| DESC | Get information about the current Figma document | Get the detail of your service in a specific Aiven project. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.401/0.557/0.124 | 0.494/0.626/0.194 |
| RANKS(SERVER/TOOL/FINAL) | 33/62/51 | 5/10/1 |
## ANALYSIS

# BAD CASE 169
## TASK
Adjust the spacing between elements in an auto-layout frame to 20 pixels.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Talk To Figma | Talk To Figma |
| TOOL | set_item_spacing | set_padding |
| DESC | Set distance between children in an auto-layout frame | Set padding values for an auto-layout frame (top, right, bottom, left) |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.313/0.506/0.080 | 0.313/0.731/0.168 |
| RANKS(SERVER/TOOL/FINAL) | 47/10/18 | 47/1/1 |
## ANALYSIS

# BAD CASE 170
## TASK
Create a duplicate of the selected node with a 20-pixel horizontal offset to the right.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Talk To Figma | GOAT |
| TOOL | clone_node | Create a position on Renzo |
| DESC | Create a copy of an existing node with optional position offset | Enables the creation of positions on Renzo. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.308/0.494/0.075 | 0.409/0.556/0.127 |
| RANKS(SERVER/TOOL/FINAL) | 53/20/27 | 1/1/1 |
## ANALYSIS

# BAD CASE 171
## TASK
Join the designated communication channel to collaborate with the Figma team.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Talk To Figma | Descope |
| TOOL | join_channel | invite-user |
| DESC | Join a specific channel to communicate with Figma | Invites a new user to your Descope project. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.510/0.519/0.137 | 0.575/0.684/0.269 |
| RANKS(SERVER/TOOL/FINAL) | 10/357/127 | 2/4/1 |
## ANALYSIS

# BAD CASE 172
## TASK
Remove all assets from the designated space.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Contentful-mcp | nomad-mcp |
| TOOL | delete_asset | delete_variable |
| DESC | Remove assets from space | Deletes a variable with CAS support. |
| PARAMETERS |  | path: (string) The path of the variable.<br>namespace: (string) The namespace of the variable. |
| SCORES(SERVER/TOOL/FINAL) | 0.379/0.539/0.110 | 0.531/0.635/0.214 |
| RANKS(SERVER/TOOL/FINAL) | 14/58/48 | 1/6/1 |
## ANALYSIS

# BAD CASE 173
## TASK
Retrieve the content of the README.md file from the main branch of the specified repository.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Gitee | Gitee |
| TOOL | get_file_content | list_repo_pulls |
| DESC | Get the content of a file in a repository | List pull requests in a repository |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.618/0.471/0.180 | 0.618/0.525/0.200 |
| RANKS(SERVER/TOOL/FINAL) | 1/158/6 | 1/56/1 |
## ANALYSIS

# BAD CASE 174
## TASK
Update the status of the current issue to "In Progress" and assign it to the project manager.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Gitee | Atlassian |
| TOOL | update_issue | jira_transition_issue |
| DESC | Update an issue | Transition an issue to a new status |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.387/0.543/0.114 | 0.472/0.588/0.164 |
| RANKS(SERVER/TOOL/FINAL) | 16/19/13 | 1/6/1 |
## ANALYSIS

# BAD CASE 175
## TASK
List all notifications for the current user.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Gitee | Linear (Go) |
| TOOL | list_user_notifications | linear_get_user_issues |
| DESC | List user notifications | Retrieves issues assigned to a specific user or the authenticated user. |
| PARAMETERS |  | userId: (Optional) Optional user ID. If not provided, returns authenticated user's issues<br>includeArchived: Include archived issues in results<br>limit: Maximum number of issues to return (default: 50) |
| SCORES(SERVER/TOOL/FINAL) | 0.453/0.633/0.182 | 0.457/0.637/0.186 |
| RANKS(SERVER/TOOL/FINAL) | 6/19/3 | 5/15/1 |
## ANALYSIS

# BAD CASE 176
## TASK
Retrieve the content of the latest project documentation page from the team's knowledge base.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Atlassian | Graphlit |
| TOOL | confluence_get_page | Query Contents |
| DESC | Get content of a specific page | Searches and retrieves contents from the knowledge base. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.000/0.000/0.000 | 0.488/0.767/0.287 |
| RANKS(SERVER/TOOL/FINAL) | -1/-1/-1 | 21/1/1 |
## ANALYSIS

# BAD CASE 177
## TASK
Retrieve all customer records from the connected database using JDBC.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | JDBC | DBHub |
| TOOL | jdbc | execute_sql |
| DESC | A server for storing and retrieving data from a database via a JDBC URL. | Executes SQL queries on the connected database. |
| PARAMETERS |  | dsn: (string) The database connection string.<br>sql: (string) The SQL query to execute. |
| SCORES(SERVER/TOOL/FINAL) | 0.266/0.623/0.103 | 0.421/0.634/0.169 |
| RANKS(SERVER/TOOL/FINAL) | 141/9/47 | 7/8/1 |
## ANALYSIS

# BAD CASE 178
## TASK
Swap 100 units of the source token for the target token with a slippage tolerance of 1%.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Solana Agent Kit | GOAT |
| TOOL | trade | Swap tokens on Uniswap |
| DESC | Swaps tokens using a DEX. | Facilitates token swapping on Uniswap. |
| PARAMETERS | targetTokenMint: (PublicKey) Target token mint<br>amount: (number) Amount to trade<br>sourceTokenMint: (PublicKey) Source token mint<br>slippage: (number) Slippage tolerance |  |
| SCORES(SERVER/TOOL/FINAL) | 0.515/0.766/0.302 | 0.546/0.749/0.306 |
| RANKS(SERVER/TOOL/FINAL) | 2/2/3 | 1/3/1 |
## ANALYSIS

# BAD CASE 179
## TASK
Close all empty token accounts in the system.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Solana Agent Kit | Solana Agent Kit |
| TOOL | closeEmptyTokenAccounts | closeEmptyTokenAccounts |
| DESC | Closes empty token accounts. | Closes empty token accounts. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.312/0.963/0.289 | 0.312/0.963/0.289 |
| RANKS(SERVER/TOOL/FINAL) | 50/1/1 | 50/1/1 |
## ANALYSIS

# BAD CASE 180
## TASK
Create a cross-chain order to transfer 1000 USDC from Ethereum (chain ID: 1) to Polygon (chain ID: 137), converting it to MATIC and sending it to recipient address 0x123...abc.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Solana Agent Kit | GOAT |
| TOOL | createDebridgeOrder | Cross-chain token swap using Mayan SDK |
| DESC | Creates a deBridge order. | Facilitates cross-chain token swaps using the Mayan SDK. |
| PARAMETERS | srcChainId: (string) Source chain ID<br>srcChainTokenIn: (string) Source token mint<br>srcChainTokenInAmount: (string) Amount of source token<br>dstChainId: (string) Destination chain ID<br>dstChainTokenOut: (string) Destination token mint<br>dstChainTokenOutRecipient: (string) Recipient address on destination chain |  |
| SCORES(SERVER/TOOL/FINAL) | 0.508/0.654/0.218 | 0.643/0.774/0.385 |
| RANKS(SERVER/TOOL/FINAL) | 5/20/45 | 1/2/1 |
## ANALYSIS

# BAD CASE 181
## TASK
Retrieve the 10 most recent conversation threads along with their associated messages from HubSpot.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | HubSpot | Intercom |
| TOOL | hubspot_get_recent_conversations | search_conversations_by_customer |
| DESC | Retrieve recent conversation threads with messages | Finds conversations for a specific customer. |
| PARAMETERS |  | customerIdentifier: (string) Customer email or Intercom ID (required)<br>startDate: (Optional, DD/MM/YYYY) Optional start date<br>endDate: (Optional, DD/MM/YYYY) Optional end date<br>keywords: (array) Optional keywords to filter by content |
| SCORES(SERVER/TOOL/FINAL) | 0.418/0.505/0.106 | 0.495/0.795/0.313 |
| RANKS(SERVER/TOOL/FINAL) | 37/443/306 | 9/1/1 |
## ANALYSIS

# BAD CASE 182
## TASK
List all available metric metadata from the Prometheus monitoring system.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Grafana | Dicom |
| TOOL | list_prometheus_metric_metadata | get_attribute_presets |
| DESC | List metric metadata | List the available levels of detail (minimal, standard, extended) for metadata query results. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.373/0.570/0.121 | 0.419/0.736/0.227 |
| RANKS(SERVER/TOOL/FINAL) | 68/111/115 | 25/1/1 |
## ANALYSIS

# BAD CASE 183
## TASK
List all available label names from the logs stored in the Loki logging system.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Grafana | OpenCTI |
| TOOL | list_loki_label_names | list_labels |
| DESC | List all available label names in logs | Lists all available labels. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.351/0.576/0.117 | 0.438/0.821/0.295 |
| RANKS(SERVER/TOOL/FINAL) | 95/139/150 | 15/1/1 |
## ANALYSIS

# BAD CASE 184
## TASK
List all users currently on call in Grafana OnCall.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Grafana | Apple Calendar |
| TOOL | list_oncall_users | Smart Schedule Management & Availability |
| DESC | List users from Grafana OnCall | Provides information about the user's schedule and finds available time slots for meetings. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.354/0.692/0.170 | 0.442/0.736/0.240 |
| RANKS(SERVER/TOOL/FINAL) | 76/4/23 | 18/1/1 |
## ANALYSIS

# BAD CASE 185
## TASK
Delete the variable with the key "user_session_token" from the system.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Airflow | nomad-mcp |
| TOOL | Delete Variable | delete_variable |
| DESC | Deletes a specific variable. | Deletes a variable with CAS support. |
| PARAMETERS | variable_key: (string) The key of the variable. | path: (string) The path of the variable.<br>namespace: (string) The namespace of the variable. |
| SCORES(SERVER/TOOL/FINAL) | 0.244/0.720/0.127 | 0.607/0.671/0.273 |
| RANKS(SERVER/TOOL/FINAL) | 131/1/12 | 1/2/1 |
## ANALYSIS

# BAD CASE 186
## TASK
Retrieve the details of the pool named "Sunset Oasis".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Airflow | Airflow |
| TOOL | Get Pool | Get Pool |
| DESC | Gets a specific pool. | Gets a specific pool. |
| PARAMETERS | pool_name: (string) The name of the pool. | pool_name: (string) The name of the pool. |
| SCORES(SERVER/TOOL/FINAL) | 0.354/0.807/0.231 | 0.354/0.807/0.231 |
| RANKS(SERVER/TOOL/FINAL) | 102/1/1 | 102/1/1 |
## ANALYSIS

# BAD CASE 189
## TASK
Register an incoming webhook for the Bitrise application with the identifier "mobile-app-ios".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Bitrise | n8n |
| TOOL | register_webhook | run_webhook |
| DESC | Register an incoming webhook for a specific application | Triggers a workflow via a webhook, passing the workflow name and optional data. |
| PARAMETERS | app_slug: (string) Identifier of the Bitrise app | workflowName: (string) The name of the workflow to trigger<br>data: (Optional, object) Additional data to pass to the webhook |
| SCORES(SERVER/TOOL/FINAL) | 0.659/0.494/0.215 | 0.516/0.717/0.265 |
| RANKS(SERVER/TOOL/FINAL) | 1/344/9 | 5/3/1 |
## ANALYSIS

# BAD CASE 190
## TASK
Retrieve the pipeline configuration for the Bitrise app with the identifier "example-app" and pipeline ID "pipeline-123".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Bitrise | Heroku |
| TOOL | get_pipeline | pipelines_info |
| DESC | Get a pipeline of a given app | Get detailed pipeline information. |
| PARAMETERS | app_slug: (string) Identifier of the Bitrise app<br>pipeline_id: (string) Identifier of the pipeline |  |
| SCORES(SERVER/TOOL/FINAL) | 0.697/0.445/0.216 | 0.503/0.832/0.348 |
| RANKS(SERVER/TOOL/FINAL) | 1/806/31 | 8/1/1 |
## ANALYSIS

# BAD CASE 191
## TASK
Invite a user with the email address "example@domain.com" to the Bitrise workspace identified by the slug "dev-team-2024".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Bitrise | Descope |
| TOOL | invite_member_to_workspace | invite-user |
| DESC | Invite a member to a workspace | Invites a new user to your Descope project. |
| PARAMETERS | workspace_slug: (string) Slug of the Bitrise workspace<br>email: (string) Email address of the user |  |
| SCORES(SERVER/TOOL/FINAL) | 0.651/0.541/0.229 | 0.682/0.794/0.430 |
| RANKS(SERVER/TOOL/FINAL) | 2/157/5 | 1/1/1 |
## ANALYSIS

# BAD CASE 192
## TASK
List the first 10 available Build Distribution versions for the connected app with ID "123e4567-e89b-12d3-a456-426614174000".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Bitrise | Heroku |
| TOOL | list_build_distribution_versions | get_app_info |
| DESC | Lists Build Distribution versions available for testers | Get detailed information about an app, including its configuration, dynos, and add-ons. |
| PARAMETERS | connected_app_id: (string) The uuidV4 identifier of the connected app<br>items_per_page: (Optional, integer) Maximum number of versions per page<br>page: (Optional, integer) Page number to return |  |
| SCORES(SERVER/TOOL/FINAL) | 0.581/0.531/0.179 | 0.492/0.742/0.271 |
| RANKS(SERVER/TOOL/FINAL) | 1/92/7 | 4/1/1 |
## ANALYSIS

# BAD CASE 193
## TASK
Retrieve the details of the monitor with ID "MNT-2024-001".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Datadog | Unstructured |
| TOOL | get-monitor | get_source_info |
| DESC | Get details of a specific monitor by ID | Get detailed information about a specific source connector. |
| PARAMETERS | monitorId: (string) ID of the monitor to fetch |  |
| SCORES(SERVER/TOOL/FINAL) | 0.000/0.000/0.000 | 0.495/0.642/0.204 |
| RANKS(SERVER/TOOL/FINAL) | -1/-1/-1 | 3/4/1 |
## ANALYSIS

# BAD CASE 194
## TASK
Retrieve the complete list of available exchanges along with their details.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | CoinMarketCap | Financial Datasets |
| TOOL | exchangeMap | get_available_crypto_tickers |
| DESC | Get mapping of all exchanges | Gets all available crypto tickers. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.397/0.590/0.138 | 0.525/0.668/0.234 |
| RANKS(SERVER/TOOL/FINAL) | 20/20/66 | 3/4/1 |
## ANALYSIS

# BAD CASE 195
## TASK
Retrieve the most recent trades for all available spot trading pairs.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | CoinMarketCap | coin_api_mcp |
| TOOL | dexPairsTradeLatest | get-coin-quotes |
| DESC | Get latest trades for spot pairs | Fetches the latest market quotes for one or more cryptocurrencies. |
| PARAMETERS |  | id: (string, optional) One or more comma-separated cryptocurrency CoinMarketCap IDs.<br>slug: (string, optional) A comma-separated list of cryptocurrency slugs.<br>symbol: (string, optional) One or more comma-separated cryptocurrency symbols. |
| SCORES(SERVER/TOOL/FINAL) | 0.345/0.636/0.139 | 0.529/0.725/0.278 |
| RANKS(SERVER/TOOL/FINAL) | 26/11/46 | 2/2/1 |
## ANALYSIS

# BAD CASE 196
## TASK
Retrieve the latest metadata for an active cryptocurrency airdrop campaign.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | CoinMarketCap | coin_api_mcp |
| TOOL | cryptoAirdrop | listing-coins |
| DESC | Get metadata about a specific airdrop | Fetches a paginated list of all active cryptocurrencies with the latest market data. |
| PARAMETERS |  | start: (integer, optional) Offset the start (1-based index) of the paginated list of items to return.<br>limit: (integer, optional) Number of results to return (default: 10, max: 5000).<br>price_min: (number, optional) Minimum USD price to filter results.<br>price_max: (number, optional) Maximum USD price to filter results.<br>market_cap_min: (number, optional) Minimum market cap to filter results.<br>market_cap_max: (number, optional) Maximum market cap to filter results.<br>convert: (string, optional) Calculate market quotes in multiple currencies.<br>sort: (string, optional) Field to sort the list of cryptocurrencies by.<br>sort_dir: (string, optional) Direction to order cryptocurrencies (asc or desc). |
| SCORES(SERVER/TOOL/FINAL) | 0.467/0.569/0.151 | 0.484/0.695/0.234 |
| RANKS(SERVER/TOOL/FINAL) | 6/86/53 | 5/1/1 |
## ANALYSIS

# BAD CASE 197
## TASK
Delete the contact with user ID 12345 from the system.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Telegram | Telegram |
| TOOL | delete_contact | delete_contact |
| DESC | Delete a contact. | Delete a contact. |
| PARAMETERS | user_id: (int) ID of the contact | user_id: (int) ID of the contact |
| SCORES(SERVER/TOOL/FINAL) | 0.325/0.896/0.260 | 0.325/0.896/0.260 |
| RANKS(SERVER/TOOL/FINAL) | 56/1/1 | 56/1/1 |
## ANALYSIS

# BAD CASE 198
## TASK
Check the online status of the user with ID 12345.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Telegram | Telegram |
| TOOL | get_user_status | get_user_status |
| DESC | Get a user's online status. | Get a user's online status. |
| PARAMETERS | user_id: (int) ID of the user | user_id: (int) ID of the user |
| SCORES(SERVER/TOOL/FINAL) | 0.291/0.833/0.202 | 0.291/0.833/0.202 |
| RANKS(SERVER/TOOL/FINAL) | 104/1/1 | 104/1/1 |
## ANALYSIS

# BAD CASE 200
## TASK
Run a Python script in a temporary sandboxed environment to process and analyze a dataset, ensuring automatic cleanup after completion.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Heroku | Data Exploration |
| TOOL | deploy_one_off_dyno | run-script |
| DESC | Execute code or commands in a sandboxed environment on a Heroku one-off dyno. Supports file creation, network access, environment variables, and automatic cleanup. Ideal for running scripts, tests, or temporary workloads. | Executes a Python script. |
| PARAMETERS |  | script: (string, required) The script to execute |
| SCORES(SERVER/TOOL/FINAL) | 0.330/0.678/0.152 | 0.482/0.762/0.280 |
| RANKS(SERVER/TOOL/FINAL) | 32/3/5 | 2/1/1 |
## ANALYSIS

# BAD CASE 201
## TASK
Execute the command `["ls", "-l", "/var/log"]` in the Pod named `nginx-pod` within the `default` namespace, targeting the `nginx` container.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Kubernetes and OpenShift | mcp-k8s-go |
| TOOL | pods_exec | Get Kubernetes pod logs |
| DESC | Execute a command in a Kubernetes Pod in the current or provided namespace with the provided name and command | Retrieves logs from a specified Kubernetes pod. |
| PARAMETERS | command: (Required, string[]) Command to execute in the Pod container. First item is the command, rest are arguments.<br>name: (Required, string) Name of the Pod<br>namespace: (Required, string) Namespace of the Pod<br>container: (Optional, string) Name of the Pod container to get logs from |  |
| SCORES(SERVER/TOOL/FINAL) | 0.529/0.407/0.114 | 0.468/0.722/0.244 |
| RANKS(SERVER/TOOL/FINAL) | 1/287/17 | 3/1/1 |
## ANALYSIS

# BAD CASE 202
## TASK
Retrieve the details of a document generation job with the identifier "JOB12345".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Box | Unstructured |
| TOOL | box_docgen_get_job_tool | check_llmtxt_status |
| DESC | Fetch a single Doc Gen job by its ID. | Retrieves the results of an LLM-optimized text generation job. |
| PARAMETERS | job_id: (str) The job identifier |  |
| SCORES(SERVER/TOOL/FINAL) | 0.478/0.871/0.362 | 0.673/0.793/0.423 |
| RANKS(SERVER/TOOL/FINAL) | 29/1/5 | 1/4/1 |
## ANALYSIS

# BAD CASE 203
## TASK
Get the latest market quotes for Bitcoin, Ethereum, and Litecoin.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | CoinMarketCap | coin_api_mcp |
| TOOL | cryptoQuotesLatest | get-coin-quotes |
| DESC | Get latest market quote for 1 or more cryptocurrencies | Fetches the latest market quotes for one or more cryptocurrencies. |
| PARAMETERS |  | id: (string, optional) One or more comma-separated cryptocurrency CoinMarketCap IDs.<br>slug: (string, optional) A comma-separated list of cryptocurrency slugs.<br>symbol: (string, optional) One or more comma-separated cryptocurrency symbols. |
| SCORES(SERVER/TOOL/FINAL) | 0.508/0.606/0.186 | 0.718/0.974/0.682 |
| RANKS(SERVER/TOOL/FINAL) | 5/44/41 | 1/1/1 |
## ANALYSIS

# BAD CASE 204
## TASK
Retrieve the historical OHLCV (Open, High, Low, Close, Volume) data for the last 30 days for all available spot trading pairs.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | CoinMarketCap | Financial Datasets |
| TOOL | dexPairsOhlcvHistorical | get_crypto_prices |
| DESC | Get historical OHLCV data for spot pairs | Gets historical prices for a crypto currency. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.424/0.662/0.186 | 0.608/0.737/0.330 |
| RANKS(SERVER/TOOL/FINAL) | 4/5/9 | 1/1/1 |
## ANALYSIS

# BAD CASE 205
## TASK
Retrieve the historical market data for the top 10 cryptocurrencies by market capitalization over the past 30 days.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | CoinMarketCap | Financial Datasets |
| TOOL | historicalCryptocurrencyListings | get_crypto_prices |
| DESC | Get historical market quotes for any cryptocurrency | Gets historical prices for a crypto currency. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.578/0.532/0.178 | 0.711/0.801/0.456 |
| RANKS(SERVER/TOOL/FINAL) | 3/97/34 | 1/1/1 |
## ANALYSIS

# BAD CASE 206
## TASK
Retrieve the metadata for the ERC20 token with the address '0x123abc' on the Ethereum mainnet.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | EVM MCP Server | GOAT |
| TOOL | get-token-info | Interact with any ERC20 token |
| DESC | Get ERC20 token metadata | Enables interaction with ERC20 tokens. |
| PARAMETERS | tokenAddress: (address/ENS) The address or ENS name of the token<br>network: (string) The network identifier |  |
| SCORES(SERVER/TOOL/FINAL) | 0.364/0.598/0.130 | 0.638/0.775/0.383 |
| RANKS(SERVER/TOOL/FINAL) | 23/38/81 | 1/1/1 |
## ANALYSIS

# BAD CASE 207
## TASK
Retrieve the details of the transaction with the hash "0x123abc456def789ghi" on the Ethereum network.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | EVM MCP Server | GOAT |
| TOOL | get-transaction | Get transaction information using Etherscan API |
| DESC | Get transaction details | Retrieves transaction information using the Etherscan API. |
| PARAMETERS | txHash: (string) The transaction hash<br>network: (string) The network identifier |  |
| SCORES(SERVER/TOOL/FINAL) | 0.312/0.636/0.126 | 0.572/0.887/0.450 |
| RANKS(SERVER/TOOL/FINAL) | 135/18/92 | 1/1/1 |
## ANALYSIS

# BAD CASE 208
## TASK
Update the title of the existing document to "Project Report Q3 2024" and modify the access permissions to "View Only" for external collaborators.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Dart | Gmail |
| TOOL | update_doc | update_label |
| DESC | Update an existing doc's properties | Updates an existing Gmail label. |
| PARAMETERS |  | id: (string) ID of the label<br>name: (string) New name of the label<br>messageListVisibility: (string) New visibility setting for message list (show or hide)<br>labelListVisibility: (string) New visibility setting for label list (labelShow, labelShowIfUnread, or labelHide) |
| SCORES(SERVER/TOOL/FINAL) | 0.478/0.385/0.088 | 0.444/0.603/0.162 |
| RANKS(SERVER/TOOL/FINAL) | 3/658/99 | 11/8/1 |
## ANALYSIS

# BAD CASE 209
## TASK
List all active incidents in the Grafana Incident monitoring system.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Grafana | Unstructured |
| TOOL | list_incidents | list_workflows_with_finished_jobs |
| DESC | List incidents in Grafana Incident | Lists all workflows that have any completed job, together with information about source and destination details. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.401/0.617/0.153 | 0.565/0.658/0.245 |
| RANKS(SERVER/TOOL/FINAL) | 59/70/99 | 2/20/1 |
## ANALYSIS

# BAD CASE 211
## TASK
Create a new file named "PlayerSettings.json" in the Unity project's Assets folder with the content `{"playerName": "Hero", "health": 100, "level": 1}`.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Unity Integration (Advanced) | DaVinci Resolve |
| TOOL | write_file | create_new_project |
| DESC | Create or overwrite a file with new content | Creates a new project in DaVinci Resolve. |
| PARAMETERS | path: (string) Path to the file, can be absolute or relative to the Unity project's Assets folder<br>content: (string) Content to write to the file | project_name: (string) The name of the new project. |
| SCORES(SERVER/TOOL/FINAL) | 0.289/0.394/0.045 | 0.373/0.501/0.094 |
| RANKS(SERVER/TOOL/FINAL) | 62/131/150 | 3/2/1 |
## ANALYSIS

# BAD CASE 213
## TASK
Delete the document with the ID "12345" from the specified MongoDB collection.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | MongoDB | Couchbase |
| TOOL | delete-one | delete_document_by_id |
| DESC | Delete a single document from a MongoDB collection | Delete a document by ID from a specified scope and collection. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.286/0.598/0.102 | 0.382/0.788/0.237 |
| RANKS(SERVER/TOOL/FINAL) | 77/8/29 | 10/1/1 |
## ANALYSIS

# BAD CASE 216
## TASK
Search for the top 5 most relevant webpages related to "best practices for sustainable agriculture".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Heurist Mesh Agent | Octagon |
| TOOL | search | octagon-deep-research-agent |
| DESC | Search for webpages related to a query | Perform comprehensive research on any topic. |
| PARAMETERS | search_term: (string) The search term<br>limit: (integer) Maximum number of results to return (default: 10) | prompt: (string) A natural language query specifying the topic to research. |
| SCORES(SERVER/TOOL/FINAL) | 0.202/0.567/0.065 | 0.532/0.763/0.310 |
| RANKS(SERVER/TOOL/FINAL) | 285/120/507 | 4/11/1 |
## ANALYSIS

# BAD CASE 217
## TASK
Generate the Abstract Syntax Tree (AST) for the provided Python function that calculates the factorial of a number.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Semgrep | Calculator |
| TOOL | get_abstract_syntax_tree | calculate |
| DESC | Output the Abstract Syntax Tree (AST) of code | Calculates/evaluates the given expression. |
| PARAMETERS | code: (string) Code to generate the AST for | expression: (string, required) Expression to be calculated |
| SCORES(SERVER/TOOL/FINAL) | 0.251/0.422/0.045 | 0.430/0.617/0.163 |
| RANKS(SERVER/TOOL/FINAL) | 94/38/97 | 2/1/1 |
## ANALYSIS

# BAD CASE 218
## TASK
Retrieve all annotations present in the active document.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Talk To Figma | OpenCTI |
| TOOL | get_annotations | list_marking_definitions |
| DESC | Get all annotations in the current document or specific node | Lists all marking definitions. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.287/0.428/0.052 | 0.358/0.618/0.137 |
| RANKS(SERVER/TOOL/FINAL) | 163/497/538 | 26/1/1 |
## ANALYSIS

# BAD CASE 220
## TASK
Aggregate the sales data for the last quarter to calculate total revenue and average order value.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | MongoDB Lens | Audiense Insights |
| TOOL | aggregate-data | get-audience-insights |
| DESC | Execute aggregation pipelines | Retrieves aggregated insights for a given audience, including demographics, behavioral traits, psychographics, and socioeconomic factors. |
| PARAMETERS |  | audience_insights_id: (string) The ID of the audience insights.<br>insights: (array of strings, optional) List of specific insight names to filter. |
| SCORES(SERVER/TOOL/FINAL) | 0.369/0.395/0.058 | 0.406/0.609/0.151 |
| RANKS(SERVER/TOOL/FINAL) | 27/426/245 | 14/3/1 |
## ANALYSIS

# BAD CASE 221
## TASK
Extract all unique customer email addresses from the provided dataset.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | MongoDB Lens | Gmail |
| TOOL | distinct-values | batch_delete_emails |
| DESC | Extract unique values for any field | Permanently deletes multiple emails in efficient batches. |
| PARAMETERS |  | messageIds: (array) List of email message IDs<br>batchSize: (Optional, integer) Number of emails to process in each batch |
| SCORES(SERVER/TOOL/FINAL) | 0.206/0.337/0.023 | 0.434/0.588/0.150 |
| RANKS(SERVER/TOOL/FINAL) | 216/925/898 | 1/2/1 |
## ANALYSIS

# BAD CASE 222
## TASK
List all available API paths along with their supported HTTP methods and summaries in a structured format.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | OpenAPI Schema | OpenAPI AnyApi |
| TOOL | list-endpoints | {prefix}_api_request_schema |
| DESC | Lists all API paths and their HTTP methods with summaries in a nested object structure | Get API endpoint schemas that match your intent. Returns endpoint details including path, method, parameters, and response formats. |
| PARAMETERS |  | query: (string) Describe what you want to do with the API (e.g., 'Get user profile information', 'Create a new job posting') |
| SCORES(SERVER/TOOL/FINAL) | 0.445/0.583/0.151 | 0.407/0.830/0.281 |
| RANKS(SERVER/TOOL/FINAL) | 16/52/33 | 33/1/1 |
## ANALYSIS

# BAD CASE 223
## TASK
Generate a trial balance report for the current fiscal year.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Xero | Financial Datasets |
| TOOL | list-trial-balance | get_income_statements |
| DESC | Retrieve a trial balance report | Get income statements for a company. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.419/0.666/0.186 | 0.366/0.719/0.189 |
| RANKS(SERVER/TOOL/FINAL) | 9/4/2 | 52/1/1 |
## ANALYSIS

# BAD CASE 224
## TASK
List all jobs associated with the latest workflow processed by the Unstructured API.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Unstructured | Unstructured |
| TOOL | list_jobs | list_workflows_with_finished_jobs |
| DESC | Lists jobs for a specific workflow from the Unstructured API. | Lists all workflows that have any completed job, together with information about source and destination details. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.690/0.885/0.540 | 0.690/0.904/0.564 |
| RANKS(SERVER/TOOL/FINAL) | 2/2/2 | 2/1/1 |
## ANALYSIS

# BAD CASE 225
## TASK
Create a list of 5 new tasks for the upcoming project deadline, including their titles, descriptions, and due dates.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ClickUp | Todoist |
| TOOL | create_bulk_tasks | todoist_create_task |
| DESC | Create multiple tasks | Create new tasks with various attributes. |
| PARAMETERS | tasks[]: (array) An array of task objects to create | content: (string) task title<br>description: (Optional, string) task description<br>due date: (Optional, string) due date<br>priority level: (Optional, number) priority level (1-4) |
| SCORES(SERVER/TOOL/FINAL) | 0.265/0.599/0.095 | 0.549/0.757/0.315 |
| RANKS(SERVER/TOOL/FINAL) | 204/8/107 | 1/1/1 |
## ANALYSIS

# BAD CASE 226
## TASK
Retrieve the details of the list with the ID "L12345" and optionally include the name if available.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ClickUp | nomad-mcp |
| TOOL | get_list | list_variables |
| DESC | Get list details | Lists variables with optional filtering and pagination. |
| PARAMETERS | listId: (string) The ID of the list to get<br>listName: (Optional, string) The name of the list to get | namespace: (string) The namespace to filter variables by.<br>prefix: (string) The prefix to filter variables by.<br>per_page: (int) The number of results per page. |
| SCORES(SERVER/TOOL/FINAL) | 0.160/0.594/0.057 | 0.505/0.680/0.234 |
| RANKS(SERVER/TOOL/FINAL) | 291/116/825 | 3/8/1 |
## ANALYSIS

# BAD CASE 227
## TASK
Create a new page titled "Project Timeline" with the content "Q2 2024 deliverables" in the specified workspace and document, setting the content format to plain text.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ClickUp | DaVinci Resolve |
| TOOL | create_document_pages | create_new_timeline |
| DESC | Create a document page | Creates a new timeline in the current project. |
| PARAMETERS | workspaceId: (string) The ID of the workspace<br>documentId: (string) The ID of the document<br>parent_page_id: (Optional, string) The ID of the parent page<br>name: (string) The name of the page<br>sub_title: (Optional, string) The subtitle of the page<br>content: (string) The content of the page<br>content_format: (Optional, string) The format of the content | timeline_name: (string) The name of the new timeline. |
| SCORES(SERVER/TOOL/FINAL) | 0.404/0.466/0.088 | 0.433/0.611/0.161 |
| RANKS(SERVER/TOOL/FINAL) | 27/113/102 | 11/2/1 |
## ANALYSIS

# BAD CASE 229
## TASK
List the first 10 available prompts, starting from the beginning of the list.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Langfuse Prompt Management | GreptimeDB |
| TOOL | get-prompts | list_prompts |
| DESC | List available prompts | Lists available prompts. |
| PARAMETERS | cursor: (Optional, string) Parameter for pagination |  |
| SCORES(SERVER/TOOL/FINAL) | 0.580/0.613/0.218 | 0.500/0.919/0.423 |
| RANKS(SERVER/TOOL/FINAL) | 3/55/14 | 16/1/1 |
## ANALYSIS

# BAD CASE 231
## TASK
Remove the current profile photo from your account.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Telegram | Telegram |
| TOOL | delete_profile_photo | delete_profile_photo |
| DESC | Remove your profile photo. | Remove your profile photo. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.420/0.923/0.358 | 0.420/0.923/0.358 |
| RANKS(SERVER/TOOL/FINAL) | 15/1/1 | 15/1/1 |
## ANALYSIS

# BAD CASE 232
## TASK
Retrieve the detailed schema and metadata for the table identified by its fully qualified name.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Apache Gravitino(incubating) | Keboola |
| TOOL | get_table_by_fqn | get_table_detail |
| DESC | Get detailed table information by fully qualified name | Gets detailed information about a specific table including its DB identifier and column information. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.281/0.565/0.090 | 0.425/0.831/0.293 |
| RANKS(SERVER/TOOL/FINAL) | 176/41/137 | 20/3/1 |
## ANALYSIS

# BAD CASE 233
## TASK
Find the folder named "Project_Documents_2024" in the connected storage system.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Box | Graphlit |
| TOOL | box_search_folder_by_name | List SharePoint Folders |
| DESC | Locate a folder by name. | Lists available folders within a SharePoint library. |
| PARAMETERS | folder_name: (str) Name of the folder |  |
| SCORES(SERVER/TOOL/FINAL) | 0.383/0.689/0.182 | 0.426/0.741/0.234 |
| RANKS(SERVER/TOOL/FINAL) | 86/6/14 | 41/3/1 |
## ANALYSIS

# BAD CASE 234
## TASK
Resolve the latest incident reported in the ServiceNow system.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ServiceNow | OpenCTI |
| TOOL | resolve_incident | get_latest_reports |
| DESC | Resolve an incident in ServiceNow | Retrieves the most recent threat intelligence reports. |
| PARAMETERS |  | first: (Optional, number) Number of reports to retrieve, defaults to 10 |
| SCORES(SERVER/TOOL/FINAL) | 0.330/0.682/0.153 | 0.496/0.682/0.231 |
| RANKS(SERVER/TOOL/FINAL) | 172/4/81 | 10/5/1 |
## ANALYSIS

# BAD CASE 235
## TASK
Approve the pending change request in the system.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ServiceNow | Heroku |
| TOOL | approve_change | pipelines_promote |
| DESC | Approve a change request | Promote apps to the next stage in a pipeline. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.304/0.651/0.129 | 0.441/0.631/0.176 |
| RANKS(SERVER/TOOL/FINAL) | 131/1/25 | 12/2/1 |
## ANALYSIS

# BAD CASE 236
## TASK
List all available knowledge bases with their respective details.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ServiceNow | Graphlit |
| TOOL | list_knowledge_bases | Query Contents |
| DESC | List knowledge bases with filtering options | Searches and retrieves contents from the knowledge base. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.345/0.613/0.130 | 0.540/0.825/0.367 |
| RANKS(SERVER/TOOL/FINAL) | 166/173/356 | 12/2/1 |
## ANALYSIS

# BAD CASE 238
## TASK
List all monitored pages for the specified application.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Raygun | Heroku |
| TOOL | list_pages | ps_list |
| DESC | List monitored pages for an application | List all dynos for an app. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.411/0.509/0.107 | 0.460/0.718/0.237 |
| RANKS(SERVER/TOOL/FINAL) | 25/395/255 | 13/1/1 |
## ANALYSIS

# BAD CASE 239
## TASK
Retrieve the latest statistics for all active log streams in the Loki logging system.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Grafana | Aranet4 |
| TOOL | query_loki_stats | get_configuration_and_db_stats |
| DESC | Get statistics about log streams | Get the current configuration and database statistics. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.403/0.507/0.103 | 0.478/0.681/0.222 |
| RANKS(SERVER/TOOL/FINAL) | 30/238/141 | 7/4/1 |
## ANALYSIS

# BAD CASE 240
## TASK
Create a new form field for a catalog item to capture customer preferences.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ServiceNow | gotoHuman |
| TOOL | create_catalog_item_variable | get-form-schema |
| DESC | Create a new variable (form field) for a catalog item | Get the schema to use when requesting a human review for a given form. |
| PARAMETERS |  | formId: (string) The form ID to fetch the schema for |
| SCORES(SERVER/TOOL/FINAL) | 0.331/0.538/0.096 | 0.423/0.610/0.157 |
| RANKS(SERVER/TOOL/FINAL) | 110/25/38 | 10/1/1 |
## ANALYSIS

# BAD CASE 241
## TASK
Delete the script include named 'UserUtils' from the ServiceNow instance.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ServiceNow | Unity Catalog |
| TOOL | delete_script_include | uc_delete_function |
| DESC | Delete a script include from ServiceNow | Deletes a function within a parent catalog and schema. |
| PARAMETERS |  | name: (string) The name of the function (not fully-qualified). |
| SCORES(SERVER/TOOL/FINAL) | 0.386/0.584/0.132 | 0.476/0.686/0.224 |
| RANKS(SERVER/TOOL/FINAL) | 36/33/33 | 6/1/1 |
## ANALYSIS

# BAD CASE 242
## TASK
List all available groups with their details.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ServiceNow | OpenCTI |
| TOOL | list_groups | list_groups |
| DESC | List groups with filtering options | Lists all groups with their members. |
| PARAMETERS |  | first: (Optional, number) Number of groups to retrieve, defaults to 10 |
| SCORES(SERVER/TOOL/FINAL) | 0.312/0.498/0.077 | 0.420/0.883/0.327 |
| RANKS(SERVER/TOOL/FINAL) | 166/439/653 | 36/2/1 |
## ANALYSIS

# BAD CASE 243
## TASK
Update all documents in the MongoDB collection where the "status" field is set to "pending" and change it to "processed".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | MongoDB | Couchbase |
| TOOL | update-many | upsert_document_by_id |
| DESC | Update multiple documents in a MongoDB collection | Upsert a document by ID to a specified scope and collection. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.289/0.559/0.090 | 0.422/0.667/0.188 |
| RANKS(SERVER/TOOL/FINAL) | 96/11/46 | 6/1/1 |
## ANALYSIS

# BAD CASE 244
## TASK
Retrieve the details of the task with ID "TASK-12345" or, if not found, search for a task named "Q2 Marketing Campaign" using smart disambiguation.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ClickUp | Todoist |
| TOOL | get_task | todoist_update_task |
| DESC | Get single task details | Update existing tasks using natural language search. |
| PARAMETERS | taskId: (string) The ID of the task to get<br>taskName: (Optional, string) The name of the task to get (with smart disambiguation) | task name: (string) partial name match to find the task<br>content: (Optional, string) new task title<br>description: (Optional, string) new task description<br>due date: (Optional, string) new due date<br>priority: (Optional, number) new priority level (1-4) |
| SCORES(SERVER/TOOL/FINAL) | 0.227/0.651/0.096 | 0.585/0.795/0.370 |
| RANKS(SERVER/TOOL/FINAL) | 281/45/629 | 4/2/1 |
## ANALYSIS

# BAD CASE 245
## TASK
Remove the tag "urgent" from the task with ID "TSK12345" in the "Project X" list.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ClickUp | Todoist |
| TOOL | remove_tag_from_task | todoist_delete_task |
| DESC | Remove tag from task | Remove tasks using natural language search. |
| PARAMETERS | tagName: (string) The name of the tag to remove<br>taskId: (string) The ID of the task to remove the tag from<br>taskName: (Optional, string) The name of the task to remove the tag from<br>listName: (Optional, string) The name of the list containing the task | task name: (string) partial name match to find the task |
| SCORES(SERVER/TOOL/FINAL) | 0.196/0.642/0.081 | 0.594/0.731/0.317 |
| RANKS(SERVER/TOOL/FINAL) | 275/8/237 | 1/1/1 |
## ANALYSIS

# BAD CASE 246
## TASK
Execute the action "send_email" with the parameters {"recipient": "john.doe@example.com", "subject": "Project Update", "body": "Please find the latest project updates attached."}.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Home Assistant | Gmail |
| TOOL | execute_action | send_email |
| DESC | Executes a specified action with given parameters. | Sends a new email immediately. |
| PARAMETERS | action: (string) The action to execute<br>parameters: (object) Parameters for the action | to: (array) List of recipient email addresses<br>subject: (string) Subject of the email<br>body: (string) Body content of the email<br>cc: (Optional, array) List of CC recipient email addresses<br>bcc: (Optional, array) List of BCC recipient email addresses |
| SCORES(SERVER/TOOL/FINAL) | 0.337/0.550/0.102 | 0.542/0.804/0.350 |
| RANKS(SERVER/TOOL/FINAL) | 38/24/29 | 1/2/1 |
## ANALYSIS

# BAD CASE 248
## TASK
Delete 50 inactive user nodes from the database in a single operation.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Talk To Figma | MongoDB Lens |
| TOOL | delete_multiple_nodes | drop-user |
| DESC | Delete multiple nodes at once efficiently | Remove database users (requires confirmation) |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.311/0.581/0.105 | 0.420/0.720/0.217 |
| RANKS(SERVER/TOOL/FINAL) | 138/65/204 | 17/1/1 |
## ANALYSIS

# BAD CASE 249
## TASK
Display the current working directory path in the workspace.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | PIF | Terminal-Control |
| TOOL | pwd | get_current_directory |
| DESC | Navigate and manage workspace context | Get the current working directory. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.398/0.429/0.073 | 0.505/0.759/0.291 |
| RANKS(SERVER/TOOL/FINAL) | 20/348/187 | 2/1/1 |
## ANALYSIS

# BAD CASE 250
## TASK
Create a copy of the task with ID "TSK123" and move it to the target list with ID "LST456".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ClickUp | Todoist |
| TOOL | duplicate_task | todoist_update_task |
| DESC | Copy task | Update existing tasks using natural language search. |
| PARAMETERS | taskId: (string) The ID of the task to duplicate<br>taskName: (Optional, string) The name of the task to duplicate<br>listId: (string) The ID of the target list<br>listName: (Optional, string) The name of the target list | task name: (string) partial name match to find the task<br>content: (Optional, string) new task title<br>description: (Optional, string) new task description<br>due date: (Optional, string) new due date<br>priority: (Optional, number) new priority level (1-4) |
| SCORES(SERVER/TOOL/FINAL) | 0.223/0.586/0.077 | 0.557/0.719/0.288 |
| RANKS(SERVER/TOOL/FINAL) | 262/19/312 | 1/1/1 |
## ANALYSIS

# BAD CASE 251
## TASK
Update the page titled "Project Timeline" in document ID "DOC123" within workspace "WS456" to include the subtitle "Q2 2024 Milestones" and formatted content detailing the key deliverables for April to June. Use markdown format for the content.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ClickUp | DaVinci Resolve |
| TOOL | update_document_page | create_new_timeline |
| DESC | Update a document page | Creates a new timeline in the current project. |
| PARAMETERS | workspaceId: (string) The ID of the workspace<br>documentId: (string) The ID of the document<br>name: (string) The name of the page<br>sub_title: (Optional, string) The subtitle of the page<br>content: (string) The content of the page<br>content_edit_mode: (Optional, string) The edit mode of the content<br>content_format: (Optional, string) The format of the content | timeline_name: (string) The name of the new timeline. |
| SCORES(SERVER/TOOL/FINAL) | 0.370/0.406/0.061 | 0.415/0.569/0.134 |
| RANKS(SERVER/TOOL/FINAL) | 35/226/200 | 10/1/1 |
## ANALYSIS

# BAD CASE 253
## TASK
Create a new frame positioned at coordinates (100, 200) with a width of 300 pixels and a height of 400 pixels, and label it "Main Display".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Talk To Figma | DaVinci Resolve |
| TOOL | create_frame | create_new_project |
| DESC | Create a new frame with position, size, and optional name | Creates a new project in DaVinci Resolve. |
| PARAMETERS |  | project_name: (string) The name of the new project. |
| SCORES(SERVER/TOOL/FINAL) | 0.398/0.419/0.070 | 0.480/0.559/0.150 |
| RANKS(SERVER/TOOL/FINAL) | 5/134/69 | 1/5/1 |
## ANALYSIS

# BAD CASE 254
## TASK
Retrieve the detailed statistics and performance metrics for the latest completed match.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | OpenDota | TFT-Match-Analyzer |
| TOOL | get_match_data | tft_match_details |
| DESC | Get detailed data for a specific match | Get detailed information about a specific TFT match. |
| PARAMETERS |  | matchId: (required, string) The match ID to get details for |
| SCORES(SERVER/TOOL/FINAL) | 0.566/0.570/0.184 | 0.581/0.777/0.350 |
| RANKS(SERVER/TOOL/FINAL) | 2/28/8 | 1/3/1 |
## ANALYSIS

# BAD CASE 255
## TASK
List all values for the 'instance' label in the Prometheus monitoring system.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Grafana | OpenCTI |
| TOOL | list_prometheus_label_values | list_labels |
| DESC | List values for a specific label | Lists all available labels. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.385/0.425/0.070 | 0.473/0.672/0.214 |
| RANKS(SERVER/TOOL/FINAL) | 63/814/620 | 7/3/1 |
## ANALYSIS

# BAD CASE 256
## TASK
Find nearby restaurants within a 5-mile radius of the current user location.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | AWS | Unstructured |
| TOOL | Search for Places Near a Location | list_destinations |
| DESC | Search for places near a specified location. | Lists available destinations from the Unstructured API. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.295/0.832/0.204 | 0.533/0.634/0.214 |
| RANKS(SERVER/TOOL/FINAL) | 182/1/4 | 1/19/1 |
## ANALYSIS

# BAD CASE 257
## TASK
Delete the Essential subscription with the ID 'ESS123456789'.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Redis Cloud API | Stripe |
| TOOL | delete_essential_subscription | cancelSubscription |
| DESC | Delete an Essential subscription | Cancels an existing subscription in Stripe. |
| PARAMETERS | subscription_id: (string) ID of the Essential subscription to delete | subscription: (string) The ID of the subscription to cancel. |
| SCORES(SERVER/TOOL/FINAL) | 0.367/0.593/0.129 | 0.350/0.773/0.209 |
| RANKS(SERVER/TOOL/FINAL) | 22/22/24 | 28/1/1 |
## ANALYSIS

# BAD CASE 258
## TASK
Retrieve the current price-to-earnings ratio and debt-to-equity ratio for Apple Inc. using natural language query.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Octagon | Financial Datasets |
| TOOL | octagon-financials-agent | get_current_stock_price |
| DESC | Retrieve financial metrics and ratios. | Get the current / latest price of a company. |
| PARAMETERS | prompt: (string) A natural language query specifying the financial metrics or ratios to retrieve. |  |
| SCORES(SERVER/TOOL/FINAL) | 0.399/0.803/0.257 | 0.609/0.791/0.381 |
| RANKS(SERVER/TOOL/FINAL) | 20/1/7 | 1/2/1 |
## ANALYSIS

# BAD CASE 260
## TASK
Search for all available dashboards in the system.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Grafana | Graphlit |
| TOOL | search_dashboards | List Notion Databases |
| DESC | Search for dashboards | Lists available databases in Notion. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.341/0.616/0.129 | 0.479/0.720/0.248 |
| RANKS(SERVER/TOOL/FINAL) | 102/66/129 | 6/2/1 |
## ANALYSIS

# BAD CASE 261
## TASK
Check the schedule for upcoming blank gameweeks in the current season.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Fantasy PL | SoccerDataAPI |
| TOOL | get_blank_gameweeks | get_livescores |
| DESC | Get information about upcoming blank gameweeks | Returns real-time information about ongoing football matches around the world. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.451/0.611/0.168 | 0.449/0.693/0.215 |
| RANKS(SERVER/TOOL/FINAL) | 3/3/2 | 4/1/1 |
## ANALYSIS

# BAD CASE 262
## TASK
List all available workflows from the Unstructured API.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Unstructured | n8n |
| TOOL | list_workflows | workflow_list |
| DESC | Lists workflows from the Unstructured API. | Lists all workflows. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.712/0.901/0.578 | 0.753/0.902/0.613 |
| RANKS(SERVER/TOOL/FINAL) | 2/3/3 | 1/2/1 |
## ANALYSIS

# BAD CASE 265
## TASK
Update the description of the field with ID 'fld123' in table 'tbl456' of Airtable base 'app789' to "Updated field description for customer records".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Airtable | Keboola |
| TOOL | update_field | update_table_description |
| DESC | Updates a field's name or description | Update the description for a given Keboola table. |
| PARAMETERS | baseId: (string, required) The ID of the Airtable base<br>tableId: (string, required) The ID of the table<br>fieldId: (string, required) The ID of the field<br>name: (string, optional) New name for the field<br>description: (string, optional) New description for the field |  |
| SCORES(SERVER/TOOL/FINAL) | 0.504/0.507/0.130 | 0.407/0.802/0.262 |
| RANKS(SERVER/TOOL/FINAL) | 6/82/19 | 38/1/1 |
## ANALYSIS

# BAD CASE 266
## TASK
Retrieve the list of fields along with their data types for the 'User' object type in the GraphQL schema.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | GraphQL Schema | Fibery |
| TOOL | get-type-fields | describe_database |
| DESC | Gets a simplified list of fields with their types for a specific GraphQL object type | Provides a detailed breakdown of a specific database's structure, showing all fields with their titles, names, and types. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.317/0.592/0.111 | 0.439/0.628/0.173 |
| RANKS(SERVER/TOOL/FINAL) | 114/9/22 | 8/3/1 |
## ANALYSIS

# BAD CASE 267
## TASK
Remove the 'customer_data' collection from the connected MongoDB database.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | MongoDB | MongoDB Lens |
| TOOL | drop-collection | drop-collection |
| DESC | Remove a collection from a MongoDB database | Remove collections from the database (requires confirmation) |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.363/0.608/0.134 | 0.435/0.685/0.204 |
| RANKS(SERVER/TOOL/FINAL) | 21/7/17 | 3/2/1 |
## ANALYSIS

# BAD CASE 269
## TASK
Generate OpenTelemetry traces with Phoenix-aware default configurations.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Arize Phoenix | oatpp-mcp |
| TOOL | arize-phoenix-otel | Logger |
| DESC | Provides a lightweight wrapper around OpenTelemetry primitives with Phoenix-aware defaults | A tool for logging purposes. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.470/0.467/0.103 | 0.458/0.577/0.153 |
| RANKS(SERVER/TOOL/FINAL) | 2/183/21 | 5/3/1 |
## ANALYSIS

# BAD CASE 270
## TASK
Update the existing script include named "UserUtils" in ServiceNow to include a new function for validating email addresses.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ServiceNow | Gmail |
| TOOL | update_script_include | search_emails |
| DESC | Update an existing script include in ServiceNow | Searches for emails using Gmail search syntax. |
| PARAMETERS |  | query: (string) Gmail search query<br>maxResults: (Optional, integer) Maximum number of results to return |
| SCORES(SERVER/TOOL/FINAL) | 0.351/0.498/0.087 | 0.471/0.590/0.164 |
| RANKS(SERVER/TOOL/FINAL) | 70/78/144 | 4/5/1 |
## ANALYSIS

# BAD CASE 272
## TASK
List all files that have been modified since the last time the context was generated.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | llm-context | Terminal-Control |
| TOOL | lc-changed | list_directory |
| DESC | List files modified since last context generation | List files and subdirectories in the specified directory. |
| PARAMETERS |  | path: (Optional, string) Directory path to list contents (default: current directory) |
| SCORES(SERVER/TOOL/FINAL) | 0.386/0.613/0.145 | 0.453/0.587/0.156 |
| RANKS(SERVER/TOOL/FINAL) | 20/5/3 | 4/9/1 |
## ANALYSIS

# BAD CASE 273
## TASK
Retrieve the performance metrics data for the last 30 days in time-series format.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Raygun | Aranet4 |
| TOOL | get_page_metrics_time_series | get_recent_data |
| DESC | Get time-series performance metrics | Get recent data from the local database. Can specify the number of measurements. |
| PARAMETERS |  | measurements: (Optional, int) Number of recent measurements to retrieve. |
| SCORES(SERVER/TOOL/FINAL) | 0.362/0.566/0.116 | 0.531/0.680/0.245 |
| RANKS(SERVER/TOOL/FINAL) | 98/102/168 | 3/4/1 |
## ANALYSIS

# BAD CASE 274
## TASK
List all currently stored Hyperbrowser profiles.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Hyperbrowser | Hyperbrowser |
| TOOL | list_profiles | list_profiles |
| DESC | Lists existing persistent Hyperbrowser profiles | Lists existing persistent Hyperbrowser profiles |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.592/0.622/0.229 | 0.592/0.622/0.229 |
| RANKS(SERVER/TOOL/FINAL) | 2/41/1 | 2/41/1 |
## ANALYSIS

# BAD CASE 275
## TASK
Select the game object with the path "Player/Weapons/Sword" in the Unity hierarchy.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Unity3d Game Engine | Unity Integration (Advanced) |
| TOOL | select_gameobject | find_assets_by_type |
| DESC | Selects game objects in the Unity hierarchy by path or instance ID | Find all assets of a specific type (e.g., Material, Prefab) |
| PARAMETERS | pathOrId: (string) The path or instance ID of the game object to select | assetType: (string) Type of asset to find |
| SCORES(SERVER/TOOL/FINAL) | 0.405/0.411/0.068 | 0.374/0.605/0.137 |
| RANKS(SERVER/TOOL/FINAL) | 1/51/28 | 10/1/1 |
## ANALYSIS

# BAD CASE 276
## TASK
Create a new file at "/documents/report.txt" with the content "Quarterly sales report for Q2 2024: $1.2M revenue."
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Golang Filesystem Server | Terminal-Control |
| TOOL | write_file | insert_file_content |
| DESC | Create new file or overwrite existing | Insert content at specific row(s) in a file. |
| PARAMETERS | path: (string) File location<br>content: (string) File content | path: (string) Path to the file<br>content: (string) Content to insert<br>row: (Optional, int) Row number to insert at (0-based)<br>rows: (Optional, list) List of row numbers to insert at (0-based) |
| SCORES(SERVER/TOOL/FINAL) | 0.248/0.557/0.077 | 0.485/0.621/0.187 |
| RANKS(SERVER/TOOL/FINAL) | 216/12/64 | 3/2/1 |
## ANALYSIS

# BAD CASE 277
## TASK
Create a new documentation page in the team's knowledge base with the title "Project Onboarding Guide" and include sections for setup instructions, common issues, and contact information.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Atlassian | Basic Memory |
| TOOL | confluence_create_page | write_note |
| DESC | Create a new page | Create or update notes in the knowledge base. |
| PARAMETERS |  | title: (string) The title of the note<br>content: (string) The content of the note<br>folder: (string) The folder where the note should be saved<br>tags: (array) Tags to associate with the note |
| SCORES(SERVER/TOOL/FINAL) | 0.639/0.405/0.165 | 0.440/0.706/0.219 |
| RANKS(SERVER/TOOL/FINAL) | 1/572/5 | 19/1/1 |
## ANALYSIS

# BAD CASE 278
## TASK
Check the details of the currently active timer.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ClickUp | DaVinci Resolve |
| TOOL | get_current_time_entry | get_current_timeline_info |
| DESC | Get currently running timer | Gets information about the current timeline. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.200/0.637/0.081 | 0.372/0.710/0.188 |
| RANKS(SERVER/TOOL/FINAL) | 281/2/172 | 35/1/1 |
## ANALYSIS

# BAD CASE 280
## TASK
Retrieve the most recent market data for all available cryptocurrency exchanges.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | CoinMarketCap | coin_api_mcp |
| TOOL | exchangeListingsLatest | get-coin-quotes |
| DESC | Get latest market data for all exchanges | Fetches the latest market quotes for one or more cryptocurrencies. |
| PARAMETERS |  | id: (string, optional) One or more comma-separated cryptocurrency CoinMarketCap IDs.<br>slug: (string, optional) A comma-separated list of cryptocurrency slugs.<br>symbol: (string, optional) One or more comma-separated cryptocurrency symbols. |
| SCORES(SERVER/TOOL/FINAL) | 0.499/0.553/0.153 | 0.630/0.849/0.454 |
| RANKS(SERVER/TOOL/FINAL) | 6/84/53 | 2/1/1 |
## ANALYSIS

# BAD CASE 281
## TASK
Store a large video file (over 16MB) in the GridFS bucket for efficient management.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | MongoDB Lens | Cloudinary |
| TOOL | gridfs-operation | upload |
| DESC | Manage large files with GridFS buckets | Upload images and videos to Cloudinary. |
| PARAMETERS |  | file: (required) Path to file, URL, or base64 data URI to upload<br>resource_type: (optional) Type of resource ('image', 'video', or 'raw')<br>public_id: (optional) Custom public ID for the uploaded asset<br>overwrite: (optional) Whether to overwrite existing assets with the same public ID<br>tags: (optional) Array of tags to assign to the uploaded asset |
| SCORES(SERVER/TOOL/FINAL) | 0.339/0.519/0.091 | 0.502/0.741/0.276 |
| RANKS(SERVER/TOOL/FINAL) | 44/58/42 | 1/2/1 |
## ANALYSIS

# BAD CASE 282
## TASK
Push three configuration files (config.json, settings.yaml, and env.properties) to the "main" branch of the "project-x" repository under the owner "dev-team" with the commit message "Update configuration files".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | GitHub | Git |
| TOOL | push_files | git_push |
| DESC | Push multiple files in a single commit | Pushes local commits to a remote repository (requires --write-access flag) |
| PARAMETERS | owner: (string) Repository owner<br>repo: (string) Repository name<br>branch: (string) Branch to push to<br>files: (array) Files to push, each with `path` and `content`<br>message: (string) Commit message |  |
| SCORES(SERVER/TOOL/FINAL) | 0.429/0.543/0.126 | 0.463/0.684/0.217 |
| RANKS(SERVER/TOOL/FINAL) | 7/14/32 | 3/1/1 |
## ANALYSIS

# BAD CASE 283
## TASK
Search for the latest research papers on quantum computing published in the last month, displaying results in English with moderate safe search filtering.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | SearXNG | Scholarly |
| TOOL | searxng_web_search | search-arxiv |
| DESC | Execute web searches with pagination | Search arXiv for articles related to the given keyword. |
| PARAMETERS | query: (string) The search query. This string is passed to external search services.<br>pageno: (Optional, number) Search page number, starts at 1 (default 1)<br>time_range: (Optional, string) Filter results by time range - one of: 'day', 'month', 'year' (default: none)<br>language: (Optional, string) Language code for results (e.g., 'en', 'fr', 'de') or 'all' (default: 'all')<br>safesearch: (Optional, number) Safe search filter level (0: None, 1: Moderate, 2: Strict) (default: instance setting) | keyword: (string) The keyword to search for. |
| SCORES(SERVER/TOOL/FINAL) | 0.282/0.403/0.046 | 0.505/0.814/0.335 |
| RANKS(SERVER/TOOL/FINAL) | 158/591/648 | 3/3/1 |
## ANALYSIS

# BAD CASE 285
## TASK
Create a new payment transaction for the latest invoice.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Xero | Stripe |
| TOOL | create-payment | createInvoice |
| DESC | Create a new payment | Creates a new invoice in Stripe. |
| PARAMETERS |  | customer: (string) The ID of the customer to create the invoice for.<br>lines: (array) An array of line items to include in the invoice. |
| SCORES(SERVER/TOOL/FINAL) | 0.401/0.494/0.098 | 0.440/0.821/0.297 |
| RANKS(SERVER/TOOL/FINAL) | 10/100/69 | 3/1/1 |
## ANALYSIS

# BAD CASE 286
## TASK
Retrieve the second page of messages from chat ID 12345, displaying 20 messages per page.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Telegram | Discord |
| TOOL | get_messages | read-messages |
| DESC | Get paginated messages. | Reads recent messages from a specified Discord channel. |
| PARAMETERS | chat_id: (int) ID of the chat<br>page: (int) Page number (1-indexed)<br>page_size: (int) Number of messages per page | server: (Optional, string) Server name or ID (required if bot is in multiple servers)<br>channel: (string) Channel name (e.g., 'general') or ID<br>limit: (Optional, number) Number of messages to fetch (default: 50, max: 100) |
| SCORES(SERVER/TOOL/FINAL) | 0.391/0.832/0.271 | 0.515/0.791/0.322 |
| RANKS(SERVER/TOOL/FINAL) | 32/3/6 | 4/8/1 |
## ANALYSIS

# BAD CASE 287
## TASK
Search for records containing the term "urgent" in the "tasks" table of Airtable base "project_management", limiting results to 50 records and focusing only on the "description" and "notes" fields.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Airtable | Todoist |
| TOOL | search_records | todoist_get_tasks |
| DESC | Search for records containing specific text | Retrieve and filter tasks. |
| PARAMETERS | baseId: (string, required) The ID of the Airtable base<br>tableId: (string, required) The ID of the table to query<br>searchTerm: (string, required) Text to search for in records<br>fieldIds: (array, optional) Specific field IDs to search in. If not provided, searches all text-based fields.<br>maxRecords: (number, optional) Maximum number of records to return. Defaults to 100. | due date: (Optional, string) filter by due date<br>priority: (Optional, number) filter by priority<br>project: (Optional, string) filter by project<br>result limit: (Optional, number) limit the number of results |
| SCORES(SERVER/TOOL/FINAL) | 0.433/0.439/0.083 | 0.526/0.726/0.277 |
| RANKS(SERVER/TOOL/FINAL) | 25/627/362 | 4/1/1 |
## ANALYSIS

# BAD CASE 288
## TASK
Stop the currently running time tracking session.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ClickUp | n8n |
| TOOL | stop_time_tracking | execution_stop |
| DESC | Stop current time tracking | Stops a running execution. |
| PARAMETERS |  | id: (string) The ID of the execution to stop |
| SCORES(SERVER/TOOL/FINAL) | 0.161/0.560/0.050 | 0.366/0.695/0.177 |
| RANKS(SERVER/TOOL/FINAL) | 279/11/217 | 9/1/1 |
## ANALYSIS

# BAD CASE 289
## TASK
Retrieve the details of the application associated with the provided API key.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Raygun | Heroku |
| TOOL | get_application_by_api_key | get_app_info |
| DESC | Get application details by API key | Get detailed information about an app, including its configuration, dynos, and add-ons. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.472/0.602/0.171 | 0.565/0.842/0.401 |
| RANKS(SERVER/TOOL/FINAL) | 17/94/47 | 2/1/1 |
## ANALYSIS

# BAD CASE 292
## TASK
List all the available connection aliases for the MongoDB database.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | MongoDB Lens | DBHub |
| TOOL | list-connections | list_connectors |
| DESC | View all available MongoDB connection aliases | Lists available connectors for database connections. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.431/0.624/0.168 | 0.420/0.724/0.220 |
| RANKS(SERVER/TOOL/FINAL) | 4/19/8 | 9/1/1 |
## ANALYSIS

# BAD CASE 293
## TASK
Retrieve the details of the import error with ID "ERR-2024-0015".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Airflow | Airflow |
| TOOL | Get Import Error Details | Get Import Error Details |
| DESC | Gets details of a specific import error. | Gets details of a specific import error. |
| PARAMETERS | import_error_id: (string) The ID of the import error. | import_error_id: (string) The ID of the import error. |
| SCORES(SERVER/TOOL/FINAL) | 0.345/0.929/0.298 | 0.345/0.929/0.298 |
| RANKS(SERVER/TOOL/FINAL) | 140/1/1 | 140/1/1 |
## ANALYSIS

# BAD CASE 294
## TASK
Insert a new document containing user details (name, email, and registration date) into the specified MongoDB collection.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | MongoDB | Descope |
| TOOL | insert-one | create-user |
| DESC | Insert a single document into a MongoDB collection | Creates a new user in your Descope project. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.334/0.521/0.090 | 0.467/0.692/0.224 |
| RANKS(SERVER/TOOL/FINAL) | 45/42/38 | 3/2/1 |
## ANALYSIS

# BAD CASE 295
## TASK
Create a new translation memory named "Technical Manuals EN-FR" with the external ID "ext_my_12345" imported from MyMemory.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Lara Translate | Rember |
| TOOL | create_memory | create_flashcards |
| DESC | Create a new translation memory | Creates flashcards with AI by taking a list of notes from Claude and generating a few flashcards for each note using the Rember API. |
| PARAMETERS | name: (string) Name of the new memory<br>external_id: (Optional, string) ID of the memory to import from MyMemory (e.g., 'ext_my_[MyMemory ID]') | notes: (list of strings) A list of notes from Claude to generate flashcards from. |
| SCORES(SERVER/TOOL/FINAL) | 0.438/0.664/0.194 | 0.543/0.688/0.257 |
| RANKS(SERVER/TOOL/FINAL) | 22/8/5 | 3/5/1 |
## ANALYSIS

# BAD CASE 297
## TASK
Retrieve the complete list of all available cryptocurrencies along with their respective symbols and identifiers.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | CoinMarketCap | coin_api_mcp |
| TOOL | cryptoCurrencyMap | listing-coins |
| DESC | Get mapping of all cryptocurrencies | Fetches a paginated list of all active cryptocurrencies with the latest market data. |
| PARAMETERS |  | start: (integer, optional) Offset the start (1-based index) of the paginated list of items to return.<br>limit: (integer, optional) Number of results to return (default: 10, max: 5000).<br>price_min: (number, optional) Minimum USD price to filter results.<br>price_max: (number, optional) Maximum USD price to filter results.<br>market_cap_min: (number, optional) Minimum market cap to filter results.<br>market_cap_max: (number, optional) Maximum market cap to filter results.<br>convert: (string, optional) Calculate market quotes in multiple currencies.<br>sort: (string, optional) Field to sort the list of cryptocurrencies by.<br>sort_dir: (string, optional) Direction to order cryptocurrencies (asc or desc). |
| SCORES(SERVER/TOOL/FINAL) | 0.485/0.701/0.239 | 0.654/0.834/0.454 |
| RANKS(SERVER/TOOL/FINAL) | 5/7/11 | 1/1/1 |
## ANALYSIS

# BAD CASE 298
## TASK
Connect to a MongoDB database using a new URI provided by the user.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | MongoDB Lens | DevDb |
| TOOL | connect-mongodb | URI Handler |
| DESC | Connect to a different MongoDB URI | Enables opening specific database tables directly from external applications or links. |
| PARAMETERS |  | connectionId: (string) The ID of the database connection<br>database: (string) The database name<br>table: (string) The table name to open<br>workspace: (Optional, string) The workspace path<br>authority: (Optional, string) The authority for the URI |
| SCORES(SERVER/TOOL/FINAL) | 0.503/0.533/0.143 | 0.458/0.688/0.217 |
| RANKS(SERVER/TOOL/FINAL) | 3/114/30 | 11/1/1 |
## ANALYSIS

# BAD CASE 299
## TASK
Revoke the pending invitation sent to the user with the email address "example@domain.com".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Raygun | Ghost |
| TOOL | revoke_invitation | Delete Invite |
| DESC | Revoke a pending invitation | Remove an invite. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.492/0.684/0.230 | 0.370/0.851/0.267 |
| RANKS(SERVER/TOOL/FINAL) | 3/9/4 | 41/1/1 |
## ANALYSIS

# BAD CASE 300
## TASK
Create a new knowledge article in the ServiceNow platform with the title "How to Reset Your Password" and include step-by-step instructions for users.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ServiceNow | Basic Memory |
| TOOL | create_article | write_note |
| DESC | Create a new knowledge article in ServiceNow | Create or update notes in the knowledge base. |
| PARAMETERS |  | title: (string) The title of the note<br>content: (string) The content of the note<br>folder: (string) The folder where the note should be saved<br>tags: (array) Tags to associate with the note |
| SCORES(SERVER/TOOL/FINAL) | 0.319/0.620/0.123 | 0.473/0.767/0.278 |
| RANKS(SERVER/TOOL/FINAL) | 139/12/44 | 10/1/1 |
## ANALYSIS

# BAD CASE 301
## TASK
Prepare a temporary branch for testing database schema changes before applying them to the main branch.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Neon | Neon |
| TOOL | prepare_database_migration | prepare_database_migration |
| DESC | Initiates a database migration process. Creates a temporary branch to apply and test the migration safely before affecting the main branch. | Initiates a database migration process. Creates a temporary branch to apply and test the migration safely before affecting the main branch. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.305/0.847/0.218 | 0.305/0.847/0.218 |
| RANKS(SERVER/TOOL/FINAL) | 105/1/1 | 105/1/1 |
## ANALYSIS

# BAD CASE 302
## TASK
Create a continuous payment stream between two Ethereum wallet addresses using Superfluid.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | GOAT | GOAT |
| TOOL | Create streams with Superfluid | Create liquidity pools on Meteora |
| DESC | Facilitates the creation of streams using Superfluid. | Enables the creation of liquidity pools on Meteora. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.651/0.701/0.319 | 0.651/0.760/0.376 |
| RANKS(SERVER/TOOL/FINAL) | 1/13/12 | 1/1/1 |
## ANALYSIS

# BAD CASE 304
## TASK
Transfer 5 ERC1155 tokens with ID "12345" from the owner's wallet to the recipient's address "0x123...abc" on the Ethereum mainnet.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | EVM MCP Server | GOAT |
| TOOL | transfer-erc1155 | Cross-chain token swap using Mayan SDK |
| DESC | Transfer ERC1155 tokens | Facilitates cross-chain token swaps using the Mayan SDK. |
| PARAMETERS | privateKey: (string) The private key of the owner<br>tokenAddress: (address/ENS) The address or ENS name of the ERC1155 token<br>tokenId: (string) The token ID<br>amount: (number) The amount of tokens to transfer<br>toAddress: (address/ENS) The address or ENS name of the recipient<br>network: (string) The network identifier |  |
| SCORES(SERVER/TOOL/FINAL) | 0.311/0.576/0.103 | 0.640/0.724/0.336 |
| RANKS(SERVER/TOOL/FINAL) | 94/58/120 | 1/2/1 |
## ANALYSIS

# BAD CASE 306
## TASK
List all files and subfolders within the folder with ID "F12345" recursively.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Box | Graphlit |
| TOOL | box_list_folder_content_by_folder_id | List SharePoint Folders |
| DESC | List folder contents. | Lists available folders within a SharePoint library. |
| PARAMETERS | folder_id: (str) ID of the folder<br>is_recursive: (bool) Whether to list recursively |  |
| SCORES(SERVER/TOOL/FINAL) | 0.300/0.788/0.186 | 0.419/0.776/0.252 |
| RANKS(SERVER/TOOL/FINAL) | 146/1/3 | 9/2/1 |
## ANALYSIS

# BAD CASE 307
## TASK
Calculate the most efficient route from the city center to the airport, including detailed turn-by-turn directions.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | AWS | NS Travel Information |
| TOOL | Calculate Routes Between Locations | Journey Planning |
| DESC | Calculate routes between locations with turn-by-turn directions. | Finds optimal travel routes with transfers and real-time updates. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.323/0.953/0.294 | 0.440/0.905/0.360 |
| RANKS(SERVER/TOOL/FINAL) | 154/1/2 | 19/2/1 |
## ANALYSIS

# BAD CASE 308
## TASK
Update the description of the table with ID 'tbl123' in the Airtable base 'app456' to "2024 customer contact information".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Airtable | Keboola |
| TOOL | update_table | update_table_description |
| DESC | Updates a table's name or description | Update the description for a given Keboola table. |
| PARAMETERS | baseId: (string, required) The ID of the Airtable base<br>tableId: (string, required) The ID of the table<br>name: (string, optional) New name for the table<br>description: (string, optional) New description for the table |  |
| SCORES(SERVER/TOOL/FINAL) | 0.531/0.497/0.140 | 0.389/0.771/0.231 |
| RANKS(SERVER/TOOL/FINAL) | 2/114/10 | 54/1/1 |
## ANALYSIS

# BAD CASE 309
## TASK
Stop the currently active real-time journey.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Virtual location (Google Street View,etc.) | Virtual location (Google Street View,etc.) |
| TOOL | stop_traveler_journey | stop_traveler_journey |
| DESC | Stops the journey (moveMode=realtime only). | Stops the journey (moveMode=realtime only). |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.304/0.875/0.233 | 0.304/0.875/0.233 |
| RANKS(SERVER/TOOL/FINAL) | 141/1/1 | 141/1/1 |
## ANALYSIS

# BAD CASE 310
## TASK
Ignore all error groups in the system to prevent further alerts.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Raygun | Heroku |
| TOOL | ignore_error_group | ps_restart |
| DESC | Set error group status to ignored | Restart specific dynos, process types, or all dynos. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.372/0.499/0.093 | 0.374/0.583/0.127 |
| RANKS(SERVER/TOOL/FINAL) | 10/41/14 | 9/2/1 |
## ANALYSIS

# BAD CASE 311
## TASK
Add a comment with the text "Please review the attached documents by EOD" to the task with ID "TASK12345" in the "Project Review" list.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ClickUp | Linear |
| TOOL | create_task_comment | linear_add_comment |
| DESC | Add a comment to a task | Add a comment to a Linear issue. |
| PARAMETERS | commentText: (string) The text of the comment<br>taskId: (string) The ID of the task to add the comment to<br>taskName: (Optional, string) The name of the task to add the comment to<br>listName: (Optional, string) The name of the list containing the task | issueId: (string) Issue ID to comment on<br>body: (string) Comment text (markdown supported)<br>createAsUser: (Optional, string) Custom username<br>displayIconUrl: (Optional, string) Custom avatar URL |
| SCORES(SERVER/TOOL/FINAL) | 0.333/0.644/0.138 | 0.520/0.803/0.335 |
| RANKS(SERVER/TOOL/FINAL) | 114/8/41 | 3/2/1 |
## ANALYSIS

# BAD CASE 312
## TASK
Check the balance of the ERC20 token at address 0x123...abc for the owner with address 0x456...def on the Ethereum mainnet.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | EVM MCP Server | GOAT |
| TOOL | get-token-balance | Get the balances of a wallet using 1inch API |
| DESC | Check ERC20 token balance | Retrieves the balances of a wallet using the 1inch API. |
| PARAMETERS | tokenAddress: (address/ENS) The address or ENS name of the token<br>ownerAddress: (address/ENS) The address or ENS name of the owner<br>network: (string) The network identifier |  |
| SCORES(SERVER/TOOL/FINAL) | 0.410/0.621/0.158 | 0.688/0.786/0.425 |
| RANKS(SERVER/TOOL/FINAL) | 17/25/64 | 1/1/1 |
## ANALYSIS

# BAD CASE 313
## TASK
List all roles assigned to the group for the Bitrise app with the identifier "my_app_slug".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Bitrise | Heroku |
| TOOL | list_group_roles | list_apps |
| DESC | List group roles for an app | List all Heroku apps. You can filter apps by personal, collaborator, team, or space. |
| PARAMETERS | app_slug: (string) Identifier of the Bitrise app<br>role_name: (string) Name of the role |  |
| SCORES(SERVER/TOOL/FINAL) | 0.624/0.510/0.199 | 0.491/0.720/0.255 |
| RANKS(SERVER/TOOL/FINAL) | 2/378/22 | 16/3/1 |
## ANALYSIS

# BAD CASE 314
## TASK
Apply the extracted configuration overrides to the specified target instances.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Talk To Figma | code-executor |
| TOOL | set_instance_overrides | configure_environment |
| DESC | Apply extracted overrides to target instances | Dynamically changes the environment configuration. |
| PARAMETERS |  | type: (string) The type of environment (e.g., 'conda', 'venv')<br>conda_name: (string) The name of the Conda environment to use (if applicable) |
| SCORES(SERVER/TOOL/FINAL) | 0.278/0.564/0.088 | 0.356/0.652/0.151 |
| RANKS(SERVER/TOOL/FINAL) | 118/11/49 | 18/1/1 |
## ANALYSIS

# BAD CASE 315
## TASK
Create a new Essential subscription for the user account.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Redis Cloud API | Redis Cloud API |
| TOOL | create_essential_subscription | get_essentials_plans |
| DESC | Create a new Essential subscription | List available Essential subscription plans (paginated) |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.396/0.620/0.152 | 0.396/0.741/0.217 |
| RANKS(SERVER/TOOL/FINAL) | 14/18/17 | 14/1/1 |
## ANALYSIS

# BAD CASE 316
## TASK
Retrieve all comments associated with the latest published post.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | CoinMarketCap | Discourse |
| TOOL | contentPostsComments | search_posts |
| DESC | Get comments for a specific post | Searches posts on a Discourse forum. |
| PARAMETERS |  | query: (string) The search query to use. |
| SCORES(SERVER/TOOL/FINAL) | 0.280/0.476/0.063 | 0.436/0.685/0.205 |
| RANKS(SERVER/TOOL/FINAL) | 145/233/381 | 10/2/1 |
## ANALYSIS

# BAD CASE 318
## TASK
Update the status of an existing incident in ServiceNow to "Resolved" and add a resolution note.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ServiceNow | Linear |
| TOOL | update_incident | linear_update_issue |
| DESC | Update an existing incident in ServiceNow | Update an existing Linear issue. |
| PARAMETERS |  | id: (string) Issue ID to update<br>title: (Optional, string) New title<br>description: (Optional, string) New description<br>priority: (Optional, number, 0-4) New priority<br>status: (Optional, string) New status name |
| SCORES(SERVER/TOOL/FINAL) | 0.302/0.597/0.108 | 0.407/0.719/0.210 |
| RANKS(SERVER/TOOL/FINAL) | 127/18/80 | 21/1/1 |
## ANALYSIS

# BAD CASE 319
## TASK
Find the nearest coffee shop to the current location using geocoding.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | AWS | AWS |
| TOOL | Search for Places Using Geocoding | Search for Places Using Geocoding |
| DESC | Search for places using geocoding. | Search for places using geocoding. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.286/0.850/0.207 | 0.286/0.850/0.207 |
| RANKS(SERVER/TOOL/FINAL) | 182/1/1 | 182/1/1 |
## ANALYSIS

# BAD CASE 320
## TASK
Delete all documents from the 'users' collection where the 'status' field is set to 'inactive'.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | MongoDB | Couchbase |
| TOOL | delete-many | delete_document_by_id |
| DESC | Delete multiple documents from a MongoDB collection | Delete a document by ID from a specified scope and collection. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.278/0.529/0.078 | 0.406/0.635/0.164 |
| RANKS(SERVER/TOOL/FINAL) | 101/13/55 | 5/1/1 |
## ANALYSIS

# BAD CASE 321
## TASK
Execute a PromQL query to retrieve the current CPU usage percentage of all nodes in the Kubernetes cluster.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Prometheus | mcp-k8s-go |
| TOOL | execute_query | List Kubernetes pods |
| DESC | Execute a PromQL instant query against Prometheus | Lists available Kubernetes pods. |
| PARAMETERS | query: (string) The PromQL query to execute |  |
| SCORES(SERVER/TOOL/FINAL) | 0.443/0.558/0.138 | 0.463/0.677/0.212 |
| RANKS(SERVER/TOOL/FINAL) | 31/82/73 | 20/1/1 |
## ANALYSIS

# BAD CASE 322
## TASK
Move an array of 5 specified tasks to the target list named "Completed Projects".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ClickUp | Todoist |
| TOOL | move_bulk_tasks | todoist_update_task |
| DESC | Move multiple tasks | Update existing tasks using natural language search. |
| PARAMETERS | tasks[]: (array) An array of task objects to move, each containing IDs or names<br>targetList: (string) The ID or name of the target list | task name: (string) partial name match to find the task<br>content: (Optional, string) new task title<br>description: (Optional, string) new task description<br>due date: (Optional, string) new due date<br>priority: (Optional, number) new priority level (1-4) |
| SCORES(SERVER/TOOL/FINAL) | 0.212/0.614/0.080 | 0.582/0.748/0.326 |
| RANKS(SERVER/TOOL/FINAL) | 281/21/387 | 1/1/1 |
## ANALYSIS

# BAD CASE 323
## TASK
Retrieve the details of a specific build with the identifier "abc123" for the Bitrise app identified as "xyz789".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Bitrise | Bitrise |
| TOOL | get_build | list_builds |
| DESC | Get a specific build of a given app | List all the builds of a specified Bitrise app or all accessible builds |
| PARAMETERS | app_slug: (string) Identifier of the Bitrise app<br>build_slug: (string) Identifier of the build | app_slug: (Optional, string) Identifier of the Bitrise app<br>sort_by: (Optional, string) Order of builds: created_at (default), running_first<br>branch: (Optional, string) Filter builds by branch<br>workflow: (Optional, string) Filter builds by workflow<br>status: (Optional, integer) Filter builds by status (0: not finished, 1: successful, 2: failed, 3: aborted, 4: in-progress)<br>next: (Optional, string) Slug of the first build in the response<br>limit: (Optional, integer) Max number of elements per page (default: 50) |
| SCORES(SERVER/TOOL/FINAL) | 0.719/0.427/0.221 | 0.719/0.616/0.318 |
| RANKS(SERVER/TOOL/FINAL) | 1/960/34 | 1/39/1 |
## ANALYSIS

# BAD CASE 324
## TASK
Create a new directory named "project_assets" within the current workspace.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | PIF | Terminal-Control |
| TOOL | mkdir | change_directory |
| DESC | Navigate and manage workspace context | Change the current working directory. |
| PARAMETERS |  | path: (string) Directory path to switch to |
| SCORES(SERVER/TOOL/FINAL) | 0.000/0.000/0.000 | 0.351/0.585/0.120 |
| RANKS(SERVER/TOOL/FINAL) | -1/-1/-1 | 12/3/1 |
## ANALYSIS

# BAD CASE 325
## TASK
Browse the list of available models for selection.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Replicate | Graphlit |
| TOOL | list_models | List Linear Projects |
| DESC | Browse available models | Lists available projects in Linear. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.343/0.534/0.098 | 0.417/0.606/0.153 |
| RANKS(SERVER/TOOL/FINAL) | 76/61/72 | 10/3/1 |
## ANALYSIS

# BAD CASE 328
## TASK
Execute a series of database operations within a single ACID transaction to ensure data consistency.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | MongoDB Lens | Heroku |
| TOOL | transaction | pg_psql |
| DESC | Execute multiple operations in a single ACID transaction | Execute SQL queries against the Heroku PostgreSQL database. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.469/0.636/0.190 | 0.493/0.716/0.253 |
| RANKS(SERVER/TOOL/FINAL) | 3/13/6 | 1/8/1 |
## ANALYSIS

# BAD CASE 329
## TASK
Retrieve the details of the document generation template with the identifier "TMPL12345".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Box | Box |
| TOOL | box_docgen_template_get_by_id_tool | box_docgen_template_get_by_id_tool |
| DESC | Retrieve details of a specific Doc Gen template. | Retrieve details of a specific Doc Gen template. |
| PARAMETERS | template_id: (str) The template identifier | template_id: (str) The template identifier |
| SCORES(SERVER/TOOL/FINAL) | 0.357/0.927/0.307 | 0.357/0.927/0.307 |
| RANKS(SERVER/TOOL/FINAL) | 108/1/1 | 108/1/1 |
## ANALYSIS

# BAD CASE 330
## TASK
Retrieve the detailed information about the currently active scene.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Unity Integration (Advanced) | DaVinci Resolve |
| TOOL | get_current_scene_info | get_current_timeline_info |
| DESC | Get detailed information about the current scene | Gets information about the current timeline. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.302/0.590/0.105 | 0.450/0.679/0.207 |
| RANKS(SERVER/TOOL/FINAL) | 167/11/53 | 2/1/1 |
## ANALYSIS

# BAD CASE 331
## TASK
Retrieve the user details associated with the email address "user@example.com".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ServiceNow | EduBase |
| TOOL | get_user | edubase_get_user |
| DESC | Get a specific user by ID, username, or email | Retrieves user information from the EduBase platform. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.241/0.479/0.055 | 0.497/0.717/0.255 |
| RANKS(SERVER/TOOL/FINAL) | 226/368/707 | 2/4/1 |
## ANALYSIS

# BAD CASE 332
## TASK
Rebuild the Bitrise pipeline with the identifier "pipeline123" for the application identified by "app456".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Bitrise | Bitrise |
| TOOL | rebuild_pipeline | generate_installable_artifact_upload_url |
| DESC | Rebuild a pipeline | Generates a signed upload URL for an installable artifact to be uploaded to Bitrise |
| PARAMETERS | app_slug: (string) Identifier of the Bitrise app<br>pipeline_id: (string) Identifier of the pipeline | connected_app_id: (string) Identifier of the Release Management connected app<br>installable_artifact_id: (string) An uuidv4 identifier for the installable artifact<br>file_name: (string) The name of the installable artifact file<br>file_size_bytes: (integer) The byte size of the installable artifact file<br>branch: (Optional, string) Name of the CI branch<br>with_public_page: (Optional, boolean) Enable public install page<br>workflow: (Optional, string) Name of the CI workflow |
| SCORES(SERVER/TOOL/FINAL) | 0.694/0.517/0.249 | 0.694/0.548/0.264 |
| RANKS(SERVER/TOOL/FINAL) | 1/157/7 | 1/81/1 |
## ANALYSIS

# BAD CASE 333
## TASK
List all available boards in the Monday.com workspace.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Monday.com | Unstructured |
| TOOL | monday-list-boards | list_workflows |
| DESC | Lists all available Monday.com boards | Lists workflows from the Unstructured API. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.350/0.525/0.097 | 0.577/0.715/0.295 |
| RANKS(SERVER/TOOL/FINAL) | 151/486/608 | 4/9/1 |
## ANALYSIS

# BAD CASE 334
## TASK
List all currently configured alert rules in the monitoring system.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Grafana | Kong Konnect |
| TOOL | list_alert_rules | List Routes |
| DESC | List alert rules | List all routes associated with a control plane. |
| PARAMETERS |  | controlPlaneId: (string) ID of the control plane<br>size: (number) Number of routes to return<br>offset: (string) Pagination offset token |
| SCORES(SERVER/TOOL/FINAL) | 0.370/0.584/0.126 | 0.452/0.688/0.214 |
| RANKS(SERVER/TOOL/FINAL) | 46/47/64 | 9/1/1 |
## ANALYSIS

# BAD CASE 336
## TASK
List all the blockchain networks currently supported by the cross-chain interoperability protocol.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Solana Agent Kit | GOAT |
| TOOL | getWormholeSupportedChains | Create a wallet, mint tokens and get test tokens on any chain using Crossmint |
| DESC | Gets the list of supported chains using Wormhole. | Facilitates the creation of wallets, minting of tokens, and retrieval of test tokens on any supported chain using Crossmint. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.398/0.815/0.264 | 0.611/0.710/0.308 |
| RANKS(SERVER/TOOL/FINAL) | 22/1/6 | 1/3/1 |
## ANALYSIS

# BAD CASE 338
## TASK
Compare the schemas of two specified collections to identify any differences in their structure.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | MongoDB Lens | Snowflake |
| TOOL | compare-schemas | list_schemas |
| DESC | Compare schemas between two collections | List all schemas within a specific database. |
| PARAMETERS |  | database: (string) Name of the database |
| SCORES(SERVER/TOOL/FINAL) | 0.469/0.582/0.159 | 0.443/0.751/0.249 |
| RANKS(SERVER/TOOL/FINAL) | 10/53/23 | 20/1/1 |
## ANALYSIS

# BAD CASE 339
## TASK
Retrieve the full details of the place identified by PlaceId "PL123456789".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | AWS | Unstructured |
| TOOL | Get Details for Specific Places | list_destinations |
| DESC | Get details for specific places by PlaceId. | Lists available destinations from the Unstructured API. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.285/0.932/0.247 | 0.558/0.696/0.270 |
| RANKS(SERVER/TOOL/FINAL) | 234/1/2 | 2/8/1 |
## ANALYSIS

# BAD CASE 340
## TASK
Add all modified files in the current directory to the staging area for the next commit.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Git | Git |
| TOOL | git_add | git_push |
| DESC | Adds file contents to the staging area | Pushes local commits to a remote repository (requires --write-access flag) |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.331/0.569/0.107 | 0.331/0.656/0.142 |
| RANKS(SERVER/TOOL/FINAL) | 28/4/5 | 28/1/1 |
## ANALYSIS

# BAD CASE 341
## TASK
Retrieve the value of the variable associated with the key "user_session_token".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Airflow | nomad-mcp |
| TOOL | Get Variable | get_variable |
| DESC | Gets a specific variable. | Gets details of a specific variable. |
| PARAMETERS | variable_key: (string) The key of the variable. | path: (string) The path of the variable.<br>namespace: (string) The namespace of the variable. |
| SCORES(SERVER/TOOL/FINAL) | 0.262/0.701/0.129 | 0.543/0.640/0.222 |
| RANKS(SERVER/TOOL/FINAL) | 140/1/7 | 1/3/1 |
## ANALYSIS

# BAD CASE 342
## TASK
List all available storage buckets owned by the authenticated user.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | AWS S3 | Keboola |
| TOOL | ListBuckets | retrieve_buckets |
| DESC | Returns a list of all buckets owned by the authenticated sender of the request | Retrieves information about all buckets in the project. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.473/0.420/0.094 | 0.415/0.905/0.340 |
| RANKS(SERVER/TOOL/FINAL) | 12/913/380 | 30/1/1 |
## ANALYSIS

# BAD CASE 344
## TASK
Create a new list named "Project Tasks" inside the folder with ID "F12345".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ClickUp | Todoist |
| TOOL | create_list_in_folder | todoist_create_task |
| DESC | Create list in folder | Create new tasks with various attributes. |
| PARAMETERS | name: (string) The name of the list to create<br>folderId: (string) The ID of the folder where the list will be created<br>folderName: (Optional, string) The name of the folder where the list will be created | content: (string) task title<br>description: (Optional, string) task description<br>due date: (Optional, string) due date<br>priority level: (Optional, number) priority level (1-4) |
| SCORES(SERVER/TOOL/FINAL) | 0.240/0.578/0.080 | 0.518/0.659/0.225 |
| RANKS(SERVER/TOOL/FINAL) | 253/30/338 | 6/2/1 |
## ANALYSIS

# BAD CASE 345
## TASK
Create a new branch from the main branch in the current Git repository.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Git | Neon |
| TOOL | git_create_branch | create_branch |
| DESC | Creates a new branch from an optional base branch | Creates a new branch within a specified Neon project. Leverages Neon's branching feature for development, testing, or migrations. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.402/0.505/0.102 | 0.280/0.868/0.211 |
| RANKS(SERVER/TOOL/FINAL) | 11/67/47 | 121/1/1 |
## ANALYSIS

# BAD CASE 346
## TASK
Create a new project file and save it to the specified directory path "/projects/new_project_2024".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | QGIS | DaVinci Resolve |
| TOOL | create_new_project | create_new_project |
| DESC | Create a new project and save it | Creates a new project in DaVinci Resolve. |
| PARAMETERS | path: (string) Path to save the new project file | project_name: (string) The name of the new project. |
| SCORES(SERVER/TOOL/FINAL) | 0.306/0.656/0.132 | 0.373/0.747/0.209 |
| RANKS(SERVER/TOOL/FINAL) | 70/4/7 | 19/1/1 |
## ANALYSIS

# BAD CASE 347
## TASK
Describe the indexes for the specified collection in the database.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | MongoDB | Chroma |
| TOOL | collection-indexes | chroma_list_collections |
| DESC | Describe the indexes for a collection | List all collections with pagination support |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.470/0.615/0.178 | 0.695/0.576/0.278 |
| RANKS(SERVER/TOOL/FINAL) | 10/51/35 | 1/85/1 |
## ANALYSIS

# BAD CASE 350
## TASK
Create a UI policy for a ServiceNow Catalog Item to enforce specific form behaviors based on user interactions.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ServiceNow | ServiceNow |
| TOOL | create_ui_policy | create_ui_policy_action |
| DESC | Creates a ServiceNow UI Policy, typically for a Catalog Item | Creates an action associated with a UI Policy to control variable states (visibility, mandatory, etc.) |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.365/0.587/0.126 | 0.365/0.719/0.188 |
| RANKS(SERVER/TOOL/FINAL) | 72/4/14 | 72/1/1 |
## ANALYSIS

# BAD CASE 351
## TASK
Search for high-priority issues assigned to a specific team member in the 'Development' team, filtering by the 'Bug' label and limiting results to 5.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Linear | Linear (Go) |
| TOOL | linear_search_issues | linear_get_user_issues |
| DESC | Search Linear issues with flexible filtering. | Retrieves issues assigned to a specific user or the authenticated user. |
| PARAMETERS | query: (Optional, string) Text to search in title/description<br>teamId: (Optional, string) Filter by team<br>status: (Optional, string) Filter by status<br>assigneeId: (Optional, string) Filter by assignee<br>labels: (Optional, string[]) Filter by labels<br>priority: (Optional, number) Filter by priority<br>limit: (Optional, number, default: 10) Max results | userId: (Optional) Optional user ID. If not provided, returns authenticated user's issues<br>includeArchived: Include archived issues in results<br>limit: Maximum number of issues to return (default: 50) |
| SCORES(SERVER/TOOL/FINAL) | 0.386/0.670/0.173 | 0.556/0.788/0.346 |
| RANKS(SERVER/TOOL/FINAL) | 21/5/8 | 1/1/1 |
## ANALYSIS

# BAD CASE 352
## TASK
Remove the document with the key "user123" from the "customers" collection.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ArangoDB | Couchbase |
| TOOL | arango_remove | delete_document_by_id |
| DESC | Remove documents from collections | Delete a document by ID from a specified scope and collection. |
| PARAMETERS | collection: (string) Collection name<br>key: (string) Document key |  |
| SCORES(SERVER/TOOL/FINAL) | 0.409/0.488/0.098 | 0.423/0.721/0.220 |
| RANKS(SERVER/TOOL/FINAL) | 9/108/57 | 6/1/1 |
## ANALYSIS

# BAD CASE 354
## TASK
List all contents of the directory "/var/log" with file and directory prefixes.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Filesystem | Terminal-Control |
| TOOL | list_directory | list_directory |
| DESC | List directory contents with [FILE] or [DIR] prefixes | List files and subdirectories in the specified directory. |
| PARAMETERS | path: (string) Directory path | path: (Optional, string) Directory path to list contents (default: current directory) |
| SCORES(SERVER/TOOL/FINAL) | 0.416/0.488/0.099 | 0.499/0.772/0.297 |
| RANKS(SERVER/TOOL/FINAL) | 7/116/37 | 1/2/1 |
## ANALYSIS

# BAD CASE 356
## TASK
Update the task instance with ID "process_data" in the DAG run "2024-05-15_run" for the DAG "data_pipeline".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Airflow | Airflow |
| TOOL | Update Task Instance | Update DAG Run |
| DESC | Updates a specific task instance. | Updates a specific DAG run. |
| PARAMETERS | dag_id: (string) The ID of the DAG.<br>dag_run_id: (string) The ID of the DAG run.<br>task_id: (string) The ID of the task. | dag_id: (string) The ID of the DAG.<br>dag_run_id: (string) The ID of the DAG run. |
| SCORES(SERVER/TOOL/FINAL) | 0.438/0.802/0.282 | 0.438/0.806/0.285 |
| RANKS(SERVER/TOOL/FINAL) | 10/2/2 | 10/1/1 |
## ANALYSIS

# BAD CASE 357
## TASK
Clear all memory caches to ensure the system retrieves fresh data.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | MongoDB Lens | Momento |
| TOOL | clear-cache | delete-cache |
| DESC | Clear memory caches to ensure fresh data | Deletes a cache from your Momento account. |
| PARAMETERS |  | name: string -- the name of the cache to delete |
| SCORES(SERVER/TOOL/FINAL) | 0.270/0.417/0.047 | 0.462/0.611/0.173 |
| RANKS(SERVER/TOOL/FINAL) | 80/207/286 | 2/3/1 |
## ANALYSIS

# BAD CASE 358
## TASK
Create a task named "Complete project documentation" in the list with ID "L12345".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ClickUp | Todoist |
| TOOL | create_task | todoist_create_task |
| DESC | Create a task | Create new tasks with various attributes. |
| PARAMETERS | name: (string) The name of the task<br>listId: (Optional, string) The ID of the list where the task will be created<br>listName: (Optional, string) The name of the list where the task will be created | content: (string) task title<br>description: (Optional, string) task description<br>due date: (Optional, string) due date<br>priority level: (Optional, number) priority level (1-4) |
| SCORES(SERVER/TOOL/FINAL) | 0.233/0.696/0.113 | 0.621/0.766/0.364 |
| RANKS(SERVER/TOOL/FINAL) | 261/6/136 | 1/1/1 |
## ANALYSIS

# BAD CASE 360
## TASK
Create an outgoing webhook for the Bitrise app with the identifier "my-app-slug" that triggers on "build_failed" and "build_succeeded" events, sending requests to "https://example.com/webhook" with custom headers "Authorization: Bearer token123" and "Content-Type: application/json".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Bitrise | n8n |
| TOOL | create_outgoing_webhook | run_webhook |
| DESC | Create an outgoing webhook for an app | Triggers a workflow via a webhook, passing the workflow name and optional data. |
| PARAMETERS | app_slug: (string) Identifier of the Bitrise app<br>events: (array) List of events to trigger the webhook<br>url: (string) URL of the webhook<br>headers: (Optional, array) Headers to be sent with the webhook | workflowName: (string) The name of the workflow to trigger<br>data: (Optional, object) Additional data to pass to the webhook |
| SCORES(SERVER/TOOL/FINAL) | 0.673/0.440/0.199 | 0.587/0.786/0.363 |
| RANKS(SERVER/TOOL/FINAL) | 1/889/24 | 3/2/1 |
## ANALYSIS

# BAD CASE 361
## TASK
List all document generation jobs that used template ID "TMPL12345", showing a maximum of 50 jobs per page. If there are more results, use the provided pagination marker to fetch the next batch.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Box | Unstructured |
| TOOL | box_docgen_template_list_jobs_tool | list_workflows_with_finished_jobs |
| DESC | List all Doc Gen jobs that used a specific template. | Lists all workflows that have any completed job, together with information about source and destination details. |
| PARAMETERS | template_id: (str) The template identifier<br>marker: (str | None, optional) Pagination marker<br>limit: (int | None, optional) Maximum number of jobs to list |  |
| SCORES(SERVER/TOOL/FINAL) | 0.455/0.886/0.357 | 0.682/0.776/0.411 |
| RANKS(SERVER/TOOL/FINAL) | 33/1/4 | 1/6/1 |
## ANALYSIS

# BAD CASE 362
## TASK
Update the details of an existing changeset with the latest modifications.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ServiceNow | Terminal-Control |
| TOOL | update_changeset | update_file_content |
| DESC | Update an existing changeset | Update content at specific row(s) in a file. |
| PARAMETERS |  | path: (string) Path to the file<br>content: (string) New content to place at the specified row(s)<br>row: (Optional, int) Row number to update (0-based)<br>rows: (Optional, list) List of row numbers to update (0-based) |
| SCORES(SERVER/TOOL/FINAL) | 0.288/0.580/0.097 | 0.432/0.653/0.184 |
| RANKS(SERVER/TOOL/FINAL) | 112/38/57 | 3/10/1 |
## ANALYSIS

# BAD CASE 363
## TASK
Stop the currently running Godot project execution.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Godot | n8n |
| TOOL | stop_project | execution_stop |
| DESC | Stop the execution of a Godot project | Stops a running execution. |
| PARAMETERS |  | id: (string) The ID of the execution to stop |
| SCORES(SERVER/TOOL/FINAL) | 0.371/0.601/0.134 | 0.446/0.830/0.307 |
| RANKS(SERVER/TOOL/FINAL) | 25/8/10 | 2/1/1 |
## ANALYSIS

# BAD CASE 364
## TASK
Navigate to the root directory of the current workspace.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | PIF | Terminal-Control |
| TOOL | cd | get_current_directory |
| DESC | Navigate and manage workspace context | Get the current working directory. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.352/0.418/0.062 | 0.433/0.718/0.223 |
| RANKS(SERVER/TOOL/FINAL) | 29/216/186 | 5/1/1 |
## ANALYSIS

# BAD CASE 365
## TASK
Retrieve the document with ID "DOC-2024-001" from the database.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Dart | Outline |
| TOOL | get_doc | Read a Document |
| DESC | Retrieve an existing doc by its ID | Get the content of a document by its ID. |
| PARAMETERS |  | docId: (string) The ID of the document to read. |
| SCORES(SERVER/TOOL/FINAL) | 0.615/0.538/0.204 | 0.483/0.830/0.333 |
| RANKS(SERVER/TOOL/FINAL) | 1/216/5 | 8/1/1 |
## ANALYSIS

# BAD CASE 366
## TASK
Trigger a new build for the Bitrise app with identifier 'app123' using the 'deploy_prod' workflow on the 'release/v1.2.0' branch, including the commit message 'Bug fixes and performance improvements'.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Bitrise | Bitrise |
| TOOL | trigger_bitrise_build | generate_installable_artifact_upload_url |
| DESC | Trigger a new build/pipeline for a specified Bitrise app | Generates a signed upload URL for an installable artifact to be uploaded to Bitrise |
| PARAMETERS | app_slug: (string) Identifier of the Bitrise app<br>branch: (Optional, string) The branch to build (default: main)<br>workflow_id: (Optional, string) The workflow to build<br>commit_message: (Optional, string) The commit message for the build<br>commit_hash: (Optional, string) The commit hash for the build | connected_app_id: (string) Identifier of the Release Management connected app<br>installable_artifact_id: (string) An uuidv4 identifier for the installable artifact<br>file_name: (string) The name of the installable artifact file<br>file_size_bytes: (integer) The byte size of the installable artifact file<br>branch: (Optional, string) Name of the CI branch<br>with_public_page: (Optional, boolean) Enable public install page<br>workflow: (Optional, string) Name of the CI workflow |
| SCORES(SERVER/TOOL/FINAL) | 0.742/0.510/0.281 | 0.742/0.595/0.328 |
| RANKS(SERVER/TOOL/FINAL) | 1/91/10 | 1/11/1 |
## ANALYSIS

# BAD CASE 367
## TASK
Retrieve detailed trace information for exceptions found in the file located at "/var/log/app/error.log" within the last 60 minutes.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Logfire | oatpp-mcp |
| TOOL | find_exceptions_in_file | Logger |
| DESC | Get detailed trace information about exceptions in a specific file | A tool for logging purposes. |
| PARAMETERS | filepath: (string) Path to the file to analyze<br>age: (int) Number of minutes to look back (max 7 days) |  |
| SCORES(SERVER/TOOL/FINAL) | 0.498/0.458/0.114 | 0.548/0.594/0.193 |
| RANKS(SERVER/TOOL/FINAL) | 5/463/86 | 1/22/1 |
## ANALYSIS

# BAD CASE 368
## TASK
Cancel the job with ID 'JOB12345'.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Unstructured | Unstructured |
| TOOL | cancel_job | cancel_crawlhtml_job |
| DESC | Delete a specific job by id. | Cancels a crawl job. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.472/0.783/0.289 | 0.472/0.801/0.303 |
| RANKS(SERVER/TOOL/FINAL) | 2/2/2 | 2/1/1 |
## ANALYSIS

# BAD CASE 369
## TASK
Retrieve the list of available catalogs along with their basic details.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Apache Gravitino(incubating) | Unstructured |
| TOOL | get_list_of_catalogs | list_sources |
| DESC | Get a list of catalogs with basic information | Lists available sources from the Unstructured API. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.304/0.598/0.109 | 0.572/0.680/0.265 |
| RANKS(SERVER/TOOL/FINAL) | 207/141/409 | 2/9/1 |
## ANALYSIS

# BAD CASE 370
## TASK
List all active documents in workspace "WS123" created by "user1", excluding deleted and archived items, with a limit of 50 documents per page.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ClickUp | Unstructured |
| TOOL | list_documents | list_workflows |
| DESC | List documents | Lists workflows from the Unstructured API. |
| PARAMETERS | workspaceId: (string) The ID of the workspace<br>documentId: (Optional, string) The ID of the document<br>creator: (Optional, string) The creator of the document<br>deleted: (Optional, boolean) Whether to include deleted documents<br>archived: (Optional, boolean) Whether to include archived documents<br>parent_id: (Optional, string) The ID of the parent item<br>parent_type: (Optional, string) The type of the parent item<br>limit: (Optional, integer) The maximum number of documents to return<br>next_cursor: (Optional, string) The cursor for pagination |  |
| SCORES(SERVER/TOOL/FINAL) | 0.310/0.573/0.102 | 0.598/0.768/0.353 |
| RANKS(SERVER/TOOL/FINAL) | 192/178/400 | 3/3/1 |
## ANALYSIS

# BAD CASE 371
## TASK
Retrieve the detailed information for the Databricks job with ID 12345.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Databricks | Keboola |
| TOOL | get_job_details | get_job_detail |
| DESC | Get detailed information about a specific Databricks job | Retrieves detailed information about a specific job, identified by the job_id, including its status, parameters, results, and any relevant metadata. |
| PARAMETERS | job_id: (int) The ID of the Databricks job |  |
| SCORES(SERVER/TOOL/FINAL) | 0.612/0.543/0.203 | 0.438/0.840/0.309 |
| RANKS(SERVER/TOOL/FINAL) | 1/179/21 | 17/1/1 |
## ANALYSIS

# BAD CASE 372
## TASK
Update the document with ID "user123" in the "customers" collection by changing the "status" field to "active".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Firebase | Couchbase |
| TOOL | firestore_update_document | upsert_document_by_id |
| DESC | Update an existing document | Upsert a document by ID to a specified scope and collection. |
| PARAMETERS | collection: (string) The name of the collection<br>id: (string) The ID of the document<br>data: (object) The data to update in the document |  |
| SCORES(SERVER/TOOL/FINAL) | 0.352/0.518/0.095 | 0.409/0.711/0.207 |
| RANKS(SERVER/TOOL/FINAL) | 33/34/31 | 7/1/1 |
## ANALYSIS

# BAD CASE 373
## TASK
Generate a detailed summary of the key themes and insights from the provided research paper on renewable energy technologies.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | HuggingFace Spaces | FireCrawl |
| TOOL | use Qwen2.5-72B-Instruct | firecrawl_deep_research |
| DESC | Provides chat capabilities using the `Qwen/Qwen2.5-72B-Instruct` space. | Conduct deep web research on a query using intelligent crawling, search, and LLM analysis. |
| PARAMETERS |  | query: (string, required) The research question or topic to explore.<br>maxDepth: (number, optional) Maximum recursive depth for crawling/search (default: 3).<br>timeLimit: (number, optional) Time limit in seconds for the research session (default: 120).<br>maxUrls: (number, optional) Maximum number of URLs to analyze (default: 50). |
| SCORES(SERVER/TOOL/FINAL) | 0.168/0.222/0.008 | 0.243/0.415/0.042 |
| RANKS(SERVER/TOOL/FINAL) | 112/714/681 | 15/2/1 |
## ANALYSIS

# BAD CASE 374
## TASK
Retrieve the response schema for the GET method of the `/users` endpoint with a 200 status code.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | OpenAPI Schema | EduBase |
| TOOL | get-response-schema | edubase_get_user |
| DESC | Gets the response schema for a specific endpoint, method, and status code | Retrieves user information from the EduBase platform. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.324/0.495/0.079 | 0.480/0.595/0.170 |
| RANKS(SERVER/TOOL/FINAL) | 66/78/105 | 3/8/1 |
## ANALYSIS

# BAD CASE 375
## TASK
Delete the resource located at `https://api.example.com/users/123` with the header `Authorization: Bearer token123`.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Rquest | OpenAPI AnyApi |
| TOOL | http_delete | {prefix}_make_request |
| DESC | Remove resources with DELETE requests | Essential for reliable execution with complex APIs where simplified implementations fail. Provides the ability to make HTTP requests to specified URLs with detailed options. |
| PARAMETERS | url: (string) The URL to send the DELETE request to<br>headers: (Optional, dict) Additional headers to include in the request<br>cookies: (Optional, dict) Cookies to include in the request | method: (string) HTTP method (GET, POST, PUT, DELETE, PATCH) (Enum: GET, POST, PUT, DELETE, PATCH)<br>url: (string) Fully qualified API URL (e.g., https://api.example.com/users/123)<br>headers: (Optional, object) Request headers<br>query_params: (Optional, object) Query parameters<br>body: (Optional, object) Request body for POST, PUT, PATCH |
| SCORES(SERVER/TOOL/FINAL) | 0.337/0.637/0.137 | 0.516/0.622/0.199 |
| RANKS(SERVER/TOOL/FINAL) | 36/5/9 | 2/6/1 |
## ANALYSIS

# BAD CASE 377
## TASK
List all available contacts in the address book.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Telegram | Telegram |
| TOOL | list_contacts | list_contacts |
| DESC | List all contacts. | List all contacts. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.291/0.927/0.250 | 0.291/0.927/0.250 |
| RANKS(SERVER/TOOL/FINAL) | 159/1/1 | 159/1/1 |
## ANALYSIS

