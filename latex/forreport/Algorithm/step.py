    class Step:

        # ... something
        
     ### PARTICELS INTIALIZATION SECTION
        def initialize_particles(self, names, q_s, m_s, r_0_s, v_0_s, a_0_s, n):
        
            for i in range(n):
                self.particles.append(Particle(names[i], q_s[i], m_s[i], r_0_s[i], v_0_s[i], a_0_s[i] ))
    
    ### FIELDS INITIALIZATION SECTION
        def initialize_fields(self):
            self.fields = Field()
    
    ### TIME STEP SECTION
        def update_particles(self, dt, argsE, argsB):
        
            for particle in self.particles:
                particle.update(self.fields, dt, argsE, argsB)

        def read_r_or_v_file_and_reshape(self, index):
        
            array_from_file = self.read_r_or_v_file(index)
            reshaped_array = self.reshaper(array_from_file)
            return reshaped_array

        # ... something else
