# --------------------------------------------------------------------------
# Source file provided under Apache License, Version 2.0, January 2004,
# http://www.apache.org/licenses/
# (c) Copyright IBM Corp. 2017, 2022
# --------------------------------------------------------------------------

import os

COMMON_API_PREFIX = "COMMON_API_"
IAM_SERVICE_URL_PREFIX = "IAM_SERVICE_URL_"
BCOS_URL_PREFIX = "BCOS_URL_"
COS_URL_PREFIX = "COS_URL_"

ENV_ID_onPrem = "on-prem"
# Dallas stages
ENV_ID_prod = "prod"
ENV_ID_qa = "qa"
ENV_ID_YS1_prod = "YS1 prod"
ENV_ID_dev = "dev"
# London stages
ENV_ID_prod_london = "prod london"
ENV_ID_qa_london = "qa london"
# detection failed (local
ENV_ID_local = "local"
# else
ENV_ID_prod_fra = "prod fra"
ENV_ID_prod_tok = "prod tok"

ENV_ID_LOCAL = "local"

ENDPOINT_DICT = {
    "COMMON_API_PROD": "https://api.dataplatform.cloud.ibm.com",
    "COMMON_API_QA": "https://api.dataplatform.test.cloud.ibm.com",
    "COMMON_API_YS1_PROD": "https://apsx-api.stage1.ng.bluemix.net",
    "COMMON_API_QA_LONDON": "https://apsx-api-qa.eu-gb.bluemix.net",
    "COMMON_API_PROD_FRA": "https://api.eu-de.dataplatform.cloud.ibm.com",

    "IAM_SERVICE_URL_PROD": "https://iam.ng.bluemix.net/oidc/token",
    "IAM_SERVICE_URL_QA": "https://iam.ng.bluemix.net/oidc/token",
    "IAM_SERVICE_URL_YS1_PROD": "https://iam.stage1.ng.bluemix.net/oidc/token",
    "IAM_SERVICE_URL_QA_LONDON": "https://iam.eu-gb.bluemix.net/oidc/token",
    "IAM_SERVICE_URL_PROD_FRA": "https://iam.eu-de.bluemix.net/oidc/token",

    "BCOS_URL_PROD": "https://s3-api.us-geo.objectstorage.softlayer.net",
    "BCOS_URL_QA": "https://s3-api.us-geo.objectstorage.softlayer.net",
    "BCOS_URL_YS1_PROD": "https://s3.us-west.objectstorage.uat.softlayer.net",
    "BCOS_URL_QA_LONDON": "https://s3.eu-geo.objectstorage.softlayer.net",
    "BCOS_URL_PROD_FRA": "https://s3.eu-geo.objectstorage.softlayer.net",

    "COS_URL_PROD": "https://s3-api.dal-us-geo.objectstorage.softlayer.net",
    "COS_URL_QA": "https://s3-api.dal-us-geo.objectstorage.softlayer.net",
    "COS_URL_YS1_PROD": "https://s3-api.dal-us-geo.objectstorage.softlayer.net",
    "COS_URL_QA_LONDON": "https://s3-api.us-geo.objectstorage.softlayer.net",

    # legacy Softlayer COS, supported only for Dallas and London
    "COS_URL_PROD_FRA": "" # not here
}

# introducing a new style of looking up endpoints
STAGE_ENDPOINTS_MAP = {
    ENV_ID_dev : {
        COMMON_API_PREFIX:
        "https://api.dataplatform.dev.cloud.ibm.com",
        IAM_SERVICE_URL_PREFIX:
        "https://iam.stage1.ng.bluemix.net/oidc/token",
        BCOS_URL_PREFIX:
        "https://s3.us-west.objectstorage.uat.softlayer.net",
        COS_URL_PREFIX:
        "https://s3-api.dal-us-geo.objectstorage.softlayer.net"
    },

    ENV_ID_prod_london : {
        COMMON_API_PREFIX:
        "https://api.eu-gb.dataplatform.cloud.ibm.com",
        IAM_SERVICE_URL_PREFIX:
        "https://iam.eu-gb.bluemix.net/oidc/token",
        BCOS_URL_PREFIX:
        "https://s3.eu-geo.objectstorage.softlayer.net",
        COS_URL_PREFIX:
        "https://s3-api.us-geo.objectstorage.softlayer.net"
    },

    ENV_ID_prod_tok : {
        COMMON_API_PREFIX:
        "https://api.jp-tok.dataplatform.cloud.ibm.com",
        IAM_SERVICE_URL_PREFIX:
        "https://iam.bluemix.net/oidc/token",
        BCOS_URL_PREFIX:
        "https://s3.ap-geo.objectstorage.softlayer.net",
        COS_URL_PREFIX: None
    }
}

