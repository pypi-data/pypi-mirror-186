from one_interfaces import apierror_pb2 as apiError
from one_interfaces import apiresponse_pb2 as apiResponse
import google
import logging


def DeserializeResponse(response):
    try:
        pbResponse = apiResponse.ApiResponse()
        if response.status_code == 404:
            pbResponse.statusCode = 404
            return pbResponse
        pbResponse.ParseFromString(response.content)
        return pbResponse
    except Exception as Argument:
        logging.exception("Error occured in deserialization process", Argument)
        
