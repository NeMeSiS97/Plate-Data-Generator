# coding: utf-8

"""
    OpenALPR Cloud API

    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re
res=[]

class PlateDetails(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, plate=None, matches_template=None, requested_topn=None, processing_time_ms=None, confidence=None, region=None, region_confidence=None, coordinates=None, candidates=None, vehicle_region=None, vehicle=None):
        """
        PlateDetails - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'plate': 'str',
            'matches_template': 'int',
            'requested_topn': 'int',
            'processing_time_ms': 'float',
            'confidence': 'float',
            'region': 'str',
            'region_confidence': 'float',
            'coordinates': 'list[Coordinate]',
            'candidates': 'list[PlateCandidate]',
            'vehicle_region': 'RegionOfInterest',
            'vehicle': 'VehicleDetails'
        }

        self.attribute_map = {
            'plate': 'plate',
            'matches_template': 'matches_template',
            'requested_topn': 'requested_topn',
            'processing_time_ms': 'processing_time_ms',
            'confidence': 'confidence',
            'region': 'region',
            'region_confidence': 'region_confidence',
            'coordinates': 'coordinates',
            'candidates': 'candidates',
            'vehicle_region': 'vehicle_region',
            'vehicle': 'vehicle'
        }

        self._plate = plate
        self._matches_template = matches_template
        self._requested_topn = requested_topn
        self._processing_time_ms = processing_time_ms
        self._confidence = confidence
        self._region = region
        self._region_confidence = region_confidence
        self._coordinates = coordinates
        self._candidates = candidates
        self._vehicle_region = vehicle_region
        self._vehicle = vehicle

    @property
    def plate(self):
        """
        Gets the plate of this PlateDetails.
        Best plate number for this plate

        :return: The plate of this PlateDetails.
        :rtype: str
        """
        return self._plate

    @plate.setter
    def plate(self, plate):
        """
        Sets the plate of this PlateDetails.
        Best plate number for this plate

        :param plate: The plate of this PlateDetails.
        :type: str
        """

        self._plate = plate

    @property
    def matches_template(self):
        """
        Gets the matches_template of this PlateDetails.
        Indicates whether the plate matched a regional text pattern

        :return: The matches_template of this PlateDetails.
        :rtype: int
        """
        return self._matches_template

    @matches_template.setter
    def matches_template(self, matches_template):
        """
        Sets the matches_template of this PlateDetails.
        Indicates whether the plate matched a regional text pattern

        :param matches_template: The matches_template of this PlateDetails.
        :type: int
        """

        self._matches_template = matches_template

    @property
    def requested_topn(self):
        """
        Gets the requested_topn of this PlateDetails.
        The max number of results requested

        :return: The requested_topn of this PlateDetails.
        :rtype: int
        """
        return self._requested_topn

    @requested_topn.setter
    def requested_topn(self, requested_topn):
        """
        Sets the requested_topn of this PlateDetails.
        The max number of results requested

        :param requested_topn: The requested_topn of this PlateDetails.
        :type: int
        """

        self._requested_topn = requested_topn

    @property
    def processing_time_ms(self):
        """
        Gets the processing_time_ms of this PlateDetails.
        Number of milliseconds to process the license plate

        :return: The processing_time_ms of this PlateDetails.
        :rtype: float
        """
        return self._processing_time_ms

    @processing_time_ms.setter
    def processing_time_ms(self, processing_time_ms):
        """
        Sets the processing_time_ms of this PlateDetails.
        Number of milliseconds to process the license plate

        :param processing_time_ms: The processing_time_ms of this PlateDetails.
        :type: float
        """

        self._processing_time_ms = processing_time_ms

    @property
    def confidence(self):
        """
        Gets the confidence of this PlateDetails.
        Confidence percentage that the plate number is correct

        :return: The confidence of this PlateDetails.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """
        Sets the confidence of this PlateDetails.
        Confidence percentage that the plate number is correct

        :param confidence: The confidence of this PlateDetails.
        :type: float
        """

        self._confidence = confidence

    @property
    def region(self):
        """
        Gets the region of this PlateDetails.
        Specified or detected region (e.g., tx for Texas)

        :return: The region of this PlateDetails.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this PlateDetails.
        Specified or detected region (e.g., tx for Texas)

        :param region: The region of this PlateDetails.
        :type: str
        """

        self._region = region

    @property
    def region_confidence(self):
        """
        Gets the region_confidence of this PlateDetails.
        Confidence percentage that the plate region is correct

        :return: The region_confidence of this PlateDetails.
        :rtype: float
        """
        return self._region_confidence

    @region_confidence.setter
    def region_confidence(self, region_confidence):
        """
        Sets the region_confidence of this PlateDetails.
        Confidence percentage that the plate region is correct

        :param region_confidence: The region_confidence of this PlateDetails.
        :type: float
        """

        self._region_confidence = region_confidence

    @property
    def coordinates(self):
        """
        Gets the coordinates of this PlateDetails.
        The X/Y coordinates of the license plate in the image Four coordinates are provided that form a polygon starting from the top-left and moving clockwise ending in the bottom left 

        :return: The coordinates of this PlateDetails.
        :rtype: list[Coordinate]
        """
	
	return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """
        Sets the coordinates of this PlateDetails.
        The X/Y coordinates of the license plate in the image Four coordinates are provided that form a polygon starting from the top-left and moving clockwise ending in the bottom left 

        :param coordinates: The coordinates of this PlateDetails.
        :type: list[Coordinate]
        """

        self._coordinates = coordinates
	global res
	res=coordinates
    @property
    def candidates(self):
        """
        Gets the candidates of this PlateDetails.
        All the top N candidates that could be the correct plate number

        :return: The candidates of this PlateDetails.
        :rtype: list[PlateCandidate]
        """
        return self._candidates

    @candidates.setter
    def candidates(self, candidates):
        """
        Sets the candidates of this PlateDetails.
        All the top N candidates that could be the correct plate number

        :param candidates: The candidates of this PlateDetails.
        :type: list[PlateCandidate]
        """

        self._candidates = candidates
	global plat
	plat = candidates

    @property
    def vehicle_region(self):
        """
        Gets the vehicle_region of this PlateDetails.


        :return: The vehicle_region of this PlateDetails.
        :rtype: RegionOfInterest
        """
        return self._vehicle_region

    @vehicle_region.setter
    def vehicle_region(self, vehicle_region):
        """
        Sets the vehicle_region of this PlateDetails.


        :param vehicle_region: The vehicle_region of this PlateDetails.
        :type: RegionOfInterest
        """

        self._vehicle_region = vehicle_region

    @property
    def vehicle(self):
        """
        Gets the vehicle of this PlateDetails.


        :return: The vehicle of this PlateDetails.
        :rtype: VehicleDetails
        """
        return self._vehicle

    @vehicle.setter
    def vehicle(self, vehicle):
        """
        Sets the vehicle of this PlateDetails.


        :param vehicle: The vehicle of this PlateDetails.
        :type: VehicleDetails
        """

        self._vehicle = vehicle

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
