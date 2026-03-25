import codecs, re

# Update projects.js chart colors
try:
    with codecs.open("e:/project/projects.js", "r", "utf-8") as f:
        js = f.read()

    js = js.replace("const neon = '#00f0ff';", "const neon = '#0ea5e9';")
    js = js.replace("const accent = '#ff0055';", "const accent = '#3b82f6';")
    js = js.replace("const completedGreen = '#00ff88';", "const completedGreen = '#16a34a';")
    js = js.replace("Chart.defaults.color = '#94a3b8';", "Chart.defaults.color = '#64748b';")
    js = js.replace("color: '#fff'", "color: '#0f172a'")
    js = js.replace("rgba(0, 240, 255, 0.2)", "rgba(14, 165, 233, 0.2)")
    js = js.replace("rgba(0, 240, 255, 0.1)", "rgba(14, 165, 233, 0.1)")

    with codecs.open("e:/project/projects.js", "w", "utf-8") as f:
        f.write(js)
except Exception as e:
    print(f"Error in JS: {e}")

# Update styles.css
try:
    with codecs.open("e:/project/styles.css", "r", "utf-8") as f:
        css = f.read()

    # 1. Replace root
    root_new = """:root {
    --primary-color: #0f172a; 
    --primary-light: #1e293b;
    --accent-color: #0ea5e9; 
    --accent-hover: #0284c7;
    --accent-secondary: #3b82f6; 
    --text-dark: #334155; 
    --text-muted: #64748b;
    --bg-main: #f8fafc; 
    --bg-white: rgba(255, 255, 255, 0.85); 
    --border-color: rgba(14, 165, 233, 0.2);
    --glass-bg: rgba(255, 255, 255, 0.7);
    --hover-shadow: 0 15px 45px rgba(14, 165, 233, 0.1);
    --transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}"""
    css = re.sub(r':root\s*\{.*?\}', root_new, css, flags=re.DOTALL)

    # 2. Fix body and odd/even backgrounds
    css = css.replace('background-color: var(--primary-color);', 'background-color: var(--bg-main);')
    css = css.replace('.evenbg { background-color: var(--primary-color); }', '.evenbg { background-color: #ffffff; }')

    # 3. Headings color
    css = re.sub(r'h1, h2, h3, h4, h5, h6\s*\{[^\}]+color: #fff;\s*\}', 
                 'h1, h2, h3, h4, h5, h6 { font-family: "Orbitron", sans-serif; font-weight: 700; color: var(--primary-color); }', css)

    # 4. Nav updates for light theme
    css = css.replace('background: rgba(10, 15, 28, 0.85);', 'background: rgba(255, 255, 255, 0.9);')
    css = css.replace('rgba(10,15,28,0.9)', 'rgba(15,23,42,0.85)')
    css = css.replace('background: rgba(10, 15, 28, 0.95);', 'background: rgba(255, 255, 255, 0.95);')
    css = css.replace('color: #e2e8f0;', 'color: var(--text-dark);')
    css = css.replace('color: #fff;', 'color: var(--primary-color);')

    # Fix footer explicitly
    css = css.replace('footer { background: var(--primary-light); color: var(--text-dark);', 
                      'footer { background: var(--primary-color); color: #fff;')

    # Fix modal explicitly
    css = css.replace('background: rgba(15,23,42,0.8);', 'background: rgba(255,255,255,0.7);')
    
    # 5. Remove filters that broke the images
    css = re.sub(r'filter[^;]+brightness[^;]+;', '', css)
    css = re.sub(r'filter[^;]+invert[^;]+;', '', css)

    with codecs.open("e:/project/styles.css", "w", "utf-8") as f:
        f.write(css)
    print("CSS updated perfectly!")
except Exception as e:
    print(f"Error in CSS: {e}")