APSX_URL_ENVVARNAME = 'RUNTIME_ENV_APSX_URL'

class Context(object):
    
    def __init__(self):
        self.determineStage()
    
    def determineStage(self):
        """Determines the runtime environment.
        
        Detection is based on RUNTIME_ENV_* environment variables.
        If detection fails, this means we are on a local environment"""
        
        STOREFRONT_BLUEMIX_PROD = "bluemix/prod"
        STOREFRONT_BLUEMIX_STAGING = "bluemix/staging"
        STOREFRONT_ONPREM = "on-prem"
        NOTEBOOK_PROD = "prod"
        NOTEBOOK_QA = "staging"
        NOTEBOOK_DEV = "dev"
        NOTEBOOK_ONPREM = "on-prem"
        REGION_DALLAS = "us-south"
        REGION_LONDON = "eu-gb"
        REGION_FRANKFURT = "eu-de"
        REGION_TOKYO = "jp-tok"
        
        env_storefront = os.getenv("RUNTIME_ENV_STOREFRONT", "invalidStorefrontEnv")
        env_notebook = os.getenv("RUNTIME_ENV_NOTEBOOK", "invalidNotebookEnv")
        env_region = os.getenv("RUNTIME_ENV_REGION", "invalidRegionEnv")
        
        self.envID = ENV_ID_LOCAL
        if env_storefront == STOREFRONT_BLUEMIX_PROD:
            if env_notebook == NOTEBOOK_PROD:
                self.envID = ENV_ID_prod # default is Dallas
                if env_region == REGION_LONDON:
                    self.envID = ENV_ID_prod_london
                elif env_region == REGION_FRANKFURT:
                    self.envID = ENV_ID_prod_fra
                elif env_region == REGION_TOKYO:
                    self.envID = ENV_ID_prod_tok
            elif env_notebook == NOTEBOOK_QA:
                self.envID = ENV_ID_qa
                if env_region == REGION_LONDON:
                    self.envID = ENV_ID_qa_london
        elif env_storefront == STOREFRONT_BLUEMIX_STAGING:
            if env_notebook == NOTEBOOK_PROD:
                self.envID = ENV_ID_YS1_prod
            elif env_notebook == NOTEBOOK_DEV:
                self.envID = ENV_ID_dev
        elif env_storefront == STOREFRONT_ONPREM:
            if env_notebook == NOTEBOOK_ONPREM:
                self.envID = ENV_ID_onPrem
                
    def get_endpoint_from_dict(self, prefix):
        if self.envID in STAGE_ENDPOINTS_MAP:
            return STAGE_ENDPOINTS_MAP[self.envID][prefix]

        key = prefix + self.envID.upper().replace(" ", "_")
        return  ENDPOINT_DICT.get(key, "")
    
    def get_service_cos_url(self, stage=None):
        return self.get_endpoint_from_dict(COS_URL_PREFIX)

    def get_bcos_service_url(self, stage=None):
        return self.get_endpoint_from_dict(BCOS_URL_PREFIX)

    def get_iam_service_url(self, stage=None):
        if(self.envID == ENV_ID_LOCAL):
            return None
        else:
            return self.get_endpoint_from_dict(IAM_SERVICE_URL_PREFIX)

    def get_common_api_url(self, stage=None):

        if (APSX_URL_ENVVARNAME in os.environ and
            (os.environ[APSX_URL_ENVVARNAME].startswith('https://') or
             os.environ[APSX_URL_ENVVARNAME].startswith('http://')
            )):
            # override, or used outside of Watson Studio Cloud
            return os.environ[APSX_URL_ENVVARNAME]

        return self.get_endpoint_from_dict(COMMON_API_PREFIX)
    
            