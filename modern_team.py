import codecs
import re

with codecs.open('e:/project/about.html', 'r', 'utf-8') as f:
    about = f.read()

# 1. Provide CSS for the new filterable grid
css_pattern = re.compile(r'\.leadership-wrapper.*?\.leader-photo-card img \{.*?\n\s+\}', re.DOTALL)
new_css = """
        /* MODERN FILTERABLE TEAM GRID */
        .team-filter { display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap; margin-bottom: 3rem; }
        .filter-btn { padding: 0.8rem 1.5rem; border-radius: 30px; border: 1px solid var(--accent-color); background: transparent; color: var(--primary-color); font-weight: 500; cursor: pointer; transition: 0.3s; }
        .filter-btn.active, .filter-btn:hover { background: var(--accent-color); color: #fff; }
        
        .directory-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 2rem; }
        .team-card { background: var(--bg-white); border-radius: 12px; overflow: hidden; box-shadow: var(--shadow-sm); transition: 0.4s; text-align: center; border: 1px solid rgba(0,0,0,0.05); }
        .team-card:hover { transform: translateY(-5px); box-shadow: var(--shadow-md); }
        .team-photo { width: 100%; aspect-ratio: 1; overflow: hidden; }
        .team-photo img { width: 100%; height: 100%; object-fit: cover; object-position: top center; transition: 0.5s; filter: grayscale(20%); }
        .team-card:hover .team-photo img { transform: scale(1.05); filter: grayscale(0%); }
        .team-info { padding: 1.5rem 1rem; }
        .team-info h3 { font-size: 1.15rem; color: var(--primary-color); margin-bottom: 0.2rem; font-weight: 600;}
        .team-info p { font-size: 0.9rem; color: var(--accent-color); font-weight: 500; }
        
        .team-card.hide { display: none; }
"""
about = css_pattern.sub(new_css, about)

# 2. Replace HTML section
html_pattern = re.compile(r'<!-- 5\. LEADERSHIP SECTION -->.*?<!-- 6\. OUR TEAM -->', re.DOTALL)
new_html = """<!-- 5. TEAM DIRECTORY SECTION -->
    <section class="about-section" style="padding-bottom: 0;">
        <div class="com_container">
            <h2 class="com-heading" style="text-align: center; margin-bottom: 2rem;">Our People</h2>
            
            <!-- Filters -->
            <div class="team-filter animate-on-scroll">
                <button class="filter-btn active" data-filter="all">All</button>
                <button class="filter-btn" data-filter="board">Board of Directors</button>
                <button class="filter-btn" data-filter="projects">Project Management</button>
                <button class="filter-btn" data-filter="hr-accounts">HR & Accounts</button>
            </div>

            <!-- Grid -->
            <div class="directory-grid animate-on-scroll" id="teamDirectory">
                <!-- Board -->
                <div class="team-card" data-category="board">
                    <div class="team-photo"><img src="logo/Ravi_Sir.jpeg" alt="Ravi Pasari"></div>
                    <div class="team-info"><h3>Ravi Pasari</h3><p>Managing Director</p></div>
                </div>
                <div class="team-card" data-category="board">
                    <div class="team-photo"><img src="logo/Amit%20Kumar%20Agarwal.jpeg" alt="Amit Kumar Agarwal"></div>
                    <div class="team-info"><h3>Amit Kumar Agarwal</h3><p>Director</p></div>
                </div>
                <div class="team-card" data-category="board">
                    <div class="team-photo"><img src="logo/Aditya todi.jpeg" alt="Aditya Todi"></div>
                    <div class="team-info"><h3>Aditya Todi</h3><p>Board Member</p></div>
                </div>
                
                <!-- Projects -->
                <div class="team-card" data-category="projects">
                    <div class="team-photo"><img src="logo/Sunil_Dubey_sir.jpeg" alt="Sunil Dubey"></div>
                    <div class="team-info"><h3>Sunil Dubey</h3><p>Project Head</p></div>
                </div>
                <div class="team-card" data-category="projects">
                    <div class="team-photo"><img src="https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=600&q=80" alt="Placeholder"></div>
                    <div class="team-info"><h3>[Name]</h3><p>Project Manager</p></div>
                </div>
                <div class="team-card" data-category="projects">
                    <div class="team-photo"><img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=600&q=80" alt="Placeholder"></div>
                    <div class="team-info"><h3>[Name]</h3><p>Project Co-ordinator</p></div>
                </div>

                <!-- HR & Accounts -->
                <div class="team-card" data-category="hr-accounts">
                    <div class="team-photo"><img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=600&q=80" alt="Placeholder"></div>
                    <div class="team-info"><h3>[Name]</h3><p>Head of HR</p></div>
                </div>
                <div class="team-card" data-category="hr-accounts">
                    <div class="team-photo"><img src="https://images.unsplash.com/photo-1556157382-97eda2d62296?w=600&q=80" alt="Placeholder"></div>
                    <div class="team-info"><h3>[Name]</h3><p>Accounts Dept</p></div>
                </div>
            </div>
        </div>
    </section>

    <!-- 6. OUR TEAM -->"""
about = html_pattern.sub(new_html, about)

# 3. Replace JS Section
js_pattern = re.compile(r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\',.*?\}\);\s*</script>', re.DOTALL)
new_js = """<script>
        document.addEventListener('DOMContentLoaded', () => {
            const filterBtns = document.querySelectorAll('.filter-btn');
            const teamCards = document.querySelectorAll('.team-card');

            filterBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                    // Remove active class
                    filterBtns.forEach(b => b.classList.remove('active'));
                    btn.classList.add('active');

                    const filterValue = btn.getAttribute('data-filter');

                    teamCards.forEach(card => {
                        if (filterValue === 'all' || card.getAttribute('data-category') === filterValue) {
                            card.classList.remove('hide');
                        } else {
                            card.classList.add('hide');
                        }
                    });
                });
            });
        });
    </script>"""
about = js_pattern.sub(new_js, about)

with codecs.open('e:/project/about.html', 'w', 'utf-8') as f:
    f.write(about)

print("SUCCESS")
