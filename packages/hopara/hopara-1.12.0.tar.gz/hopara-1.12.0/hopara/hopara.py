import json
import logging
import requests

from requests.compat import urljoin

from hopara.config import Config
from hopara.request import Request
from hopara.table import Table
from hopara.view import View


BATCH_SIZE = 50000


logger = logging.getLogger('pyhopara')


class Hopara:
    """This class handles all data operations such as creating tables and inserting rows.
    """
    def __init__(self, organization: str = 'hopara.io'):
        """Initialize with the organization you want to operate.
        Usually the organization is the domain of your work e-mail (e.g. mycompany.com).
        :param organization: Name of the organization.
        :type organization: str
        """
        self.config = Config()
        self.__tenant = organization
        self.request = Request(self.config, {'tenant': self.__tenant})
        logger.info(f'ORGANIZATION: {organization}')
        logger.info(f'HOST: {self.config.get_dataset_url()}')
        logger.info(f'USER: {self.config.get_client_id() or self.config.get_email()}')

    def get_table_url(self, table: Table) -> str:
        return urljoin(self.config.get_dataset_url(), f'/table/{table.name}/')

    def get_view_url(self, view: View) -> str:
        return urljoin(self.config.get_dataset_url(), f'/view/{view.name}/')

    def get_row_url(self, table: Table) -> str:
        return urljoin(self.get_table_url(table), 'row') + f'?dataSource={table.data_source}' 

    def refresh_stats(self, view: View):
        """ Refresh the stats for a view
        :param view: view name
        """
        url = urljoin(self.get_view_url(view), 'refresh-stats') + f'?dataSource={view.data_source}'
        response = self.request.post(url, {})
        logger.info(f'RESPONSE: {response} / {response.content}\n')

    def delete_table(self, table: Table):
        """ Delete a table
        :param table: table
        :type table: hopara.Table
        """
        url = self.get_table_url(table) + f'?dataSource={table.data_source}' 
        response = self.request.delete(url, table.get_payload())
        logger.info(f'RESPONSE: {response} / {response.content}\n')

    def create_table(self, table: Table, recreate: bool = False):
        """ Create a table
        :param table: table name
        :type table: hopara.Table
        :param recreate: If set to ``True`` the table will be deleted and recreated. If set to ``False`` new columns will be added to the existing table.
        Default: False.
        **If True is set all data previously store in the table will be permanently removed.**
        :type recreate: bool
        """
        if recreate:
            self.delete_table(table)
        url = self.get_table_url(table)
        logger.info(f'URL: {url}')
        logger.info(f'TABLE: {json.dumps(table.get_payload())}')
        response = self.request.post(url, table.get_payload())
        logger.info(f'RESPONSE: {response} / {response.content}\n')

    def __insert_rows(self, url, rows: list):
        response = self.request.post(url, rows)
        logger.info(f'RESPONSE: {response} / {response.content}')

    def insert_rows(self, table: Table, rows: list):
        """ Insert rows in a table.
        :param table: table object
        :type table: hopara.Table
        :param rows: the data to be inserted in the following format: ``[{'col1': 1, 'col2': 'a'}, {'col1': 2, 'col2': 'b'}]``
        """
        url = self.get_row_url(table)
        logger.info(f'URL: {url}')
        logger.info(f'SAMPLE: {json.dumps(rows[0])}')

        if BATCH_SIZE >= len(rows):
            return self.__insert_rows(url, rows)
        batches = range(0, len(rows), BATCH_SIZE)
        logger.info(f'Processing {len(rows):,} rows in {len(batches):,} batches of {BATCH_SIZE:,} rows each...')
        for i, start in enumerate(batches, 1):
            end = min(start + BATCH_SIZE, len(rows))
            self.__insert_rows(url, rows[start:end])

    def __upload_file(self, file_path, resource_type, resource_name=None):
        url = urljoin(self.config.get_resource_url(), f'/{resource_type}' + f'/{resource_name}' if resource_name else '')
        with open(file_path, 'rb') as fp:
            # Se é um recurso nomeado, vamos sobrescrever, logo é PUT
            request_func = requests.put if resource_name else requests.post
            response = request_func(url, files={'file': fp}, headers={'tenant': self.__tenant})
            response.raise_for_status()
            logger.info(f'RESPONSE: {response} / {response.content}')
            return response.json()

    def upload_image(self, file_path):
        return self.__upload_file(file_path, 'image')

    def upload_model(self, file_path, resource_name):
        return self.__upload_file(file_path, 'model', resource_name)

    def upload_icon(self, file_path, resource_name):
        return self.__upload_file(file_path, 'icon', resource_name)


if __name__ == "__main__":
    hopara = Hopara()
