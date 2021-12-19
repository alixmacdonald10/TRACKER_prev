import random

import cv2
import numpy as np


class background():
    
    def __init__(
        self, width, height, channels, 
        background_mean, background_variance=1
    ):
        self.width = width
        self.height = height
        self.channels = channels
        self.background_mean = background_mean
        self.background_variance = background_variance

        # create base image object
        self.blank_image = np.zeros((self.height, self.width, channels), dtype=np.uint8)

        # add streak(s)
        #   self.streaked_image = self.add_streak()

        # create noisy image
        self.add_noise()
  
  
    def add_streak(self):
        pass

  
  
    def add_noise(self):
        '''
        Adds random gaussian distributed noise to the blank image.
        - mean: mean of distribution
        - variance: variance of distribution (non negative)  (counts^2 per pixel - default is 1)
        '''      

        self.background_sigma = np.sqrt(self.background_variance)
        gaussian = np.random.normal(self.background_mean, self.background_sigma, (self.height, self.width)).astype('float32')
        
        # create base noisy image to add noise too
        noisy_image = np.zeros(self.blank_image.shape, dtype=np.uint8)

        # apply noise to image
        if len(self.blank_image.shape) == 2:
            # grayscale
            noisy_image = img + gaussian 
        else:
            # rgb
            noisy_image[:, :, 0] = self.blank_image[:, :, 0] + np.abs(gaussian)
            noisy_image[:, :, 1] = self.blank_image[:, :, 1] + np.abs(gaussian)
            noisy_image[:, :, 2] = self.blank_image[:, :, 2] + np.abs(gaussian)

        self.noisy_image = (noisy_image * 255).astype(np.uint8)
          
        

if __name__ == "__main__":
    
    height = 256
    width = height
    channels = 3
    background_mean = 0
    background_variance = 1
    
    
    img = background(
        height=height, width=width, channels=channels,
        background_mean=background_mean, background_variance=background_variance
    )
    cv2.imshow("blank image test", img.blank_image)
    cv2.imshow("noisy image test", img.noisy_image)
    # cv2.imshow("streaked image", img.streaked_image)
    # cv2.imshow("streaked image no noise", img.streaked_image_denoised)
    cv2.waitKey()
    cv2.destroyAllWindows()
    