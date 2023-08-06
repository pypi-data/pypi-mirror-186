class arguments:
    """
    arguments list xxx=yyy

    delimter =

    returns dictionary of terms
    """
    args = {}
    delimiter = "="

    def __init__(self, args, delimters : str = "="):
        if delimters is not None :
            self.delimiter = delimters
        if type(args) is dict:
            self.args = args

        elif type(args) is list:
            self.args = self.splitParmeters(args)

    def splitParmeters(self,lines):
        newS = {}
        for word in lines:
            word = word.split(self.delimiter)
            if len(word) > 1:
                ww1 = word[0]
                ww2 = word[1]

                newS.update({ww1: ww2})
        return newS

    def getDefault(self, key, default):
        value = self.args.get(key)
        if value is None:
            return default
        return value
