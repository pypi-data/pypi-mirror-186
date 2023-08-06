from io import BytesIO
from pathlib import Path
from time import sleep
from xml.etree import ElementTree
from zipfile import ZipFile

import requests

from acodis_error import *
from _acodis_auth import AcodisAuth
from _acodis_logger import HandlerLog

log = HandlerLog().get_log()


# Acodis API handler

class AcodisAPIHandler:

    def __init__(self, base_url: str):
        """
        Acodis API handler object to communicate with Acodis API
        for performing Intelligent Document Processing (IDP) workflows

        Parameters:
        -----------
        base_url Base URL for Accessing Acodis API.
        (e.g. https://instance.acodis.io/workbench/api/transaction)
        :return: The AcodisAPIHandler object
        :doc-author: Ricardo Filipe dos Santos
        """

        log.info("Initializing Acodis API handler...")

        self._user = None
        self._password = None
        self.auth = None
        self.status = None
        self.transaction_id = None
        self.xml = None

        if "acodis.io" in base_url:
            self.base_url = base_url
        else:
            raise AcodisError("Base URL does not seem to be an Acodis address")

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    def authenticate(self, **kwargs):
        """
        The authenticate function is used to authenticate the user with the Acodis API.
        It takes two arguments, user and password, which are both required.
        If these values are not set in the class instance or as function arguments, an error will be raised.

        :param self: Refer to the object of the class
        :param **kwargs: Pass in the user and password parameters from the authenticate function
        :return: A dictionary containing the authentication token and a list of groups
        :doc-author: Ricardo Filipe dos Santos
        """
        if len(kwargs) == 2:
            if kwargs.get('user') is not None and kwargs.get('password') is not None:
                self.user = kwargs['user']
                self.password = kwargs['password']
                auth = AcodisAuth(self.user, self.password)
                self.auth = auth()
            else:
                raise AcodisAuthError("User and password not set. Please define them in the class instance or as "
                                      "function arguments using 'user' and 'password'.")

        elif self.user is not None and self.password is not None:
            auth = AcodisAuth(self.user, self.password)
            self.auth = auth()
        else:
            raise AcodisAuthError("User and password not set. Please set them before authenticating.")

        log.debug("Authentication successful for user: {username}".format(username=self.auth.username))

    def upload_pdf(self, pdf_path: str):
        """
        The upload_pdf function takes a PDF file and uploads it through the Acodis API.
        It returns the transaction ID of the upload, which is used in subsequent calls
        to check on its status.

        :param self: Access the class attributes and methods
        :param pdf_path:str: The path to the PDF file to be used in Acodis IDP workflow
        :return: The transaction id
        :doc-author: Trelent
        """

        pdf_name = Path(pdf_path).name
        with open(pdf_path, 'rb') as f:
            files = [(
                'files',
                (
                    pdf_name,
                    f,
                    'application/pdf'
                )
            )]

            payload = {
                'configuration': {
                    "outputs": ["export"]
                }
            }

            response = requests.post(
                self.base_url,
                auth=self.auth,
                files=files,
                data=payload
            )

            try:
                response.raise_for_status()
                self.transaction_id = response.json()['transactionId']

            except requests.exceptions.HTTPError as err:
                log.error(err)
                raise AcodisApiError(err)

    def get_status(self):
        state = requests.get(
            self.base_url + '/' + self.transaction_id,
            auth=self.auth
        )

        try:
            state.raise_for_status()
            try:
                state.json()['errorMessage'] is None
            except AcodisError(state.json()['errorMessage']) as err:
                log.error(err)
                raise AcodisError(err)
            finally:
                self.status = state.json()['state'].lower()
        except requests.exceptions.HTTPError as err:
            log.error(err)
            raise SystemExit(err)

    def wait_for_completion(self):

        log.info("Waiting for workflow to complete...")

        self.get_status()
        while self.status == 'running':
            sleep(5)
            self.get_status()
        if self.status == 'completed':
            log.info("Workflow completed.")
        else:
            log.error("Error while handling status request: " + self.status)
            raise AcodisError("Error while handling status request: " + self.status)

    def download_prediction(self):
        if self.status == 'completed':
            log.info("Downloading prediction...")

            response = requests.get(
                self.base_url + '/' + self.transaction_id + '/output',
                auth=self.auth
            )
            try:
                response.raise_for_status()
                zip_buffer = BytesIO(response.content)
                zip_obj = ZipFile(zip_buffer)

                for file in zip_obj.namelist():
                    if file.endswith('.xml'):
                        self.xml = ElementTree.fromstring(zip_obj.read(file))
                        return ElementTree.fromstring(zip_obj.read(file))

            except requests.exceptions.HTTPError as err:
                log.error(err)
                raise SystemExit(err)

    def workflow(self, pdf_path: str):
        """
        The workflow function is the main entry point for the API. It takes a PDF file and returns
        a prediction of the features define in the Acodis workflow.
        The workflow function does this by:
            1) Uploading the PDF to Acodis, where it will be processed according to the workflow steps.
            2) Polling Acodis until the prediction is complete, at which point we download and return that result.

        :param self: Access the class attributes'
        :param pdf_path:str: Pass the path of the pdf file to be processed
        :return: The xml file with the predictions made by Acodis models
        :doc-author: Ricardo Filpe dos Santos
        """
        self.upload_pdf(pdf_path)
        self.wait_for_completion()
        self.download_prediction()

        log.debug("Workflow completed for the following file: " + Path(pdf_path).name)
        log.debug("Transaction ID: " + self.transaction_id)
