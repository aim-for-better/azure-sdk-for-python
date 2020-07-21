# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class RecognitionModel(str, Enum):

    recognition_01 = "recognition_01"
    recognition_02 = "recognition_02"
    recognition_03 = "recognition_03"


class Gender(str, Enum):

    male = "male"
    female = "female"


class GlassesType(str, Enum):

    no_glasses = "noGlasses"
    reading_glasses = "readingGlasses"
    sunglasses = "sunglasses"
    swimming_goggles = "swimmingGoggles"


class HairColorType(str, Enum):

    unknown = "unknown"
    white = "white"
    gray = "gray"
    blond = "blond"
    brown = "brown"
    red = "red"
    black = "black"
    other = "other"


class AccessoryType(str, Enum):

    head_wear = "headWear"
    glasses = "glasses"
    mask = "mask"


class BlurLevel(str, Enum):

    low = "Low"
    medium = "Medium"
    high = "High"


class ExposureLevel(str, Enum):

    under_exposure = "UnderExposure"
    good_exposure = "GoodExposure"
    over_exposure = "OverExposure"


class NoiseLevel(str, Enum):

    low = "Low"
    medium = "Medium"
    high = "High"


class FindSimilarMatchMode(str, Enum):

    match_person = "matchPerson"
    match_face = "matchFace"


class TrainingStatusType(str, Enum):

    nonstarted = "nonstarted"
    running = "running"
    succeeded = "succeeded"
    failed = "failed"


class SnapshotApplyMode(str, Enum):

    create_new = "CreateNew"


class SnapshotObjectType(str, Enum):

    face_list = "FaceList"
    large_face_list = "LargeFaceList"
    large_person_group = "LargePersonGroup"
    person_group = "PersonGroup"


class OperationStatusType(str, Enum):

    notstarted = "notstarted"
    running = "running"
    succeeded = "succeeded"
    failed = "failed"


class FaceAttributeType(str, Enum):

    age = "age"
    gender = "gender"
    head_pose = "headPose"
    smile = "smile"
    facial_hair = "facialHair"
    glasses = "glasses"
    emotion = "emotion"
    hair = "hair"
    makeup = "makeup"
    occlusion = "occlusion"
    accessories = "accessories"
    blur = "blur"
    exposure = "exposure"
    noise = "noise"


class DetectionModel(str, Enum):

    detection_01 = "detection_01"
    detection_02 = "detection_02"
