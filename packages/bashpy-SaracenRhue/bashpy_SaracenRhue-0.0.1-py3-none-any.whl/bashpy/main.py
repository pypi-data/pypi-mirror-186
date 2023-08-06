from os import system

def curl_script(url:str):
    """curl_script(url:str) -> None
    Curls and runs a bash script from a given url.
    """
    system(f'bash -c "$(curl {url})"')


def wget_retry(url:str, tries:int=0, timeout:int=5):
    """wget_retry(url:str, retry:int=3) -> None
    Downloads a file from a given url with wget (and reconnects when interrupted).
    """
    system(f'wget -c --retry-connrefused --tries={tries} --timeout={timeout} {url}')

def reload_bash():
    """reload_bash() -> None
    Reloads the ~/.bashrc file.
    """
    system('source ~/.bashrc')

def reload_zsh():
    """reload_zsh() -> None
    Reloads the ~/.zshrc file.
    """
    system('source ~/.zshrc')