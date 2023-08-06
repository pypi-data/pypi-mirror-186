import base64
import datetime
import gzip
import pandas as pd
import requests
import json


class SpotifyCredential:
    access_token = None
    access_token_expires = datetime.datetime.now()
    access_token_did_expire = True
    need_access = False
    range_api_success = [200, 201, 202, 203, 204, 205, 206, 207, 208, 226]
    token_url = "https://accounts.spotify.com/api/token"

    def __init__(self, client_id, client_secret):
        """
        Função que recebe os parametros necessários para a autenticação
        Args:
            client_id: Credential id client
            client_secret: Credential secret client
        """
        self.client_id = client_id
        self.client_secret = client_secret

    def get_client_credentials(self):
        """
        Recebe o client id e os client secrets e funciona para encodificar e decodificar as credenciais
        Returns: retorna as credenciais codificadas em base64

        """
        if self.client_secret is None or self.client_id is None:
            raise Exception("You must set client_id and client_secret")
        client_creds = f"{self.client_id}:{self.client_secret}"
        client_creds_b64 = base64.b64encode(client_creds.encode())
        return client_creds_b64.decode()

    def get_token_headers(self):
        """
        Utiliza as credenciais encodificadas com base 64 e nos retorna o header com as credenciais no formato que
        precisamos
        Returns: Header que possui a credencial encodificada em base 64

        """
        client_creds_b64 = self.get_client_credentials()
        return {"Authorization": f"Basic {client_creds_b64}"}

    @staticmethod
    def get_token_data() -> dict:
        """

        Returns: grant_type da credencial.

        """
        return {"grant_type": "client_credentials"}

    def perform_auth(self):
        """
        Realiza o processo de autenticação
        Returns: True em caso de sucesso

        """
        token_url = self.token_url
        token_data = self.get_token_data()
        token_headers = self.get_token_headers()
        r = requests.post(token_url, data=token_data, headers=token_headers, allow_redirects=True, verify=True)
        if r.status_code not in range(200, 299):
            raise Exception("Could not authenticate client.")
            # return False
        data = r.json()
        now = datetime.datetime.now()
        access_token = data['access_token']
        expires_in = data['expires_in']  # seconds
        expires = now + datetime.timedelta(seconds=expires_in)
        self.access_token = access_token
        self.access_token_expires = expires
        self.access_token_did_expire = expires < now
        return True

    def get_access_token(self):
        """
        Utiliza o access token verificando a checagem se o mesmo está expirado
        Returns: Token de autenticação.

        """
        token = self.access_token
        expires = self.access_token_expires
        now = datetime.datetime.now()
        if expires < now or token is None:
            self.perform_auth()
            return self.get_access_token()
        return token

    def get_resource_header(self):
        """
        Utiliza a função get_access_token para pegar o token e o coloca em um formato de header para utilização
        Returns: Header no formato para utilização.

        """
        if not self.need_access:
            access_token = self.get_access_token()
            return {"Authorization": f"Bearer {access_token}"}
        raise Exception('Need Access Token')


