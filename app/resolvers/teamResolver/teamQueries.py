from ariadne import QueryType
from app.repository.team import team

query = QueryType()


@query.field("team")
def resolveGetTeam(obj, info, teamID):
    return team.getByTeam(teamID)


@query.field("teams")
def resolveGetAllTeams(obj, info):
    return team.getAllTeams()

