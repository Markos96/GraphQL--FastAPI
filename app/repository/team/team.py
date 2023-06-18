from app.config.db import SessionLocal
from app.model.team import Team
from fastapi import status
from graphql import GraphQLError


session = SessionLocal()


def saveTeam(teamInput):
    try:
        team = Team(**teamInput)
        session.add(team)
        session.commit()
        session.refresh(team)
        return team
    except:
        session.rollback()
        raise GraphQLError("Error saving team")


def getByTeam(teamID):
    try:
        team = session.query(Team).get(teamID)

        if not team:
            raise GraphQLError("Team not found",
                               extensions={"code": status.HTTP_404_NOT_FOUND})

        return team
    except:
        session.rollback()
        raise GraphQLError("Error getting team")


def getAllTeams():
    try:
        teams = session.query(Team).all()
        return teams
    except:
        session.rollback()
        raise GraphQLError("Error getting teams")


def modifiedTeam(teamInput, teamID):
    try:
        team = session.query(Team).get(teamID)

        if not team:
            raise GraphQLError("Team not found",
                               extensions={"code": status.HTTP_404_NOT_FOUND})

        for key, value in teamInput.items():
            if hasattr(team, key) and value is None:
                setattr(team, key, value)

        session.commit()
        session.refresh(team)
        return team
    except:
        session.rollback()
        raise GraphQLError("Error saving team")


def deleteTeam(teamID):
    try:
        team = session.query(Team).get(teamID)

        if not team:
            raise GraphQLError("Team not found",
                               extensions={"code": status.HTTP_404_NOT_FOUND})

        session.delete(team)
        session.commit()
    except:
        session.rollback()
        raise GraphQLError("Error deleting team")