from mongo import MongoSession

import yapot

import requests

import time
import uuid

class Converter(object):

    def __init__(self,uri='mongodb://localhost:27017/', \
            download_dir='./docs/', resolution=200, verbose=False):

        self._session = MongoSession(
            uri=uri
        )
        self.download_dir = download_dir
        self.resolution = resolution
        self.verbose = verbose

    def _download_document(self, doc_url):

        if self.verbose == True:
            print "Downloading document ..."

        success = False
        if True:
        #try:
            filename = str(uuid.uuid4())
            r = requests.get(doc_url)
            with open('{0}{1}'.format(self.download_dir, filename),'wb') as f:
                f.write(r.content)
            success = True

            if self.verbose == True:
                print "Document downloaded successfully."

        #except:
        #    pass

        return filename

    def _convert_document(self, doc):

        """
        doc = {
            "parent_url": parent_url,
            "doc_url": doc_url,
            "scraper_id": "",
            "scrape_datetime": datetime.datetime.utc(),
            "converted": False,
            "convert_datetime": None,
            "local_filename": "",
            "link_text": link_text,
            "document_meta_data": {
            },
            "contents": "",
        }
        """

        if self.verbose == True:
            print "Unconverted document found, processing."

        success = False
        if True:
        #try:

            doc_filename = self._download_document(doc['doc_url'])
            doc_path = '{0}{1}'.format(self.download_dir, doc_filename)

            start_time = time.time()
            success, pdf_text = yapot.convert_document(
                pdf_filename     = doc_path,
                resolution       = self.resolution,
                delete_files     = True,
                page_delineation = '\n--------\n',
                verbose          = self.verbose,
                make_thumbs      = True,
                thumb_size       = 512,
                thumb_dir        = self.download_dir,
                thumb_prefix     = '{0}_thumb_page_'.format(doc_filename),
            )
            convert_time = time.time() - start_time

            if self.verbose == True:
                print "Updating document ..."

            if success == True:
                session.update_document(
                    id                 = doc['_id'],
                    contents           = pdf_text,
                    document_meta_data = {},
                    local_filename     = doc_filename,
                    convert_time       = convert_time,
                )

            success = True

            if self.verbose == True:
                print "Done updating document."

        #except:
        #    pass

        if self.verbose == True:
            print "Done processing document."

        return success

    def start_converting(self, ):

        if True:
        #try:
            while(1):
                if self.verbose == True:
                    print "Checking for unconverted documents ..."
                success, doc = self._session.get_one_unconverted()
                print success, doc
                if success and doc != None:
                    self._convert_document(doc)
                time.sleep(1)
        #except:
        #    pass
        
        return

if __name__ == '__main__':

    # TODO: decode switches from CLI
    converter = Converter(verbose=True)
    results = converter._session.documents.remove({})
    success = converter._session.add_document(
        parent_url = 'http://timduffy.me/',
        doc_url = 'http://timduffy.me/Resume-TimDuffy-20130813.pdf',
        scraper_id = str(uuid.uuid4()),
        link_text = 'Resume',
    )
    print success
    results = converter._session.documents.find()
    docs = []
    for result in results:
        docs.append(result)
    print docs
    converter.start_converting()

