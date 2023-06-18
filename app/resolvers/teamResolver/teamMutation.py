from ariadne import MutationType
from app.repository.team import team

mutation = MutationType()


@mutation.field("createTeam")
def resolveCreateTeam(obj, info, teamInput):
    return team.saveTeam(teamInput)


@mutation.field("modifiedTeam")
def resolveModifiedTeam(obj, info, teamInput, teamID):
    return team.modifiedTeam(teamInput, teamID)


@mutation.field("deleteTeam")
def resolveDeleteTeam(obj, info, teamID):
    return team.deleteTeam(teamID)


mutation_resolvers = {
    "createTeam": resolveCreateTeam,
    "modifiedTeam": resolveModifiedTeam,
    "deleteTeam": resolveDeleteTeam
}