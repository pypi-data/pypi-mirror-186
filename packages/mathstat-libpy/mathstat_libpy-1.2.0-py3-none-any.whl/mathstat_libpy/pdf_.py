from IPython.display import IFrame
import requests
import os
from functools import lru_cache
from pathlib import Path


def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)


def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None


def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

class PDF:

    def __init__(self, workdir: Path = None):
        self.workdir = workdir

        self.filenames = ['q_full.pdf',
                          'q4.pdf',
                          'q56.pdf',
                          'matstat_q.pdf',
                          'q1.pdf',
                          'q2.pdf',
                          'q3.pdf',
                          'q1_full.pdf',
                          'q2_full.pdf',
                          'q3_full.pdf',
                          'formula.pdf',
                          'theory.pdf']
        file_ids = ['1e0OQjiTv1NAXOqfyH1haEoidrSi5yee5',
                    '10wmTx77V38vqEb96g0ObYNxuqA_ofKct',
                    '1HgPD9vOJkcID2Dn6wY-Gdqzlml87Pqg6',
                    '1yrsDHVtai7kEdxdaiOaxcwZ07Y_l0_RA',
                    '1G4jWEd-RWktpy4dsoFhWPCOUmvrbOKFN',
                    '1w4vzUcfFaVq68T8gB21tTbnSPtphDeQi',
                    '1NbP83jeeiq5O7RrtHVpatjjFZnqvOyY_',
                    '1pUANEiJLeSYjarxfTGYeknhf5NGGvTwl',
                    '1Q5rzPMiUoXg37bFwooH9yBHlBW7LyyZY',
                    '15BkVcLYEBScDHuigb7TrgKREDWn8Eb-6',
                    '14vifoOobwVXEKGvwauieLW85TJwHsA8A',
                    '1yWSCc5IcI8WY1oczfHo7erahbW_metNL']

        if self.workdir is not None:
            self.filenames = [os.path.join(self.workdir, file) for file in self.filenames]

        self.paths = dict(zip(self.filenames, file_ids))
        self.inv_paths = dict(zip(file_ids, self.filenames))

    @lru_cache
    def load_pdf(self) -> None:
        for file_id, path in self.inv_paths.items():
            download_file_from_google_drive(file_id, path)

    def show_pdf(self, filename):
        if self.workdir is not None:
            filename = os.path.join(self.workdir, filename)
            filename = os.path.relpath(filename)
        return IFrame(filename, width=750, height=750)
