# BAD CASE 0
## TASK
Update the file "src/utils/helpers.js" in the project with ID "project-123" by adding a new utility function for formatting dates. The commit message should be "Add date formatting utility" and the changes should be pushed to the "feature/date-utils" branch.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | GitLab | Ghost |
| TOOL | create_or_update_file | Edit User |
| DESC | Create or update a single file in a project | Update user details. |
| PARAMETERS | project_id: (string) Project ID or URL-encoded path<br>file_path: (string) Path where to create/update the file<br>content: (string) Content of the file<br>commit_message: (string) Commit message<br>branch: (string) Branch to create/update the file in<br>previous_path: (Optional, string) Path of the file to move/rename |  |
| SCORES(SERVER/TOOL/FINAL) | 0.439/0.576/0.145 | 0.501/0.628/0.198 |
| RANKS(SERVER/TOOL/FINAL) | 127/15/41 | 13/1/1 |
## ANALYSIS

# BAD CASE 1
## TASK
Resume the execution of the DAG with the ID "daily_data_pipeline".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Airflow | Airflow |
| TOOL | Unpause DAG | Update DAG |
| DESC | Unpauses a specific DAG. | Updates a specific DAG. |
| PARAMETERS | dag_id: (string) The ID of the DAG. | dag_id: (string) The ID of the DAG. |
| SCORES(SERVER/TOOL/FINAL) | 0.570/0.678/0.262 | 0.570/0.706/0.284 |
| RANKS(SERVER/TOOL/FINAL) | 1/6/6 | 1/1/1 |
## ANALYSIS

# BAD CASE 2
## TASK
Retrieve the last 30 days of sales data from the 'monthly-sales' endpoint, filtering by the 'region' parameter set to 'North America'.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Tinybird | Intercom |
| TOOL | request-pipe-data | list_conversations |
| DESC | Requests data from a Pipe Endpoint via an HTTP request. Pipe endpoints can have parameters to filter the analytical data | Retrieves all conversations within a date range with content filtering. |
| PARAMETERS | name: (string) The name of the Pipe Endpoint<br>parameters: (Optional, object) Parameters to filter the data | startDate: (DD/MM/YYYY) Start date (required)<br>endDate: (DD/MM/YYYY) End date (required)<br>keyword: (string) Filter to include conversations with this text<br>exclude: (string) Filter to exclude conversations with this text |
| SCORES(SERVER/TOOL/FINAL) | 0.446/0.584/0.152 | 0.606/0.585/0.215 |
| RANKS(SERVER/TOOL/FINAL) | 70/19/37 | 1/16/1 |
## ANALYSIS

# BAD CASE 3
## TASK
Run a select query to retrieve the top 10 highest-selling products from the sales database for Q1 2024.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Tinybird | Apache IoTDB |
| TOOL | run-select-query | select_query |
| DESC | Allows to run a select query over a Data Source to extract insights | Execute SELECT queries to read data from the database |
| PARAMETERS | query: (string) The SQL select query | query_sql: (string) The SELECT SQL query to execute |
| SCORES(SERVER/TOOL/FINAL) | 0.425/0.573/0.140 | 0.538/0.640/0.220 |
| RANKS(SERVER/TOOL/FINAL) | 130/16/60 | 5/2/1 |
## ANALYSIS

# BAD CASE 4
## TASK
Retrieve the top 5 products matching the search term "wireless headphones" from the product catalog.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Shopify | Glean |
| TOOL | get-products | Search |
| DESC | Get all products or search by title | Provides a list of search results given a query. |
| PARAMETERS | searchTitle: (optional string) Filter products by title<br>limit: (number) Maximum number of products to return |  |
| SCORES(SERVER/TOOL/FINAL) | 0.466/0.580/0.157 | 0.526/0.588/0.182 |
| RANKS(SERVER/TOOL/FINAL) | 25/5/6 | 2/4/1 |
## ANALYSIS

# BAD CASE 5
## TASK
Retrieve the product details for the item with ID "PRD-2024-0456".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Shopify | Productboard |
| TOOL | get-product-by-id | get_product_detail |
| DESC | Get a specific product by ID | Retrieves detailed information about a specific product. |
| PARAMETERS | productId: (string) ID of the product to retrieve |  |
| SCORES(SERVER/TOOL/FINAL) | 0.502/0.617/0.192 | 0.552/0.684/0.258 |
| RANKS(SERVER/TOOL/FINAL) | 2/2/8 | 1/1/1 |
## ANALYSIS

# BAD CASE 6
## TASK
List all available apps sorted by creation date, starting from the app with the slug "example-app" and limit the results to 20 per page.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Bitrise | Raygun |
| TOOL | list_apps | list_applications |
| DESC | List all the apps available for the authenticated account | List all applications under your account |
| PARAMETERS | sort_by: (Optional, string) Order of the apps: last_build_at (default) or created_at<br>next: (Optional, string) Slug of the first app in the response<br>limit: (Optional, integer) Max number of elements per page (default: 50) |  |
| SCORES(SERVER/TOOL/FINAL) | 0.419/0.613/0.158 | 0.512/0.658/0.222 |
| RANKS(SERVER/TOOL/FINAL) | 236/7/40 | 31/2/1 |
## ANALYSIS

# BAD CASE 7
## TASK
Retrieve the latest insights for the top 5 trending tokens in the market.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | GOAT | CoinMarketCap |
| TOOL | Get token insights using BirdEye API | communityTrendingToken |
| DESC | Provides token insights using the BirdEye API. | Get trending tokens in the cryptocurrency community |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.595/0.618/0.228 | 0.593/0.771/0.352 |
| RANKS(SERVER/TOOL/FINAL) | 4/34/33 | 5/2/1 |
## ANALYSIS

# BAD CASE 8
## TASK
Retrieve the latest market data for the top 10 cryptocurrencies by market capitalization.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | GOAT | coin_api_mcp |
| TOOL | Get coin information using Coinmarketcap API | get-coin-quotes |
| DESC | Fetches coin information using the Coinmarketcap API. | Fetches the latest market quotes for one or more cryptocurrencies. |
| PARAMETERS |  | id: (string, optional) One or more comma-separated cryptocurrency CoinMarketCap IDs.<br>slug: (string, optional) A comma-separated list of cryptocurrency slugs.<br>symbol: (string, optional) One or more comma-separated cryptocurrency symbols. |
| SCORES(SERVER/TOOL/FINAL) | 0.557/0.681/0.258 | 0.653/0.751/0.369 |
| RANKS(SERVER/TOOL/FINAL) | 6/14/27 | 1/2/1 |
## ANALYSIS

# BAD CASE 9
## TASK
Retrieve the latest price and trading volume data for the top 5 trending tokens on the Ethereum network.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | GOAT | CoinMarketCap |
| TOOL | Get token information using Dexscreener API | communityTrendingToken |
| DESC | Provides token information using the Dexscreener API. | Get trending tokens in the cryptocurrency community |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.564/0.538/0.171 | 0.602/0.739/0.328 |
| RANKS(SERVER/TOOL/FINAL) | 6/155/99 | 3/2/1 |
## ANALYSIS

# BAD CASE 10
## TASK
Retrieve the detailed metrics for the index with the unique identifier "IDX-2024-001".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Meilisearch | Meilisearch |
| TOOL | get-index-metrics | get-index-metrics |
| DESC | Get detailed metrics for a specific index | Get detailed metrics for a specific index |
| PARAMETERS | uid: (string) Unique identifier for the index | uid: (string) Unique identifier for the index |
| SCORES(SERVER/TOOL/FINAL) | 0.410/0.721/0.213 | 0.410/0.721/0.213 |
| RANKS(SERVER/TOOL/FINAL) | 150/1/1 | 150/1/1 |
## ANALYSIS

# BAD CASE 11
## TASK
Retrieve the first 15 documents from the index with the unique identifier "customer_reviews".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Meilisearch | Outline |
| TOOL | get-documents | Read a Document |
| DESC | Retrieve documents from an index with pagination | Get the content of a document by its ID. |
| PARAMETERS | indexUid: (string) Unique identifier for the index<br>offset: (Optional, integer) Number of results to skip (default: 0)<br>limit: (Optional, integer) Maximum number of results to return (default: 20) | docId: (string) The ID of the document to read. |
| SCORES(SERVER/TOOL/FINAL) | 0.462/0.647/0.193 | 0.586/0.613/0.220 |
| RANKS(SERVER/TOOL/FINAL) | 86/2/6 | 1/8/1 |
## ANALYSIS

# BAD CASE 12
## TASK
Search for documents containing the keyword "machine learning" across all indices, limiting the results to 15 per index and sorting them by publication date in descending order.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Meilisearch | Outline |
| TOOL | search | Search for Documents |
| DESC | Flexible search across single or multiple indices with filtering and sorting options | Search for documents by keywords. |
| PARAMETERS | query: (string) The search query (required)<br>indexUid: (Optional, string) Specific index to search in<br>limit: (Optional, integer) Maximum number of results per index (default: 20)<br>offset: (Optional, integer) Number of results to skip (default: 0)<br>filter: (Optional, string) Filter expression<br>sort: (Optional, array of strings) Sorting rules |  |
| SCORES(SERVER/TOOL/FINAL) | 0.537/0.624/0.209 | 0.693/0.747/0.387 |
| RANKS(SERVER/TOOL/FINAL) | 36/13/21 | 1/1/1 |
## ANALYSIS

# BAD CASE 13
## TASK
Retrieve the details of the task with the unique identifier "TASK-12345".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Meilisearch | ClickUp |
| TOOL | get-task | get_task |
| DESC | Get information about a specific task | Get single task details |
| PARAMETERS | uid: (string) Unique identifier for the task | taskId: (string) The ID of the task to get<br>taskName: (Optional, string) The name of the task to get (with smart disambiguation) |
| SCORES(SERVER/TOOL/FINAL) | 0.445/0.688/0.211 | 0.476/0.720/0.247 |
| RANKS(SERVER/TOOL/FINAL) | 174/3/6 | 83/1/1 |
## ANALYSIS

