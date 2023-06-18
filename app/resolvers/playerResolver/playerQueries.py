from ariadne import QueryType
from app.repository.player import player

query = QueryType()


@query.field("players")
def resolveGetAllPlayers(obj, info):
    return player.getAllPlayers()


@query.field("player")
def resolveGetPlayerById(obj, info, playerID):
    return player.getByPlayer(playerID)


@query.field("playersByTeam")
def resolveGetPlayersByTeam(obj, info, teamID):
    return player.getPlayerByTeam(teamID)

