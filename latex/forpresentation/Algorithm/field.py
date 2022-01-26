    class Field:
        #... something

        def uniform_E_field(self, E):
            return E

        def radial_E_field(self, r, V, center = [0,0,0]):
            #Get the distance vector of the particle from the electrode
            dr = [(r[0] - center[0]), (r[1] - center[1]), 0]
            #Get the electric field
            E = V * dr
            return E

        def uniform_B_field(self, B):
            return B

        def helmholtz_coil_B_field(self, n, I, R, B_hat, mu_0):
            return ( (4/5)**1.5 * ( (mu_0 * n * I) / (R) ) * B_hat)

        def two_helmholtz_B_field(self, n1, I1, R1, B1_hat, n2, I2, R2, B2_hat, mu_0):
            B1 = helmholtz(self, n1, I1, R1, mu_0, B1_hat)
            B2 = helmholtz(self, n2, I2, R2, mu_0, B2_hat)
        
            #Calculate the resultant of two magnetic fields
            B_hat = B1_hat + B2_hat
            return B_hat  

        #...something else
    
