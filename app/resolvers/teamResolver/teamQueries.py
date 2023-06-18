from ariadne import QueryType
from app.repository.team import team

query = QueryType()


@query.field("team")
def resolverGetTeam(obj, info, teamID):
    return team.getByTeam(teamID)


@query.field("teams")
def resolverGetAllTeams(obj, info):
    return team.getAllTeams()

