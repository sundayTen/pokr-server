import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.auth.api import router as auth_router
from api.index import router as index_router
from api.initiatives.api import router as initiative_router
from api.me.api import router as me_router
from api.objectives.api import router as objective_router
from api.reviews.api import router as review_router
from api.templates.api import router as template_router
from db.config import Base, engine
from env import ENVIRONMENT

Base.metadata.create_all(bind=engine)
app = FastAPI(docs_url="/api/docs", redoc_url="/api/redoc")

origins = ["http://127.0.0.1:3000", "http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(index_router, tags=["INDEX"], prefix="/api")
app.include_router(auth_router, tags=["AUTH"], prefix="/api/auth")
app.include_router(initiative_router, tags=["INITIATIVE"], prefix="/api/initiatives")
app.include_router(me_router, tags=["ME"], prefix="/api/me")
app.include_router(objective_router, tags=["OBJECTIVE"], prefix="/api/objectives")
app.include_router(review_router, tags=["REVIEW"], prefix="/api/reviews")
app.include_router(template_router, tags=["TEMPLATE"], prefix="/api/templates")

if __name__ == "__main__":
    if ENVIRONMENT == "local":
        uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
    else:
        uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=False)
