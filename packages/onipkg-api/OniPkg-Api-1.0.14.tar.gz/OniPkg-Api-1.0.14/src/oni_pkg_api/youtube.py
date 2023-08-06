from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from typing import List

class YoutubeAnalytics:
    """
    Classe que executa as ações get da api Youtube Analytics
    """
    def __init__(self, content_owner_id, credentials, name2job_id: dict):
        self.content_owner_id = content_owner_id
        self.credentials = credentials
        self.name2job_id = name2job_id
        self.youtube_reporting = self.get_authenticated_service()

    def get_authenticated_service(self):
        """
        Valida a credencial e constroi o objeto da API
        Returns:

        """
        return build('youtubereporting', 'v1', credentials=self.credentials)


    # Remove keyword arguments that are not set.
    @staticmethod
    def remove_empty_kwargs(**kwargs):
        """
        Remove keyword arguments that are not set
        Args:
            **kwargs: keyword arguments to remove
        Returns:
        """
        good_kwargs = {}
        if kwargs is not None:
            for key, value in kwargs.items():
                if value:
                    good_kwargs[key] = value
        return good_kwargs

    # Call the YouTube Reporting API's jobs.create method to create a job.
    def create_reporting_job(self, report_type, name, **kwargs):
        """
        Cria report job
        Args:
            report_type: id do report_type encontrado na documentação oficial
            name: Nome desejado do report
            **kwargs: keyword arguments

        Returns:
        """
        # Provide keyword arguments that have values as request parameters.
        kwargs = self.remove_empty_kwargs(**kwargs)
        reporting_job = self.youtube_reporting.jobs().create(body=dict(reportTypeId=report_type, name=name), **kwargs
                                                             ).execute()
        print(f"Reporting job {reporting_job.get('name')} created for reporting type {reporting_job.get('reportTypeId')} at "
              f"{reporting_job.get('createTime')}")

    @staticmethod
    def value_default(value, default):
        """
        Função que retrna o default se não passar um value
        Args:
            value: Valor desejado
            default: Valor default

        Returns:
            Se não passar value retorna default

        """
        return value or default

    def system_managed_bool(self, value):
        """
        Retorna o booleando da valor selecionado é igual a y
        Args:
            value: Valor selecionado de system_managed

        Returns:
            Booleano se o valor é y
        """
        value = self.value_default(value, 'n')
        return value == 'y'

    def create_job(self, include_system_managed, report_type, name):
        """
        Método main do arquivo que executa o procedimento de criar job
        Args:
            include_system_managed: Booleano se deseja incluir os jobs do sistema
            report_type: id do report_type encontrado na documentação oficial
            name: Nome desejado do report
        Returns:

        """
        # The 'name' option specifies the name that will be used for the reporting job.

        include_system_managed = self.system_managed_bool(include_system_managed)
        name = self.value_default(name, None)
        report_type = self.value_default(report_type, None)
        try:
            # Prompt user to select report type if they didn't set one on command line.
            # Create the job.
            if report_type:
                self.create_reporting_job(report_type, name, onBehalfOfContentOwner=self.content_owner_id)
        except HttpError as e:
            print(f'An HTTP error {e.resp.status} occurred:\n {e.content}')


    #Delete Job
    def delete_reporting_job(self, job_id, **kwargs):
        """
        Função que deleta o report
        Args:
            job_id: id do job definido na documentação oficial
            **kwargs: keyword arguments
        Returns:

        """
        kwargs = self.remove_empty_kwargs(**kwargs)
        reporting_job = self.youtube_reporting.jobs().delete(jobId=job_id, **kwargs).execute()
        print(f"Deleted the report_job: {job_id}")


    def delete_job(self, name_job):
        """
        Função main do arquivo
        Args:
            name_job: Nome do job a ser deletado
        Returns:

        """
        job_id = self.name2job_id[name_job]
        job_id = self.value_default(job_id, None)
        youtube_reporting = self.get_authenticated_service()
        try:
            # Prompt user to select report type if they didn't set one on command line.
            # Delete the job.
            self.delete_reporting_job(job_id, onBehalfOfContentOwner=self.content_owner_id)
        except HttpError as e:
            print(f'An HTTP error {e.resp.status} occurred:\n {e.content}')


    #List Reports
    def list_reporting_jobs(self, **kwargs):
        """
        Lista todos os reports da conta
        Args:
            **kwargs: keyword arguments
        Returns:
            Booleano se há jobs para esta conta
        """
        # Only include the onBehalfOfContentOwner keyword argument if the user
        # set a value for the --content_owner argument.
        kwargs = self.remove_empty_kwargs(**kwargs)

        # Retrieve the reporting jobs for the user (or content owner).
        info_report = self.youtube_reporting.jobs().list(**kwargs).execute()

        if 'jobs' in info_report and info_report.get('jobs'):
            jobs = info_report.get('jobs')
            for job in jobs:
                print(f"Reporting job id: {job.get('id')}\n name: {job.get('name')}\n for reporting type: {job.get('reportTypeId')}\n")
        else:
            print('No jobs found')
            return False

        return True


    def list_jobs(self):
        """
        Função que implementa exceção para o método list_reporting_jobs
        Returns:
        """
        youtube_reporting = self.get_authenticated_service()
        try:
            # If the user has not specified a job ID or report URL, retrieve a list
            # of available jobs and prompt the user to select one.
            self.list_reporting_jobs( onBehalfOfContentOwner=self.content_owner_id)

        except HttpError as e:
            print(f"An HTTP error {e.resp.status} occurred:\n{e.content}")


    #Get json of one job
    def get_info_report(self, name_job: str, start_date, end_date):
        """
        Gera o dataframe do report desejado
        Args:
            name_job: Name of the job
            start_date: Start date of report
            end_date: End date of report

        Returns:
            Json of report desired
        """
        start_date = f'{start_date}T07:00:00Z'
        end_date = f'{end_date}T07:00:00Z'
        # Retrieve available reports for the selected job.
        youtube_reporting = self.get_authenticated_service()
        job_id = self.name2job_id[name_job]
        return youtube_reporting.jobs().reports().list(jobId=job_id, onBehalfOfContentOwner=self.content_owner_id,
                                                       startTimeAtOrAfter=start_date, startTimeBefore=end_date
                                                       ).execute()


