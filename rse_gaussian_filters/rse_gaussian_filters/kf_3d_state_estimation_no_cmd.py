# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

import rclpy

import numpy as np

from rse_motion_models.velocity_motion_models import velocity_motion_model
from rse_observation_models.odometry_observation_models import odometry_observation_model

from .filters.kf import KalmanFilter
from .kf_node import KalmanFilterNode


def main(args=None):
    # Initialize the Kalman Filter
    mu0 = np.zeros(3)
    Sigma0 = np.eye(3)
    # proc_noise_std = [1000.02, 1000.02, 1000.01] 
    # obs_noise_std = [0.002, 0.002, 0.001]
    proc_noise_std = [0.002, 0.002, 0.001]
    obs_noise_std = [1000.02, 1000.02, 1000.01]

    kf = KalmanFilter(mu0, Sigma0,
                      velocity_motion_model,
                      odometry_observation_model,
                      proc_noise_std = proc_noise_std,
                      obs_noise_std = obs_noise_std)

    rclpy.init(args=args)
    kalman_filter_node = KalmanFilterNode(kf)
    rclpy.spin(kalman_filter_node)
    kalman_filter_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()


        
        
      