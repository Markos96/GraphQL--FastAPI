from ariadne import MutationType
from app.repository.player import player

mutation = MutationType()


@mutation.field("createPlayer")
def resolveSavePlayer(obj, info, playerInput):
    return player.savePlayer(playerInput)


@mutation.field("modifiedPlayer")
def resolveModifiedPlayer(obj, info, playerInput, playerID):
    return player.modifyPlayer(playerInput, playerID)


@mutation.field("deletePlayer")
def resolveDeletePlayer(obj, info, playerID):
    return player.deletePlayer(playerID)


mutation_resolvers = {
    "createPlayer": resolveSavePlayer,
    "modifiedPlayer": resolveModifiedPlayer,
    "deletePlayer": resolveDeletePlayer
}
