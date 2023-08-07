import requests
import puan.logic.plog as pg

from puan import Proposition
from dataclasses import dataclass
from typing import Optional, Tuple, Any

@dataclass
class Client:

    url: str

    @staticmethod
    def _extract_data(response, key) -> Tuple[Optional[Any], Optional[str]]:

        """
            Extracts data from response by using given callable `key` function.

            Returns
            -------
            Tuple[Optional[str], Optional[str]]
                Left side is Any data, if it was successfully got. Else None.
                Right side is an error string, if something went wrong. Else None.
        """

        if response.ok:
            data = response.json()
            if data['error']:
                return None, data['error']
            return key(data), None
        return None, response.text

    def commit(self, model: Proposition, branch: str = 'main') -> Tuple[Optional[str], Optional[str]]:

        """
            Commits `model` onto branch `branch`.

            Returns
            -------
            Tuple[Optional[str], Optional[str]]
                Left side is the commit sha string, if it was successfully got. Else None.
                Right side is an error string, if something went wrong. Else None.
        """
        return self._extract_data(
            requests.post(
                f"{self.url}/{model.id}/{branch}/commit", 
                json=model.to_b64()
            ), 
            key=lambda x: x['commit']['sha'],
        )
        

    def checkout(self, sha: str) -> Optional[Proposition]:

        """
            Checkout committed proposition by sha string.

            Returns
            -------
            Proposition
        """
        return self._extract_data(
            requests.get(f"{self.url}/commit/{sha}"), 
            key=lambda commit: pg.from_b64(
                commit['commit']['data'],
            ),
        )
