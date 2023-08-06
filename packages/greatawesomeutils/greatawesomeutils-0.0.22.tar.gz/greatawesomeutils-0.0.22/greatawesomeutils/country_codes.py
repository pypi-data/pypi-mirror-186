from .base_data import BaseData

class CountryCodes(BaseData):
    def get_data(self):
        if False:
        # if IS_PRODUCTION:
            N_US = 0
            N_GB = 0
            N_FR = 0
            N_NL = 100
            N_NO = 0
            N_CA = 0
            N_IN = 0
            # N_US = 50
            # N_GB = 10
            # N_FR = 10
            # N_NL = 10
            # N_NO = 10
            # N_CA = 10
            # N_IN = 0
        else:
            N_US = 0
            N_GB = 0
            N_FR = 0
            N_NL = 100
            N_NO = 0
            N_CA = 0
            N_IN = 0

        US = [{"country_code": "US"}] * N_US
        GB = [{"country_code": "GB"}] * N_GB
        FR = [{"country_code": "FR"}] * N_FR
        NL = [{"country_code": "NL"}] * N_NL
        NO = [{"country_code": "NO"}] * N_NO
        CA = [{"country_code": "CA"}] * N_CA
        IN = [{"country_code": "IN"}] * N_IN

        result = US+GB+FR+NL+NO+CA+IN
        return result


CountryCodesInstance = CountryCodes() 

