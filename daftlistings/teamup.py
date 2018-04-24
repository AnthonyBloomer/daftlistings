from .enums import TeamUpWith, TeamupSearch, QueryParam, County
from .exceptions import DaftInputException
from .request import Request
from .person import Person


class Teamup(object):

    def __init__(self):
        self.url = "http://www.daft.ie/searchteamup.daft?"
        self.team_up_with = TeamUpWith.ANY
        self.move_in_date = 0
        self.county = County.ALL
        self.query_params = ""
        self.rent = ""

    def set_team_up_with(self, team_up_with):
        """
        Who would you like to team up with?
        :param team_up_with: TeamUpWith
        :return:
        """
        if not isinstance(team_up_with, TeamUpWith):
            raise DaftInputException("team_up_with should be an instance of TeamUpWith")
        self.team_up_with = str(TeamupSearch.TEAM_UP_WITH) + str(team_up_with)

    def set_county(self, county):
        """
        What county do you live in?
        :param county: County
        :return:
        """
        self.county = str(TeamupSearch.COUNTY) + str(county) + str(TeamupSearch.AREA)

    def set_rent(self, rent):
        """
        How much rent would you be willing to pay each per month?
        :param rent: int
        :return:
        """
        self.rent = str(TeamupSearch.RENT) + str(rent)

    def set_move_in_date(self, move_in_date):
        """
        When would you be ready to start looking for a place?
        :param move_in_date: int
        :return:
        """
        self.move_in_date = str(TeamupSearch.MOVE_IN_DATE) + str(move_in_date)

    def get_results(self):
        """
        This function returns a list of Person objects.
        :return:
        """
        search_results = []
        self.query_params += str(self.county) + str(self.move_in_date) + str(self.team_up_with)
        self.url += self.query_params + str(QueryParam.FIND_TEAMUPS)
        request = Request()
        soup = request.get(self.url)
        results = soup.find_all('table', {'class': 'tenant_result'})
        [search_results.append(Person(result)) for result in results]
        return search_results
