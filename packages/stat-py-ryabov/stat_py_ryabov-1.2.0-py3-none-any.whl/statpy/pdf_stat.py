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

        self.filenames = ['q1.pdf', 'q2.pdf', 'q3.pdf', 'q123.pdf', 'q461.pdf', 'q462.pdf']
        file_ids = ['1xQQ_UBvNYXdrCE4zyoHIRj7rGQQ6z_aL',
                    '1kwxcFeMr5RDGchj_JoD6LC4qVbGL0CEL',
                    '1hKKm3fQbDfN47tnFtHpuFFHhMlIsbPuK',
                    '1Y1KsTuU8nIpjaO_V45TECmhthht9jHru',
                    '1R1tmemS7kDLoAlBKzmP-SEakw_eDipxJ',
                    '1naGRwv9MCPKfauOew7RZIsWkHU9KLPd4']

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
