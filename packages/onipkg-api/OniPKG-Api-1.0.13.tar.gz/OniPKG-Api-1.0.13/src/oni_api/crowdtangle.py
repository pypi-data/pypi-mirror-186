import requests
import datetime


class CrowdTangle:
    """
    Classe que faz o request do endpoint e retorna um dataframe com as informações
    """
    def __init__(self, ct_token):
        self.today = datetime.datetime.now().date()
        self.ct_token = ct_token

    @staticmethod
    def create_payload_leader(account_ids=None, count=None, end_date=None, list_id=None, offset=None,
                              order_by=None, sort_by=None, start_date=None):
        """
        Cria o payload que será utilizado na request
        Args:
            account_ids: ids of accounts
            count: number of items returned
            end_date: end date of the search
            list_id: The list of the leaderboard to retrieve.
            offset: The number of rows to offset.
            order_by: the order of the sort. asc ou desc(ascendente ou descendente)
            sort_by: The method by which the accountStatistics are sorted.	total_interactions or interaction_rate
            start_date: The startDate of the leaderboard rage.

        Returns: Payload com as informações colocadas

        """
        payload = {'accountIds': account_ids, 'count': count, 'endDate': end_date, 'listId': list_id, 'offset': offset,
                   'orderBy': order_by, 'sortBy': sort_by, 'startDate': start_date}
        payload = {k: v for k, v in payload.items() if v}
        return payload

    def create_payload_posts(self, accounts=None, branded_content=None, count=None, end_date=None, include_history=None,
                             language=None, list_ids=None, min_interactions=None, offset=None,
                             page_admin_top_country=None, search_term=None, sort_by=None, start_date=None,
                             timeframe=None, types=None, verified=None):
        """
        Gera payload para posteriormente fazer o request do endpoint
        Args:
            accounts: String of nickcnames of accounts or id of list of account
            branded_content: Boolean to include or exclude branded content
            count: Number of items to return
            end_date: Data final que o post foi criado
            include_history: Boolean to include or exclude history data
            language: Code of language of post
            list_ids: Id that contains a set of account ids
            min_interactions: Filters items that have had at least d interactions
            offset: Offset to start the search used to paginate
            page_admin_top_country: Limits to only posts where the page is set to the country
            search_term: Returns posts with the search term
            sort_by: Sorting the items
            start_date: Initial date of creation of the post that will be returned in the request
            timeframe: Set end_date = end_date - timeframe
            types: Type of post to return
            verified: Whether verified accounts should be limited or excluded from return

        Returns:

        """
        payload = {'accounts': accounts, 'brandedContent': branded_content, 'count': count, 'endDate': end_date,
                   'includeHistory': include_history, 'language': language, 'listIds': list_ids,
                   'minInteractions': min_interactions, 'offset': offset, 'pageAdminTopCountry': page_admin_top_country,
                   'searchTerm': search_term, 'sortBy': sort_by, 'startDate': start_date, 'timeframe': timeframe,
                   'types': types, 'verified': verified}

        payload = {k: v for k, v in payload.items() if v}
        return payload

    @staticmethod
    def create_payload_post(include_history):
        """
        Cria o payload que será utilizado na request
        Args:
            include_history: If you want to generate multiple samples of data for the post

        Returns: Payload com as informações colocadas

        """
        payload = {'includeHistory': include_history}
        payload = {k: v for k, v in payload.items() if v}
        return payload

    def make_request_leader(self, payload=None):
        """
       Returns the request link to API
        Args:
            payload: payload used in request

        Returns: object type request

        """
        return requests.get('https://api.crowdtangle.com/leaderboard', headers={'x-api-token': self.ct_token},
                            params=payload)

    def make_request_posts(self, payload=None):
        return requests.get('https://api.crowdtangle.com/posts', headers={'x-api-token': self.ct_token}, params=payload)

    def make_request_post(self, post_id, payload):
        return requests.get(f'https://api.crowdtangle.com/post/{post_id}', headers={'x-api-token': self.ct_token},
                            params=payload)

    def get_leader(self, account_ids=None, count=None, end_date=None, list_id=None, offset=None, order_by=None,
                   sort_by=None, start_date=None):
        """

        Args:
            account_ids: ids of the accounts we want to use
            count: amount of items we want to return
            end_date: day the search should stop
            list_id: The list of the leaderboard to retrieve.
            offset: The number of rows to offset.
            order_by: the order of the sort.
            sort_by: The method by which the accountStatistics are sorted.
            start_date: The startDate of the leaderboard rage.

        Returns: organized information
        """
        payload = self.create_payload_leader(account_ids, count, end_date, list_id, offset, order_by, sort_by,
                                             start_date)
        response = self.make_request_leader(payload)
        return response.json()

    def get_posts(self, accounts=None, branded_content=None, count=None, end_date=None, include_history=None,
                 language=None, list_ids=None, min_interactions=None, offset=None, page_admin_top_country=None,
                 search_term=None, sort_by=None, start_date=None, timeframe=None, types=None, verified=None):
        """

        Args:
            accounts: Account nickname string or platform id
            branded_content: Limits or excludes branded content items
            count: Number of items returned
            end_date: End date the post was created
            include_history: Returns data with time series
            language: Code of the source language of the post
            list_ids: Id that contains a set of account ids
            min_interactions: Filters items that have had at least d interactions
            offset: The offset of the return item used for paging
            page_admin_top_country: Limits to only posts where the page is set to the country
            search_term: Returns posts with the search term
            sort_by: Sorting the items
            start_date: Initial date of creation of the post that will be returned in the request
            timeframe: Set end_date = end_date - timeframe
            types: Type of post to return
            verified: Whether verified accounts should be limited or excluded from return

        Returns:

        """
        # Define os valores das variáveis
        payload = self.create_payload_posts(accounts, branded_content, count, end_date, include_history, language,
                                            list_ids, min_interactions, offset, page_admin_top_country, search_term,
                                            sort_by, start_date, timeframe, types, verified)
        # Faz o request com os valores definidos
        response = self.make_request_posts(payload)
        return response.json()

    def get_post(self, post_id=None, include_history=False):
        """

        Args:
            post_id: id of post on format  [number]_[number]
            include_history: If you want to generate multiple samples of data for the post
        Returns: organized information
        """
        payload = self.create_payload_post(include_history)
        response = self.make_request_post(post_id, payload)
        return response.json()
