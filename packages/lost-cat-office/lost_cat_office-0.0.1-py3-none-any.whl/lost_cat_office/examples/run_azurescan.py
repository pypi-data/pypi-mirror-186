"""A simple module to demostrate how to run the azure scanner
to run it requires the following:
 Env Var
    Name:   AZURE_STORAGE_CONNSTTR
    Value:  <The connection string used to connected to the azure blob storage>
"""
import logging
from datetime import datetime
import os
import multiprocessing as mp
import threading as td

from queue import Empty
from lost_cat_office.processors.azureblob_processor import AzureStorageProcessor

nb_name = "AzureExp"
if not os.path.exists("logs"):
    os.mkdir("logs")

logger = logging.getLogger(__name__)
_logname = "{}.{}".format(nb_name, datetime.now().strftime("%Y%m%d"))
logging.basicConfig(filename=f'logs\log.{_logname}.log', level=logging.INFO)

def loader(uri:str, in_queue: mp.Queue, out_queue: mp.Queue):
    """ Initiate the ABS
        Add the base uri
    """
    try:
        azbc_obj = AzureStorageProcessor()
    except Exception as ex:
        logger.error("Error loading class %s", ex)
        print("Unable to load class!")
        return

    # load the path for the run...
    in_queue.put({"uri": uri, "uriid": -1})

    # start the scan
    azbc_obj.in_queue(in_queue=in_queue)
    azbc_obj.out_queue(out_queue=out_queue)
    azbc_obj.scan()
    out_queue.put("DONE")

def reader(out_queue: mp.Queue):
    while out_queue:
        try:
        # set a timeout, and handle the semiphore case too
            o_item = out_queue.get(timeout=10) if out_queue else None
            # URIs
            #   -> Metadata
            #   -> Versions
            #       -> metadata
            if o_item == "DONE":
                break

            # if the user wants to kill the queue if there are not entries...
            # requires timeout set, otherwise the queue get blocks...
            if not o_item:
                break

            logger.debug("Out: %s", o_item)

            # save the item to the catalog...
            _uri = o_item.get("uri")

            # process and do something with the item
            logger.info("URI: %s", _uri)

        except Empty:
            break

if __name__ == "__main__":
    """run the processor and process the outputs"""
    uri = "" # <<<< put the path or root name for the blob storate folder here

    # create the queue to read from and load
    in_queue = mp.Queue()
    out_queue = mp.Queue()

    # start this in a thread...
    threads = []

    # the loader class
    threads.append(td.Thread(target=loader, args=[uri, in_queue, out_queue]))

    # the reader class
    for i in range(5):
        threads.append(td.Thread(target=reader, args=[out_queue]))

    for t in threads:
        t.start()
        t.join()

    
