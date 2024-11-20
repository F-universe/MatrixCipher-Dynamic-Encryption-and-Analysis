This project aims to create a secure key for encrypting and decrypting files. 
Here's how the key is generated:

When you run the app.py code, it starts a Flask application where the user can input any word.
Upon clicking "Search," a Selenium WebDriver fetches the corresponding Wikipedia page for that word. 
The letters from the page are then displayed in a 64x64 matrix.

Next, a second matrix is generated, this time populated with custom PNG images created by me. 
These images are placed in the matrix according to specific criteria. For example, if two consecutive
consonants appear in the first matrix, the image 1.png will be displayed in the corresponding cell of 
the second matrix.

Finally, a numerical key is created. Each row of this key represents the sum of the colored pixels of
the images found in the corresponding row of the second matrix. This numerical key is then saved and 
used to encrypt and decrypt messages using the crypting.py and decrypting.py scripts.
