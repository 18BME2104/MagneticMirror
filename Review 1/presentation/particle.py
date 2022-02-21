    class Particle:
        #... other things
        
        def Boris_update(self, afield, argsE, argsB):
            # Define q_prime
            q_prime = (self.charge / self.mass) * (dt / 2)
        
            # Get E and B fields from the afield argument by passing in the current position of the particle
            argsE = V, center
            E = afield.get_E_field(self.r, V, center)
            argsB = n, I, R, B_hat, mu_0
            B = afield.get_B_field(self.r, n, I, R, B_hat, mu_0)
        
            #Boris velocity update
            v_minus = self.v + q_prime * E
            v_plus = v_minus + q_prime * 2 * np.cross(v_minus, B)
            v_new = v_plus + q_prime * E
        
            self.v = v_new
        
        
            #could have also done:
            #self.v += (2 * q_prime) * (E + np.cross( (self.v + q_prime * E), B))
        
            #update position
            self.r += v_new * dt

        #... some other things 
