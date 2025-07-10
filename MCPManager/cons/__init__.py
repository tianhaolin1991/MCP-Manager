import os

## proxy settings
os.environ["HTTP_PROXY"] = "http://127.0.0.1:7890"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7890"
os.environ["NO_PROXY"] = "localhost,127.0.0.1"