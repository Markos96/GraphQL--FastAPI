from ariadne import MutationType
from app.repository.player import player

mutation = MutationType()


@mutation.field("createPlayer")
def resolverSavePlayer(obj, info, playerInput):
    return player.savePlayer(playerInput)


@mutation.field("modifiedPlayer")
def resolverModifiedPlayer(obj, info, playerInput, playerID):
    return player.modifyPlayer(playerInput, playerID)


@mutation.field("deletePlayer")
def resolverDeletePlayer(obj, info, playerID):
    return player.deletePlayer(playerID)


mutation_resolvers = {
    "createPlayer": resolverSavePlayer,
    "modifiedPlayer": resolverModifiedPlayer,
    "deletePlayer": resolverDeletePlayer
}