# BAD CASE 14
## TASK
Retrieve the first 20 tasks that were enqueued after 2024-05-01 and have a status of "completed", sorted in reverse chronological order.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Meilisearch | Todoist |
| TOOL | get-tasks | todoist_get_tasks |
| DESC | List tasks with optional filters | Retrieve and filter tasks. |
| PARAMETERS | limit: (Optional, integer) Maximum number of tasks to return<br>from: (Optional, integer) Number of tasks to skip<br>reverse: (Optional, boolean) Sort order of tasks<br>batchUids: (Optional, array of strings) Filter by batch UIDs<br>uids: (Optional, array of strings) Filter by task UIDs<br>canceledBy: (Optional, string) Filter by cancellation source<br>types: (Optional, array of strings) Filter by task types<br>statuses: (Optional, array of strings) Filter by task statuses<br>indexUids: (Optional, array of strings) Filter by index UIDs<br>afterEnqueuedAt: (Optional, string) Filter by enqueue time<br>beforeEnqueuedAt: (Optional, string) Filter by enqueue time<br>afterStartedAt: (Optional, string) Filter by start time<br>beforeStartedAt: (Optional, string) Filter by start time<br>afterFinishedAt: (Optional, string) Filter by finish time<br>beforeFinishedAt: (Optional, string) Filter by finish time | due date: (Optional, string) filter by due date<br>priority: (Optional, number) filter by priority<br>project: (Optional, string) filter by project<br>result limit: (Optional, number) limit the number of results |
| SCORES(SERVER/TOOL/FINAL) | 0.424/0.482/0.098 | 0.464/0.619/0.178 |
| RANKS(SERVER/TOOL/FINAL) | 91/190/226 | 15/2/1 |
## ANALYSIS

# BAD CASE 15
## TASK
Perform a basic health check on the system to ensure all essential services are running properly.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Meilisearch | NS Travel Information |
| TOOL | health-check | Service Updates |
| DESC | Basic health check | Checks for disruptions, maintenance work, and engineering activities. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.468/0.659/0.203 | 0.539/0.703/0.266 |
| RANKS(SERVER/TOOL/FINAL) | 70/4/7 | 3/2/1 |
## ANALYSIS

# BAD CASE 16
## TASK
Check the comprehensive health status of the system.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Meilisearch | NS Travel Information |
| TOOL | get-health-status | Service Updates |
| DESC | Comprehensive health status | Checks for disruptions, maintenance work, and engineering activities. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.435/0.727/0.230 | 0.527/0.682/0.245 |
| RANKS(SERVER/TOOL/FINAL) | 126/1/5 | 3/7/1 |
## ANALYSIS

# BAD CASE 17
## TASK
Retrieve the current system-level information including CPU, memory, and disk usage.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Meilisearch | Meilisearch |
| TOOL | get-system-info | get-system-info |
| DESC | Get system-level information | Get system-level information |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.516/0.800/0.331 | 0.516/0.800/0.331 |
| RANKS(SERVER/TOOL/FINAL) | 143/1/1 | 143/1/1 |
## ANALYSIS

# BAD CASE 18
## TASK
Search for documents containing the keyword "machine learning" in the "research_papers" collection, focusing on the "title" and "abstract" fields, and return a maximum of 20 results sorted by publication date in descending order.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Typesense | Outline |
| TOOL | typesense_query | Search for Documents |
| DESC | Search for documents in Typesense collections with powerful filtering | Search for documents by keywords. |
| PARAMETERS | query_text: (string) The query text to search for<br>collection_name: (string) The name of the collection to search<br>search_fields: (array) Fields to search within<br>filters: (object, optional) Filters to apply to the search<br>sort_options: (object, optional) Options for sorting results<br>limit: (number, optional) Maximum number of results to return |  |
| SCORES(SERVER/TOOL/FINAL) | 0.576/0.574/0.190 | 0.675/0.706/0.337 |
| RANKS(SERVER/TOOL/FINAL) | 6/20/21 | 1/1/1 |
## ANALYSIS

# BAD CASE 19
## TASK
Retrieve the document with ID "user123" from the "customers" collection.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Typesense | EduBase |
| TOOL | typesense_get_document | edubase_get_user |
| DESC | Retrieve specific documents by ID from collections | Retrieves user information from the EduBase platform. |
| PARAMETERS | collection_name: (string) The name of the collection<br>document_id: (string) The ID of the document to retrieve |  |
| SCORES(SERVER/TOOL/FINAL) | 0.481/0.620/0.185 | 0.610/0.636/0.247 |
| RANKS(SERVER/TOOL/FINAL) | 21/17/15 | 1/8/1 |
## ANALYSIS

# BAD CASE 20
## TASK
Analyze the structure and contents of the "customer_data" collection.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Typesense | Typesense |
| TOOL | analyze_collection | analyze_collection |
| DESC | Analyze collection structure and contents | Analyze collection structure and contents |
| PARAMETERS | collection_name: (string) The name of the collection | collection_name: (string) The name of the collection |
| SCORES(SERVER/TOOL/FINAL) | 0.464/0.759/0.267 | 0.464/0.759/0.267 |
| RANKS(SERVER/TOOL/FINAL) | 103/1/1 | 103/1/1 |
## ANALYSIS

# BAD CASE 21
## TASK
Generate an image from the provided text content using OpenAI's image generation capabilities.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Graphlit | Image Generation |
| TOOL | Publish as Image (OpenAI Image Generation) | generate_image |
| DESC | Publishes content as an image using OpenAI. | Generates images using the Flux model based on text prompts. |
| PARAMETERS |  | prompt: (required) Text description of the image to generate<br>seed: (optional) Random seed for reproducible generation<br>aspect_ratio: (optional) Image aspect ratio (default: '1:1')<br>output_format: (optional) Output format - 'webp', 'jpg', or 'png' (default: 'webp')<br>num_outputs: (optional) Number of images to generate (1-4, default: 1) |
| SCORES(SERVER/TOOL/FINAL) | 0.410/0.766/0.241 | 0.644/0.688/0.305 |
| RANKS(SERVER/TOOL/FINAL) | 121/1/3 | 1/3/1 |
## ANALYSIS

# BAD CASE 22
## TASK
Upload a PDF document to the knowledge base for future reference and retrieval.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Graphlit | Basic Memory |
| TOOL | Files | write_note |
| DESC | Ingests files into the knowledge base. | Create or update notes in the knowledge base. |
| PARAMETERS |  | title: (string) The title of the note<br>content: (string) The content of the note<br>folder: (string) The folder where the note should be saved<br>tags: (array) Tags to associate with the note |
| SCORES(SERVER/TOOL/FINAL) | 0.535/0.702/0.264 | 0.614/0.726/0.324 |
| RANKS(SERVER/TOOL/FINAL) | 12/5/8 | 2/2/1 |
## ANALYSIS

# BAD CASE 23
## TASK
Retrieve the latest 10 unread emails from the primary inbox in Google Mail.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Graphlit | Gmail Headless |
| TOOL | Google Mail | get_recent_emails |
| DESC | Connects to Google Mail to ingest emails. | Retrieves recent emails with the first 1k characters of each email body. |
| PARAMETERS |  | google_access_token: (string) The access token required to authenticate the request.<br>max_results: (Optional, integer) The maximum number of emails to retrieve. Default is 5.<br>unread_only: (Optional, boolean) Whether to retrieve only unread emails. Default is false. |
| SCORES(SERVER/TOOL/FINAL) | 0.419/0.664/0.185 | 0.612/0.716/0.314 |
| RANKS(SERVER/TOOL/FINAL) | 111/2/12 | 1/1/1 |
## ANALYSIS

# BAD CASE 24
## TASK
Retrieve all pages and databases from the connected Notion workspace.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Graphlit | scrapling-fetch |
| TOOL | Notion | s-fetch-page |
| DESC | Connects to Notion to ingest data. | Retrieves complete web pages with pagination support. |
| PARAMETERS |  | url: (string) The URL of the web page to fetch.<br>mode: (string) The protection level to use ('basic', 'stealth', 'max-stealth').<br>start_index: (Optional, integer) The starting index for pagination.<br>max_length: (Optional, integer) The maximum length of content to retrieve. |
| SCORES(SERVER/TOOL/FINAL) | 0.500/0.642/0.206 | 0.569/0.702/0.280 |
| RANKS(SERVER/TOOL/FINAL) | 28/16/19 | 3/2/1 |
## ANALYSIS

# BAD CASE 25
## TASK
Fetch all active issues from the connected Linear workspace.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Graphlit | Linear (Go) |
| TOOL | Linear | linear_get_issue |
| DESC | Connects to Linear to ingest data. | Retrieves a single Linear issue by its ID. |
| PARAMETERS |  | issueId: (required) ID of the issue to retrieve |
| SCORES(SERVER/TOOL/FINAL) | 0.515/0.677/0.236 | 0.608/0.707/0.304 |
| RANKS(SERVER/TOOL/FINAL) | 43/10/16 | 3/1/1 |
## ANALYSIS

# BAD CASE 26
## TASK
Retrieve all open issues assigned to the "Development" team from the Jira project "Web Platform" created in the last 30 days.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Graphlit | Linear (Go) |
| TOOL | Jira | linear_get_user_issues |
| DESC | Connects to Jira to ingest data. | Retrieves issues assigned to a specific user or the authenticated user. |
| PARAMETERS |  | userId: (Optional) Optional user ID. If not provided, returns authenticated user's issues<br>includeArchived: Include archived issues in results<br>limit: Maximum number of issues to return (default: 50) |
| SCORES(SERVER/TOOL/FINAL) | 0.437/0.573/0.143 | 0.548/0.593/0.193 |
| RANKS(SERVER/TOOL/FINAL) | 58/16/31 | 2/6/1 |
## ANALYSIS

