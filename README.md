Ubuntu Image Fetcher
A Python tool for mindfully collecting images from the web with built-in duplicate prevention and size limitations.

📋 Description
The Ubuntu Image Fetcher is a command-line utility that allows users to download multiple images from the web while implementing thoughtful constraints to promote responsible downloading practices. The tool includes duplicate detection, file size limitations, and image type verification.

✨ Features
Multiple URL Support: Process multiple image URLs in a single execution

Duplicate Prevention: Automatically skips duplicate filenames

Size Limitation: Rejects files larger than 5MB to promote mindful downloading

Image Type Verification: Only downloads actual image files

Error Handling: Comprehensive error handling for network issues and invalid URLs

Organized Storage: Saves all images to a dedicated "Fetched_Images" folder

🛠️ Installation
Ensure you have Python 3.6+ installed on your system

Install the required dependency:

bash
pip install requests
🚀 Usage
Run the script:

bash
python ubuntu_image_fetcher.py
When prompted, enter image URLs separated by commas:

text
Enter image URLs separated by commas: https://example.com/image1.jpg, https://example.com/image2.png
The script will download valid images to the "Fetched_Images" directory

📁 Output
All successfully downloaded images are saved in the Fetched_Images/ directory, which is automatically created if it doesn't exist.

⚙️ Configuration
The script has the following configurable parameters in the code:

MAX_SIZE = 5 * 1024 * 1024 (5MB maximum file size)

timeout = 10 (10-second timeout for requests)

You can modify these values in the source code to meet your specific needs.

🔒 Safety Features
Validates that URLs point to actual images (checks Content-Type header)

Prevents duplicate downloads

Limits file size to avoid excessively large downloads

Includes comprehensive error handling for network issues

📝 Example
text
Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Enter image URLs separated by commas: https://example.com/photo.jpg, https://example.com/image.png

✓ Successfully fetched: photo.jpg
✓ Image saved to Fetched_Images/photo.jpg

✓ Successfully fetched: image.png
✓ Image saved to Fetched_Images/image.png

Connection strengthened. Community enriched.
🐛 Troubleshooting
Common issues and solutions:

URLs not working: Ensure URLs are direct links to image files

"Skipping non-image URL": The URL doesn't point to an image file

"Skipping duplicate": The filename already exists in the Fetched_Images directory

"file too large": The image exceeds the 5MB size limit

📄 License
This project is open source and available under the MIT License.

🤝 Contributing
Contributions, issues, and feature requests are welcome. Feel free to check the issues page.

🙏 Acknowledgments
Built with the Requests library for HTTP operations

