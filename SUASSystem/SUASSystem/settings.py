class GCSSettings(object):

    CAMERA_NORTH_OFFSET = 20

    UAV_CONNECTION_STRING = "tcp:127.0.0.1:14551"

    INTEROP_URL = "http://10.10.130.2:8000"
    INTEROP_USERNAME = "Flint"   #"img_proc_test"
    INTEROP_PASSWORD = "271824758" #robotics

    MSL_ALT = 446.42#22
    SDA_MIN_ALT = 50#110

    GENERATED_DATA_LOCATION = "image_data"
    '''
    BASE_LETTER_CATEGORIZER_PCA_PATH
    Vale's path: /Users/vtolpegin/Desktop/GENERATED FORCED WINDOW PCA
    '''
    VALE_BASE_LETTER_CATEGORIZER_PATH = "/Users/vtolpegin/Desktop/GENERATED FORCED WINDOW PCA"
    BASE_LETTER_CATEGORIZER_PCA_PATH = VALE_BASE_LETTER_CATEGORIZER_PATH
    '''
    BASE_ORIENTATION_CLASSIFIER_PCA_PATH:
    Vale's path: /Users/vtolpegin/Desktop/GENERATED 180 ORIENTATION PCA
    '''
    VALE_BASE_ORIENTATION_CLASSIFIER_PCA_PATH = "/Users/vtolpegin/Desktop/GENERATED 180 ORIENTATION PCA"
    BASE_ORIENTATION_CLASSIFIER_PCA_PATH = VALE_BASE_ORIENTATION_CLASSIFIER_PCA_PATH

    SD_CARD_NAME = "NX500"

    MIN_DIST_BETWEEN_TARGETS_KM = 30.0/1000.0
    KNOTS_PER_METERS_PER_SECOND = 1.94384448

    IMAGE_PROC_PPSI = 1.5

    UAV_VERSION_TYPES = ("9.1","10")
    UAV_VERSION = UAV_VERSION_TYPES[0]
