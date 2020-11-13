
import json

config = {
    "network" : [
        #connect from home
        {
            "is_active"  : True,
            "opc_addr"   : "opc.tcp://192.168.250.1:4840"
        },
        
    ],
    "hardware_addr" : {
        "axis_a_encoder_position_addr" : "ns=4;s=N1_Ch1_Encoder_Present_Position",
        "axis_b_encoder_position_addr" : "ns=4;s=N2_Ch2_Encoder_Present_Position",
        "axis_c_encoder_position_addr" : "ns=4;s=N3_Ch3_Encoder_Present_Position",
        "axis_d_encoder_position_addr" : "ns=4;s=N4_Ch4_Encoder_Present_Position",

        "axis_a_set_vel_addr" : "",
        "axis_b_set_vel_addr" : "",
        "axis_c_set_vel_addr" : "",
        "axis_d_set_vel_addr" : "",

        "axis_a_in_home_flag_addr" : "",
        "axis_b_in_home_flag_addr" : "",
        "axis_c_in_home_flag_addr" : "",
        "axis_d_in_home_flag_addr" : "",


        "start_stop_flag_addr" : "ns=4;s=Start"
    },
    "hardware" : {
        "encoder_scale" : 100,
        "vel_scale"     : 100,
        "arduino_port"  : "/dev/ttyACM0",
        "arduino_bound" : 9600,
        "min_limit"     : 0,
        "max_limit"     : 50
    },

    "soft" : {
        "update_time" : 10
    }
}

def create():
    out_config = open('config/client_config.json', 'w')
    out_config.write(json.dumps(config, sort_keys=True, indent=4))

if __name__ == "__main__":
    create()

    