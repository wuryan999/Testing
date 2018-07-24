
import math
import random


class OrganSegmentator():
    def __init__(self):
        ## Target_size
        self.target_size = (256, 256)

        ## Only for NPY files.
        self.target_file = ''
        return

    def run(self):
        '''
        Please run this function AFTER setting all parameter.
        :return:
        A dictionary that have image path each have an organ name as a key and a path info as a value.
        '''
        result = {
            'Lungs': './img/sample_ich001.png',
            'Liver': './img/sample_iph001.png',
            'Kidney': './img/sample_iph001.png',
            'Spleen': './img/sample_iph001.png',
            'Muscles': './img/sample_iph001.png',
        }

        return result