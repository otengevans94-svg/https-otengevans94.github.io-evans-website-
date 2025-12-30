import os
import zipfile

# Base folder for the new website
base_dir = "/mnt/data/evans-website-enhanced"
images_dir = os.path.join(base_dir, "images")
os.makedirs(images_dir, exist_ok=True)

# HTML content (enhanced version with placeholders for images)
files = {
    "index.html": """<!DOCTYPE html>
<html lang='en'>
<head>
<meta charset='UTF-8'>
<title>Evans View Hotel | Home</title>
<link rel='stylesheet' href='style.css'>
</head>
<body>
<header>
<h1>Evans View Hotel</h1>
<nav>
<a href='index.html'>Home</a>
<a href='about.html'>About</a>
<a href='services.html'>Services</a>
<a href='gallery.html'>Gallery</a>
<a href='contact.html'>Contact</a>
</nav>
</header>
<section class='hero'>
<img src='images/hotel1.jpg' alt='Hotel Exterior'>
<div class='hero-text'><h2>Welcome to Evans View Hotel</h2><p>Luxury and comfort in one place</p></div>
</section>
<section>
<p>Relax, dine, and enjoy your stay with our top-notch services.</p>
</section>
<footer>
<p>&copy; 2026 Evans View Hotel</p>
</footer>
</body>
</html>""",
    "about.html": """<!DOCTYPE html>
<html lang='en'>
<head>
<meta charset='UTF-8'>
<title>About Us | Evans View Hotel</title>
<link rel='stylesheet' href='style.css'>
</head>
<body>
<header>
<h1>About Evans View Hotel</h1>
<nav>
<a href='index.html'>Home</a>
<a href='about.html'>About</a>
<a href='services.html'>Services</a>
<a href='gallery.html'>Gallery</a>
<a href='contact.html'>Contact</a>
</nav>
</header>
<section>
<p>Evans View Hotel offers affordable luxury, exceptional service, and a relaxing environment for all guests.</p>
<img src='images/lobby.jpg' alt='Hotel Lobby'>
</section>
<footer>
<p>&copy; 2026 Evans View Hotel</p>
</footer>
</body>
</html>""",
    "services.html": """<!DOCTYPE html>
<html lang='en'>
<head>
<meta charset='UTF-8'>
<title>Services | Evans View Hotel</title>
<link rel='stylesheet' href='style.css'>
</head>
<body>
<header>
<h1>Our Services</h1>
<nav>
<a href='index.html'>Home</a>
<a href='about.html'>About</a>
<a href='services.html'>Services</a>
<a href='gallery.html'>Gallery</a>
<a href='contact.html'>Contact</a>
</nav>
</header>
<section class='services'>
<ul>
<li><img src='images/room.jpg' alt='Luxury Rooms'> Luxury Rooms</li>
<li><img src='images/restaurant.jpg' alt='Restaurant'> Restaurant & Bar</li>
<li><img src='images/pool.jpg' alt='Pool'> Swimming Pool</li>
<li>Free Wi-Fi</li>
<li>24/7 Customer Support</li>
</ul>
</section>
<footer>
<p>&copy; 2026 Evans View Hotel</p>
</footer>
</body>
</html>""",
    "gallery.html": """<!DOCTYPE html>
<html lang='en'>
<head>
<meta charset='UTF-8'>
<title>Gallery | Evans View Hotel</title>
<link rel='stylesheet' href='style.css'>
</head>
<body>
<header>
<h1>Gallery</h1>
<nav>
<a href='index.html'>Home</a>
<a href='about.html'>About</a>
<a href='services.html'>Services</a>
<a href='gallery.html'>Gallery</a>
<a href='contact.html'>Contact</a>
</nav>
</header>
<section class='gallery'>
<img src='images/hotel1.jpg' alt='Hotel Exterior'>
<img src='images/lobby.jpg' alt='Hotel Lobby'>
<img src='images/room.jpg' alt='Room'>
<img src='images/restaurant.jpg' alt='Restaurant'>
<img src='images/pool.jpg' alt='Pool'>
</section>
<footer>
<p>&copy; 2026 Evans View Hotel</p>
</footer>
</body>
</html>""",
    "contact.html": """<!DOCTYPE html>
<html lang='en'>
<head>
<meta charset='UTF-8'>
<title>Contact | Evans View Hotel</title>
<link rel='stylesheet' href='style.css'>
</head>
<body>
<header>
<h1>Contact Us</h1>
<nav>
<a href='index.html'>Home</a>
<a href='about.html'>About</a>
<a href='services.html'>Services</a>
<a href='gallery.html'>Gallery</a>
<a href='contact.html'>Contact</a>
</nav>
</header>
<section>
<p>Email: info@evansviewhotel.com</p>
<p>Phone: +233 000 000 000</p>
<p>Location: Accra, Ghana</p>
</section>
<footer>
<p>&copy; 2026 Evans View Hotel</p>
</footer>
</body>
</html>""",
    "style.css": """body { font-family: Arial, sans-serif; margin: 0; padding: 0; }
header { background: #2c3e50; color: white; padding: 15px; }
nav a { color: white; margin-right: 15px; text-decoration: none; }
nav a:hover { color: #ffcc00; }
section { padding: 20px; }
.hero { position: relative; }
.hero img { width: 100%; height: auto; }
.hero-text { position: absolute; top: 30%; left: 10%; color: white; background-color: rgba(0,0,0,0.4); padding: 20px; border-radius: 10px; }
.services ul { list-style: none; padding: 0; }
.services li { margin: 10px 0; }
.gallery img { width: 200px; margin: 10px; border-radius: 10px; transition: transform 0.3s; }
.gallery img:hover { transform: scale(1.1); }
footer { background: #eee; text-align: center; padding: 10px; }"""
}

# Placeholder images from previous generation (same for demonstration)
image_files = [
    "hotel1.jpg", "room.jpg", "restaurant.jpg", "pool.jpg", "lobby.jpg"
]

# Save all files
for name, content in files.items():
    with open(os.path.join(base_dir, name), 'w') as f:
        f.write(content)

# Create placeholder images
for img in image_files:
    with open(os.path.join(images_dir, img), 'wb') as f:
        f.write(b'')  # empty placeholder, you can replace with real images later

# Zip the entire folder
zip_path = "/mnt/data/evans-website-enhanced.zip"
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, file_list in os.walk(base_dir):
        for file in file_list:
            full_path = os.path.join(root, file)
            zipf.write(full_path, arcname=os.path.relpath(full_path, base_dir))

zip_path
