
url_template = "https://b2c.voegol.com.br/compra/busca-parceiros?pv=br&tipo=DF&de=ORIGEM&para=DESTINO&ida=DD-MM-YYYY&ADT=1&CHD=0&INF=0"

def query_to_url(query):
    return url_template.replace('ORIGEM', query.origem).replace('DESTINO', query.destino).replace('DD-MM-YYYY', query.data_ida)


def download_chrome_driver():
    '''Download the latest chrome driver and extract it to the current folder'''
    import requests
    import wget
    import zipfile
    import os

    # get the latest chrome driver version number
    url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
    response = requests.get(url)
    version_number = response.text

    # build the donwload url
    download_url = "https://chromedriver.storage.googleapis.com/" + version_number +"/chromedriver_win32.zip"

    # download the zip file using the url built above
    latest_driver_zip = wget.download(download_url,'chromedriver.zip')

    # extract the zip file
    with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
        zip_ref.extractall() # you can specify the destination folder path here
    # delete the zip file downloaded above
    os.remove(latest_driver_zip)