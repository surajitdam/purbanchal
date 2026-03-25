import codecs

try:
    with codecs.open('e:/project/projects.html', 'r', 'utf-8') as f:
        html = f.read()

    # Variables
    html = html.replace('--proj-bg: #0a0f1c;', '--proj-bg: #f8fafc;')
    html = html.replace('--proj-neon: #00f0ff;', '--proj-neon: #FF6600;')
    html = html.replace('--proj-neon-dim: rgba(0, 240, 255, 0.2);', '--proj-neon-dim: rgba(255, 102, 0, 0.2);')
    html = html.replace('--proj-panel: rgba(16, 25, 43, 0.6);', '--proj-panel: #ffffff;')
    html = html.replace('--proj-panel-border: rgba(0, 240, 255, 0.3);', '--proj-panel-border: rgba(5, 20, 36, 0.1);')
    html = html.replace('--proj-text: #e2e8f0;', '--proj-text: #1e293b;')
    html = html.replace('--proj-muted: #94a3b8;', '--proj-muted: #64748b;')
    html = html.replace('--proj-accent: #ff0055;', '--proj-accent: #051424;')

    # Headings and fonts
    html = html.replace("h1, h2, h3, h4 { font-family: 'Orbitron', sans-serif; color: #fff; }", "h1, h2, h3, h4 { font-family: 'Poppins', sans-serif; color: var(--proj-accent); }\n        .logo a { color: var(--proj-accent) !important; text-shadow: none; font-weight: 800; font-family: 'Poppins', sans-serif; }")
    html = html.replace("'Orbitron'", "'Poppins'")

    # Navbar
    html = html.replace("background: rgba(10, 15, 28, 0.8) !important;", "background: #ffffff !important; box-shadow: 0 4px 20px rgba(0,0,0,0.05);")
    html = html.replace("color: #fff !important;", "color: #1e293b !important;")
    html = html.replace("style=\"text-shadow: 0 0 10px var(--proj-neon); color: var(--proj-neon) !important;\"", "style=\"text-shadow: none; color: var(--proj-neon) !important; font-weight: 600;\"")

    # Hero
    html = html.replace("text-shadow: 0 0 20px rgba(0, 240, 255, 0.8);", "text-shadow: none;")
    html = html.replace("background: linear-gradient(90deg, #fff, var(--proj-neon));", "background: linear-gradient(90deg, var(--proj-accent), var(--proj-neon));")

    # Generic bright text fixes
    html = html.replace("color: #fff", "color: var(--proj-accent)")

    # Inputs
    html = html.replace("background: rgba(0,0,0,0.5);", "background: #f8fafc;")

    # Modal & Footer
    html = html.replace("rgba(10,15,28,0.9)", "rgba(255,255,255,0.95)")
    html = html.replace("rgba(0,0,0,0.3)", "rgba(240,245,250,0.8)")
    
    # Grid bg colors
    html = html.replace("rgba(0, 240, 255, 0.05)", "rgba(255, 102, 0, 0.05)")

    # Filter invert on map
    html = html.replace("filter: invert(1)", "filter: invert(0)")

    with codecs.open('e:/project/projects.html', 'w', 'utf-8') as f:
        f.write(html)
except Exception as e:
    print(e)


try:
    with codecs.open('e:/project/projects.js', 'r', 'utf-8') as f:
        js = f.read()

    js = js.replace("const neon = '#00f0ff';", "const neon = '#FF6600';")
    js = js.replace("const accent = '#ff0055';", "const accent = '#051424';")
    js = js.replace("const text = '#e2e8f0';", "const text = '#1e293b';")
    js = js.replace("color: '#fff'", "color: '#051424'")
    js = js.replace("rgba(0, 240, 255, 0.2)", "rgba(255, 102, 0, 0.2)")
    js = js.replace("rgba(0, 240, 255, 0.1)", "rgba(255, 102, 0, 0.1)")

    with codecs.open('e:/project/projects.js', 'w', 'utf-8') as f:
        f.write(js)
except Exception as e:
    print(e)
