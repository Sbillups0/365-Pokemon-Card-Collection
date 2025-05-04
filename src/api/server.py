from fastapi import FastAPI
from src.api import inventory, catalog #carts, bottler, barrels, admin, info
from starlette.middleware.cors import CORSMiddleware
#NOTE FROM SHANE: STILL NEEDS TO BE MODIFIED, CONFUSED AS TO HOW.

description = """
Buy some cards and stuff, or don't...
"""
tags_metadata = [
    {
        "name": "inventory",
        "description": "Get the current inventory of shop and buying capacity.",
    },
    {
        "name": "catalog",
        "description": "Get the current catalog of packs.",
    }
]

app = FastAPI(
    title="Pokemon-Card-Collection",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Shane Billups",
        "email": "sbillups@calpoly.edu",
    },
    openapi_tags=tags_metadata,
)

origins = ["https://potion-exchange.vercel.app"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "OPTIONS"],
    allow_headers=["*"],
)

app.include_router(inventory.router)
app.include_router(catalog.router)



@app.get("/")
async def root():
    return {"message": "Pokemon cards are ready for collecting!"}