# BAD CASE 27
## TASK
Upload a document from the local machine to the connected cloud storage service.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Graphlit | Cloudinary |
| TOOL | OneDrive | upload |
| DESC | Connects to OneDrive to ingest files. | Upload images and videos to Cloudinary. |
| PARAMETERS |  | file: (required) Path to file, URL, or base64 data URI to upload<br>resource_type: (optional) Type of resource ('image', 'video', or 'raw')<br>public_id: (optional) Custom public ID for the uploaded asset<br>overwrite: (optional) Whether to overwrite existing assets with the same public ID<br>tags: (optional) Array of tags to assign to the uploaded asset |
| SCORES(SERVER/TOOL/FINAL) | 0.512/0.641/0.210 | 0.626/0.689/0.297 |
| RANKS(SERVER/TOOL/FINAL) | 26/6/8 | 1/4/1 |
## ANALYSIS

# BAD CASE 28
## TASK
Search for the latest news articles about renewable energy advancements.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Hyperbrowser | Tavily search |
| TOOL | search_with_bing | tavily_news_search |
| DESC | Query the web and get results with Bing search | Searches recent news articles with publication dates. |
| PARAMETERS |  | query: (string, required) Search query<br>max_results: (integer, optional) Maximum number of results to return (default: 5, max: 20)<br>days: (integer, optional) Number of days back to search (default: 3)<br>include_domains: (list or string, optional) List of domains to specifically include in results<br>exclude_domains: (list or string, optional) List of domains to exclude from results |
| SCORES(SERVER/TOOL/FINAL) | 0.468/0.501/0.117 | 0.568/0.720/0.295 |
| RANKS(SERVER/TOOL/FINAL) | 68/236/211 | 3/1/1 |
## ANALYSIS

# BAD CASE 29
## TASK
Retrieve the latest product listings from the specified e-commerce API endpoint, including query parameters for category "electronics" and a limit of 20 items per page.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Rquest | Productboard |
| TOOL | http_get | get_products |
| DESC | Perform GET requests with optional parameters | Retrieves a list of products from Productboard. |
| PARAMETERS | url: (string) The URL to send the GET request to<br>headers: (Optional, dict) Additional headers to include in the request<br>cookies: (Optional, dict) Cookies to include in the request<br>params: (Optional, dict) Query parameters to include in the request |  |
| SCORES(SERVER/TOOL/FINAL) | 0.509/0.459/0.119 | 0.559/0.624/0.217 |
| RANKS(SERVER/TOOL/FINAL) | 28/793/316 | 5/2/1 |
## ANALYSIS

# BAD CASE 30
## TASK
Update the user profile with the new email address "user@example.com" by sending a PUT request to the API endpoint "/api/users/123". Include the necessary authentication headers and ensure the request body is formatted as JSON.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Rquest | Inoyu |
| TOOL | http_put | update_my_profile |
| DESC | Update resources with PUT requests | Update properties of your profile. Takes a properties object with key-value pairs to update. |
| PARAMETERS | url: (string) The URL to send the PUT request to<br>data: (Optional, dict or string) Data to send in the body of the request<br>json: (Optional, dict) JSON data to send in the body of the request<br>headers: (Optional, dict) Additional headers to include in the request<br>cookies: (Optional, dict) Cookies to include in the request<br>files: (Optional, dict) Files to send in the body of the request | properties: (object) Key-value pairs to update, supporting string, number, boolean, and null values |
| SCORES(SERVER/TOOL/FINAL) | 0.543/0.583/0.185 | 0.643/0.655/0.276 |
| RANKS(SERVER/TOOL/FINAL) | 10/30/23 | 1/3/1 |
## ANALYSIS

# BAD CASE 31
## TASK
Update the user profile with the new email address "user@example.com" by sending a PATCH request to the API endpoint "/users/123". Include the necessary authentication headers and send the data in JSON format.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Rquest | Inoyu |
| TOOL | http_patch | update_my_profile |
| DESC | Partially update resources | Update properties of your profile. Takes a properties object with key-value pairs to update. |
| PARAMETERS | url: (string) The URL to send the PATCH request to<br>data: (Optional, dict or string) Data to send in the body of the request<br>json: (Optional, dict) JSON data to send in the body of the request<br>headers: (Optional, dict) Additional headers to include in the request<br>cookies: (Optional, dict) Cookies to include in the request<br>files: (Optional, dict) Files to send in the body of the request | properties: (object) Key-value pairs to update, supporting string, number, boolean, and null values |
| SCORES(SERVER/TOOL/FINAL) | 0.557/0.488/0.151 | 0.614/0.663/0.270 |
| RANKS(SERVER/TOOL/FINAL) | 4/416/94 | 1/2/1 |
## ANALYSIS

# BAD CASE 32
## TASK
Store the configuration settings for the production environment in the key-value store.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | consul-mcp | Azure |
| TOOL | Put values in KV store | Manage key-value pairs |
| DESC | Adds or updates values in the Consul key-value store. | Manages key-value pairs within an App Configuration store. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.451/0.638/0.183 | 0.508/0.694/0.245 |
| RANKS(SERVER/TOOL/FINAL) | 87/4/7 | 7/1/1 |
## ANALYSIS

# BAD CASE 33
## TASK
Fetch the current price from the Pyth price feed with the ID "0xca80ba6dc32e08d06f1aa886011eed1d77c77be9eb761cc10d72b7d0a2fd57a6".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Solana Agent Kit | Solana Agent Kit |
| TOOL | getPythPrice | getPythPrice |
| DESC | Fetches the price from a Pyth price feed. | Fetches the price from a Pyth price feed. |
| PARAMETERS | priceFeedID: (string) Pyth price feed ID | priceFeedID: (string) Pyth price feed ID |
| SCORES(SERVER/TOOL/FINAL) | 0.405/0.840/0.285 | 0.405/0.840/0.285 |
| RANKS(SERVER/TOOL/FINAL) | 123/1/1 | 123/1/1 |
## ANALYSIS

# BAD CASE 34
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
| SERVER | Solana Agent Kit | Solana Agent Kit |
| TOOL | createDriftVault | depositIntoDriftVault |
| DESC | Creates a new Drift vault. | Deposits tokens into a Drift vault. |
| PARAMETERS | name: (string) Name of the vault<br>marketName: (string) Market name<br>redeemPeriod: (number) Redemption period in days<br>maxTokens: (number) Maximum tokens<br>minDepositAmount: (number) Minimum deposit amount<br>managementFee: (number) Management fee in percentage<br>profitShare: (number) Profit share in percentage<br>hurdleRate: (number) Hurdle rate in percentage<br>permissioned: (boolean) Whether the vault is permissioned | amount: (number) Amount to deposit<br>vaultAddress: (string) Vault address |
| SCORES(SERVER/TOOL/FINAL) | 0.514/0.530/0.145 | 0.514/0.578/0.172 |
| RANKS(SERVER/TOOL/FINAL) | 5/19/22 | 5/1/1 |
## ANALYSIS

# BAD CASE 35
## TASK
Retrieve the current details of the active Drift user account.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Solana Agent Kit | Solana Agent Kit |
| TOOL | driftUserAccountInfo | driftUserAccountInfo |
| DESC | Gets information about the Drift user account. | Gets information about the Drift user account. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.422/0.900/0.342 | 0.422/0.900/0.342 |
| RANKS(SERVER/TOOL/FINAL) | 190/1/1 | 190/1/1 |
## ANALYSIS

# BAD CASE 36
## TASK
Scale the number of dynos up to 5 for the production environment.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Heroku | Heroku |
| TOOL | ps_scale | ps_scale |
| DESC | Scale the number of dynos up or down, or resize dynos. | Scale the number of dynos up or down, or resize dynos. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.414/0.822/0.279 | 0.414/0.822/0.279 |
| RANKS(SERVER/TOOL/FINAL) | 115/1/1 | 115/1/1 |
## ANALYSIS

# BAD CASE 37
## TASK
Retrieve detailed information about all available pipelines in the system.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Heroku | Heroku |
| TOOL | pipelines_info | pipelines_info |
| DESC | Get detailed pipeline information. | Get detailed pipeline information. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.491/0.898/0.396 | 0.491/0.898/0.396 |
| RANKS(SERVER/TOOL/FINAL) | 139/1/1 | 139/1/1 |
## ANALYSIS

# BAD CASE 38
## TASK
Query the Heroku PostgreSQL database for all active user accounts created in the last 30 days.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Heroku | Heroku |
| TOOL | pg_psql | pg_psql |
| DESC | Execute SQL queries against the Heroku PostgreSQL database. | Execute SQL queries against the Heroku PostgreSQL database. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.600/0.729/0.319 | 0.600/0.729/0.319 |
| RANKS(SERVER/TOOL/FINAL) | 1/1/1 | 1/1/1 |
## ANALYSIS

# BAD CASE 39
## TASK
Retrieve details about the currently highlighted or selected item.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Talk To Figma | Productboard |
| TOOL | get_selection | get_feature_detail |
| DESC | Get information about the current selection | Retrieves detailed information about a specific feature. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.498/0.771/0.296 | 0.586/0.814/0.388 |
| RANKS(SERVER/TOOL/FINAL) | 170/4/9 | 21/1/1 |
## ANALYSIS

# BAD CASE 40
## TASK
Retrieve detailed information for the nodes with IDs [101, 102, 103, 104].
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Talk To Figma | Memory |
| TOOL | get_nodes_info | open_nodes |
| DESC | Get detailed information about multiple nodes by providing an array of node IDs | Retrieve specific nodes by name. |
| PARAMETERS |  | names: (string[]) List of node names to retrieve |
| SCORES(SERVER/TOOL/FINAL) | 0.415/0.760/0.240 | 0.518/0.747/0.289 |
| RANKS(SERVER/TOOL/FINAL) | 235/1/5 | 27/3/1 |
## ANALYSIS

