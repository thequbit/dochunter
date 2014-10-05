import json
import os
import datetime

from pymongo import MongoClient

class MongoSession():


    def __init__(self, uri='mongodb://localhost:27017/',db='dochunter'):

        self._dbclient = MongoClient(uri)
        self._db = self._dbclient[db]

        self.documents = self._db['documents']
        self.runs = self._db['runs']
        self.scrapers = self._db['scrapers']


    def add_document(self, parent_url, doc_url, scraper_id, link_text):

        success = False
        if True:
        #try:
            doc = {
                "parent_url": parent_url,
                "doc_url": doc_url,
                "scraper_id": "",
                "scrape_datetime": datetime.datetime.now(),
                "converted": False,
                "convert_datetime": None,
                "convert_time": 0,
                "local_filename": "",
                "link_text": link_text,
                "document_meta_data": {
                },
                "contents": "",
            }
            self.documents.insert(doc)
            success = True
        #except:
        #    pass

        return success

    def get_one_unconverted(self):

        success = False
        try:
            doc = self.documents.find_one({'converted': False})
            success = True
        except:
            pass

        return success, doc

    def update_document(self, id, contents, document_meta_data, \
            local_filename, convert_time):

        success = False
        try:

            doc = self.documents.find_one({'_id': id})

            doc['contents'] = contents
            doc['document_meta_data'] = document_meta_data
            doc['local_filename'] = local_filename
            doc['convert_time'] = convert_time
            doc['converted'] = True

            newdoc = self.documents.update(
                {'_id': id},
                doc,
            )
            
            success = True

        except:
            pass

        return success, newdoc

    def register_run(self, parent_url, processed_links, bad_links, \
            link_count, ignored_count, url_data, bandwidth, start_datetime):

        success = False
        try:
            run = {
                'parent_url': parent_url,
                'processed_links': processed_links,
                'bad_links': bad_links,
                'link_count': link_count,
                'ignored_count': ignored_count,
                'url_data': url_data,
                'bandwidth': bandwidth,
                'start_datetime': start_datetime,
                'finish_datetime': datetime.datetime.now(),
            }
            self.runs.insert(run)
            success = True
        except:
            pass

        return success

    def update_scraper_status(self, scraper_id, parent_url, status, url_data):

        success = False
        try:
            status = {
                'scraper_id': scraper_id,
                'parent_url': parent_url,
                'status': status,
                'url_data': url_data,
            }
            self.scrapers.update(
                {'scraper_id': scraper_id},
                status,
                True, #upsert
            )
            success = True
        except:
            pass

        return success
