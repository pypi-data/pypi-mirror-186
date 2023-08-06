import datetime
from kraken_thing import json_xp as json
from kraken_thing.kraken_class_observation import Observation
import uuid
from urllib.parse import urlparse
from kraken_schema_org import kraken_schema_org as k
from kraken_thing import normalize_id

class Thing:

    def __init__(self, record_type = None, record_id = None):
        """
        A class to represent a schema.org Thing
        """
        
        self.db = []

        self._original_record_type = None
        self._normalized_record_type = None
        self._valid_record_type = None
        
        self._original_record_id = None
        self._original_record_ids = []
        self._normalized_record_id = None
        self._valid_record_id = None

        
        self.record_type = record_type
        self.record_id = record_id
        
        # Add id if none
        if record_type and not record_id:
            self.record_id = str(uuid.uuid4())

    
    def __str__(self):
        return str(self.dump())

    def __repr__(self):
        return str(self.dump())


    def __eq__(self, other):
        """
        """
        if self.record_id == other.record_id and self.record_type == other.record_type:
            return True
        else:
            return False

    def __add__(self, other):
        """
        """
        
        new_t = Thing(self.record_type, self.record_id)

        #Load self record
        for i in self.db:
            new_t.db.append(i)

        # Load other record
        for i in other.db:
            new_t.db.append(i)

        return new_t
    
    
    """ Main
    """

        
    def set(self, key, value, credibility = None, date = None):
        """Set individual key, overrides if exist
        """

        # Adjust key
        if not key.startswith('@') and not key.startswith('schema:'):
            key = 'schema:' + key

        # Handle @ type and @id
        if key in ['@type', 'record_type']:
            self.record_type = value
            return

        if key in ['@id', 'record_id']:
            self.record_id = value
            return

        # convert to list
        if not isinstance(value, list):
            value = [value]

        # Convert to thing if record
        new_value = []
        for v in value:
            
            if isinstance(v, dict) and '@type' in v.keys():
                new_v = Thing()
                new_v.load(v)
                v = new_v
            new_value.append(v)

        # Convert to observations
        for i in new_value:
            o = Observation(self.record_type, self.record_id, key, i, credibility, date)
            if o not in self.db:
                self.db.append(o)

        # Update record_id (if new info make it available)
        if not self._valid_record_id:
            self.get_normalized_record_id()

        
        return

    def get(self, key, dummy = None):
        """
        Retrieve all values for given key ifrom best to worst

        
        Parameters
        ----------
        key: str
            Key of the value to get
        dummy: not used, there to simulate normal get fn behavior
        """
        if not key.startswith('@') and not key.startswith('schema:'):
            key = 'schema:' + key

        obs = []
        for i in self.db:
            if i.key == key:
                obs.append(i)

        if not obs or len(obs) == 0:
            return []
        
        values = []
        for i in sorted(obs, reverse=True):
            values.append(i.value)
            
        return values

    def get_best(self, key):
        '''Returns best value
        '''
        value = self.get(key)

        if value and len(value) > 0:
            return value[0]
        else:
            return None


        
    def load(self, record, append=False):
        """
        Load complete record
        
        Parameters
        ----------
        record: dict
            Dict of the record to load. Also accepts json.
        append: bool
            If true, will append value to existing value
        """

        # Handle json
        if isinstance(record, str):
            record = json.loads(record)


        self.record_type = record.get('@type', None)
        self.record_id = record.get('@id', None)
        record_id = normalize_id.normalize_id(record)
        if record_id:
            self.record_id = record_id
        
        # Add id if none
        if self.record_type and not self.record_id:
            self.record_id = str(uuid.uuid4())
        
        for k, v in record.items():
            if k not in ['@type', '@id']:
                self.set(k, v)

        

    def dump(self):
        """Dump complete record without class
        """

        # Add id if none
        if self.record_type and not self.record_id:
            self.record_id = str(uuid.uuid4())
        
        record = {
            '@type': self.record_type,
            '@id': self.record_id
        }

        # Convert Things to dict
        for o in self.db:
            if not record.get(o.key, None):
                record[o.key] = []
            
            if isinstance(o.value, Thing):
                record[o.key].append(o.value.dump())
            else:
                record[o.key].append(o.value)

        # Remove lists and empty values
        new_record = {}
        for k, v in record.items():
            if v and len(v) == 1:
                new_record[k] = v[0]
            elif v and len(v) > 1:
                new_record[k] = v
        
        return new_record

    @property
    def json(self):
        """
        """
        return json.dumps()
        
    @json.setter
    def json(self, value):
        """
        """
        record = json.loads(value)
        self.load(record)
        

    """Observations
    """

    def load_observations(self, observations):
        '''Load observations in list of dict format
        '''
        if not isinstance(observations, list):
            observations = [observations]

        for i in observations:
            o = Observation(self.record_type, self.record_id)
            o.load(i)
            self.db.append(o)
            
        return

    def dump_observations(self):
        '''Returns list of obs in dict format
        '''
        obs = []
        for i in self.db:
            obs.append(i.dump())

        return obs

    
    """Properties
    """
    @property
    def record_type(self):
        return self._record_type

    @record_type.setter
    def record_type(self, value):

        if isinstance(value, list) and not isinstance(value, str) and len(value) == 0:
            return
        if isinstance(value, list) and not isinstance(value, str) and len(value) == 1:
            value=value[0]
        if value is not None and not isinstance(value, str):
            return

        # Normalize type
        new_value = k.normalize_type(value)
        if new_value:
            value = new_value

        # Change obs
        for i in self.db:
            i.record_type = value
        
        self._record_type = value

    @property
    def record_id(self):

        if self._valid_record_id:
            return self._normalized_record_id
        else:
            return self._original_record_id

    @record_id.setter
    def record_id(self, value):

        if isinstance(value, list) and len(value) == 0:
            return
        if isinstance(value, list) and len(value) == 1:
            value=value[0]
        if value is not None and not isinstance(value, str):
            return

        self._original_record_id = value
        self._original_record_ids.append(value)
        
        
        self.get_normalized_record_id()
        
        # Change obs
        for i in self.db:
            i.record_id = self.record_id
        

    def get_normalized_record_id(self):
        '''
        '''
        self._normalized_record_id = normalize_id.normalize_id(self.dump())
        
        if self._normalized_record_id:
            self._valid_record_id = True
            # Change obs
            for i in self.db:
                i.record_id = self.record_id

    
    def update_record_ref(self, old_record_type, old_record_id, new_record_type, new_record_id):
        '''Updates all value with new record_ref
        '''
        for i in obs:
            if isinstance(i.original_value, Thing):
                
                if i.original_value.record_type == old_record_type and i.original_value.record_id == old_record_id:
                    i.original_value.record_type = new_record_type
                    i.original_value.record_id = new_record_id
            
            if isinstance(i.normalized_value, Thing):
                i.normalized_value.record_type = i.normalized_value.get('@type', None)
                i.normalized_value.record_id = i.normalized_value.get('@id', None)

                if value_type == old_record_type and value_id == old_record_id:
                    i.normalized_value.record_type = new_record_type
                    i.normalized_value.record_id = new_record_id
        

    @property
    def record_ref(self):
        record = {
            '@type': self.record_type,
            '@id': self.record_id
        }
        return record

    @record_ref.setter
    def record_ref(self, value):
        self.load(value)
    
    @property
    def name(self):
        return self.get_best('schema:name')

    @name.setter
    def name(self, value):
        self.set('schema:name', value)

    @property
    def url(self):
        return self.get_best('schema:url')

    @url.setter
    def url(self, value):
        self.set('schema:url', value)


    @property
    def url_domain(self):
        domain = urlparse(data).netloc
        domain = domain.replace('www.', '')
    
    """Conditions
    """

    @property
    def is_status_active(self):
        """
        """
        if self.get_best('schema:actionStatus') == 'schema:ActiveActionStatus':
            return True
        return False

    @property
    def is_status_completed(self):
        """
        """
        if self.get_best('schema:actionStatus') == 'schema:CompletedActionStatus':
            return True
        return False

    @property
    def is_status_failed(self):
        """
        """
        if self.get_best('schema:actionStatus') == 'schema:FailedActionStatus':
            return True
        return False

    @property
    def is_status_potential(self):
        """
        """
        if self.get_best('schema:actionStatus') == 'schema:PotentialActionStatus':
            return True
        return False

    
    """Actions
    """
    def set_status_active(self):
        """
        """
        self.set('schema:actionStatus', 'schema:ActiveActionStatus')
    
    def set_status_completed(self):
        """
        """
        self.set('schema:actionStatus', 'schema:CompletedActionStatus')
    
    def set_status_failed(self):
        """
        """
        self.set('schema:actionStatus', 'schema:FailedActionStatus')
    
    def set_status_potential(self):
        """
        """
        self.set('schema:actionStatus', 'schema:PotentialActionStatus')
    