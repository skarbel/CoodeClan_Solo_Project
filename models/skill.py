class Pet:
    def __init__(self, pet_name, pet_dob, pet_type, treatment_notes, id = None):
        self.pet_name = pet_name
        self.pet_dob = pet_dob
        self.pet_type = pet_type
        self.treatment_notes = treatment_notes
        self.id = id