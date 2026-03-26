import codecs

with codecs.open('e:/project/about.html', 'r', 'utf-8') as f:
    about = f.read()

about = about.replace("https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=2000&q=80", "logo/banner%20photo%20who%20we%20are%20page.jpeg")

about = about.replace("https://images.unsplash.com/photo-1556157382-97eda2d62296?w=800&q=80", "logo/Amit%20Kumar%20Agarwal.jpeg")

with codecs.open('e:/project/about.html', 'w', 'utf-8') as f:
    f.write(about)

print("SUCCESS")
