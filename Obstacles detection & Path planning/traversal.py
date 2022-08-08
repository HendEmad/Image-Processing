# -*- coding: utf-8 -*-

# Traversing through the image to perform image processing
from joblib.numpy_pickle_utils import xrange


def sliding_window(image, stepSize, windowSize):
    # slide a window across the image
    for y in xrange(0, image.shape[0], stepSize):
        for x in xrange(0, image.shape[1], stepSize):
            # yield the current window
            yield x, y, image[y:y + windowSize[1], x:x + windowSize[0]]
