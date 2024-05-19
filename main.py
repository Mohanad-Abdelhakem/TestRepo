import os
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
templates = Jinja2Templates(directory=parent_directory)


@app.get("/")
async def main_page(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
