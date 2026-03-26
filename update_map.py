import codecs
import re

with codecs.open('e:/project/projects.html', 'r', 'utf-8') as f:
    content = f.read()

# Replace CSS
css_pattern = re.compile(r'/\*\s*MAP SECTION\s*\*/.*?/\*\s*CREDIBILITY\s*\*/', re.DOTALL)
new_css = """/* MAP SECTION - FUTURISTIC DARK THEME */
        .dark-map-bg { background: #020617; padding: 6rem 0; text-align: center; border-top: 1px solid #1e293b; border-bottom: 1px solid #1e293b;}
        .futuristic-map {
            position: relative; width: 100%; max-width: 1000px; margin: 0 auto; padding: 2rem;
            aspect-ratio: 16/9; background: url('https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Assam_in_India_%28disputed_hatched%29.svg/1024px-Assam_in_India_%28disputed_hatched%29.svg.png') no-repeat center center;
            background-size: contain; filter: invert(1) brightness(0.8) contrast(1.5);
            border: 1px solid rgba(0,240,255,0.1); border-radius: 20px;
            box-shadow: inset 0 0 50px rgba(0,0,0,0.8), 0 0 40px rgba(0,240,255,0.05);
        }
        .nodes-wrapper {
            position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 5;
        }
        .map-node {
            position: absolute; border-radius: 50%; cursor: pointer; transition: 0.3s;
        }
        .map-node::before {
            content: attr(data-tooltip); position: absolute; bottom: 150%; left: 50%; transform: translateX(-50%);
            background: rgba(2, 6, 23, 0.9); color: #fff; padding: 0.5rem 1rem; border-radius: 4px; border: 1px solid #00f0ff;
            font-size: 0.85rem; white-space: nowrap; opacity: 0; visibility: hidden; transition: 0.3s; pointer-events: none;
            box-shadow: 0 0 15px rgba(0, 240, 255, 0.4); text-transform: uppercase; letter-spacing: 1px; font-family: 'Inter', sans-serif; z-index: 10;
        }
        .map-node:hover::before { opacity: 1; bottom: 180%; visibility: visible; }
        .map-node:hover { transform: scale(1.5); z-index: 10; }

        .node-hub {
            width: 16px; height: 16px; background: #00f0ff; box-shadow: 0 0 20px #00f0ff, 0 0 40px #00f0ff;
        }
        .node-hub::after {
            content: ''; position: absolute; inset: -15px; border: 2px solid #00f0ff; border-radius: 50%;
            animation: pulseHub 2s infinite;
        }
        .node-assam {
            width: 8px; height: 8px; background: #00e1ff; box-shadow: 0 0 10px #00e1ff; animation: breathing 3s infinite alternate;
        }
        .node-outside {
            width: 12px; height: 12px;
        }
        .outside-purple { background: #b500ff; box-shadow: 0 0 15px #b500ff;}
        .outside-purple::after { content: ''; position: absolute; inset: -10px; border: 1px solid #b500ff; border-radius: 50%; animation: pulseHub 2.5s infinite; }
        .outside-green { background: #00ff88; box-shadow: 0 0 15px #00ff88;}
        .outside-green::after { content: ''; position: absolute; inset: -10px; border: 1px solid #00ff88; border-radius: 50%; animation: pulseHub 2.5s infinite; }

        @keyframes pulseHub { 0% { transform: scale(0.5); opacity: 1; } 100% { transform: scale(2.5); opacity: 0; } }
        @keyframes breathing { 0% { transform: scale(1); opacity: 0.6; } 100% { transform: scale(1.3); opacity: 1; } }
        @keyframes flowLineAnim { to { stroke-dashoffset: -20; } }
        .anim-line { animation: flowLineAnim 1s linear infinite; }

        /* CREDIBILITY */"""
content = css_pattern.sub(new_css, content)

