import numpy as np
from PIL import Image


# Load the image using PIL
def load_image(image_path):
    image = Image.open(image_path)
    return np.array(image)


# Save the image using PIL
def save_image(image_array, output_path):
    image = Image.fromarray(image_array.astype(np.uint8))
    image.save(output_path)


# 1. Flip the image horizontally and vertically
def flip_image(image_array):
    flipped_h = np.flip(image_array, axis=1)  # Left-to-right
    flipped_v = np.flip(image_array, axis=0)  # Up-to-down
    return flipped_h, flipped_v


# 2. Add random noise
def add_noise(image_array, noise_level=30):
    noise = np.random.randint(-noise_level, noise_level, image_array.shape, dtype=np.int16)
    noisy_image = np.clip(image_array + noise, 0, 255)  # Clip values to 0-255
    return noisy_image.astype(np.uint8)


# 3. Brighten a specific channel (e.g., Red)
def brighten_channel(image_array, channel=0, value=40):
    brightened_image = image_array.copy()
    brightened_image[:, :, channel] = np.clip(brightened_image[:, :, channel] + value, 0, 255)
    return brightened_image.astype(np.uint8)


# 4. Apply a mask (Black rectangle in the center)
def apply_mask(image_array, mask_size=(100, 100)):
    masked_image = image_array.copy()
    h, w, _ = image_array.shape
    start_x = (w - mask_size[0]) // 2
    start_y = (h - mask_size[1]) // 2
    masked_image[start_y:start_y + mask_size[1], start_x:start_x + mask_size[0]] = [0, 0, 0]
    return masked_image


# Main function to process the image
def main():
    image_path = "birds.jpg"
    output_dir = "output/"

    # Load image
    image = load_image(image_path)

    # Perform transformations
    flipped_h, flipped_v = flip_image(image)
    noisy_image = add_noise(image)
    brightened_image = brighten_channel(image, channel=0, value=40)  # Increase Red Channel
    masked_image = apply_mask(image)

    # Save the modified images
    save_image(flipped_h, output_dir + "flipped_horizontal.jpg")
    save_image(flipped_v, output_dir + "flipped_vertical.jpg")
    save_image(noisy_image, output_dir + "noisy.jpg")
    save_image(brightened_image, output_dir + "brightened.jpg")
    save_image(masked_image, output_dir + "masked.jpg")

    print("Image processing completed. Check the 'output' directory.")


# Run the script
if __name__ == "__main__":
    main()
