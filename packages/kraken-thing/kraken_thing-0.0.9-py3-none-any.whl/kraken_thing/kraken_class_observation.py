
import datetime
import kraken_datatype as dt 
from kraken_schema_org import kraken_schema_org as k
from kraken_thing import json_xp as json

class Observation:

    def __init__(self, record_type, record_id, key, value, credibility = None, date = None):

        self.record_type = record_type
        self.record_id = record_id
        
        self.original_key = key
        self.normalized_key = None
        self.valid_key = False
        
        
        self.original_value = value
        self.normalized_value = None
        self.valid_value = False     # bool if value has been validated
        self.value = value
        self.credibility = credibility
        self.date = date

        self.db_date = datetime.datetime.now()


        # metadata
        self.agent = None
        self.instrument = None
        self.object = None

        self.key = key
        self.value = value
    
    def __repr__(self):

        return json.dumps(self.dump())

    
    def __eq__(self, other):
        '''
        '''

        if self.dump() == other.dump():
            return True

        return False


    def __gt__(self, other):
        '''
        '''
        if not self.base_equal(other):
            return False

        # Credibility
        if self.credibility and not other.credibility:
            return True
        if other.credibility and not self.credibility:
            return False
        
        if self.credibility and other.credibility and self.credibility > other.credibility:
            return True
        if self.credibility and other.credibility and self.credibility < other.credibility:
            return False

            
        # date
        if self.date and not other.date:
            return True
        if other.date and not self.date:
            return False
        
        if self.date and other.date and self.date > other.date:
            return True
        if self.date and other.date and self.date < other.date:
            return False

        # db date
        if self.db_date and not other.db_date:
            return True
        if other.db_date and not self.db_date:
            return False
        
        if self.db_date and other.db_date and self.db_date > other.db_date:
            return True
        if self.db_date and other.db_date and self.db_date < other.db_date:
            return False

        
        return False

    def __ge__(self, other):
        '''
        '''
        if self > other:
            return True

        if self.logic_equal(other):
            return True
            
        return False

    
    def __lt__(self, other):
        '''
        '''
        if other > self:
            return True
        return False

    def __le__(self, other):
        '''
        '''
        
        if other > self:
            return True

        if self.logic_equal(other):
            return True
            
        return False

    
    def base_equal(self, other):
        '''Equality for only basic fields
        '''
        if not self.record_type == other.record_type:
            return None
        if not self.record_id == other.record_id:
            return False
        if not self.key == other.key:
            return False
        return True

    def logic_equal(self, other):
        '''Equality on all but value 
        '''
        if not self.base_equal(other):
            return False

        if not self.credibility == other.credibility:
            return False
        if not self.date == other.date:
            return False

        return True


        
    
    def keys(self):
        '''
        '''
        return ['record_type', 'record_id', 'key', 'original_key', 'normalized_key', 'valid_key', 'value', 'original_value', 'normalized_value', 'valid_value', 'credibility', 'date']
    
        
    def load(self, record):
        '''
        '''

        for i in self.keys:
            setattr(self, i, record.get(i, None))

    
    def dump(self):
        '''
        '''
        record = {}
        for i in self.keys():
            value = getattr(self, i, None)
            record[i] = value

        return record


    '''properties
    '''

    @property
    def key(self):
        '''
        '''
        if self.normalized_key:
            return self.normalized_key
        else:
            return self.original_key

    @key.setter
    def key(self, value):
        '''
        '''
        self.original_key = value
        self.valid_key = False
        
        self.normalized_key = k.normalize_key(self.key)
        if self.normalized_key:
            self.valid_key = True
    
    @property 
    def value(self):
        '''
        '''
        if self.normalized_value:
            return self.normalized_value
        else:
            return self.original_value


    @value.setter
    def value(self, value):
        '''
        '''
        
        # Validate value
        self.original_value = value
        self.valid_value = False
        
        # Get datatypes
        datatypes = k.get_datatype(self.record_type, self.key)
        if datatypes:
            for i in datatypes:
                r = None
                try:
                    r = dt.validate(i, value)
                except:
                    a=1
                
                if r and r is True:
                    try:
                        self.normalized_value = dt.normalize(i, value)
                        self.valid_value = True
                    except:
                        self.valid_value = False
                    return
        