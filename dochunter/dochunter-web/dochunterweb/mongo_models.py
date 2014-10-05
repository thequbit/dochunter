import json
import os

from pymongo import MongoClient

class MongoSession():


    def __init__(self, uri='mongodb://localhost:27017/',db='dochunter'):

        self._dbclient - MongoClient(uri)
        self._db = _dbclient[db]

        self.documents = self._db['documents']
        self.runs = self._db['runs']
        

    def add_document(self, parent_url, doc_url, scraper_id, link_text):

        success = False
        try:
            doc = {
                "parent_url": parent_url,
                "doc_url": doc_url,
                "scraper_id": "",
                "scrape_datetime": datetime.datetime.utc(),
                "converted": False,
                "local_filename": "",
                "link_text": link_text,
                "document_meta_data": {
                },
                "contents": "",
            }
            self.documents.insert(doc)
            success = True
        except:
            pass

        return sucess

    def get_document_by_id(self,id):

        success = False
        try:
            doc = self.documents.find_one({'id': id})
            success = True
        except:
            pass

        return success, doc

    def get_documents_by_parent_url(self, parent_url):
    
        success = False
        docs = []
        try:
            # get all of the documents for the parent url, excluding 
            # the converted contents text
            results = self.documnets.find(
                {
                    'parent_url': parent_url
                },
                {
                    'parent_url': 1,
                    'doc_url': 1,
                    'scraper_id': 1,
                    'scrape_datetime': 1,
                    'converted': 1,
                    'local_filename': 1,
                    'link_text': 1,
                    'document_meta_data': 1,
                },
            )
            for result in docs:
                docs.append(result)
            success = True
        except:
            pass

        return docs

    
