    class Sampler:
        #... something

        def sample_same_given_position(self, r, n):
            positions = []
            for i in range(n):
                positions.append(r)
        
            return np.array(positions)
    
        def sample_same_given_distance_all_random_direction(self, d, n):
            positions = []
        
            for i in range(n):
                positions.append(d * uniform_random_unit_vector())
        
            return np.array(positions)
    
        def sample_same_given_velocity_same_direction(self, v, n):
            velocities = []
            for i in range(n):
                velocities.append(v)
            
            return np.array(velocities)
    
        def sample_same_given_speed_all_random_direction(self, s, n):
            velocities = []
        
            for i in range(n):
                velocities.append(s * uniform_random_unit_vector())
        
            return np.array(velocities)
    
        def sample_velocity_uniformKE_same_given_direction(self):
            pass
        
        def sample_velocity_uniformKE_all_random_directions(self, n):
            pass
        
        def sample_Maxwellian_speed(self, v_median, K, T, m, n):
            alpha = math.sqrt(K * T / m) 
            speeds = stats.maxwell.rvs(loc = v_median, scale = alpha, size = n)
            return speeds
    
        def sample_Maxwellian_velocity_same_given_direction(self, v_median, K, T, m, v_hat, n):
            speeds = sample_Maxwellian_speed(self, v_median, K, T, m, n)
            velocities = np.outer(speeds, v_hat)
        
            assert len(velocities) == n, 'Dimensions don\'t match. There is some error in multiplying \
            speeds and the direction'
        
            return np.array(velocities)
    
        def sample_Maxwellian_velocity_same_random_direction(self, v_median, K, T, m, n):   
            speeds = sample_Maxwellian_speed(self, v_median, K, T, m, n)
            direction = self.uniform_random_unit_vector()
            velocities = np.outer(speeds, direction)
        
            assert len(velocities) == n, 'Dimensions don\'t match. There is some error in multiplying \
            speeds and the direction'
        
            return np.array(velocities)
    
        def sample_Maxwellian_velocity_all_random_direction(self, v_median, K, T, m, n):
            speeds = sample_Maxwellian_speed(self, v_median, K, T, m, n)
            velocities = []
            for i in range(n):
                velocities.append(speeds[i] * np.array(uniform_random_unit_vector()))
        
            assert len(velocities) == n, 'Dimensions don\'t match. There is some error in multiplying \
            speeds and directions'
        
            return np.array(velocities)     
        
        def sample_parabolic_velocity(self):
            pass

        #... something else
