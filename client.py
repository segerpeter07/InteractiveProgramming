#!/usr/bin/env python3
"""Small example OSC client

This program sends 10 random values between 0.0 and 1.0 to the /filter address,
waiting for 1 seconds between each value.
"""
import argparse
import time

from pythonosc import udp_client


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1",
                        help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=5005,
                        help="The port the OSC server is listening on")
    args = parser.parse_args()

    client = udp_client.SimpleUDPClient(args.ip, args.port)

<<<<<<< HEAD
    for x in range(100):
        client.send_message("/filter", 'hi')
        time.sleep(.01)
=======
    for x in range(10):
        client.send_message("/filter", 'Pranay is dead')
        # time.sleep(1)
>>>>>>> 856f1716ef61cf7347544f97eb186237a01b4f85
