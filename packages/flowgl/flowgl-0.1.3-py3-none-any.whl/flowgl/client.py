from typing import Any, Dict

import pandas as pd
from requests_toolbelt import sessions


class Client:
    def __init__(
        self,
        username: str,
        password: str,
        base_url: str = "https://api.flow.gl/v1/",
    ):
        self._client = sessions.BaseUrlSession(base_url=base_url)
        # get token
        response = self._client.post('access_token', json={
            'email': username,
            'grant_type': 'password',
            'password': password,
        })
        if response.status_code != 200:
            raise Exception('Failed to get access token')
        token = response.json()['data']['access_token']
        self._client.headers.update({
            'Authorization': f'Bearer {token}',
        })

    def push_data(
        self,
        data: pd.DataFrame,
        *,  # keyword-only arguments
        dataset_id: int = None,
        dataset_title: str = None,
    ) -> Dict[str, Any]:
        """
        Push data (in a pandas DataFrame) to the Flow API.

        Either `dataset_id` or `dataset_title` must be specified.

        Returns the dataset object, including the dataset ID and dataset version ID.
        """
        request_kwargs = {}
        if dataset_id is None:
            if dataset_title is None:
                raise Exception('Either dataset_id or dataset_title must be specified, but both are None')

            request_kwargs['data'] = {
                'title': dataset_title,
                'source': "API",
            }
            request_kwargs['url'] = 'datasets'
            request_kwargs['method'] = 'POST'
        else:
            if dataset_title is not None:
                raise Exception('Either dataset_id or dataset_title must be specified, not both')

            request_kwargs['url'] = f'datasets/{dataset_id}'
            request_kwargs['method'] = 'PUT'
        request_kwargs['files'] = {
            'file': ('data.csv', data.to_csv(index=False)),
        }
        response = self._client.request(**request_kwargs)
        if response.status_code // 100 != 2:
            error_message = f'Code {response.status_code}'
            try:
                error_message += f', {response.json()}'
            except Exception:
                pass
            raise RuntimeError(f'Failed to push data: {error_message}')
        return response.json()['data']