# BAD CASE 41
## TASK
Batch create or update 10 annotations for a dataset with unique identifiers and labels.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Talk To Figma | Basic Memory |
| TOOL | set_multiple_annotations | write_note |
| DESC | Batch create/update multiple annotations efficiently | Create or update notes in the knowledge base. |
| PARAMETERS |  | title: (string) The title of the note<br>content: (string) The content of the note<br>folder: (string) The folder where the note should be saved<br>tags: (array) Tags to associate with the note |
| SCORES(SERVER/TOOL/FINAL) | 0.414/0.800/0.264 | 0.558/0.703/0.276 |
| RANKS(SERVER/TOOL/FINAL) | 247/1/2 | 3/2/1 |
## ANALYSIS

# BAD CASE 42
## TASK
Scan and intelligently chunk text nodes from a large design file for efficient processing.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Talk To Figma | Talk To Figma |
| TOOL | scan_text_nodes | scan_text_nodes |
| DESC | Scan text nodes with intelligent chunking for large designs | Scan text nodes with intelligent chunking for large designs |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.472/0.893/0.376 | 0.472/0.893/0.376 |
| RANKS(SERVER/TOOL/FINAL) | 104/1/1 | 104/1/1 |
## ANALYSIS

# BAD CASE 43
## TASK
Create prepared queries to optimize the efficiency of service discovery operations.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | consul-mcp | consul-mcp |
| TOOL | Create prepared queries | Create prepared queries |
| DESC | Creates prepared queries for efficient service discovery. | Creates prepared queries for efficient service discovery. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.512/0.908/0.422 | 0.512/0.908/0.422 |
| RANKS(SERVER/TOOL/FINAL) | 132/1/1 | 132/1/1 |
## ANALYSIS

# BAD CASE 44
## TASK
List all available items in the current inventory.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Xero | Outline |
| TOOL | list-items | List Collections |
| DESC | Retrieve a list of items | List all available collections. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.509/0.725/0.268 | 0.512/0.830/0.353 |
| RANKS(SERVER/TOOL/FINAL) | 45/16/12 | 44/1/1 |
## ANALYSIS

# BAD CASE 45
## TASK
Create a new entry in the system with the following details: title "Project Kickoff", description "Initial meeting to discuss project goals and timelines", and due date "2024-07-15".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Contentful-mcp | DaVinci Resolve |
| TOOL | create_entry | create_new_timeline |
| DESC | Create new entries | Creates a new timeline in the current project. |
| PARAMETERS |  | timeline_name: (string) The name of the new timeline. |
| SCORES(SERVER/TOOL/FINAL) | 0.511/0.607/0.188 | 0.476/0.683/0.222 |
| RANKS(SERVER/TOOL/FINAL) | 19/11/9 | 56/1/1 |
## ANALYSIS

# BAD CASE 46
## TASK
Retrieve the details of the current organization, including its name, address, and contact information.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Xero | SingleStore |
| TOOL | list-organisation-details | organization_info |
| DESC | Retrieve details about an organisation | Retrieve details about the user's current organization |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.493/0.820/0.332 | 0.557/0.816/0.371 |
| RANKS(SERVER/TOOL/FINAL) | 104/1/2 | 13/2/1 |
## ANALYSIS

# BAD CASE 47
## TASK
Generate a motivational quote about perseverance and success.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Xero | Qwen_Max |
| TOOL | create-quote | qwen_max |
| DESC | Create a new quote | Generates text using the Qwen Max language model. |
| PARAMETERS |  | prompt: (string) The input prompt for the model.<br>max_tokens: (number) The maximum number of tokens to generate in the output.<br>temperature: (number) Controls the randomness of the model's output. |
| SCORES(SERVER/TOOL/FINAL) | 0.223/0.558/0.069 | 0.463/0.480/0.107 |
| RANKS(SERVER/TOOL/FINAL) | 164/1/6 | 2/6/1 |
## ANALYSIS

# BAD CASE 48
## TASK
Retrieve detailed information about the group with ID 'GRP12345'.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Okta | whale-tracker-mcp |
| TOOL | get_group | get_transaction_details |
| DESC | Retrieves detailed information about a specific group. | Retrieve detailed information about a specific transaction by its ID. |
| PARAMETERS |  | transaction_id: (string) The ID of the transaction to retrieve details for. |
| SCORES(SERVER/TOOL/FINAL) | 0.388/0.756/0.222 | 0.547/0.664/0.241 |
| RANKS(SERVER/TOOL/FINAL) | 181/1/2 | 1/4/1 |
## ANALYSIS

# BAD CASE 49
## TASK
Search for contacts with the name "John Smith" in the address book.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Telegram | MCP Toolbox for Databases |
| TOOL | search_contacts | search-hotels-by-name |
| DESC | Search contacts. | Search for hotels based on name. |
| PARAMETERS | query: (str) Search query | name: (string) The name of the hotel. |
| SCORES(SERVER/TOOL/FINAL) | 0.361/0.759/0.208 | 0.621/0.637/0.252 |
| RANKS(SERVER/TOOL/FINAL) | 237/1/5 | 1/10/1 |
## ANALYSIS

# BAD CASE 50
## TASK
Export all contacts in JSON format.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Telegram | Telegram |
| TOOL | export_contacts | export_contacts |
| DESC | Export all contacts as JSON. | Export all contacts as JSON. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.418/0.985/0.406 | 0.418/0.985/0.406 |
| RANKS(SERVER/TOOL/FINAL) | 75/1/1 | 75/1/1 |
## ANALYSIS

# BAD CASE 51
## TASK
Generate an image using a color palette consisting of shades of blue and green.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | AWS | Image Generation |
| TOOL | Color-Guided Image Generation | generate_image |
| DESC | Generate images with specific color palettes. | Generates images using the Flux model based on text prompts. |
| PARAMETERS |  | prompt: (required) Text description of the image to generate<br>seed: (optional) Random seed for reproducible generation<br>aspect_ratio: (optional) Image aspect ratio (default: '1:1')<br>output_format: (optional) Output format - 'webp', 'jpg', or 'png' (default: 'webp')<br>num_outputs: (optional) Number of images to generate (1-4, default: 1) |
| SCORES(SERVER/TOOL/FINAL) | 0.287/0.784/0.176 | 0.576/0.610/0.215 |
| RANKS(SERVER/TOOL/FINAL) | 217/1/4 | 1/6/1 |
## ANALYSIS

# BAD CASE 52
## TASK
Retrieve the latest 10 unread emails from the inbox folder in Microsoft Outlook.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Graphlit | Gmail Headless |
| TOOL | Microsoft Outlook email | get_recent_emails |
| DESC | Connects to Microsoft Outlook to ingest emails. | Retrieves recent emails with the first 1k characters of each email body. |
| PARAMETERS |  | google_access_token: (string) The access token required to authenticate the request.<br>max_results: (Optional, integer) The maximum number of emails to retrieve. Default is 5.<br>unread_only: (Optional, boolean) Whether to retrieve only unread emails. Default is false. |
| SCORES(SERVER/TOOL/FINAL) | 0.416/0.670/0.187 | 0.539/0.691/0.257 |
| RANKS(SERVER/TOOL/FINAL) | 110/3/6 | 1/1/1 |
## ANALYSIS

# BAD CASE 53
## TASK
Retrieve the latest 10 open issues from the GitHub repository for project "Alpha".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Graphlit | Gitee |
| TOOL | GitHub Issues | get_repo_issue_detail |
| DESC | Connects to GitHub to ingest issues. | Get details of a repository issue |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.482/0.628/0.190 | 0.551/0.639/0.225 |
| RANKS(SERVER/TOOL/FINAL) | 29/3/7 | 3/2/1 |
## ANALYSIS

# BAD CASE 54
## TASK
Search for the latest podcast episodes discussing advancements in artificial intelligence.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Graphlit | mcp-local-rag |
| TOOL | Web Search (including Podcast Search) | rag_search |
| DESC | Performs web searches and ingests the results. | Performs a web search to fetch the latest information and provides it to the model to enhance its responses. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.464/0.524/0.127 | 0.605/0.600/0.220 |
| RANKS(SERVER/TOOL/FINAL) | 70/102/91 | 1/2/1 |
## ANALYSIS

# BAD CASE 55
## TASK
Retrieve the contents of the "src/utils" directory from the "main" branch of the "example-repo" repository owned by "github-user".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | GitHub | Gitee |
| TOOL | get_file_contents | get_file_content |
| DESC | Get contents of a file or directory | Get the content of a file in a repository |
| PARAMETERS | owner: (string) Repository owner<br>repo: (string) Repository name<br>path: (string) Path to file/directory<br>branch: (optional string) Branch to get contents from |  |
| SCORES(SERVER/TOOL/FINAL) | 0.573/0.549/0.180 | 0.599/0.630/0.238 |
| RANKS(SERVER/TOOL/FINAL) | 2/56/24 | 1/2/1 |
## ANALYSIS

# BAD CASE 58
## TASK
Create a duplicate of the selected node with a 20-pixel horizontal offset to the right.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Talk To Figma | Talk To Figma |
| TOOL | clone_node | clone_node |
| DESC | Create a copy of an existing node with optional position offset | Create a copy of an existing node with optional position offset |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.386/0.777/0.233 | 0.386/0.777/0.233 |
| RANKS(SERVER/TOOL/FINAL) | 182/1/1 | 182/1/1 |
## ANALYSIS

# BAD CASE 59
## TASK
Update the status of the current issue to "In Progress" and assign it to the project manager.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Gitee | TickTick |
| TOOL | update_issue | update_project |
| DESC | Update an issue | Update an existing project |
| PARAMETERS |  | projectId: (string) Project identifier<br>name: (optional string) Project name<br>color: (optional string) Project color<br>sortOrder: (optional number) Project sort order<br>viewMode: (optional string) View mode ('list', 'kanban', 'timeline')<br>kind: (optional string) Project kind ('TASK', 'NOTE') |
| SCORES(SERVER/TOOL/FINAL) | 0.493/0.689/0.234 | 0.555/0.733/0.298 |
| RANKS(SERVER/TOOL/FINAL) | 41/5/7 | 1/1/1 |
## ANALYSIS

