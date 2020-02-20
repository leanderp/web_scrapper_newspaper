import logging
import subprocess
import os

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)
news_sites_uids = ['eluniversal', 'elpais']

def main():
    _extract()
    _transform()
    _load()

def _extract():
    logger.info('Starting extract process')
    for news_sites_uid in news_sites_uids:
        subprocess.run(['python', 'main.py', news_sites_uid], cwd='./extract')
        file_generate = _search_file('.\extract', news_sites_uid)
        dirty_data_filename = '{}.csv'.format(news_sites_uid)
        subprocess.run(['move', '.\extract\{}'.format(file_generate), '.\Transform\{}'.format(dirty_data_filename)], shell = True)

        
def _transform():
    logger.info(' Starting transform process')
    for news_sites_uid in news_sites_uids:
        dirty_data_filename = '{}.csv'.format(news_sites_uid)
        clean_data_filename = 'clean_{}'.format(dirty_data_filename)
        subprocess.run(['python', 'newspaper_receipe.py', dirty_data_filename], cwd='./Transform')
        subprocess.run(['del', '.\Transform\{}'.format(dirty_data_filename)], shell = True)
        subprocess.run(['move', '.\Transform\{}'.format(clean_data_filename), '.\load\{}'.format(dirty_data_filename)], shell = True)


def _load():
    logger.info('Stanting load process')
    for news_sites_uid in news_sites_uids:
        clean_data_filename = '{}.csv'.format(news_sites_uid)
        subprocess.run(['python', 'main.py', clean_data_filename], cwd='./load')
        subprocess.run(['del', '.\load\{}'.format(clean_data_filename)], shell= True)

def _search_file(path, file_match):
    logger.info('Searching file')
    for rutas in list(os.walk(path))[0]:
        if len(rutas) > 1:
            for file in rutas:
                if file_match in file:
                    logger.info('File: {}'.format(file))
                    return file
    return None

if __name__ == "__main__":
    main()