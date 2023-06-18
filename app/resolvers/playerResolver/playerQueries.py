from ariadne import QueryType
from app.repository.player import player

query = QueryType()


@query.field("players")
def resolverGetAllPlayers(obj, info):
    return player.getAllPlayers()


@query.field("player")
def resolverGetPlayerById(obj, info, playerID):
    return player.getByPlayer(playerID)


@query.field("playersByTeam")
def resolverGetPlayersByTeam(obj, info, teamID):
    return player.getPlayerByTeam(teamID)

