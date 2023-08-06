from . import bing
from . import google
from . import yandex
from . import apple
from . import baidu
# i don't know why i picked this. i literally can't call extractor.[service]
# unless if i import them here, and __all__ causes pyinstaller to act very weirdly. too bad!

class ServiceNotSupported(Exception):
    message = "Service does not support this function"
    pass

class ServiceNotFound(Exception):
    message = "Service not found"
    pass

class ServiceShortURLFound(Exception):
    message = "Short URL used. Avoid using them as they don't work with this service"
    pass

class NoPanoIDAvailable(Exception):
    message = "Panorama ID not available in parsed coordinate"

class PanoIDInvalid(Exception):
    message = "Invalid Panorama ID. Please input a valid one and try again"

class MetadataPanoIDParsed(Exception):
    message = "Service cannot parse Panorama ID to obtain metadata"

class MetadataCoordsParsed(Exception):
    message = "Service cannot parse coordinates to obtain metadata"