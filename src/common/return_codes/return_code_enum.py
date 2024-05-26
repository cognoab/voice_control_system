from enum import IntEnum, auto


# fmt: off
class ReturnCode(IntEnum):
    SUCCESS          = 0
    UNEXPECTED_ERROR = 1

    STT_ERROR = 1_000
    """Speech-To-Text general error"""
    STT_UNSUPPORT_LANGUAGE       = auto()
    STT_FILE_NOT_FOUND           = auto()
    STT_TRANSCRIPT_FAILED        = auto()
    STT_DETECT_LANGUAGE_FAILED   = auto()
    STT_INVALID_DATA             = auto()
    STT_INVALID_FORMAT           = auto()
    STT_FAILED_TO_DOWNLOAD_MODEL = auto()

    TTC_ERROR = 2_000
    """Text-To-Command general error"""
    TTC_UNKNOWN_COMMAND = auto()
    TTC_PARSING_ERROR   = auto()

    CX_ERROR = 3_000
    """Command Executor general error"""
    CX_NO_HANDLER        = auto()
    CX_PERMISSION_DENIED = auto()
    CX_INVALID_DATA      = auto()

    VC_ERROR = 4_000
    """Voice Control general error"""
# fmt: on