class YoutubeDataApi:
    """
    Classe que faz a requisição para youtube_data_api
    If you intend to get data use credential_key
    If you intend to post data use credentials_service_account
    """
    def __init__(self, credential_key=None, credentials_service_account=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if credential_key:
            self.youtube_get = self.authenticate_credentials_key(credential_key)
        if credentials_service_account:
            self.youtube_post = self.authenticated_client_secrets(credentials_service_account)

    def authenticate_credentials_key(self, credential_key):
        """
        Função que autentica a credencial do tipo key
        Args:
            credential_key: Credencial do tipo key
        Returns: API Buildada

        """
        return build('youtube', 'v3', developerKey=credential_key)

    def list_channels(self, channel_id: str, part: List[str]):
        """
        Função que retorna estatísticas básicas do canal
        Args:
            channel_id: id do canal do youtube
            part: Recursos que deseja que tenha no json

        Returns:

        """
        return self.youtube_get.channels().list(id=channel_id, part=part, maxResults=50).execute()

    def list_videos(self, video_id: str, part: List[str]):
        """
        Função que retorna informações primordiais do vídeo
        Args:
            video_id: id de um video
            part: Recursos que deseja que tenha no json
        Returns: "snippets" de um video

        """
        try:
            return self.youtube_get.videos().list(part=part, id=video_id).execute()
        except Exception:
            return ''

    @staticmethod
    def authenticated_client_secrets(credentials):
        """
        Args:
            credentials: credentials of service account
        Função que cria o objeto credential caso foi validado as permissões do token
        Returns:

        """
        return build('youtube', 'v3', credentials=credentials)

    def make_request_body(self, category_id, title, description, tags, published_date, made_for_kids=False,
                          notify_subscribers=False):
        """
        Função que define o corpo de requisição da chamada da API
        Args:
            category_id: Category of video
            title: Title of video
            description: Description of video
            tags: Tags of video (list) min 3 elements
            published_date: Date of publication of video
            made_for_kids: If video is made for kids
            notify_subscribers: If subscribers will be notified
        Returns:

        """
        request_body = {
            'snippet': {
                'categoryI': category_id,
                'title': title,
                'description': description,
                'tags': tags
            },
            'status': {
                'privacyStatus': 'private',
                'publishAt': published_date,
                'selfDeclareMadeForKids': made_for_kids,
            },
            'notifySubscribers': notify_subscribers
        }
        return request_body

    def send_video(self, video_path, category_id, title, description, tags, published_date,
                   made_for_kids=False, notify_subscribers=False):
        """
        Função que realiza o envio do Video para o YouTube pela API
        Args:
            video_path: File of Video to send to YouTube
            category_id: Category of video
            title: Title of video
            description: Description of video
            tags: Tags of video (list) min 3 elements
            published_date: Date of publication of video
            made_for_kids: If video is made for kids
            notify_subscribers: If subscribers will be notified

        Returns:

        """

        video = MediaFileUpload(video_path)
        return self.youtube_post.videos().insert(part='snippet,status', body=self.make_request_body(
            category_id, title, description, tags, published_date, made_for_kids, notify_subscribers), media_body=video
                                                 ).execute()

    def set_thumbnail(self, thumbnail_path, video_path, category_id, title, description, tags, published_date,
                      made_for_kids, notify_subscribers):
        """
        Função que configura a thumbnail do vídeo e faz o envio do vídeo
        Args:
            thumbnail_path: File of image to set as thumbnail
            video_path: File of Video to send to YouTube
            category_id: Category of video
            title: Title of video
            description: Description of video
            tags: Tags of video (list) min 3 elements
            published_date: Date of publication of video
            made_for_kids: If video is made for kids
            notify_subscribers: If subscribers will be notified

        Returns:

        """
        thumbnail = MediaFileUpload(thumbnail_path)
        return self.youtube_post.thumbnails().set(
            videoId=self.send_video(video_path, category_id, title, description, tags, published_date,
                                    made_for_kids, notify_subscribers).get('id'), media_body=thumbnail).execute()
