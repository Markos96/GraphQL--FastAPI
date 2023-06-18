from ariadne import QueryType
from app.repository.league import league

query = QueryType()


@query.field("leagues")
def resolverGetAllLeagues(obj, info):
    leagues = league.getAllLeagues()
    return leagues


@query.field("league")
def resolverGetLeague(obj, info, leagueID):
    leagues = league.getLeague(leagueID)
    return leagues
