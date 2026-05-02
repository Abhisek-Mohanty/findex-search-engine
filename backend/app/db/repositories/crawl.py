import io
import secrets
from typing import Any
from sqlalchemy import or_
from starlette.exceptions import HTTPException
from sqlalchemy.orm import load_only, contains_eager, joinedload
import re

from app.api.response.http_response import SendErrorResponse, SendExportResponse, SendSuccessResponse

from app.resources.helper.common import *
from app.db.repositories.base import BaseRepository
from app.resources.helper.moment import Moment
from app.core.config import CLIENT_PATH, DEFAULT_PASSWORD, SUPPORT_MAILID, HR_SUPPORT_MAIL, VERIFICATION_LINK_VALID_DAYS
from app.resources.constant import EMPLOYEEMENT_STATUS, STATUS, VERIFCATION_TYPE
from app.services import security
from app.resources.library.S3.index import s3Bucket
from app.resources.library.email.sns import SnsEmail
from app.resources.library.digio.digio import Digio
from app.resources.library.crimecheck.crimeCheck import CrimeChecks
from app.resources.library.msme.msme import MSME
from fastapi.encoders import jsonable_encoder

from app.models.domain.db import *

class EmployeeRepository(BaseRepository):  
    pass