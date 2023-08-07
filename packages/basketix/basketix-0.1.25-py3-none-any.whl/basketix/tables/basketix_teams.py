"""Basketix teams table"""

from .dynamodb_table import DynamoDBTable
from ..models import BasketixTeamsModel

class BasketixTeamsTable(DynamoDBTable[BasketixTeamsModel]):
    def __init__(self, environment: str):
        DynamoDBTable.__init__(self, 'basketix-teams', environment,  'weekId', 'teamId')
