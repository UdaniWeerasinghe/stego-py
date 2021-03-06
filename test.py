from shutil import copyfile
import os
import cv2
import en_stego
import de_stego

# Create dist if it doesn't exist
if not os.path.exists('dist'):
    os.makedirs('dist')

# Base example
# Copy sample files to dist
# copyfile('./samples/strawberries.png', './dist/strawberries.png')
# copyfile('./samples/violet.png', './dist/violet.png')

# Hide the child image inside parent
# en_image = en_stego.hide('./dist/strawberries.png', './dist/violet.png')
# cv2.imwrite('./dist/en.png', en_image)

# Show the child image inside parent
# de_image = de_stego.show('./dist/en.png')
# cv2.imwrite('./dist/de.png', de_image)


### Experiment 1
copyfile('./samples/right.jpg', './dist/right.jpg')
copyfile('./samples/up.jpg', './dist/up.jpg')

en_image = en_stego.hide('./dist/right.jpg', './dist/up.jpg')
cv2.imwrite('./dist/en.jpg', en_image)

de_image = de_stego.show('./dist/en.jpg')
cv2.imwrite('./dist/de.jpg', de_image)