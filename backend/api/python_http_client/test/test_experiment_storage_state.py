# coding: utf-8

"""
    Kubeflow Pipelines API

    This file contains REST API specification for Kubeflow Pipelines. The file is autogenerated from the swagger definition.  # noqa: E501

    The version of the OpenAPI document: 1.0.0-dev.1
    Contact: kubeflow-pipelines@google.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kfp_server_api
from kfp_server_api.models.experiment_storage_state import ExperimentStorageState  # noqa: E501
from kfp_server_api.rest import ApiException

class TestExperimentStorageState(unittest.TestCase):
    """ExperimentStorageState unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ExperimentStorageState
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kfp_server_api.models.experiment_storage_state.ExperimentStorageState()  # noqa: E501
        if include_optional :
            return ExperimentStorageState(
            )
        else :
            return ExperimentStorageState(
        )

    def testExperimentStorageState(self):
        """Test ExperimentStorageState"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
