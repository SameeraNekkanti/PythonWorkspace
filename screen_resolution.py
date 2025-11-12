def scale_resolutions(resolution,factor):
    scaled=[]
    for width, height in resolution:
        width1=int(width*factor)
        height1=int(height*factor)
        scaled.append((width1,height1))
    return scaled
    
resolution = [
    (1920, 1080),
    (1280, 720),
    (2560, 1440)
]

factor = 0.5  # scale down to half size

result = scale_resolutions(resolution, factor)
print(result)

