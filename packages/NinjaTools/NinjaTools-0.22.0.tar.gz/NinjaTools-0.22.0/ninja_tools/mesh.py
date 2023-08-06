import os
import re
import subprocess
from pathlib import Path
from urllib.parse import quote

from bs4 import BeautifulSoup
from requests import Session, Response, codes
from colorama import Fore, init
import shutil

# Colorama init
init(autoreset=True)


class Web:
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.session = Session()
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' \
                          '(KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        self.headers = {
            'User-Agent': self.user_agent
        }

    def get(self, url: str, referer: str = None, headers: dict = None, soup: bool = False, **kwargs):
        """
        Parameters
        ----------
        url: str
            url is the url of the request to be performed
        referer: str
            A url sent as referer in request header
        headers: str
            custom header in a dictionary format.
            if none was provided, we will use a random user-agent
        soup: bool
            specify if the request will come as a soup object
        """

        if not self.validate_url(url):
            raise ValueError('Invalid URL')

        if self.verbose:
            print(f'{Fore.CYAN}URL: {url}')

        if headers:
            self.headers.update(headers)

        if referer:
            headers[referer] = referer

        try:
            r = self.session.get(url, headers=headers, **kwargs)

            if soup:
                if r.status_code == 200:
                    return self.soup(r)

                return None

            return r

        except Exception as e:
            print(f'Error: {e}')

    def download(self, url: str, file_name: str):
        r = self.get(url, stream=True)
        if r.status_code == codes.ok:

            folders = Path(file_name).parents[0]
            Path(folders).mkdir(parents=True, exist_ok=True)

            with open(file_name, "wb") as f:
                for data in r:
                    f.write(data)

                if os.path.exists(file_name):
                    return True
        return None

    def aria2c_download(self, url: str, file_name: str, executable: str = r'aria2c\aria2c.exe'):

        # If path not exists download executable
        if not os.path.exists(executable):
            print(f'{Fore.LIGHTCYAN_EX}Aria2c not found, downloading...')
            executable_url = 'https://github.com/aria2/aria2/releases/download/' \
                             'release-1.36.0/aria2-1.36.0-win-64bit-build1.zip'
            self.download(executable_url, 'aria2c.zip')
            shutil.unpack_archive('aria2c.zip', 'download_temp_aria2c')

            # Get folders in aria2c
            folder = os.listdir('download_temp_aria2c')[0]

            # Copy folder to aria2c
            shutil.copytree(f'download_temp_aria2c/{folder}', 'aria2c')

            # Remove temp files and folders
            os.remove('aria2c.zip')
            shutil.rmtree('download_temp_aria2c')

            print(f'{Fore.LIGHTCYAN_EX}Aria2c downloaded!')

        parameters = "--disable-ipv6 -k 1M -s 16 -x 16"

        cmd = f"{executable} {parameters} " \
              f"--user-agent=\"{self.headers['User-Agent']}\" " \
              f"-d \"{Path(file_name).parents[0]}\" " \
              f"-o \"{Path(file_name).name}\" \"{url}\""

        try:
            folders = Path(file_name).parents[0]
            Path(folders).mkdir(parents=True, exist_ok=True)

            sp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

            print("Download started: {}".format(Path(file_name).name))

            msg_content = ''

            for _line in sp.stdout:
                # print(_line)
                line = _line.decode(encoding="utf-8", errors="ignore")

                msg_content += line

                match = re.search(r"\[FileAlloc:(.*?) (.*?)]", line)
                if match:
                    print("{} | Progress: {}".format(Path(file_name).name, match.group(2).strip()))

            sp.wait()

            if '(OK):download completed' in msg_content:
                print("Download finished: {} | Saved to: {}".format(Path(file_name).name, file_name))
                return True

            if 'Exception:' in msg_content:
                print(f'{Fore.RED}Error occurred.')
                return False

            return False
        except Exception as e:
            print(f'{Fore.RED}Error: {e}')
            return False

    @staticmethod
    def soup(res):
        """
        converts the requests responses to soup objects
        """
        if isinstance(res, Response):
            res = res.text
            return BeautifulSoup(res, 'html.parser')

        return res

    @staticmethod
    def validate_url(url: str):
        regex = re.compile(r"^(?:http|ftp)s?://"  # http:// or https://
                           r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"
                           r"localhost|"  # localhost...
                           r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or ip
                           r"(?::\d+)?"  # optional port
                           r"(?:/?|[/?]\S+)$", re.IGNORECASE, )
        return re.match(regex, url) is not None

    @staticmethod
    def uni_escape(text: str):
        text.encode().decode('unicode-escape')
        return text

    @staticmethod
    def url_encode(text: str):
        return quote(text)
