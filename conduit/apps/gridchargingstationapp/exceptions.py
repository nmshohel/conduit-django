from rest_framework.exceptions import APIException


class GridChargingStationDoesNotExist(APIException):
    status_code = 400
    default_detail = 'The requested Solar does not exist.'