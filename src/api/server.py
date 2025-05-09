from fastapi import FastAPI
from src.api import inventory, catalog, packs, user, collection, cards  # carts, bottler, barrels, admin, info

from starlette.middleware.cors import CORSMiddleware
#NOTE FROM SHANE: STILL NEEDS TO BE MODIFIED, CONFUSED AS TO HOW.

description = """
Buy some cards and stuff, or don't...
"""
# OpenAPI descriptions and info for the API documentation
tags_metadata = [
    {
        "name": "inventory",
        "description": "Get the current inventory of packs owned by user",
    },
    {
        "name": "catalog",
        "description": "Get the current catalog of packs available to purchase.",
    },
    {
        "name": "packs",
        "description": "Purchase packs from the current catalog and add them to inventory."
    },
    {
        "name": "users",
        "description": "Register a new user that could buy and keep inventory of packs"
    },
    {
        "name": "collection",
        "description": "View the current collection of cards owned by user, if Type is specified, only cards of that type will be returned."
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
app.include_router(packs.router)
app.include_router(user.router)
app.include_router(collection.router)
app.include_router(cards.router)



@app.get("/")
async def root():
    return {"message": "Pokemon cards are ready for collecting!"}
