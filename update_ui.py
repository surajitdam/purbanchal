import codecs
import re

# --- 1. Update index.html link
with codecs.open('e:/project/index.html', 'r', 'utf-8') as f:
    idx = f.read()

idx = re.sub(r'(<div class="business-right-sec" id="tab-civil-water">.*?<div class="elplore-more-cta">\s*<a href=")services\.html(">)', r'\g<1>services.html#jjm-work\g<2>', idx, flags=re.DOTALL)

with codecs.open('e:/project/index.html', 'w', 'utf-8') as f:
    f.write(idx)

# --- 2. Update about.html Core Values Cards
with codecs.open('e:/project/about.html', 'r', 'utf-8') as f:
    about = f.read()

css_old = ".value-card { background: var(--bg-white); padding: 3rem 2rem; border-radius: 12px; text-align: center; box-shadow: var(--shadow-sm); transition: 0.3s; border-bottom: 3px solid transparent; border: 1px solid rgba(0,0,0,0.05); }"
css_new = """.value-card { position: relative; background-size: cover; background-position: center; padding: 3rem 2rem; border-radius: 12px; text-align: center; box-shadow: var(--shadow-sm); transition: 0.3s; border-bottom: 3px solid transparent; overflow: hidden; }
        .value-card::before { content: ''; position: absolute; inset: 0; background: rgba(5, 20, 36, 0.75); z-index: 1; transition: 0.3s; }
        .value-card:hover::before { background: rgba(5, 20, 36, 0.85); }
        .value-card i, .value-card h3, .value-card p { position: relative; z-index: 2; color: #fff !important; }"""
about = about.replace(css_old, css_new)

about = about.replace('<div class="value-card animate-on-scroll">\n                    <i class="fa-solid fa-award value-icon">', 
                      '<div class="value-card animate-on-scroll" style="background-image: url(\'https://images.unsplash.com/photo-1497366216548-37526070297c?w=600&q=80\');">\n                    <i class="fa-solid fa-award value-icon">')
about = about.replace('<div class="value-card animate-on-scroll">\n                    <i class="fa-solid fa-shield-halved value-icon">',
                      '<div class="value-card animate-on-scroll" style="background-image: url(\'https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&q=80\');">\n                    <i class="fa-solid fa-shield-halved value-icon">')
about = about.replace('<div class="value-card animate-on-scroll">\n                    <i class="fa-solid fa-handshake-angle value-icon">',
                      '<div class="value-card animate-on-scroll" style="background-image: url(\'https://images.unsplash.com/photo-1600880292203-757bb62b4baf?w=600&q=80\');">\n                    <i class="fa-solid fa-handshake-angle value-icon">')
about = about.replace('<div class="value-card animate-on-scroll">\n                    <i class="fa-solid fa-lightbulb value-icon">',
                      '<div class="value-card animate-on-scroll" style="background-image: url(\'https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=600&q=80\');">\n                    <i class="fa-solid fa-lightbulb value-icon">')

with codecs.open('e:/project/about.html', 'w', 'utf-8') as f:
    f.write(about)

# --- 3. Update services.html with JJM section
with codecs.open('e:/project/services.html', 'r', 'utf-8') as f:
    srv = f.read()

