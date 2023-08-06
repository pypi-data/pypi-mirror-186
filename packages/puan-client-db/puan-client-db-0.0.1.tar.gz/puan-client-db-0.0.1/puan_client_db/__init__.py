import requests
import puan.logic.plog as pg

from puan import Proposition
from dataclasses import dataclass
from typing import Optional

@dataclass
class Client:

    url: str

    def init(self, model: Proposition) -> Optional[str]:

        """
            Initializing a new version control monitor on `model`.

            Returns
            -------
            bool
        """
        response = requests.post(f"{self.url}/model/init", json={'id': model.id, 'name': '', 'data': model.to_b64()})
        if response.ok:
            return response.json()['error']
        return response.text

    def commit(self, model: Proposition, branch: str = 'main') -> bool:

        """
            Commits `model` onto branch `branch`.

            Returns
            -------
            bool
        """

        return requests.post(f"{self.url}/{model.id}/{branch}/commit", json=model.to_b64()).ok

    def commit_assume(self, model_id: str, assumption: dict, branch: str = 'main', sha: str = None) -> Optional[Proposition]:

        """
            Assumes something on a model's commit (default latest) and returns the new assumed proposition.

            Returns
            -------
            Optional[Proposition]
        """
        proposition = self.get_commit(model_id, branch=branch, sha=sha)
        return proposition.assume(assumption)

    def get_commit(self, model_id: str, branch: str = 'main', sha: str = None) -> Optional[Proposition]:

        """
            Gets latest commit for model (and branch). If `sha` is supplied, then that commit is got.

            Returns
            -------
            Proposition
        """
        if sha:
            commit = requests.get(f"{self.url}/commit/{sha}").json()
        else:
            commit = requests.get(f"{self.url}/{model_id}/{branch}/latest").json()

        return pg.from_b64(commit['commit']['data']) if commit['error'] is None else None

    def create_branch(self, model_id: str, branch: str, on_branch: str = "main") -> bool:

        """
            Creates a new branch for model.

            Returns
            -------
            bool
        """
        response = requests.post(f"{self.url}/{model_id}/{on_branch}/branch?name={branch}")
        return response.ok and response.json()['error'] is None