class SpotifyPublic(SpotifyCredential):
    """
    Classe que faz todas as funções relacionadas com a API do spotify, desde autenticação até a chamada do API
    """
    def __init__(self, client_id, client_secret):
        """
        Função que recebe os parametros necessários para a autenticação
        Args:
            client_id: Credential id client
            client_secret: Credential secret client
        """
        super().__init__(client_id, client_secret)

    @staticmethod
    def get_resource(lookup_id, resource_type='', version='v1', api_lookup_type=None, extra_filter=None, market=None,
                     search_type=None):
        """
        Recebe os parametros que utilizaremos na metodo de request da api e nos
        redireciona para qual metodo que queremos
        Args:
            search_type:
            lookup_id: id que sera utilizado na busca
            resource_type: tipo de busca que queremos fazer
            version: versão da api que utilizaremos (v1 como padrão)
            api_lookup_type: tipo de pesquisa que queremos fazer se o resource type for algo generico, utilizado
            na busca de playlists como o resource_type é user
            extra_filter: filtro extra caso necessário, utilizar como disponivel no site do api do spotify
            market: mercado em que queremos fazer a busca (Ex:BR)

        Returns: Dict com as informações que foram requesitadas pelo metodo em que a função foi utilizada

        """
        endpoint = f"https://api.spotify.com/{version}/{resource_type}/{lookup_id}"
        if api_lookup_type is not None:
            endpoint = f"https://api.spotify.com/{version}/{resource_type}/{lookup_id}/{api_lookup_type}"
        if market is not None:
            endpoint = f"https://api.spotify.com/{version}/{resource_type}/{lookup_id}/{api_lookup_type}?{market}"
        if extra_filter is not None:
            endpoint = f"https://api.spotify.com/{version}/{resource_type}/{lookup_id}/{api_lookup_type}{extra_filter}"
        if search_type is not None:
            if resource_type:
                endpoint = f"https://api.spotify.com/{version}/{resource_type}/{lookup_id}?{search_type}"
                if api_lookup_type:
                    endpoint = f"https://api.spotify.com/{version}/{resource_type}/{lookup_id}/{api_lookup_type}?{search_type}"
            else:
                endpoint = f"https://api.spotify.com/{version}/{lookup_id}?{search_type}"
        return endpoint

    def get_artist_top_tracks(self, artist_id, offset=0):
        """

        Args:
            artist_id: id de um artista
            offset: Initial position of the items to return.

        Returns: top tracks desse artista

        """
        endpoint = self.get_resource(resource_type='artists', lookup_id=artist_id,
                                     api_lookup_type=f'top-tracks?market=br&limit=50&offset={offset}')
        header = self.get_resource_header()
        return requests.get(endpoint, headers=header).json()

    def get_playlist(self, playlist_id, offset=0):
        """

        Args:
            playlist_id: id da playlist
            offset: Initial position of the items to return.

        Returns: Json with info of tracks from the playlist

        """
        endpoint = self.get_resource(resource_type='playlists', lookup_id=playlist_id,
                                     search_type=f'limit=50&offset={offset}')
        header = self.get_resource_header()
        return requests.get(endpoint, headers=header).json()

    def get_search_artist_type_playlist(self, artist, offset=0):
        """

        Args:
            artist: nome do artista
            offset: Initial position of the items to return.

        Returns: playlist editoriais do artista

        """
        endpoint = self.get_resource(lookup_id='search', search_type=f'q="artist:{artist}"&type=playlist&offset='
                                                                     f'{offset}&limit=50')
        header = self.get_resource_header()
        return requests.get(endpoint, headers=header).json()

    def get_categories(self, offset=0):
        """
        Função que retorna as categorias disponíveis na api do spotify
        Args:
            offset: Initial position of the items to return.
        Returns: List of categories

        """
        endpoint = self.get_resource(resource_type='browse', lookup_id='categories',
                                     search_type=f'limit=50&offset={offset}')
        header = self.get_resource_header()
        return requests.get(endpoint, headers=header).json()

    def get_info_endpoint(self, endpoint):
        header = self.get_resource_header()
        return requests.get(endpoint, headers=header).json()

    def get_single_browse_category(self, category_id, offset=0):
        """
        Get info of the playlist of a category
        Args:
            category_id: id da categoria
            offset: Initial position of the items to return.

        Returns: playlists da categoria

        """
        endpoint = self.get_resource(resource_type='browse', lookup_id='categories',
                                     api_lookup_type=f'{category_id}/playlists', search_type=f'limit=50&offset={offset}'
                                     )
        header = self.get_resource_header()
        return requests.get(endpoint, headers=header).json()

    def get_featured_playlists(self, timestamp=None, offset=0):
        """
        Get info of the featured playlists
        Args:
            timestamp: timestamp of the date that you want to get the featured playlists
            offset: Initial position of the items to return.
        Returns: playlists em destaque

        """
        endpoint = self.get_resource(resource_type='browse', lookup_id='featured-playlists',
                                     search_type=f'timestamp={timestamp}&limit=50&offset={offset}')
        header = self.get_resource_header()
        return requests.get(endpoint, headers=header).json()

    def get_users_playlists(self, user_id, offset=0):
        """

        Args:
            user_id: id do usuario
            offset: Initial item returned

        Returns: playlists do usuario

        """
        endpoint = self.get_resource(resource_type='users', lookup_id=user_id,
                                     api_lookup_type='playlists', search_type=f'limit=50&offset={offset}')
        header = self.get_resource_header()
        return requests.get(endpoint, headers=header).json()

    def get_track(self, track_id):
        """
        Get info of the playlist of a track
        Args:
            track_id: id do track

        Returns: playlists que contém o track

        """
        endpoint = self.get_resource(resource_type='tracks', lookup_id=track_id, search_type='limit=50')
        header = self.get_resource_header()
        return requests.get(endpoint, headers=header).json()

    def get_several_tracks(self, track_ids):
        """
        Get info about several tracks
        Args:
            track_ids: list of track ids
        Returns: Dict with info of tracks
        """
        endpoint = self.get_resource(lookup_id='tracks', search_type=f'ids={track_ids}&limit=50')
        header = self.get_resource_header()
        return requests.get(endpoint, headers=header).json()

    def get_several_artists(self, artist_id):
        """
        Get info about several artists
        Args:
            artist_id: list of artist ids
        Returns: Dict with info of artists
        """
        endpoint = self.get_resource(lookup_id='artists', search_type=f'ids={artist_id}&limit=50')
        header = self.get_resource_header()
        return requests.get(endpoint, headers=header).json()


