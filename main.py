from ariadne import QueryType, MutationType, make_executable_schema
from ariadne.asgi import GraphQL
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schema.types import type_defs
import uvicorn


query = QueryType()
mutation = MutationType()

schema = make_executable_schema(type_defs, query, mutation)

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_route("/graphql", GraphQL(schema=schema))

if __name__ == '__main__':
    uvicorn.run(app, port=8000)

