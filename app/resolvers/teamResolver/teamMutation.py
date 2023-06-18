from ariadne import MutationType
from app.repository.team import team

mutation = MutationType()


@mutation.field("createTeam")
def resolverCreateTeam(obj, info, teamInput):
    return team.saveTeam(teamInput)


@mutation.field("modifiedTeam")
def resolverModifiedTeam(obj, info, teamInput, teamID):
    return team.modifiedTeam(teamInput, teamID)


@mutation.field("deleteTeam")
def resolverDeleteTeam(obj, info, teamID):
    return team.deleteTeam(teamID)


mutation_resolvers = {
    "createTeam": resolverCreateTeam,
    "modifiedTeam": resolverModifiedTeam,
    "deleteTeam": resolverDeleteTeam
}