from .settings import WORLD_CPI, WORLD_ER, WORLD_PATH, DOWNLOAD_CPI
import os

def download_and_extract(url):
    """
    download_and_extract downloads the zip file at the given url and extracts its non-metadata files.
    
    :param url: the url at which to find the zip.
    """
    from io import BytesIO
    from zipfile import ZipFile
    from requests import get

    filename_ = WORLD_CPI if url == DOWNLOAD_CPI else WORLD_ER

    request = get(url)
    zipfile = ZipFile(BytesIO(request.content))
    zipinfo = zipfile.infolist()

    for inf in zipinfo:
        if not "Metadata" in inf.filename:
            inf.filename = filename_

    with ZipFile(BytesIO(request.content)) as zipObj:
        for info in zipObj.infolist():
            if not "Metadata" in info.filename:
                info.filename = os.path.basename(filename_)
                zipObj.extract(info, WORLD_PATH)
                


"""
def fetch_csv(url='https://www-genesis.destatis.de/genesisWS/services/ExportService_2010?method=TabellenExport&kennung={}&passwort={}&namen=61111-0002&bereich=alle&format=datencsv&strukturinformation=false&komprimierung=false&transponieren=false&startjahr=1960&endjahr=2021&zeitscheiben=&regionalmerkmal=&regionalschluessel=&sachmerkmal=&sachschluessel=&sachmerkmal2=&sachschluessel2=&sachmerkmal3=&sachschluessel3=&stand=01.01.2001+09%3A00&auftrag=false&sprache=de'.format(USER, PASS), filepath_=DATA_CPI):
    ""
    fetch_csv downloads the most recent consumer price indices from the Federal Office of Statistics if a more recent dataset is available than the current.

    :param url: the url from which to download the csv file. Doesn't need to be changed (usually).
    :param filepath_: the path to where to save the csv file.
    ""
    if is_dataset_up_to_date() or not os.path.isfile(filepath_):
        response = urllib.request.urlopen(url).read()
        tree = ET.fromstring(response)

        csv_str = tree.findall('.//tabellenDaten')[0].text.split("\n", 5)[5]

        with open(filepath_, "w") as csv_file:
            split_string = csv_str.split("\n")
            for i, line in enumerate(split_string):
                if i == 0:
                    csv_file.write("Jahr;Monat;Verbraucherpreisindex\n")
                elif i >= len(split_string)-4 or i == 1:
                    continue
                else:
                    l = line.split(";")
                    line_ = "{};{};{}\n".format(l[0], l[1], l[2].replace(',','.'))
                    csv_file.write(line_)

def is_dataset_up_to_date(url='https://www-genesis.destatis.de/genesisWS/web/RechercheService_2010?method=NeueDatenKatalog&kennung={}&passwort={}&filter=61111&typ=StatistikUpdates&stand={}&listenLaenge=15&sprache=de'.format(USER, PASS, LAST_UPDATE)):
    ""
    is_dataset_up_to_date checks for updates to the cpi table since the last fetch.

    :param url: the url to check for updates on the dataset.

    :return: True/ False based on whether or not a newer version of the dataset is available.
    ""
    
    response = urllib.request.urlopen(url).read()
    tree = ET.fromstring(response)

    filesize = os.path.getsize(DATA_UPDATE_LOG)
    if filesize == 0:
        _update_log()
        return True

    try:
        tree.findall('.//neueDatenKatalogEintraege')[1].find('datum').text
        _update_log()
        return True
    except Exception:
        return False

def _update_log():
    ""
    _update_log is a helper method for writing the current date into a log file.
    ""
    with open(DATA_UPDATE_LOG, "w") as update_log:
        update_log.write(datetime.today().strftime('%d.%m.%Y'))
"""