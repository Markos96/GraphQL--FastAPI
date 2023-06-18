from app.config.db import SessionLocal
from graphql import GraphQLError
from fastapi import status
from app.model.player import Player

session = SessionLocal()


def savePlayer(playerInput):
    try:
        player = Player(**playerInput)
        session.add(player)
        session.commit()
        return player
    except Exception as e:
        session.rollback()
        raise GraphQLError(str(e))


def getByPlayer(playerID):
    try:
        player = session.query(Player).get(playerID)

        if not player:
            raise GraphQLError("Player not found",
                               extensions={"code": status.HTTP_404_NOT_FOUND})
        return player
    except Exception as e:
        session.rollback()
        raise GraphQLError(str(e))


def getAllPlayers():
    try:
        players = session.query(Player).all()
        return players
    except Exception as e:
        session.rollback()
        raise GraphQLError(str(e))


def modifyPlayer(playerInput, playerID):
    try:
        player = session.query(Player).get(playerID)

        if not player:
            raise GraphQLError("Player not found",
                               extensions={"code": status.HTTP_404_NOT_FOUND})

        for key, value in playerInput.items():
            if hasattr(player, key) and value is not None:
                setattr(player, key, value)

        session.commit()
        return player

    except Exception as e:
        session.rollback()
        raise GraphQLError(str(e))


def deletePlayer(playerID):
    try:
        player = session.query(Player).get(playerID)

        if not player:
            raise GraphQLError("Player not found",
                               extensions={"code": status.HTTP_404_NOT_FOUND})

        session.delete(player)
        session.commit()
    except Exception as e:
        session.rollback()
        raise GraphQLError(str(e))


def getPlayerByTeam(teamID):
    try:
        players = session.query(Player).filter(Player.id_team == teamID).all()

        if not players:
            raise GraphQLError("Player not found",
                               extensions={"code": status.HTTP_404_NOT_FOUND})
        return players
    except Exception as e:
        session.rollback()
        raise GraphQLError(str(e))