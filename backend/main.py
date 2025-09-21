from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import data_handler
import logging
import os

os.makedirs("logs", exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%d-%m-%Y %I:%M:%S %p",
    filename="logs/app.log",
    filemode="a"
)

app = FastAPI(
    title="PDF AI Query Assistant",
    description="Api for uploading PDFs, querying content via LLM, and managing data",
    version="1.0.0"
)


app.include_router(
    data_handler.router,
    prefix="/api/v1",
    tags=["Data Handling And Chat With PDF"]
)

@app.get("/", response_class=HTMLResponse, tags=["Root"])
def read_root():
    """
    Provides a simple HTML welcome page with a link to the swagger (OpenAPI) docs
    """
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
    <title> PDF AI Query Assistant </title>
    <style>
    body { font-family: Arial, sans-serif; padding: 2rem; background: #f9f9f9; }
    .container { max-width: 600px; margin: auto; background: #fff; padding: 2rem; }
    h1 { color: #333; }
    a { color: #007acc; text-decoration: none; }
    a:hover { text-decoration: underline; }
    </style>
    </head>
    <body>
        <div class="container">
         <h1>Welcome to the PDF AI Query Assistant</h1>
         <p>View the automatically generated API documentation here:</p>
         <p><a href="/docs" target="_blank">Swagger UI (OpenAPI Docs)</a></p>
       </div>
      </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app, host="127.0.0.1", port=8000
    )