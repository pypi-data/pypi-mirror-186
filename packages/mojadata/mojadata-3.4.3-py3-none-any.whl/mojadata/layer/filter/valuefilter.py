from six import text_type

class ValueFilter(object):
    '''
    Compares a section of a value to a target value.

    :param target_val: the target value to compare against
    :type target_val: any string-convertible type
    '''

    def __init__(self, target_val, *args, **kwargs):
        self._target_val = target_val
        
    def __call__(self, val):
        '''
        Evaluates the filter against a value.

        :returns: True if the values match, False if not
        '''
        return text_type(val) == text_type(self._target_val)
