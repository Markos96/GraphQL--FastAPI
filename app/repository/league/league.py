from app.config.db import SessionLocal
from app.model.league import League
from graphql import GraphQLError
from fastapi import status

session = SessionLocal()


def createLeague(leagueInput):
    try:
        league = League(**leagueInput)
        session.add(league)
        session.commit()
        return league

    except:
        session.rollback()
        raise GraphQLError('Could not create league')


def getLeague(leagueID):
    try:
        league = session.query(League).get(leagueID)

        if not league:
            raise GraphQLError('League not found',
                           extensions={"code": status.HTTP_404_NOT_FOUND})

        return league

    except:
        session.rollback()
        raise GraphQLError('Error getting league',
                           extensions={"code": status.HTTP_500_INTERNAL_SERVER_ERROR})


def getAllLeagues():
    try:
        leagues = session.query(League).all()
        return leagues

    except:
        session.rollback()
        raise GraphQLError('Error getting leagues',
                           extensions={"code": status.HTTP_500_INTERNAL_SERVER_ERROR})

