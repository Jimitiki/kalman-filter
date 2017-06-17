import socket
import json

s = None

def open_connection(address):
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(address)
    #res = s.recv(1024)

def send_command(command):
    global s
    s.send(command.encode('utf-8'))
    res = s.recv(8124)
    if res == None:
        return None
    return json.loads(res.decode('utf-8'))

def where_robot():
    return send_command("where robot")

def where_markers():
    return send_command("where others")

def where_all():
    return send_command("where")

def set_speed(a, b):
    return send_command("speed " + str(a) + " " + str(b))

def get_speed():
    return send_command("speed")

def set_pid_params(kp, ki, kd):
    params = {}
    params["kp"] = send_command("param kp " + str(kp))["kp"]
    params["ki"] = send_command("param ki " + str(kp))["ki"]
    params["kd"] = send_command("param kd " + str(kd))["kd"]

def close_connection():
    global s
    s.close()
