from rest_framework.exceptions import APIException


class NetMeterDoesNotExist(APIException):
    status_code = 400
    default_detail = 'The requested Net Meter does not exist.'