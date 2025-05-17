# -*- coding: utf-8 -*-
#
#     ||          ____  _ __
#  +------+      / __ )(_) /_______________ _____  ___
#  | 0xBC |     / __  / / __/ ___/ ___/ __ `/_  / / _ \
#  +------+    / /_/ / / /_/ /__/ /  / /_/ / / /_/  __/
#   ||  ||    /_____/_/\__/\___/_/   \__,_/ /___/\___/
#
#  Copyright (C) 2016 Bitcraze AB
#
#  Crazyflie Nano Quadcopter Client
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
"""
Simple example that connects to the crazyflie at `URI` and runs a figure 8
sequence. This script requires some kind of location system, it has been
tested with the flow deck and the lighthouse positioning system.

Change the URI variable to your Crazyflie configuration.
"""
import logging
import time

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.utils import uri_helper
from cflib.utils.reset_estimator import reset_estimator

URI = uri_helper.uri_from_env(default="radio://0/90/2M/E7E7E7E7E7")
MOTION_DELAY = 0.1
YAW = 0

# Only output errors from the logging framework
logging.basicConfig(level=logging.ERROR)

if __name__ == "__main__":
    # Initialize the low-level drivers
    cflib.crtp.init_drivers()

    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache="./cache")) as scf:
        cf = scf.cf

        reset_estimator(scf)
        time.sleep(1)

        # Arm the Crazyflie
        cf.platform.send_arming_request(True)
        time.sleep(1)

        print("Before takeoff")
        cf.high_level_commander.takeoff(absolute_height_m=0.2, duration_s=2)
        time.sleep(4)

        counter = 0.1
        for _ in range(5):
            print(f"Setting x to {counter}")
            cf.high_level_commander.start_trajectory
            cf.commander.send_position_setpoint(x=counter, y=0, z=0.2, yaw=YAW)
            counter += 0.1
            time.sleep(MOTION_DELAY)

        
        print("Landing...")
        cf.high_level_commander.land(0, 5)
