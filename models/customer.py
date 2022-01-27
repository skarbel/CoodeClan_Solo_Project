class Customer:

    def __init__(self, customer_name, contact_details, registered, id = None):
        self.customer_name = customer_name
        self.contact_details = contact_details
        self.registered = registered
        self.id = id