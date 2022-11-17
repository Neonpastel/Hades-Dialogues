from re import findall

class Dialogue():

    def __init__(self):
        self.sentences = []
        self.id = ""
    
    def get_description(self):
        return self._description
    
    @property
    def description(self):
        return " ".join(split_camelcase_into_array(self.id))

    def readable(self):
        joined_sentences = "\n".join(self.sentences)
        return "{0}\n{1}".format(self.description, joined_sentences)
    
    def __str__(self):
        return self.readable()

    def __repr__(self):
        return self.readable()
        

def split_camelcase_into_array(string):
    return findall(r"[A-Z][a-z0-9]*", string)