from app.config.db import SessionLocal
from app.model.league import League
from graphql import GraphQLError

session = SessionLocal()


def create_league(leagueInput):
    league = League(name=leagueInput.get("name"))

    session.add(league)
    session.commit()


def modified_league(leagueInput, leagueID):
    try:
        league = session.query(League).get(leagueID)

        if not league:
            raise GraphQLError("The database does not contain players",
                               extensions={"code": 404})

        for key, value in leagueInput.items():
            if hasattr(league, key) and value is not None:
                setattr(league, key, value)

        session.commit()

    except Exception as error:
        raise Exception(f"Occurred during from database {error}")

    return league

