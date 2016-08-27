from __future__ import absolute_import
from __future__ import print_function

import os, sys
from PIL import Image
from project.celery import app
import logging
import time

logger = logging.getLogger(__name__)


def thumbnail_name(file_path):
    return 'images/' + file_path.split('/')[-1].split('.')[0] + ".thumbnail.jpg"


@app.task
def create_thumbnail(file_path):
    time.sleep(10)
    size = (128, 128)
    outfile = thumbnail_name(file_path)

    if file_path != outfile:
        try:
            im = Image.open(file_path)
            im.thumbnail(size)
            im.save(outfile, "JPEG")
            logger.info('Creathed thumbnal to {0}'.format(outfile))
        except IOError as e:
            logger.error("cannot create thumbnail for {0}: {1}".format(file_path, e))
