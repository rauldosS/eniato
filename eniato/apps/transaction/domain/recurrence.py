class Recurrence:

    def __init__(self, attributes={}):
        self.id = attributes['id']
        self.fixed = attributes['fixed']
        self.repeat_amount = attributes['repeat_amount']
        self.repeat_period = attributes['repeat_period']

    def set_id(self, id):
        self.id = id