# BAD CASE 60
## TASK
Retrieve the content of the latest project documentation page from the team's knowledge base.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Atlassian | EduBase |
| TOOL | confluence_get_page | edubase_get_user |
| DESC | Get content of a specific page | Retrieves user information from the EduBase platform. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.499/0.625/0.195 | 0.647/0.677/0.297 |
| RANKS(SERVER/TOOL/FINAL) | 55/43/42 | 1/7/1 |
## ANALYSIS

# BAD CASE 62
## TASK
Create a cross-chain order to transfer 1000 USDC from Ethereum (chain ID: 1) to Polygon (chain ID: 137), converting it to MATIC and sending it to recipient address 0x123...abc.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Solana Agent Kit | Base Free USDC Transfer |
| TOOL | createDebridgeOrder | tranfer-usdc |
| DESC | Creates a deBridge order. | Analyzes the value of the purchased items and schedules a USDC transfer to the recipient via the Base chain. Does not wait for the transaction to complete. |
| PARAMETERS | srcChainId: (string) Source chain ID<br>srcChainTokenIn: (string) Source token mint<br>srcChainTokenInAmount: (string) Amount of source token<br>dstChainId: (string) Destination chain ID<br>dstChainTokenOut: (string) Destination token mint<br>dstChainTokenOutRecipient: (string) Recipient address on destination chain | usdc_amount: (number) USDC amount, greater than 0.<br>recipient: (string) Recipient's on-chain address or ENS domain (e.g., example.eth). |
| SCORES(SERVER/TOOL/FINAL) | 0.525/0.572/0.172 | 0.610/0.595/0.221 |
| RANKS(SERVER/TOOL/FINAL) | 3/7/8 | 1/5/1 |
## ANALYSIS

# BAD CASE 64
## TASK
Delete the variable with the key "user_session_token" from the system.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Airflow | Ghost |
| TOOL | Delete Variable | Delete User |
| DESC | Deletes a specific variable. | Remove a user. |
| PARAMETERS | variable_key: (string) The key of the variable. |  |
| SCORES(SERVER/TOOL/FINAL) | 0.373/0.711/0.188 | 0.468/0.726/0.247 |
| RANKS(SERVER/TOOL/FINAL) | 175/2/4 | 10/1/1 |
## ANALYSIS

# BAD CASE 65
## TASK
Retrieve the details of the pool named "Sunset Oasis".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Airflow | Airflow |
| TOOL | Get Pool | Get Pool |
| DESC | Gets a specific pool. | Gets a specific pool. |
| PARAMETERS | pool_name: (string) The name of the pool. | pool_name: (string) The name of the pool. |
| SCORES(SERVER/TOOL/FINAL) | 0.340/0.728/0.181 | 0.340/0.728/0.181 |
| RANKS(SERVER/TOOL/FINAL) | 243/1/1 | 243/1/1 |
## ANALYSIS

# BAD CASE 66
## TASK
List all available plugins in the system.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Airflow | Airflow |
| TOOL | Get Plugins | Get Plugins |
| DESC | Gets a list of plugins. | Gets a list of plugins. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.442/0.879/0.341 | 0.442/0.879/0.341 |
| RANKS(SERVER/TOOL/FINAL) | 236/1/1 | 236/1/1 |
## ANALYSIS

# BAD CASE 70
## TASK
Retrieve the first 20 chats from the paginated list, starting from page 1.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Telegram | Telegram |
| TOOL | get_chats | get_chats |
| DESC | Get a paginated list of chats. | Get a paginated list of chats. |
| PARAMETERS | page: (int) Page number (1-indexed)<br>page_size: (int) Number of chats per page | page: (int) Page number (1-indexed)<br>page_size: (int) Number of chats per page |
| SCORES(SERVER/TOOL/FINAL) | 0.401/0.849/0.289 | 0.401/0.849/0.289 |
| RANKS(SERVER/TOOL/FINAL) | 143/1/1 | 143/1/1 |
## ANALYSIS

# BAD CASE 71
## TASK
List all users who are currently blocked from accessing the system.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Telegram | Telegram |
| TOOL | get_blocked_users | get_blocked_users |
| DESC | List blocked users. | List blocked users. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.429/0.883/0.335 | 0.429/0.883/0.335 |
| RANKS(SERVER/TOOL/FINAL) | 106/1/1 | 106/1/1 |
## ANALYSIS

# BAD CASE 73
## TASK
Check the online status of the user with ID 12345.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Telegram | Telegram |
| TOOL | get_user_status | get_user_status |
| DESC | Get a user's online status. | Get a user's online status. |
| PARAMETERS | user_id: (int) ID of the user | user_id: (int) ID of the user |
| SCORES(SERVER/TOOL/FINAL) | 0.413/0.810/0.271 | 0.413/0.810/0.271 |
| RANKS(SERVER/TOOL/FINAL) | 186/1/1 | 186/1/1 |
## ANALYSIS

# BAD CASE 74
## TASK
Retrieve all prototype reactions with visual highlight animations from the connected nodes.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Talk To Figma | Talk To Figma |
| TOOL | get_reactions | get_reactions |
| DESC | Get all prototype reactions from nodes with visual highlight animation | Get all prototype reactions from nodes with visual highlight animation |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.381/0.930/0.330 | 0.381/0.930/0.330 |
| RANKS(SERVER/TOOL/FINAL) | 202/1/1 | 202/1/1 |
## ANALYSIS

# BAD CASE 75
## TASK
Extract the override properties from the currently selected component instance.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Talk To Figma | Talk To Figma |
| TOOL | get_instance_overrides | get_instance_overrides |
| DESC | Extract override properties from a selected component instance | Extract override properties from a selected component instance |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.413/0.955/0.377 | 0.413/0.955/0.377 |
| RANKS(SERVER/TOOL/FINAL) | 170/1/1 | 170/1/1 |
## ANALYSIS

# BAD CASE 76
## TASK
Run a Python script in a temporary sandboxed environment to process and analyze a dataset, ensuring automatic cleanup after completion.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Heroku | code-sandbox-mcp |
| TOOL | deploy_one_off_dyno | sandbox_exec |
| DESC | Execute code or commands in a sandboxed environment on a Heroku one-off dyno. Supports file creation, network access, environment variables, and automatic cleanup. Ideal for running scripts, tests, or temporary workloads. | Execute commands in the sandboxed environment. |
| PARAMETERS |  | container_id: (string, required) ID of the container returned from the initialize call<br>commands: (array, required) List of command(s) to run in the sandboxed environment |
| SCORES(SERVER/TOOL/FINAL) | 0.451/0.686/0.212 | 0.588/0.737/0.319 |
| RANKS(SERVER/TOOL/FINAL) | 116/3/9 | 2/1/1 |
## ANALYSIS

# BAD CASE 77
## TASK
Search for all PDF files containing the keyword "financial report" in their names within the specified folder IDs.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Box | Outline |
| TOOL | box_search_tool | Search for Documents |
| DESC | Search for files in Box. | Search for documents by keywords. |
| PARAMETERS | query: (str) The query to search for.<br>file_extensions: (List[str], optional) File extensions to filter results.<br>where_to_look_for_query: (List[str], optional) Locations to search (e.g. NAME, DESCRIPTION, FILE_CONTENT, COMMENTS, TAG).<br>ancestor_folder_ids: (List[str], optional) List of folder IDs in which to search. |  |
| SCORES(SERVER/TOOL/FINAL) | 0.426/0.645/0.177 | 0.606/0.726/0.320 |
| RANKS(SERVER/TOOL/FINAL) | 126/4/22 | 3/1/1 |
## ANALYSIS

# BAD CASE 78
## TASK
Retrieve the details of a document generation job with the identifier "JOB12345".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Box | n8n |
| TOOL | box_docgen_get_job_tool | workflow_get |
| DESC | Fetch a single Doc Gen job by its ID. | Gets details of a specific workflow. |
| PARAMETERS | job_id: (str) The job identifier | id: (string) The ID of the workflow |
| SCORES(SERVER/TOOL/FINAL) | 0.442/0.665/0.196 | 0.492/0.708/0.247 |
| RANKS(SERVER/TOOL/FINAL) | 167/6/21 | 40/1/1 |
## ANALYSIS

# BAD CASE 79
## TASK
Create a new file named "PlayerSettings.json" in the Unity project's Assets folder with the content `{"playerName": "Hero", "health": 100, "level": 1}`.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Unity Integration (Advanced) | Unity3d Game Engine |
| TOOL | write_file | add_asset_to_scene |
| DESC | Create or overwrite a file with new content | Adds an asset from the AssetDatabase to the Unity scene |
| PARAMETERS | path: (string) Path to the file, can be absolute or relative to the Unity project's Assets folder<br>content: (string) Content to write to the file | assetPath: (string) The path of the asset to add |
| SCORES(SERVER/TOOL/FINAL) | 0.530/0.491/0.138 | 0.610/0.599/0.223 |
| RANKS(SERVER/TOOL/FINAL) | 3/127/28 | 1/4/1 |
## ANALYSIS

# BAD CASE 81
## TASK
Aggregate the sales data for the last quarter to calculate total revenue and average order value.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | MongoDB Lens | Financial Datasets |
| TOOL | aggregate-data | get_current_stock_price |
| DESC | Execute aggregation pipelines | Get the current / latest price of a company. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.400/0.464/0.086 | 0.501/0.633/0.201 |
| RANKS(SERVER/TOOL/FINAL) | 139/578/620 | 6/1/1 |
## ANALYSIS

