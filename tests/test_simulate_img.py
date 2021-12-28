from simulate_images.simulate_img import background


def test_background():
    
    width = 64
    height = 64
    channels = 3
    background_mean = 0
    
    assert background(width, height, channels, 
        background_mean) is not None