import codecs

about_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Who We Are | Purbanchal Synergies Pvt. Ltd.</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="styles.css">
    <style>
        .about-hero {
            position: relative; width: 100%; height: 60vh; min-height: 500px;
            background: linear-gradient(rgba(5, 20, 36, 0.7), rgba(5, 20, 36, 0.9)), url('https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=2000&q=80') center/cover;
            display: flex; align-items: center; justify-content: center; text-align: center; color: white;
        }
        .about-hero h1 { font-family: 'Poppins'; font-size: 3.5rem; font-weight: 700; margin-bottom: 1rem; color: #fff; line-height: 1.2;}
        .about-hero p { font-size: 1.2rem; font-weight: 300; letter-spacing: 1px; color: #e2e8f0; }
        
        .about-section { padding: 6rem 0; }
        .core-identity { text-align: center; max-width: 800px; margin: 0 auto; }
        .core-identity h2 { font-size: 2.5rem; color: var(--primary-color); margin-bottom: 1.5rem; }
        .core-identity p { font-size: 1.15rem; color: var(--text-color); line-height: 1.8; margin-bottom: 1rem; }

        .story-timeline { display: flex; justify-content: space-between; position: relative; padding: 3rem 0; flex-wrap: wrap; gap: 2rem;}
        .story-timeline::before { content: ''; position: absolute; top: 50px; left: 0; width: 100%; height: 1px; background: rgba(5, 20, 36, 0.1); z-index: 1;}
        .story-step { position: relative; z-index: 2; text-align: center; flex: 1; min-width: 200px;}
        .story-dot { width: 20px; height: 20px; background: var(--accent-color); border-radius: 50%; margin: 0 auto 1.5rem; border: 4px solid var(--bg-white); box-shadow: 0 0 0 2px rgba(255, 102, 0, 0.2); transition: 0.3s; }
        .story-step:hover .story-dot { transform: scale(1.3); box-shadow: 0 0 15px rgba(255,102,0,0.4); }
        .story-step h4 { color: var(--primary-color); font-size: 1.1rem; margin-bottom: 0.5rem; }
        .story-step p { font-size: 0.95rem; color: var(--text-muted); }

        .values-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem; }
        .value-card { background: var(--bg-white); padding: 3rem 2rem; border-radius: 12px; text-align: center; box-shadow: var(--shadow-sm); transition: 0.3s; border-bottom: 3px solid transparent; border: 1px solid rgba(0,0,0,0.05); }
        .value-card:hover { transform: translateY(-10px); box-shadow: var(--shadow-md); border-bottom-color: var(--accent-color); }
        .value-icon { font-size: 2.5rem; color: var(--accent-color); margin-bottom: 1.5rem; transition: 0.3s;}
        .value-card:hover .value-icon { transform: scale(1.1); }
        .value-card h3 { color: var(--primary-color); font-size: 1.4rem; margin-bottom: 1rem; }

        .leadership-wrapper { display: flex; gap: 4rem; position: relative; align-items: flex-start; }
        .leadership-left { flex: 0 0 40%; position: sticky; top: 120px; height: auto; }
        .leadership-right { flex: 0 0 60%; display: flex; flex-direction: column; gap: 15vh; padding-bottom: 20vh; }
        
        .leader-info-box { position: absolute; top: 0; left: 0; width: 100%; opacity: 0; transform: translateY(20px); transition: all 0.6s cubic-bezier(0.4, 0, 0.2, 1); visibility: hidden; }
        .leader-info-box.active { opacity: 1; transform: translateY(0); visibility: visible; position: relative;}
        .leader-info-box h2 { font-size: 3rem; color: var(--primary-color); margin-bottom: 0.5rem; line-height: 1.2; }
        .leader-info-box h4 { font-size: 1.2rem; color: var(--accent-color); margin-bottom: 1.5rem; font-weight: 500; letter-spacing: 1px; text-transform: uppercase; }
        .leader-info-box p { font-size: 1.1rem; color: var(--text-muted); line-height: 1.8; }
        
        .leader-photo-card { height: 70vh; min-height: 500px; border-radius: 20px; overflow: hidden; position: relative; box-shadow: var(--shadow-md); transform: scale(0.95); transition: 0.6s; opacity: 0.5; filter: grayscale(100%); }
        .leader-photo-card.in-view { transform: scale(1); opacity: 1; filter: grayscale(0%); }
        .leader-photo-card img { width: 100%; height: 100%; object-fit: cover; object-position: top center; }

        .team-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; }
        .team-img-box { border-radius: 8px; overflow: hidden; aspect-ratio: 1; }
        .team-img-box img { width: 100%; height: 100%; object-fit: cover; transition: 0.5s; }
        .team-img-box:hover img { transform: scale(1.1); }
        .team-subtext { text-align: center; margin-top: 3rem; font-size: 1.3rem; font-weight: 500; color: var(--primary-color); font-family: 'Poppins'; }

        .trust-wrap { display: flex; justify-content: center; gap: 5rem; text-align: center; flex-wrap: wrap; }
        .trust-item { display: flex; align-items: center; gap: 1rem; }
        .trust-icon { width: 50px; height: 50px; background: rgba(5,20,36,0.05); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: var(--accent-color); font-size: 1.5rem; }
        .trust-text { font-weight: 600; color: var(--primary-color); font-size: 1.1rem; }

        .vision-section { padding: 8rem 0; text-align: center; background: var(--primary-color); color: white; }
        .vision-text { font-size: 2.5rem; max-width: 900px; margin: 0 auto; font-family: 'Poppins'; font-weight: 300; line-height: 1.4; color: #fff;}
        .vision-text span { color: var(--accent-color); font-weight: 600; }

        @media (max-width: 991px) {
            .leadership-wrapper { flex-direction: column; }
            .leadership-left { position: relative; top: 0; margin-bottom: 3rem; }
            .leader-info-box { position: relative; opacity: 1; transform: none; visibility: visible; display: none; }
            .leader-info-box.active { display: block; }
            .leader-photo-card { height: 50vh; opacity: 1; transform: none; filter: none; margin-bottom: 2rem;}
            .leadership-right { gap: 2rem; padding-bottom: 0; }
            .team-grid { grid-template-columns: 1fr 1fr; }
            .story-timeline::before { display: none; }
            .story-step { display: flex; align-items: center; text-align: left; gap: 1.5rem; margin-bottom: 1.5rem; }
            .story-dot { margin: 0; }
        }
        @media (max-width: 768px) {
            .about-hero h1 { font-size: 2.5rem; }
            .team-grid { grid-template-columns: 1fr; }
            .trust-wrap { gap: 2rem; flex-direction: column; align-items: flex-start; }
        }
    </style>
</head>
<body class="animationcss">
    <header class="navbar navbar-transparent">
        <div class="com_container headerWrapper">
            <div class="logo">
                <a href="index.html">
                    <img src="logo/pspl%20logo.png" alt="Logo" style="max-height: 60px; margin-right: 15px;">
                    Purbanchal Synergies
                </a>
            </div>
            <div class="menu-toggle"><i class="fa-solid fa-bars"></i></div>
            <div class="left-menu nav-main">
                <nav>
                    <ul class="nav-wrap nav-links">
                        <li><a href="index.html">Home</a></li>
                        <li><a href="about.html" class="active-link">Who We Are</a></li>
                        <li><a href="projects.html">Projects</a></li>
                        <li><a href="services.html">Services</a></li>
                        <li><a href="contact.html">Contact Us</a></li>
                    </ul>
                </nav>
            </div>
            <div class="search-bar mob-search-icon">
                <a href="contact.html" class="gradient-button header-cta">Work With Us</a>
            </div>
        </div>
    </header>

    <!-- 1. HERO SECTION -->
    <section class="about-hero">
        <div class="com_container animate-on-scroll">
            <h1>Driven by People.<br>Powered by Innovation.</h1>
            <p>Building the future of smart energy and electrical infrastructure</p>
        </div>
    </section>

    <!-- 2. WHO WE ARE -->
    <section class="about-section oddbg">
        <div class="com_container">
            <div class="core-identity animate-on-scroll">
                <h2>Who We Are</h2>
                <p>We are a premier electrical infrastructure and smart metering company dedicated to shaping resilient energy grids. With a strong, deeply rooted presence across Assam, we are the trusted execution partner for government utilities, corporate clients, and public sector enterprises.</p>
            </div>
        </div>
    </section>

    <!-- 3. OUR STORY -->
    <section class="about-section">
        <div class="com_container">
            <h2 class="com-heading" style="text-align: center; margin-bottom: 4rem;">Our Story</h2>
            <div class="story-timeline animate-on-scroll">
                <div class="story-step">
                    <div class="story-dot"></div>
                    <h4>The Beginning</h4>
                    <p>Started our legacy as Purbanchal Enterprise.</p>
                </div>
                <div class="story-step">
                    <div class="story-dot"></div>
                    <h4>Evolution</h4>
                    <p>Grew to form Purbanchal Synergies Pvt Ltd.</p>
                </div>
                <div class="story-step">
                    <div class="story-dot"></div>
                    <h4>Expansion</h4>
                    <p>Expanded into smart metering & EPC.</p>
                </div>
                <div class="story-step">
                    <div class="story-dot"></div>
                    <h4>Scale</h4>
                    <p>Executed large-scale transformative projects.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- 4. CORE VALUES -->
    <section class="about-section oddbg">
        <div class="com_container">
            <h2 class="com-heading" style="text-align: center; margin-bottom: 4rem;">What Defines Us</h2>
            <div class="values-grid">
                <div class="value-card animate-on-scroll">
                    <i class="fa-solid fa-award value-icon"></i>
                    <h3>Excellence</h3>
                    <p>Delivering the highest standard is our baseline.</p>
                </div>
                <div class="value-card animate-on-scroll">
                    <i class="fa-solid fa-shield-halved value-icon"></i>
                    <h3>Reliability</h3>
                    <p>Proven track record of timely execution.</p>
                </div>
                <div class="value-card animate-on-scroll">
                    <i class="fa-solid fa-handshake-angle value-icon"></i>
                    <h3>Transparency</h3>
                    <p>Absolute clarity in all engagements.</p>
                </div>
                <div class="value-card animate-on-scroll">
                    <i class="fa-solid fa-lightbulb value-icon"></i>
                    <h3>Innovation</h3>
                    <p>Implementing next-gen technologies.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- 5. LEADERSHIP SECTION -->
    <section class="about-section" style="padding-bottom: 0;">
        <div class="com_container">
            <h2 class="com-heading" style="margin-bottom: 4rem;">Leadership</h2>
            <div class="leadership-wrapper">
                <!-- Left: Sticky Details -->
                <div class="leadership-left">
                    <div class="leader-info-box active" id="info-leader-1">
                        <h2>Sunil Dubey</h2>
                        <h4>Managing Director</h4>
                        <p>With decades of visionary leadership, Mr. Sunil Dubey has been the driving force behind our strategic expansion across Eastern India. His unwavering commitment to operational excellence has firmly established Purbanchal Synergies as a premier name in the electrical sector.</p>
                    </div>
                    <div class="leader-info-box" id="info-leader-2">
                        <h2>Ravi Sir</h2>
                        <h4>Executive Director</h4>
                        <p>Bringing immense field expertise and technical acumen, Ravi Sir leads aggressive execution strategies. His focus on seamless on-ground deployment and stringent quality control ensures every large-scale project is delivered flawlessly.</p>
                    </div>
                </div>
                <!-- Right: Scrolling Photos -->
                <div class="leadership-right">
                    <div class="leader-photo-card" id="card-leader-1" data-id="1">
                        <img src="logo/Sunil_Dubey_sir.jpeg" alt="Sunil Dubey">
                    </div>
                    <div class="leader-photo-card" id="card-leader-2" data-id="2">
                        <img src="logo/Ravi_Sir.jpeg" alt="Ravi Sir">
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 6. OUR TEAM -->
    <section class="about-section oddbg">
        <div class="com_container">
            <div class="team-grid">
                <div class="team-img-box animate-on-scroll"><img src="https://images.unsplash.com/photo-1541888040600-4b3f17215f60?w=600&q=80" alt="Team Work"></div>
                <div class="team-img-box animate-on-scroll"><img src="https://images.unsplash.com/photo-1508514177221-188b1cf16e9d?w=600&q=80" alt="Team Work"></div>
                <div class="team-img-box animate-on-scroll"><img src="https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?w=600&q=80" alt="Team Work"></div>
            </div>
            <div class="team-subtext animate-on-scroll">A team of skilled professionals delivering excellence on ground.</div>
        </div>
    </section>

    <!-- 7. TRUST INDICATORS -->
    <section class="about-section" style="padding: 4rem 0;">
        <div class="com_container">
            <div class="trust-wrap animate-on-scroll">
                <div class="trust-item">
                    <div class="trust-icon"><i class="fa-solid fa-clock-rotate-left"></i></div>
                    <div class="trust-text">20+ Years Experience</div>
                </div>
                <div class="trust-item">
                    <div class="trust-icon"><i class="fa-solid fa-certificate"></i></div>
                    <div class="trust-text">ISO Certified</div>
                </div>
                <div class="trust-item">
                    <div class="trust-icon"><i class="fa-solid fa-building-shield"></i></div>
                    <div class="trust-text">Trusted by Government Utilities</div>
                </div>
            </div>
        </div>
    </section>

    <!-- 8. VISION -->
    <section class="vision-section">
        <div class="com_container animate-on-scroll">
            <p class="vision-text">"To build <span>smarter</span>, <span>sustainable</span>, and <span>future-ready</span> energy infrastructure."</p>
        </div>
    </section>

    <footer>
        <div class="com_container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <div class="logo" style="margin-bottom: 1rem;">
                        <img src="logo/pspl%20logo.png" alt="PSPL Logo" style="max-height: 50px; margin-right: 10px;">
                        PSPL
                    </div>
                    <p>Delivering end-to-end solutions across energy, infrastructure, manufacturing, and technology.</p>
                    <div class="social-links">
                        <a href="#"><i class="fa-brands fa-linkedin-in"></i></a>
                        <a href="#"><i class="fa-brands fa-twitter"></i></a>
                    </div>
                </div>
                <div>
                    <h4 class="footer-title">Quick Links</h4>
                    <ul class="footer-links">
                        <li><a href="index.html">Home</a></li>
                        <li><a href="about.html">Who We Are</a></li>
                        <li><a href="projects.html">Projects</a></li>
                        <li><a href="services.html">Services</a></li>
                        <li><a href="contact.html">Contact Us</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="footer-title">Services</h4>
                    <ul class="footer-links">
                        <li><a href="services.html">Smart Metering</a></li>
                        <li><a href="services.html">Power Distribution</a></li>
                        <li><a href="services.html">Solar EPC</a></li>
                        <li><a href="services.html">Civil & Water</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="footer-title">Contact Us</h4>
                    <ul class="footer-links" style="line-height:2;">
                        <li><i class="fa-solid fa-location-dot" style="color:var(--accent-color);margin-right:10px;"></i> B.K Enclave, Panbazar,<br><span style="margin-left:25px;">Guwahati-781001, Assam</span></li>
                        <li><i class="fa-solid fa-phone" style="color:var(--accent-color);margin-right:10px;"></i> +91-3614081063</li>
                        <li><i class="fa-solid fa-envelope" style="color:var(--accent-color);margin-right:10px;"></i> pspl@purbanchalenterprise.com</li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 Purbanchal Synergies Pvt. Ltd. All Rights Reserved.</p>
            </div>
        </div>
    </footer>

    <script src="main.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            if(window.innerWidth <= 991) return;

            const cards = document.querySelectorAll('.leader-photo-card');
            const infoBoxes = document.querySelectorAll('.leader-info-box');

            const observer = new IntersectionObserver((entries) => {
                let observedAny = false;
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('in-view');
                        const id = entry.target.getAttribute('data-id');
                        infoBoxes.forEach(box => box.classList.remove('active'));
                        const targetBox = document.getElementById('info-leader-' + id);
                        if(targetBox) targetBox.classList.add('active');
                    } else {
                        entry.target.classList.remove('in-view');
                    }
                });
            }, {
                root: null,
                rootMargin: '-30% 0px -40% 0px',
                threshold: 0.1
            });

            cards.forEach(card => observer.observe(card));
        });
    </script>
</body>
</html>"""

with codecs.open('e:/project/about.html', 'w', 'utf-8') as f:
    f.write(about_content)

print("SUCCESS")
