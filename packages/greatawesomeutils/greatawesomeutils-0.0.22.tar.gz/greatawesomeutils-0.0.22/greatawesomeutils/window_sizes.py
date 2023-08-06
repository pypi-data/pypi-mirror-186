from .base_data import BaseData
class WindowSizes(BaseData):
    def get_data(self):

        # Windows
        N_1920_1080 = 35
        N_1366_768 = 26
        N_1536_864 = 16
        N_1280_720 = 9
        N_1440_900 = 9
        N_1600_900 = 5
        _1920_1080 = [{"window_size": "1920,1080"}] * N_1920_1080
        _1366_768 = [{"window_size": "1366,768"}] * N_1366_768
        _1536_864 = [{"window_size": "1536,864"}] * N_1536_864
        _1280_720 = [{"window_size": "1280,720"}] * N_1280_720
        _1440_900 = [{"window_size": "1440,900"}] * N_1440_900
        _1600_900 = [{"window_size": "1600,900"}] * N_1600_900

        result = _1920_1080 + _1366_768 + _1536_864 + _1280_720 + _1440_900 + _1600_900
        return result

WindowSizesInstance = WindowSizes() 