# BAD CASE 82
## TASK
Extract all unique customer email addresses from the provided dataset.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | MongoDB Lens | Shopify |
| TOOL | distinct-values | get-customers |
| DESC | Extract unique values for any field | Get customers or search by name/email |
| PARAMETERS |  | searchQuery: (optional string) Filter customers by name or email<br>limit: (optional number, default: 10) Maximum number of customers to return |
| SCORES(SERVER/TOOL/FINAL) | 0.363/0.694/0.175 | 0.525/0.619/0.201 |
| RANKS(SERVER/TOOL/FINAL) | 194/1/6 | 2/8/1 |
## ANALYSIS

# BAD CASE 83
## TASK
Retrieve the details of the list with the ID "L12345" and optionally include the name if available.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ClickUp | whale-tracker-mcp |
| TOOL | get_list | get_transaction_details |
| DESC | Get list details | Retrieve detailed information about a specific transaction by its ID. |
| PARAMETERS | listId: (string) The ID of the list to get<br>listName: (Optional, string) The name of the list to get | transaction_id: (string) The ID of the transaction to retrieve details for. |
| SCORES(SERVER/TOOL/FINAL) | 0.448/0.685/0.210 | 0.605/0.683/0.282 |
| RANKS(SERVER/TOOL/FINAL) | 186/5/26 | 2/6/1 |
## ANALYSIS

# BAD CASE 84
## TASK
Create a new page titled "Project Timeline" with the content "Q2 2024 deliverables" in the specified workspace and document, setting the content format to plain text.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ClickUp | DaVinci Resolve |
| TOOL | create_document_pages | create_new_timeline |
| DESC | Create a document page | Creates a new timeline in the current project. |
| PARAMETERS | workspaceId: (string) The ID of the workspace<br>documentId: (string) The ID of the document<br>parent_page_id: (Optional, string) The ID of the parent page<br>name: (string) The name of the page<br>sub_title: (Optional, string) The subtitle of the page<br>content: (string) The content of the page<br>content_format: (Optional, string) The format of the content | timeline_name: (string) The name of the new timeline. |
| SCORES(SERVER/TOOL/FINAL) | 0.466/0.594/0.164 | 0.502/0.682/0.233 |
| RANKS(SERVER/TOOL/FINAL) | 64/8/14 | 21/1/1 |
## ANALYSIS

# BAD CASE 86
## TASK
Approve the pending change request in the system.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ServiceNow | ServiceNow |
| TOOL | approve_change | approve_change |
| DESC | Approve a change request | Approve a change request |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.450/0.823/0.305 | 0.450/0.823/0.305 |
| RANKS(SERVER/TOOL/FINAL) | 128/1/1 | 128/1/1 |
## ANALYSIS

# BAD CASE 87
## TASK
List all available knowledge bases with their respective details.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ServiceNow | Basic Memory |
| TOOL | list_knowledge_bases | search_notes |
| DESC | List knowledge bases with filtering options | Search across the knowledge base. |
| PARAMETERS |  | query: (string) The search query<br>page: (integer) The page number for paginated results<br>page_size: (integer) The number of items per page |
| SCORES(SERVER/TOOL/FINAL) | 0.443/0.776/0.267 | 0.605/0.760/0.350 |
| RANKS(SERVER/TOOL/FINAL) | 199/1/4 | 1/2/1 |
## ANALYSIS

# BAD CASE 88
## TASK
Create a new issue titled "Implement user authentication" in the development team with a priority level of 2 (high) and an initial status of "In Progress". Include a description outlining the required authentication flow and security measures.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Linear | AWS |
| TOOL | linear_create_issue | Security-First Development Workflow |
| DESC | Create a new Linear issue. | Implement a security-first development workflow. |
| PARAMETERS | title: (string) Issue title<br>teamId: (string) Team ID to create issue in<br>description: (Optional, string) Issue description (markdown supported)<br>priority: (Optional, number, 0-4) Priority level (1=urgent, 4=low)<br>status: (Optional, string) Initial status name |  |
| SCORES(SERVER/TOOL/FINAL) | 0.581/0.552/0.187 | 0.501/0.672/0.226 |
| RANKS(SERVER/TOOL/FINAL) | 1/52/13 | 53/1/1 |
## ANALYSIS

# BAD CASE 90
## TASK
Retrieve all messages and shared files from the Microsoft Teams workspace for the past 7 days.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Graphlit | SingleStore |
| TOOL | Microsoft Teams | workspace_groups_info |
| DESC | Connects to Microsoft Teams to ingest messages and files. | Retrieve details about the workspace groups accessible to the user |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.441/0.688/0.209 | 0.559/0.674/0.254 |
| RANKS(SERVER/TOOL/FINAL) | 81/1/6 | 2/3/1 |
## ANALYSIS

# BAD CASE 91
## TASK
Create a new form field for a catalog item to capture customer preferences.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ServiceNow | ServiceNow |
| TOOL | create_catalog_item_variable | create_catalog_item_variable |
| DESC | Create a new variable (form field) for a catalog item | Create a new variable (form field) for a catalog item |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.379/0.842/0.269 | 0.379/0.842/0.269 |
| RANKS(SERVER/TOOL/FINAL) | 258/1/1 | 258/1/1 |
## ANALYSIS

# BAD CASE 92
## TASK
List all available groups with their details.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ServiceNow | OpenCTI |
| TOOL | list_groups | list_groups |
| DESC | List groups with filtering options | Lists all groups with their members. |
| PARAMETERS |  | first: (Optional, number) Number of groups to retrieve, defaults to 10 |
| SCORES(SERVER/TOOL/FINAL) | 0.448/0.755/0.255 | 0.493/0.900/0.400 |
| RANKS(SERVER/TOOL/FINAL) | 191/13/41 | 75/1/1 |
## ANALYSIS

# BAD CASE 93
## TASK
Retrieve the details of the task with ID "TASK-12345" or, if not found, search for a task named "Q2 Marketing Campaign" using smart disambiguation.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ClickUp | OpenCTI |
| TOOL | get_task | get_campaign_by_name |
| DESC | Get single task details | Retrieves campaign information by name. |
| PARAMETERS | taskId: (string) The ID of the task to get<br>taskName: (Optional, string) The name of the task to get (with smart disambiguation) | name: (string) Campaign name |
| SCORES(SERVER/TOOL/FINAL) | 0.503/0.585/0.172 | 0.516/0.662/0.226 |
| RANKS(SERVER/TOOL/FINAL) | 82/23/37 | 62/1/1 |
## ANALYSIS

# BAD CASE 94
## TASK
Execute the action "send_email" with the parameters {"recipient": "john.doe@example.com", "subject": "Project Update", "body": "Please find the latest project updates attached."}.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Home Assistant | Telegram |
| TOOL | execute_action | get_last_interaction |
| DESC | Executes a specified action with given parameters. | Get the most recent message with a contact. |
| PARAMETERS | action: (string) The action to execute<br>parameters: (object) Parameters for the action | contact_id: (int) ID of the contact |
| SCORES(SERVER/TOOL/FINAL) | 0.462/0.602/0.168 | 0.473/0.636/0.191 |
| RANKS(SERVER/TOOL/FINAL) | 83/4/13 | 71/2/1 |
## ANALYSIS

# BAD CASE 95
## TASK
Delete 50 inactive user nodes from the database in a single operation.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Talk To Figma | Ramp |
| TOOL | delete_multiple_nodes | clear_table |
| DESC | Delete multiple nodes at once efficiently | Clears a table in the ephemeral database. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.388/0.733/0.208 | 0.503/0.677/0.231 |
| RANKS(SERVER/TOOL/FINAL) | 233/1/7 | 23/4/1 |
## ANALYSIS

# BAD CASE 96
## TASK
Create a copy of the task with ID "TSK123" and move it to the target list with ID "LST456".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ClickUp | Todoist |
| TOOL | duplicate_task | todoist_create_task |
| DESC | Copy task | Create new tasks with various attributes. |
| PARAMETERS | taskId: (string) The ID of the task to duplicate<br>taskName: (Optional, string) The name of the task to duplicate<br>listId: (string) The ID of the target list<br>listName: (Optional, string) The name of the target list | content: (string) task title<br>description: (Optional, string) task description<br>due date: (Optional, string) due date<br>priority level: (Optional, number) priority level (1-4) |
| SCORES(SERVER/TOOL/FINAL) | 0.536/0.652/0.228 | 0.574/0.655/0.246 |
| RANKS(SERVER/TOOL/FINAL) | 8/9/7 | 2/8/1 |
## ANALYSIS

# BAD CASE 97
## TASK
Find nearby restaurants within a 5-mile radius of the current user location.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | AWS | Brave Search |
| TOOL | Search for Places Near a Location | brave_local_search |
| DESC | Search for places near a specified location. | Search for local businesses and services |
| PARAMETERS |  | query: (string) Local search terms<br>count: (Optional, number) Number of results (max 20) |
| SCORES(SERVER/TOOL/FINAL) | 0.434/0.739/0.237 | 0.579/0.646/0.241 |
| RANKS(SERVER/TOOL/FINAL) | 173/1/2 | 2/5/1 |
## ANALYSIS

# BAD CASE 102
## TASK
Create a new folder named "Project_2024" under the parent folder with ID "12345" and set its description to "All project files for 2024".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Box | TickTick |
| TOOL | box_manage_folder_tool | create_project |
| DESC | Create, update, or delete folders in Box. | Create a new project |
| PARAMETERS | action: (str) Action to perform: 'create', 'delete', or 'update'<br>folder_id: (str, optional) ID of the folder (required for delete/update)<br>name: (str, optional) Folder name (required for create, optional for update)<br>parent_id: (str, optional) Parent folder ID (required for create, optional for update)<br>description: (str, optional) Folder description (optional for update)<br>recursive: (bool, optional) Whether to delete recursively (optional for delete) | name: (string) Project name<br>color: (optional string) Project color (default: '#4772FA')<br>viewMode: (optional string) View mode ('list', 'kanban', 'timeline') (default: 'list')<br>kind: (optional string) Project kind ('TASK', 'NOTE') (default: 'TASK') |
| SCORES(SERVER/TOOL/FINAL) | 0.398/0.541/0.117 | 0.540/0.636/0.218 |
| RANKS(SERVER/TOOL/FINAL) | 247/100/339 | 3/2/1 |
## ANALYSIS