class SpotifyPrivate(SpotifyCredential):
    """
    Classe que faz todas as funções relacionadas com a API do spotify, desde autenticação até a chamada do API Privada
    """

    def __init__(self, client_id, client_secret, licensor, access_token_const, date):
        """
        Função que recebe os parametros necessários para a autenticação
        Args:
            date: Data da requisição
            client_id:
            day: Dia da data de requisição
        """
        super().__init__(client_id, client_secret)
        self.year = date.strftime('%Y')
        self.month = date.strftime('%m')
        self.day = date.strftime('%d')
        self.header = self.get_resource_header()
        self.licensor = licensor
        self.access_token_const = access_token_const

    def get_data_streams(self, country) -> requests.models.Response:
        """
        Faz a request para o endpoint streams
        Args:
            country: Code of the country
        Returns: Respota da request
        """
        url = f'https://provider-api.spotify.com/v1/analytics/{self.licensor}/enhanced/streams/{self.year}/' \
              f'{self.month}/{self.day}/{country}'
        return requests.get(url, headers=self.header)

    def get_data_country(self) -> requests.models.Response:
        """
        Faz a request para o endpoint streams
        Returns: Respota da request
        """
        url = f'https://provider-api.spotify.com/v1/analytics/{self.licensor}/enhanced/streams/{self.year}/' \
              f'{self.month}/{self.day}'
        return requests.get(url, headers=self.header)

    def get_data_users(self) -> requests.models.Response:
        """
        Faz a request para o endpoint streams
        Returns: Respota da request
        """
        url = f'https://provider-api.spotify.com/v1/analytics/{self.licensor}/enhanced/users/{self.year}/{self.month}/'\
              f'{self.day}'
        return requests.get(url, headers=self.header)

    def get_data_tracks(self) -> requests.models.Response:
        """
        Faz a request para o endpoint tracks
        Returns: Respota da request
        """
        url = f'https://provider-api.spotify.com/v1/analytics/{self.licensor}/enhanced/tracks/{self.year}/' \
              f'{self.month}/{self.day}'
        return requests.get(url, headers=self.header)

    def get_data_aggregated_streams(self) -> requests.models.Response:
        """
        Faz a request para o endpoint aggregated streams
        Returns: Respota da request
        """
        url = f'https://provider-api.spotify.com/v1/analytics/{self.licensor}/enhanced/aggregatedstreams/{self.year}/' \
              f'{self.month}/{self.day}'
        return requests.get(url, headers=self.header)

    def get_data_sub_30_secs_streams(self, country: str) -> requests.models.Response:
        """
        Faz a request para o endpoint sub 30 secs streams
        Args:
            country: Code of the country
        Returns: Respota da request
        """
        url = f'https://provider-api.spotify.com/v1/analytics/{self.licensor}/enhanced/sub_30_sec_streams/{self.year}/' \
              f'{self.month}/{self.day}/{country}'
        return requests.get(url, headers=self.header)

    def get_full_access_header(self) -> dict:
        """
        Cria um header que possui o token com autorização, necessário para requests que necessitam de autorização
        Returns: Header com o token que possui autorização
        """
        return {"Authorization": f"Bearer {self.access_token_const}"}

    @staticmethod
    def request2json(request):
        """
        Função que transforma a resposta da request em um dataframe
        Args:
            request: request feita para o endpoint
        Returns:
            DataFrame com os dados da request
        """
        decompressed_response = gzip.decompress(request.content)
        my_json = decompressed_response.decode('utf-8')
        my_json = f'[{my_json}]'
        my_json = my_json.replace('\n', '')
        my_json = my_json.replace('}{', '},{')
        return json.loads(my_json)

    def get_tracks(self) -> pd.DataFrame:
        """
        Função que retorna o dataframe do endpoint tracks
        Args:
            type: Extensão do arquivo que vai ser escrito
        Returns:
            DataFrame tracks
        """
        return self.request2json(self.get_data_tracks())

    def get_users(self) -> pd.DataFrame:
        """
        Função que retorna o dataframe do endpoint users
        Args:
            type: Extensão do arquivo que vai ser escrito
        Returns:
            DataFrame users
        """
        return self.request2json(self.get_data_users())

    def get_streams(self, country) -> pd.DataFrame:
        """
        Função que retorna o dataframe do endpoint streams para um país específico
        Args:
            country: Code of the country
        Returns:
            DataFrame streams de um país
        """
        return self.request2json(self.get_data_streams(country))

    def get_sub_30_streams(self, country) -> pd.DataFrame:
        """
        Função que retorna o dataframe do endpoint sub30_secs_streams para um país específico
        Args:
            country: Code of the country
        Returns:
            DataFrame sub30_secs_streams streams de um país
        """
        return self.request2json(self.get_data_sub_30_secs_streams(country))

    def get_aggregated_streams(self) -> pd.DataFrame:
        """
        Função que retorna o dataframe do endpoint aggregated_streams
        Returns:
            DataFrame aggregated_streams
        """
        return self.request2json(self.get_data_aggregated_streams())
