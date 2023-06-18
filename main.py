from ariadne import QueryType, MutationType, make_executable_schema
from ariadne.asgi import GraphQL
from fastapi import FastAPI
from app.resolvers.teamResolver import teamMutation, teamQueries
from app.resolvers.playerResolver import playerMutation, playerQueries
from app.resolvers.leagueResolver import leagueMutation, leagueQueries
from fastapi.middleware.cors import CORSMiddleware
from app.schema.types import type_defs
import uvicorn


query = QueryType()
mutation = MutationType()


# Queries player

query.set_field("players", playerQueries.resolverGetAllPlayers)
query.set_field("player", playerQueries.resolverGetPlayerById)
query.set_field("playersByTeam", playerQueries.resolverGetPlayersByTeam)


# Queries team

query.set_field("teams", teamQueries.resolverGetAllTeams)
query.set_field("team", teamQueries.resolverGetTeam)


# Queries league

query.set_field("leagues", leagueQueries.resolverGetAllLeagues)
query.set_field("league", leagueQueries.resolverGetLeague)


# Mutations player
mutation.set_field("createPlayer", playerMutation.resolverSavePlayer)
mutation.set_field("modifiedPlayer", playerMutation.resolverModifiedPlayer)
mutation.set_field("deletePlayer", playerMutation.resolverDeletePlayer)


# Mutations team
mutation.set_field("createTeam", teamMutation.resolverCreateTeam)
mutation.set_field("modifiedTeam", teamMutation.resolverModifiedTeam)
mutation.set_field("deleteTeam", teamMutation.resolverDeleteTeam)


# Mutations league
mutation.set_field("createLeague", leagueMutation.resolverCreateLeague)


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

