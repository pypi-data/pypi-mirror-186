from .base_data import BaseData
from greatawesomeutils.lang import *

class UserAgents(BaseData):
    def get_data(self):
        
        if is_windows():
            _106_AGENT = {"user_agent":        "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.37"}
            _105_AGENT = {"user_agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
            _104_2_AGENT = {"user_agent":  "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36"}
            _104_1_AGENT = {"user_agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.101 Safari/537.36"}
            _103_AGENT = {"user_agent":  "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36"}
            _101_AGENT = {"user_agent":  "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951 Safari/537.36"}
            _100_AGENT = {"user_agent":    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896 Safari/537.36"}
            _99_AGENT = {"user_agent":   "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844 Safari/537.36"}
            _98_AGENT = {"user_agent":    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758 Safari/537.36"}
            _97_AGENT = {"user_agent":    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692 Safari/537.36"}
            _96_AGENT = {"user_agent":    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664 Safari/537.36"}
            _95_AGENT = {"user_agent":    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638 Safari/537.36"}
            _94_AGENT = {"user_agent":   "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606 Safari/537.36"}
        else:
            _106_AGENT = {"user_agent":        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.37"}
            _105_AGENT = {"user_agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
            _104_2_AGENT = {"user_agent":  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36"}
            _104_1_AGENT = {"user_agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.101 Safari/537.36"}
            _103_AGENT = {"user_agent":  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36"}
            _101_AGENT = {"user_agent":  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951 Safari/537.36"}
            _100_AGENT = {"user_agent":    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896 Safari/537.36"}
            _99_AGENT = {"user_agent":   "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844 Safari/537.36"}
            _98_AGENT = {"user_agent":    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758 Safari/537.36"}
            _97_AGENT = {"user_agent":    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692 Safari/537.36"}
            _96_AGENT = {"user_agent":    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664 Safari/537.36"}
            _95_AGENT = {"user_agent":    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638 Safari/537.36"}
            _94_AGENT = {"user_agent":   "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606 Safari/537.36"}


        # Versions
        V_106 = 37
        V_105 = 42
        V_104_1 = 1
        V_104_2 = 1
        V_103 = 2
        V_101 = 1
        V_99 = 10
        V_100 = 1
        V_98 = 1
        V_97 = 1
        V_96 = 1
        V_95 = 1
        V_94 = 1

        _106 = [_106_AGENT] * V_106
        _105 = [
            _105_AGENT] * V_105
        _104_1 = [
            _104_1_AGENT] * V_104_1
        _104_2 = [
            _104_2_AGENT] * V_104_2
        _103 = [
            _103_AGENT] * V_103
        _101 = [
            _101_AGENT] * V_101
        _99 = [
            _99_AGENT] * V_99
        _100 = [
            _100_AGENT] * V_100
        _98 = [
            _98_AGENT] * V_98
        _97 = [
            _97_AGENT] * V_97
        _96 = [
            _96_AGENT] * V_96
        _95 = [
            _95_AGENT] * V_95
        _94 = [_94_AGENT] * V_94

        result = _106 + _105 + _104_1 + _104_2 + _103 + \
            _101 + _99 + _100 + _98 + _97 + _96 + _95 + _94

        return result

UserAgentsInstance = UserAgents() 
if __name__ == '__main__':
    print(UserAgentsInstance.get_hashed_value('a'))
    print(UserAgentsInstance.get_hashed_value('a'))
    print(UserAgentsInstance.get_hashed_value('b'))
