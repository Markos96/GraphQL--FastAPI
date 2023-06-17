from ariadne import QueryType
from app.repository import league

query = QueryType()

@query.field("leagues")
def resolveGetLeagues(obj, info):
    return leagues