# BAD CASE 104
## TASK
Retrieve the details of the marketing campaign named "Summer Sale 2024".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | OpenCTI | Productboard |
| TOOL | get_campaign_by_name | get_product_detail |
| DESC | Retrieves campaign information by name. | Retrieves detailed information about a specific product. |
| PARAMETERS | name: (string) Campaign name |  |
| SCORES(SERVER/TOOL/FINAL) | 0.332/0.604/0.121 | 0.438/0.615/0.166 |
| RANKS(SERVER/TOOL/FINAL) | 238/3/15 | 10/2/1 |
## ANALYSIS

# BAD CASE 105
## TASK
Create a new file at "/documents/report.txt" with the content "Quarterly sales report for Q2 2024: $1.2M revenue."
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Golang Filesystem Server | Financial Datasets |
| TOOL | write_file | get_cash_flow_statements |
| DESC | Create new file or overwrite existing | Get cash flow statements for a company. |
| PARAMETERS | path: (string) File location<br>content: (string) File content |  |
| SCORES(SERVER/TOOL/FINAL) | 0.452/0.551/0.138 | 0.531/0.634/0.213 |
| RANKS(SERVER/TOOL/FINAL) | 61/37/42 | 1/1/1 |
## ANALYSIS

# BAD CASE 106
## TASK
Create a new documentation page in the team's knowledge base with the title "Project Onboarding Guide" and include sections for setup instructions, common issues, and contact information.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Atlassian | Graphlit |
| TOOL | confluence_create_page | Configure Project |
| DESC | Create a new page | Configures a project in the knowledge base. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.534/0.603/0.194 | 0.547/0.684/0.256 |
| RANKS(SERVER/TOOL/FINAL) | 22/6/8 | 13/1/1 |
## ANALYSIS

# BAD CASE 107
## TASK
Push three configuration files (config.json, settings.yaml, and env.properties) to the "main" branch of the "project-x" repository under the owner "dev-team" with the commit message "Update configuration files".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | GitHub | llm-context |
| TOOL | push_files | lc-init |
| DESC | Push multiple files in a single commit | Initialize project configuration |
| PARAMETERS | owner: (string) Repository owner<br>repo: (string) Repository name<br>branch: (string) Branch to push to<br>files: (array) Files to push, each with `path` and `content`<br>message: (string) Commit message |  |
| SCORES(SERVER/TOOL/FINAL) | 0.455/0.615/0.172 | 0.609/0.631/0.242 |
| RANKS(SERVER/TOOL/FINAL) | 82/3/13 | 2/2/1 |
## ANALYSIS

# BAD CASE 108
## TASK
Search for the latest research papers on quantum computing published in the last month, displaying results in English with moderate safe search filtering.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | SearXNG | Tavily search |
| TOOL | searxng_web_search | tavily_news_search |
| DESC | Execute web searches with pagination | Searches recent news articles with publication dates. |
| PARAMETERS | query: (string) The search query. This string is passed to external search services.<br>pageno: (Optional, number) Search page number, starts at 1 (default 1)<br>time_range: (Optional, string) Filter results by time range - one of: 'day', 'month', 'year' (default: none)<br>language: (Optional, string) Language code for results (e.g., 'en', 'fr', 'de') or 'all' (default: 'all')<br>safesearch: (Optional, number) Safe search filter level (0: None, 1: Moderate, 2: Strict) (default: instance setting) | query: (string, required) Search query<br>max_results: (integer, optional) Maximum number of results to return (default: 5, max: 20)<br>days: (integer, optional) Number of days back to search (default: 3)<br>include_domains: (list or string, optional) List of domains to specifically include in results<br>exclude_domains: (list or string, optional) List of domains to exclude from results |
| SCORES(SERVER/TOOL/FINAL) | 0.462/0.456/0.097 | 0.511/0.634/0.206 |
| RANKS(SERVER/TOOL/FINAL) | 42/272/209 | 5/1/1 |
## ANALYSIS

# BAD CASE 111
## TASK
Retrieve the details of the import error with ID "ERR-2024-0015".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Airflow | Airflow |
| TOOL | Get Import Error Details | Get Import Error Details |
| DESC | Gets details of a specific import error. | Gets details of a specific import error. |
| PARAMETERS | import_error_id: (string) The ID of the import error. | import_error_id: (string) The ID of the import error. |
| SCORES(SERVER/TOOL/FINAL) | 0.350/0.742/0.192 | 0.350/0.742/0.192 |
| RANKS(SERVER/TOOL/FINAL) | 236/1/1 | 236/1/1 |
## ANALYSIS

# BAD CASE 113
## TASK
List all files and subfolders within the folder with ID "F12345" recursively.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Box | Terminal-Control |
| TOOL | box_list_folder_content_by_folder_id | list_directory |
| DESC | List folder contents. | List files and subdirectories in the specified directory. |
| PARAMETERS | folder_id: (str) ID of the folder<br>is_recursive: (bool) Whether to list recursively | path: (Optional, string) Directory path to list contents (default: current directory) |
| SCORES(SERVER/TOOL/FINAL) | 0.405/0.690/0.193 | 0.471/0.717/0.242 |
| RANKS(SERVER/TOOL/FINAL) | 116/4/9 | 10/1/1 |
## ANALYSIS

# BAD CASE 114
## TASK
List all available datasets in the connected database.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Airflow | ClickHouse |
| TOOL | List Datasets | list_tables |
| DESC | Lists all datasets. | List all tables in a database. |
| PARAMETERS |  | database: (string) The name of the database. |
| SCORES(SERVER/TOOL/FINAL) | 0.484/0.861/0.359 | 0.626/0.825/0.426 |
| RANKS(SERVER/TOOL/FINAL) | 107/1/7 | 2/2/1 |
## ANALYSIS

# BAD CASE 115
## TASK
Apply the extracted configuration overrides to the specified target instances.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Talk To Figma | Talk To Figma |
| TOOL | set_instance_overrides | set_instance_overrides |
| DESC | Apply extracted overrides to target instances | Apply extracted overrides to target instances |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.399/0.909/0.330 | 0.399/0.909/0.330 |
| RANKS(SERVER/TOOL/FINAL) | 245/1/1 | 245/1/1 |
## ANALYSIS

# BAD CASE 116
## TASK
Retrieve all comments associated with the latest published post.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | CoinMarketCap | HDW LinkedIn |
| TOOL | contentPostsComments | get_linkedin_post_comments |
| DESC | Get comments for a specific post | Retrieve comments for a LinkedIn post. |
| PARAMETERS |  | urn: (required)<br>sort: (optional, default: relevance; allowed values: relevance, recent)<br>count: (optional, default: 10)<br>timeout: (optional, default: 300) |
| SCORES(SERVER/TOOL/FINAL) | 0.432/0.701/0.213 | 0.468/0.745/0.260 |
| RANKS(SERVER/TOOL/FINAL) | 96/4/6 | 34/1/1 |
## ANALYSIS

# BAD CASE 118
## TASK
Delete all documents from the 'users' collection where the 'status' field is set to 'inactive'.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | MongoDB | Ghost |
| TOOL | delete-many | Delete User |
| DESC | Delete multiple documents from a MongoDB collection | Remove a user. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.412/0.594/0.145 | 0.500/0.649/0.211 |
| RANKS(SERVER/TOOL/FINAL) | 67/33/51 | 3/6/1 |
## ANALYSIS

# BAD CASE 119
## TASK
Execute a PromQL query to retrieve the current CPU usage percentage of all nodes in the Kubernetes cluster.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Prometheus | Kubernetes and OpenShift |
| TOOL | execute_query | resources_get |
| DESC | Execute a PromQL instant query against Prometheus | Get a Kubernetes resource in the current cluster |
| PARAMETERS | query: (string) The PromQL query to execute | apiVersion: (Required, string) apiVersion of the resource (e.g., v1, apps/v1, networking.k8s.io/v1)<br>kind: (Required, string) kind of the resource (e.g., Pod, Service, Deployment, Ingress)<br>name: (Required, string) Name of the resource<br>namespace: (Optional, string) Namespace to retrieve the namespaced resource from. Ignored for cluster-scoped resources. Uses configured namespace if not provided. |
| SCORES(SERVER/TOOL/FINAL) | 0.582/0.604/0.212 | 0.557/0.682/0.259 |
| RANKS(SERVER/TOOL/FINAL) | 1/15/8 | 4/1/1 |
## ANALYSIS

# BAD CASE 120
## TASK
List all available pools in the system.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Airflow | Airflow |
| TOOL | List Pools | List Pools |
| DESC | Lists all pools. | Lists all pools. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.432/0.910/0.358 | 0.432/0.910/0.358 |
| RANKS(SERVER/TOOL/FINAL) | 178/1/1 | 178/1/1 |
## ANALYSIS

# BAD CASE 121
## TASK
Create a new directory named "project_assets" within the current workspace.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | PIF | TickTick |
| TOOL | mkdir | create_project |
| DESC | Navigate and manage workspace context | Create a new project |
| PARAMETERS |  | name: (string) Project name<br>color: (optional string) Project color (default: '#4772FA')<br>viewMode: (optional string) View mode ('list', 'kanban', 'timeline') (default: 'list')<br>kind: (optional string) Project kind ('TASK', 'NOTE') (default: 'TASK') |
| SCORES(SERVER/TOOL/FINAL) | 0.554/0.607/0.204 | 0.523/0.698/0.255 |
| RANKS(SERVER/TOOL/FINAL) | 2/56/19 | 7/1/1 |
## ANALYSIS

