from ariadne import MutationType
from app.repository.league import league

mutation = MutationType()

@mutation.field("createLeague")
def resolverCreateLeague(obj, info, leagueInput):
    return league.createLeague(leagueInput)

mutation_resolvers = {
    "createLeague": resolverCreateLeague
}