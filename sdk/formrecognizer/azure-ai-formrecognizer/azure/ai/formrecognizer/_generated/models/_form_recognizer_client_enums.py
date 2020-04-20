# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6246, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum

class ContentType(str, Enum):
    """Content type for upload
    """

    application_pdf = "application/pdf"  #: Content Type 'application/pdf'.
    image_jpeg = "image/jpeg"  #: Content Type 'image/jpeg'.
    image_png = "image/png"  #: Content Type 'image/png'.
    image_tiff = "image/tiff"  #: Content Type 'image/tiff'.

class FieldValueType(str, Enum):
    """Semantic data type of the field value.
    """

    string = "string"
    date = "date"
    time = "time"
    phone_number = "phoneNumber"
    number = "number"
    integer = "integer"
    array = "array"
    object = "object"

class Language(str, Enum):
    """Language code
    """

    en = "en"
    es = "es"

class LengthUnit(str, Enum):
    """The unit used by the width, height and boundingBox properties. For images, the unit is "pixel".
    For PDF, the unit is "inch".
    """

    pixel = "pixel"
    inch = "inch"

class ModelStatus(str, Enum):
    """Status of the model.
    """

    creating = "creating"
    ready = "ready"
    invalid = "invalid"

class OperationStatus(str, Enum):
    """Status of the queued operation.
    """

    not_started = "notStarted"
    running = "running"
    succeeded = "succeeded"
    failed = "failed"

class TrainStatus(str, Enum):
    """Status of the training operation.
    """

    succeeded = "succeeded"
    partially_succeeded = "partiallySucceeded"
    failed = "failed"
