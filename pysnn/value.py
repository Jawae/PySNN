import torch


#########################################################
# XOR
#########################################################
class RewardXOR():
    r"""Determine XOR reward based on total number of output spikes."""
    def __init__(self, threshold):
        self.threshold = threshold

    def __call__(self, net_out, label):
        if label == 1:
            if (net_out> self.threshold):
                reward = 1
            else:
                reward = -1
        elif label == 0:
            if (net_out < self.threshold):
                reward = 1
            else:
                reward = -1

        return reward


class GuideXOR():
    r"""Determine XOR guiding signal based on total number of output spikes."""
    def __init__(self, threshold):
        self.threshold = threshold

    def __call__(self, net_out, label):
        if label == 1:
            if (net_out > self.threshold):
                reward = 0
            else:
                reward = -1
        elif label == 0:
            if (net_out < self.threshold):
                reward = 0
            else:
                reward = 1

        return reward