    class Run:

        # ... something
        def create_particles(self):
            pass
    
        def update_particles(self):
            pass
    
        def remove_particles(self):
            # This might include particles moving outside the chamber (the Electric and Magnetic fields or
            # simply positions of interest) or particles being absorbed for example in a coating process
            pass
    
        def create_fields(self):
            pass
    
        def change_fields(self):
            pass

        #... something else
