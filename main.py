from fastapi import FastAPI , HTTPException , Query , Depends
from fastapi.middleware.cors import CORSMiddleware
from app.routers import users
from app.routers import auth


app  = FastAPI();

app.include_router(users.router)
app.include_router(auth.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