# BAD CASE 123
## TASK
Retrieve the details of the document generation template with the identifier "TMPL12345".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Box | eSignatures |
| TOOL | box_docgen_template_get_by_id_tool | query_template |
| DESC | Retrieve details of a specific Doc Gen template. | Retrieve template content and info |
| PARAMETERS | template_id: (str) The template identifier |  |
| SCORES(SERVER/TOOL/FINAL) | 0.344/0.731/0.184 | 0.454/0.710/0.229 |
| RANKS(SERVER/TOOL/FINAL) | 278/1/3 | 57/2/1 |
## ANALYSIS

# BAD CASE 124
## TASK
Retrieve the user details associated with the email address "user@example.com".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ServiceNow | EduBase |
| TOOL | get_user | edubase_get_user |
| DESC | Get a specific user by ID, username, or email | Retrieves user information from the EduBase platform. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.380/0.670/0.170 | 0.679/0.708/0.340 |
| RANKS(SERVER/TOOL/FINAL) | 279/11/83 | 1/3/1 |
## ANALYSIS

# BAD CASE 126
## TASK
Compare the schemas of two specified collections to identify any differences in their structure.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | MongoDB Lens | MongoDB Lens |
| TOOL | compare-schemas | compare-schemas |
| DESC | Compare schemas between two collections | Compare schemas between two collections |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.376/0.908/0.310 | 0.376/0.908/0.310 |
| RANKS(SERVER/TOOL/FINAL) | 161/1/1 | 161/1/1 |
## ANALYSIS

# BAD CASE 128
## TASK
Retrieve the full details of the place identified by PlaceId "PL123456789".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | AWS | Travel Planner |
| TOOL | Get Details for Specific Places | getPlaceDetails |
| DESC | Get details for specific places by PlaceId. | Get detailed information about a specific place |
| PARAMETERS |  | placeId: (string) Google Place ID to retrieve details for |
| SCORES(SERVER/TOOL/FINAL) | 0.341/0.813/0.225 | 0.534/0.679/0.246 |
| RANKS(SERVER/TOOL/FINAL) | 236/1/2 | 2/4/1 |
## ANALYSIS

# BAD CASE 129
## TASK
Retrieve the value of the variable associated with the key "user_session_token".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Airflow | EduBase |
| TOOL | Get Variable | edubase_get_user |
| DESC | Gets a specific variable. | Retrieves user information from the EduBase platform. |
| PARAMETERS | variable_key: (string) The key of the variable. |  |
| SCORES(SERVER/TOOL/FINAL) | 0.400/0.630/0.159 | 0.590/0.623/0.229 |
| RANKS(SERVER/TOOL/FINAL) | 237/15/57 | 1/17/1 |
## ANALYSIS

# BAD CASE 132
## TASK
Read the contents of a binary file named "data.dat" located in the "/documents" directory.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | AWS | Filesystem |
| TOOL | File Access with Text and Binary Support | read_file |
| DESC | Access files with text and binary support. | Read complete contents of a file |
| PARAMETERS |  | path: (string) File path |
| SCORES(SERVER/TOOL/FINAL) | 0.435/0.689/0.206 | 0.584/0.641/0.240 |
| RANKS(SERVER/TOOL/FINAL) | 148/1/9 | 1/7/1 |
## ANALYSIS

# BAD CASE 133
## TASK
Remove the document with the key "user123" from the "customers" collection.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ArangoDB | Ghost |
| TOOL | arango_remove | Delete User |
| DESC | Remove documents from collections | Remove a user. |
| PARAMETERS | collection: (string) Collection name<br>key: (string) Document key |  |
| SCORES(SERVER/TOOL/FINAL) | 0.365/0.619/0.140 | 0.484/0.681/0.224 |
| RANKS(SERVER/TOOL/FINAL) | 146/10/35 | 4/1/1 |
## ANALYSIS

# BAD CASE 134
## TASK
Update or insert a document with the ID "user_12345" into the "customers" collection within the "ecommerce" scope. Ensure the document contains the latest customer details including name, email, and purchase history.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Couchbase | Shopify |
| TOOL | upsert_document_by_id | update-customer |
| DESC | Upsert a document by ID to a specified scope and collection. | Update a customer's information |
| PARAMETERS |  | id: (string, required) Shopify customer ID (numeric ID only, like "6276879810626")<br>firstName: (string, optional) Customer's first name<br>lastName: (string, optional) Customer's last name<br>email: (string, optional) Customer's email address<br>phone: (string, optional) Customer's phone number<br>tags: (array of strings, optional) Tags to apply to the customer<br>note: (string, optional) Note about the customer<br>taxExempt: (boolean, optional) Whether the customer is exempt from taxes<br>metafields: (array of objects, optional) Customer metafields for storing additional data |
| SCORES(SERVER/TOOL/FINAL) | 0.484/0.612/0.181 | 0.632/0.712/0.320 |
| RANKS(SERVER/TOOL/FINAL) | 94/8/27 | 1/1/1 |
## ANALYSIS

# BAD CASE 137
## TASK
List all document generation jobs that used template ID "TMPL12345", showing a maximum of 50 jobs per page. If there are more results, use the provided pagination marker to fetch the next batch.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Box | Outline |
| TOOL | box_docgen_template_list_jobs_tool | Read a Document |
| DESC | List all Doc Gen jobs that used a specific template. | Get the content of a document by its ID. |
| PARAMETERS | template_id: (str) The template identifier<br>marker: (str | None, optional) Pagination marker<br>limit: (int | None, optional) Maximum number of jobs to list | docId: (string) The ID of the document to read. |
| SCORES(SERVER/TOOL/FINAL) | 0.401/0.641/0.165 | 0.577/0.562/0.187 |
| RANKS(SERVER/TOOL/FINAL) | 243/1/17 | 1/24/1 |
## ANALYSIS

# BAD CASE 138
## TASK
List all active documents in workspace "WS123" created by "user1", excluding deleted and archived items, with a limit of 50 documents per page.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | ClickUp | SingleStore |
| TOOL | list_documents | list_virtual_workspaces |
| DESC | List documents | List all starter workspaces accessible to the user |
| PARAMETERS | workspaceId: (string) The ID of the workspace<br>documentId: (Optional, string) The ID of the document<br>creator: (Optional, string) The creator of the document<br>deleted: (Optional, boolean) Whether to include deleted documents<br>archived: (Optional, boolean) Whether to include archived documents<br>parent_id: (Optional, string) The ID of the parent item<br>parent_type: (Optional, string) The type of the parent item<br>limit: (Optional, integer) The maximum number of documents to return<br>next_cursor: (Optional, string) The cursor for pagination |  |
| SCORES(SERVER/TOOL/FINAL) | 0.528/0.597/0.188 | 0.629/0.626/0.248 |
| RANKS(SERVER/TOOL/FINAL) | 12/12/18 | 1/5/1 |
## ANALYSIS

# BAD CASE 139
## TASK
Update the document with ID "user123" in the "customers" collection by changing the "status" field to "active".
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Firebase | Shopify |
| TOOL | firestore_update_document | update-customer |
| DESC | Update an existing document | Update a customer's information |
| PARAMETERS | collection: (string) The name of the collection<br>id: (string) The ID of the document<br>data: (object) The data to update in the document | id: (string, required) Shopify customer ID (numeric ID only, like "6276879810626")<br>firstName: (string, optional) Customer's first name<br>lastName: (string, optional) Customer's last name<br>email: (string, optional) Customer's email address<br>phone: (string, optional) Customer's phone number<br>tags: (array of strings, optional) Tags to apply to the customer<br>note: (string, optional) Note about the customer<br>taxExempt: (boolean, optional) Whether the customer is exempt from taxes<br>metafields: (array of objects, optional) Customer metafields for storing additional data |
| SCORES(SERVER/TOOL/FINAL) | 0.457/0.671/0.206 | 0.612/0.726/0.322 |
| RANKS(SERVER/TOOL/FINAL) | 148/7/22 | 1/2/1 |
## ANALYSIS

# BAD CASE 140
## TASK
Generate a detailed summary of the key themes and insights from the provided research paper on renewable energy technologies.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | HuggingFace Spaces | Deepseek_R1 |
| TOOL | use Qwen2.5-72B-Instruct | deepseek_r1 |
| DESC | Provides chat capabilities using the `Qwen/Qwen2.5-72B-Instruct` space. | Generates advanced text using the Deepseek R1 model with configurable parameters. |
| PARAMETERS |  | prompt: (string) The input prompt for text generation<br>max_tokens: (number) Maximum tokens to generate<br>temperature: (number) Controls randomness, default is 0.2 |
| SCORES(SERVER/TOOL/FINAL) | 0.320/0.402/0.052 | 0.454/0.495/0.111 |
| RANKS(SERVER/TOOL/FINAL) | 200/297/578 | 2/7/1 |
## ANALYSIS

# BAD CASE 141
## TASK
Delete the resource located at `https://api.example.com/users/123` with the header `Authorization: Bearer token123`.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Rquest | Ghost |
| TOOL | http_delete | Delete User |
| DESC | Remove resources with DELETE requests | Remove a user. |
| PARAMETERS | url: (string) The URL to send the DELETE request to<br>headers: (Optional, dict) Additional headers to include in the request<br>cookies: (Optional, dict) Cookies to include in the request |  |
| SCORES(SERVER/TOOL/FINAL) | 0.440/0.613/0.165 | 0.502/0.640/0.206 |
| RANKS(SERVER/TOOL/FINAL) | 65/2/8 | 9/1/1 |
## ANALYSIS

# BAD CASE 143
## TASK
List all available contacts in the address book.
## DETAILS
| Item | TARGET | MATCHED |
| ---- | ------ | ------- |
| SERVER | Telegram | Telegram |
| TOOL | list_contacts | list_contacts |
| DESC | List all contacts. | List all contacts. |
| PARAMETERS |  |  |
| SCORES(SERVER/TOOL/FINAL) | 0.454/0.929/0.392 | 0.454/0.929/0.392 |
| RANKS(SERVER/TOOL/FINAL) | 106/1/1 | 106/1/1 |
## ANALYSIS

