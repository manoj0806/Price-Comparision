import wget

# Set up the image URL
image_url = "https://collector-PX35v5YGcp.perimeterx.net/api/v1/collector/noScript.gif?appId=PX35v5YGcp"

# Use wget download method to download specified image url.
image_filename = wget.download(image_url)

print('Image Successfully Downloaded: ', image_filename)