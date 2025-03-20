# Create a function, where I give it the path and then it goes through the files in the path opens the tiffs and stacks them 

def stack_tiffs(path):
    files = glob(path + '*.tiff')
    for i, file in enumerate(files):
        print(file)
        ds = gdal.Open(file)
        data = ds.ReadAsArray()
        if i == 0:
            stacked_data = data
        else:
            stacked_data = np.dstack((stacked_data, data))
    return stacked_data


# Create a function that does what we did above. I am assuming that the full banded images is already loaded, so our beginning is stacked data 

def visualize(data, band1, band2, band3):
    # Extract bands
    band1 = data[:, :, band1]
    band2 = data[:, :, band2]
    band3 = data[:, :, band3]
    
    # Normalize the bands to [0, 1] range
    max_value = band1.max()  # Maximum value from your dataset
    band1 = band1 / max_value
    band2 = band2 / max_value
    band3 = band3 / max_value
    
    # Stack the extracted bands to create an RGB image
    rgb_image = np.stack((band1, band2, band3), axis=-1)
    
    # Plot the RGB image
    plt.figure(figsize=(10, 15))
    plt.imshow(rgb_image)
    plt.axis('off')  # Hide axis for a cleaner image
    plt.show()