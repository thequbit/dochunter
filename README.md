dochunter
=========

website and infrastructure for finding, converting, indexing, and managing documents online

How it works:

![dochunter](http://i.imgur.com/iRmXO1u.png)


First, fork the repo and clone it locally

    > git clone https://github.com/<your_user_name>/dochunter

Second, install these programs:

    > sudo apt-get install imagemagick
    > sudo apt-get install tesseract-ocr
    > sudo apt-get install mongodb
    > sudo apt-get install rabbitmq-server
    > sudo apt-get install mysql-server
    > sudo apt-get install mysql-client
    
Third, install these libs

    > pip install barkingowl
    > pip instlal yapot
    > pip install pymongo
    > pip install pyramid
    > pip install mysql-python
    > pip install waitress

Fourth, launch the intrastructure

    > cd dochunter/dochunter/dochunter-intrastructure
    > ./launch_intrastructure.sh

Finally, launch the website

    > cd dochunter/dochunter/dochunter-web
    > pserve development.ini
            - or -
    > pserve production.ini (after setting configuring mysql)
    
    
    
