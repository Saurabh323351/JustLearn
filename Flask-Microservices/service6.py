
"""
Example of Timer extension
"""

from random import choice

from nameko.timer import timer

class PingService(object):

    name="ping_service"

    @timer(interval=1)
    def ping_me(self):

        """
        pings every seconds
        :return:
        """
        print(choice(['SAURABH','RAJAT','SHUBHAM','PAPA' ,'BHAI','SANTOSH BHAI','MA']))