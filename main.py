from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from config.DataBase import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.users import user_router




app = FastAPI()
app.title= "Proyecto Platzi"


app.add_middleware(ErrorHandler)

app.include_router(movie_router)
app.include_router(user_router)



Base.metadata.create_all(bind=engine)



movies = [
    {
		"id": 1,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Navi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	},
    {
		"id": 2,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	}
]

@app.get("/", tags=['home'])
def message():
    return {"Hello": "World"}




