import random
import matplotlib.pyplot as plt



if __name__ == "__main__":

    ENC_Master_position = 0
    ENC_Slave_position  = 0

    master_vel                = 6.28 * 3000 #Deg 
    slave_vel                 = 6.28 * 3000 #Deg 
    time_step                 = 0.001 #sec
    simulation_time           = 100  #sec

    external_influence_flag  = False
    external_influence_value = 1

    time      = 0
    old_error = 0
    integrate = 0

    P         = 0.005
    D         = 0.009
    I         = 0.005

    k         = 0.05
    J         = 10000

    time_array            = []
    master_position_array = []
    slave_position_array  = []
    error_array           = []

    integrat_time        = 0
    while True:
        
        ENC_Master_position += master_vel * k * time * (1 / J)
        ENC_Slave_position  += slave_vel  * k * time * (1 / J)
        Error_master_salve  = ENC_Master_position - ENC_Slave_position

        if not external_influence_flag:
            random_value = random.random() / 1000
            if time > (simulation_time / 4):
                ENC_Slave_position += (external_influence_value)
                external_influence_flag = True
        print(Error_master_salve)
        integrate += (Error_master_salve * time_step)
        if(integrat_time >= 1):
            integrat_time = 0
            integrate = 0
        else:
            integrat_time += time_step
        dE = (Error_master_salve - old_error) / time_step
        old_error = Error_master_salve

        slave_vel += P * Error_master_salve + D * dE + I * integrate

        time_array.append(time)
        master_position_array.append(ENC_Master_position)
        slave_position_array.append(ENC_Slave_position)
        error_array.append(Error_master_salve)
        time += time_step

        if time > simulation_time:
            break

        pass
    plt.plot(time_array, error_array, "-")
    plt.show()
    pass