jjm_html = """
    <!-- JAL JEEVAN MISSION (JJM) PHOTO GALLERY SECTION -->
    <section id="jjm-work" class="section-padding" style="background: var(--bg-white); border-top: 1px solid rgba(0,0,0,0.05);">
        <div class="com_container">
            <div class="com-heading" style="text-align: center; margin-bottom: 2rem;">
                <h2 class="titleAnimation animate-on-scroll">Civil & Water Infrastructure (JJM)</h2>
                <p style="color: var(--text-muted); font-size: 1.1rem; max-width: 800px; margin: 1rem auto 3rem;">We are proud execution partners of the Jal Jeevan Mission, ensuring safe and adequate drinking water through individual household tap connections by 2024 to all households in rural Assam.</p>
            </div>
            
            <div class="jjm-gallery" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; padding: 1rem;">
                <div class="jjm-item animate-on-scroll" style="border-radius: 12px; overflow: hidden; box-shadow: var(--shadow-sm); aspect-ratio: 4/3; position: relative;">
                    <img src="https://images.unsplash.com/photo-1541888040600-4b3f17215f60?w=800&q=80" alt="JJM Infrastructure" style="width: 100%; height: 100%; object-fit: cover; transition: 0.5s;">
                    <div style="position: absolute; bottom: 0; left: 0; width: 100%; padding: 1rem; background: linear-gradient(transparent, rgba(0,0,0,0.8)); color: white; font-weight: 500; font-family: 'Poppins';">Piping & Trenching</div>
                </div>
                <div class="jjm-item animate-on-scroll" style="border-radius: 12px; overflow: hidden; box-shadow: var(--shadow-sm); aspect-ratio: 4/3; position: relative;">
                    <img src="https://images.unsplash.com/photo-1508514177221-188b1cf16e9d?w=800&q=80" alt="JJM Reservoir" style="width: 100%; height: 100%; object-fit: cover; transition: 0.5s;">
                    <div style="position: absolute; bottom: 0; left: 0; width: 100%; padding: 1rem; background: linear-gradient(transparent, rgba(0,0,0,0.8)); color: white; font-weight: 500; font-family: 'Poppins';">Reservoir Construction</div>
                </div>
                <div class="jjm-item animate-on-scroll" style="border-radius: 12px; overflow: hidden; box-shadow: var(--shadow-sm); aspect-ratio: 4/3; position: relative;">
                    <img src="https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?w=800&q=80" alt="JJM Water Treatment" style="width: 100%; height: 100%; object-fit: cover; transition: 0.5s;">
                    <div style="position: absolute; bottom: 0; left: 0; width: 100%; padding: 1rem; background: linear-gradient(transparent, rgba(0,0,0,0.8)); color: white; font-weight: 500; font-family: 'Poppins';">Treatment Plant</div>
                </div>
                <div class="jjm-item animate-on-scroll" style="border-radius: 12px; overflow: hidden; box-shadow: var(--shadow-sm); aspect-ratio: 4/3; position: relative;">
                    <img src="https://images.unsplash.com/photo-1558449028-b53a39d100fc?w=800&q=80" alt="JJM Household Tap" style="width: 100%; height: 100%; object-fit: cover; transition: 0.5s;">
                    <div style="position: absolute; bottom: 0; left: 0; width: 100%; padding: 1rem; background: linear-gradient(transparent, rgba(0,0,0,0.8)); color: white; font-weight: 500; font-family: 'Poppins';">Household Connectivity</div>
                </div>
                <div class="jjm-item animate-on-scroll" style="border-radius: 12px; overflow: hidden; box-shadow: var(--shadow-sm); aspect-ratio: 4/3; position: relative;">
                    <img src="https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=800&q=80" alt="JJM Commissioning" style="width: 100%; height: 100%; object-fit: cover; transition: 0.5s;">
                    <div style="position: absolute; bottom: 0; left: 0; width: 100%; padding: 1rem; background: linear-gradient(transparent, rgba(0,0,0,0.8)); color: white; font-weight: 500; font-family: 'Poppins';">Site Commissioning</div>
                </div>
                <div class="jjm-item animate-on-scroll" style="border-radius: 12px; overflow: hidden; box-shadow: var(--shadow-sm); aspect-ratio: 4/3; position: relative;">
                    <img src="https://images.unsplash.com/photo-1497366216548-37526070297c?w=800&q=80" alt="JJM Site Planning" style="width: 100%; height: 100%; object-fit: cover; transition: 0.5s;">
                    <div style="position: absolute; bottom: 0; left: 0; width: 100%; padding: 1rem; background: linear-gradient(transparent, rgba(0,0,0,0.8)); color: white; font-weight: 500; font-family: 'Poppins';">Engineering Planning</div>
                </div>
            </div>
            
            <p style="text-align: center; margin-top: 2rem; color: var(--text-muted); font-size: 0.95rem;"><i>* Currently displaying high-res proxy images. You can seamlessly replace the <code>src="..."</code> tag with your real JJM field photos!</i></p>
        </div>
        <style>
            .jjm-item { transition: 0.3s; cursor: pointer; }
            .jjm-item:hover { transform: translateY(-5px); box-shadow: var(--shadow-md); }
            .jjm-item:hover img { transform: scale(1.1); }
        </style>
    </section>

    <!-- FOOTER -->"""

srv = srv.replace("<!-- FOOTER -->", jjm_html)

with codecs.open('e:/project/services.html', 'w', 'utf-8') as f:
    f.write(srv)

print("SUCCESS")