# Replace HTML
html_pattern = re.compile(r'<!-- MAP SECTION -->.*?<!-- CREDIBILITY SECTION -->', re.DOTALL)
new_html = """<!-- MAP SECTION -->
    </div> <!-- Close com_container to allow full width for dark map section -->
    
    <section class="map-section dark-map-bg">
        <h2 class="pt-title" style="color:#fff;">Grid <span style="color:#00f0ff;">Network</span></h2>
        <div class="map-container futuristic-map">
            <!-- SVG Connecting Lines -->
            <svg class="map-lines" style="position: absolute; top:0; left:0; width:100%; height:100%; pointer-events:none; z-index: 1;">
               <defs>
                  <linearGradient id="grad-green" x1="100%" y1="0%" x2="0%" y2="100%">
                     <stop offset="0%" stop-color="#00f0ff" />
                     <stop offset="100%" stop-color="#00ff88" />
                  </linearGradient>
                  <linearGradient id="grad-purple" x1="100%" y1="0%" x2="0%" y2="100%">
                     <stop offset="0%" stop-color="#00f0ff" />
                     <stop offset="100%" stop-color="#b500ff" />
                  </linearGradient>
               </defs>
               <line x1="82%" y1="45%" x2="77%" y2="52%" stroke="url(#grad-green)" stroke-width="2" opacity="0.6" stroke-dasharray="5,5" class="anim-line" />
               <line x1="82%" y1="45%" x2="75%" y2="50%" stroke="url(#grad-purple)" stroke-width="2" opacity="0.6" stroke-dasharray="5,5" class="anim-line" />
               <line x1="82%" y1="45%" x2="76%" y2="51%" stroke="url(#grad-purple)" stroke-width="2" opacity="0.6" stroke-dasharray="5,5" class="anim-line" />
            </svg>

            <!-- Nodes -->
            <div class="nodes-wrapper">
                <!-- Hub -->
                <div class="map-node node-hub" style="top:44.5%; left:82%;" data-tooltip="Guwahati (Main Hub)"></div>
                <!-- Assam Cluster -->
                <div class="map-node node-assam" style="top:43.5%; left:81%; animation-delay: 0.1s;" data-tooltip="Nalbari"></div>
                <div class="map-node node-assam" style="top:44%; left:81.5%; animation-delay: 0.2s;" data-tooltip="Rangia"></div>
                <div class="map-node node-assam" style="top:44.8%; left:83%; animation-delay: 0.3s;" data-tooltip="Mangaldoi"></div>
                <div class="map-node node-assam" style="top:45%; left:82.5%; animation-delay: 0.4s;" data-tooltip="Sonapur"></div>
                <div class="map-node node-assam" style="top:44.2%; left:82.2%; animation-delay: 0.5s;" data-tooltip="Narengi"></div>
                <div class="map-node node-assam" style="top:44.9%; left:81.8%; animation-delay: 0.6s;" data-tooltip="Azara"></div>
                <div class="map-node node-assam" style="top:44.2%; left:81.9%; animation-delay: 0.7s;" data-tooltip="Amingaon"></div>
                <div class="map-node node-assam" style="top:45.5%; left:78%; animation-delay: 0.8s;" data-tooltip="Kokrajhar"></div>
                <div class="map-node node-assam" style="top:46%; left:79%; animation-delay: 0.9s;" data-tooltip="Goalpara"></div>
                <div class="map-node node-assam" style="top:44.5%; left:79.5%; animation-delay: 0.1s;" data-tooltip="Bongaigaon"></div>
                <div class="map-node node-assam" style="top:44.8%; left:80%; animation-delay: 0.2s;" data-tooltip="Barpeta"></div>
                <div class="map-node node-assam" style="top:45.5%; left:79.2%; animation-delay: 0.3s;" data-tooltip="Abhayapuri"></div>
                <div class="map-node node-assam" style="top:43.5%; left:84%; animation-delay: 0.4s;" data-tooltip="Nagaon"></div>
                <div class="map-node node-assam" style="top:44%; left:84.5%; animation-delay: 0.5s;" data-tooltip="Kampur"></div>
                <div class="map-node node-assam" style="top:44.3%; left:84.8%; animation-delay: 0.6s;" data-tooltip="Doboka"></div>
                <div class="map-node node-assam" style="top:42.5%; left:84.5%; animation-delay: 0.7s;" data-tooltip="Tezpur"></div>
                <div class="map-node node-assam" style="top:42%; left:87%; animation-delay: 0.8s;" data-tooltip="Jorhat"></div>
                <div class="map-node node-assam" style="top:42.5%; left:86.5%; animation-delay: 0.9s;" data-tooltip="Golaghat"></div>
                <div class="map-node node-assam" style="top:41.5%; left:87.5%; animation-delay: 0.1s;" data-tooltip="Sibsagar"></div>
                <div class="map-node node-assam" style="top:40%; left:88.5%; animation-delay: 0.2s;" data-tooltip="Dibrugarh"></div>
                <div class="map-node node-assam" style="top:39.5%; left:89%; animation-delay: 0.3s;" data-tooltip="Tinsukia"></div>
                <div class="map-node node-assam" style="top:45.3%; left:82.8%; animation-delay: 0.4s;" data-tooltip="Changsari"></div>

                <!-- Outside Assam -->
                <div class="map-node node-outside outside-purple" style="top:52%; left:77%;" data-tooltip="Malda (West Bengal) - Smart Meters"></div>
                <div class="map-node node-outside outside-purple" style="top:50%; left:75%;" data-tooltip="Bhagalpur (Bihar) - Smart Meters"></div>
                <div class="map-node node-outside outside-green" style="top:51%; left:76%;" data-tooltip="Sahibganj (Jharkhand) - Infrastructure"></div>
            </div>
        </div>
    </section>

    <!-- CREDIBILITY SECTION -->"""
content = html_pattern.sub(new_html, content)

with codecs.open('e:/project/projects.html', 'w', 'utf-8') as f:
    f.write(content)

print("SUCCESS")
