from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi. responses import HTMLResponse, RedirectResponse
from typing import Annotated
from uuid import uuid4

nota = []

templateJinja = Jinja2Templates(directory='templates')

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templateJinja.TemplateResponse("index.html", { "request": request, "notas_list": nota})


@app.get("/notas/delete", response_class=RedirectResponse)
def delete_nota(nota_id: str):
    for notas in nota:
        if nota_id == str(notas["id"]):
            nota.remove(notas)
    return RedirectResponse("/", status_code=303) 


@app.post("/notas/add", response_class=RedirectResponse)
def create_nota(posit_name: Annotated[str, Form()]):
    new_nota = {
        "id": uuid4(),
        "name": posit_name
    } 
    nota.append(new_nota)
    return RedirectResponse("/", status_code=303)


#Mini-Stick	Como un post-it digital pequeño.
#python -m venv venv
#venv\Scripts\activate
#pip install fastapi uvicorn 
#uvicorn main:app --reload