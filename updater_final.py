import codecs
import re
import glob

# 1. Update projects.js to put Eastern Railway at the top
with codecs.open('e:/project/projects.js', 'r', 'utf-8') as f:
    pjs = f.read()

new_proj = '''{
        id: 0, title: "Smart Metering & Infrastructure", category: "Smart Metering", location: "Malda, Bhagalpur, Sahibganj", value: "₹ 280 Lakh", valueNumeric: 2.80, status: "Ongoing", progress: 60, client: "Eastern Railway", loa: "N/A", date: "Ongoing", desc: "Installation of Smart Energy Meters, Infrastructure Design, and System Integration for Eastern Railway (Indian Railways)"
    },
    '''

pjs = pjs.replace("const projectsData = [\n    {", "const projectsData = [\n    " + new_proj + "{")

with codecs.open('e:/project/projects.js', 'w', 'utf-8') as f:
    f.write(pjs)

# 2. Update index.html featured card and globally fix emails
with codecs.open('e:/project/index.html', 'r', 'utf-8') as f:
    idx = f.read()

# Update the first card's image
idx = idx.replace('https://images.unsplash.com/photo-1541888040600-4b3f17215f60?w=600&q=80', 'https://images.unsplash.com/photo-1474487548417-781cb71495f3?w=600&q=80', 1)
# Update text
idx = idx.replace('<div class="overlay-text">APDCL</div>', '<div class="overlay-text">Eastern Railway</div>', 1)
idx = re.sub(r'<div class="card-date-text">Power Distribution</div>\s*<div class="card-sub-text">\s*<a href="projects\.html">33/11kV Substation infrastructure development\s*for APDCL\.</a>', 
             r'<div class="card-date-text">Smart Metering</div>\n                                            <div class="card-sub-text">\n                                                <a href="projects.html">Smart Energy Meters & Electrical Infrastructure for Indian Railways.</a>', 
             idx, count=1)

with codecs.open('e:/project/index.html', 'w', 'utf-8') as f:
    f.write(idx)

# 3. Apply the new email globally to all pages!
for file in glob.glob('e:/project/*.html'):
    with codecs.open(file, 'r', 'utf-8') as f:
        c = f.read()
    c = c.replace('amiprojects@purbanchalenterprise.com', 'pspl@purbanchalenterprise.com')
    with codecs.open(file, 'w', 'utf-8') as f:
        f.write(c)

print("SUCCESS")
