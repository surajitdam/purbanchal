document.addEventListener('DOMContentLoaded', () => {

    // Navbar Scroll
    const navbar = document.querySelector('.navbar');
    const syncNavbarState = () => {
        if (!navbar) return;
        navbar.classList.toggle('scrolled', window.scrollY > 50);
    };
    window.addEventListener('scroll', syncNavbarState);
    syncNavbarState();

    // Mobile Menu Toggle
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    if (menuToggle && navbar && navLinks) {
        menuToggle.setAttribute('aria-expanded', 'false');
        menuToggle.addEventListener('click', () => {
            const isOpen = navbar.classList.toggle('nav-open');
            menuToggle.setAttribute('aria-expanded', String(isOpen));
        });

        navLinks.addEventListener('click', (event) => {
            if (event.target.closest('a') && window.innerWidth <= 1024) {
                navbar.classList.remove('nav-open');
                menuToggle.setAttribute('aria-expanded', 'false');
            }
        });

        window.addEventListener('resize', () => {
            if (window.innerWidth > 1024) {
                navbar.classList.remove('nav-open');
                menuToggle.setAttribute('aria-expanded', 'false');
            }
        });
    }

    // Hero Swiper Initialization
    if (typeof Swiper !== 'undefined' && document.querySelector('.HeroSlider')) {
        const heroSwiper = new Swiper('.HeroSlider', {
            loop: true,
            effect: 'fade', // Smooth crossfade over zooming images
            fadeEffect: {
                crossFade: true
            },
            autoplay: {
                delay: 6000,
                disableOnInteraction: false,
            },
            speed: 1000,
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },
            on: {
                autoplayTimeLeft(s, time, progress) {
                    const pbar = document.getElementById('pbar');
                    if(pbar) {
                        pbar.style.width = `${(1 - progress) * 100}%`;
                    }
                }
            }
        });
    }

    // 3 Card Slider Initialization
    if (typeof Swiper !== 'undefined' && document.querySelector('.three-imgSlideWrapper')) {
        new Swiper('.three-imgSlideWrapper', {
            slidesPerView: 1.2,
            spaceBetween: 20,
            loop: true,
            breakpoints: {
                640: { slidesPerView: 2, spaceBetween: 20 },
                1024: { slidesPerView: 3, spaceBetween: 30 },
            }
        });
    }

    // Vertical Tabs (Core Services)
    const tabLinks = document.querySelectorAll('.business-left-sec .businessThumb button');
    const tabs = document.querySelectorAll('.business-right-sec');

    const setActiveTab = (link) => {
        tabLinks.forEach((tabLink) => {
            const isActive = tabLink === link;
            tabLink.classList.toggle('active', isActive);
            tabLink.setAttribute('aria-selected', String(isActive));
            tabLink.setAttribute('tabindex', isActive ? '0' : '-1');
        });

        tabs.forEach((tab) => {
            tab.classList.remove('active');
            tab.setAttribute('hidden', '');
        });

        const targetId = link.getAttribute('data-business-sub-tab');
        const targetTab = document.getElementById(targetId);
        if (targetTab) {
            targetTab.classList.add('active');
            targetTab.removeAttribute('hidden');
        }
    };

    if (tabLinks.length > 0 && tabs.length > 0) {
        tabLinks.forEach((link, index) => {
            link.addEventListener('click', () => {
                setActiveTab(link);
            });

            link.addEventListener('keydown', (event) => {
                if (event.key !== 'ArrowDown' && event.key !== 'ArrowUp' && event.key !== 'ArrowRight' && event.key !== 'ArrowLeft') {
                    return;
                }

                event.preventDefault();
                const direction = event.key === 'ArrowDown' || event.key === 'ArrowRight' ? 1 : -1;
                const nextIndex = (index + direction + tabLinks.length) % tabLinks.length;
                tabLinks[nextIndex].focus();
                setActiveTab(tabLinks[nextIndex]);
            });
        });

        const initialActiveTab = document.querySelector('.business-left-sec .businessThumb button.active') || tabLinks[0];
        setActiveTab(initialActiveTab);
    }

    // Intersection Observer for Animate on Scroll
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, { threshold: 0.1 });
    
    document.querySelectorAll('.animate-on-scroll').forEach(el => observer.observe(el));

    // Number Counter Animation
    const animCounters = document.querySelectorAll('.stat-num');
    let counted = false;
    const counterObserver = new IntersectionObserver((entries) => {
        if (entries[0].isIntersecting && !counted) {
            counted = true;
            animCounters.forEach(counter => {
                const targetText = counter.getAttribute('data-target');
                if(!targetText) return;

                const target = parseInt(targetText);
                const duration = 2000;
                const step = target / (duration / 16);
                let current = 0;

                // Extract suffix if any
                const suffix = counter.getAttribute('data-suffix') || '';

                // Format numbers to Indian Numbering System
                const formatNumber = (num) => {
                    return Math.floor(num).toLocaleString('en-IN');
                };

                const updateCounter = () => {
                    current += step;
                    if (current < target) {
                        counter.innerText = formatNumber(current) + suffix;
                        requestAnimationFrame(updateCounter);
                    } else {
                        counter.innerText = formatNumber(target) + suffix;
                    }
                };
                updateCounter();
            });
        }
    }, { threshold: 0.5 });
    
    const statsSection = document.querySelector('.stats-section');
    if (statsSection && animCounters.length > 0) {
        counterObserver.observe(statsSection);
    }

    // PROJECTS GRID FOR PROJECTS.HTML (Preserved Logic)
    const projectsContainer = document.getElementById('full-projects-container');
    const filterBtns = document.querySelectorAll('.filter-btn');

    if (typeof projects !== 'undefined' && projectsContainer) {
        const sortedProjects = projects.sort((a, b) => b.valueLakh - a.valueLakh);

        const renderProjects = (filterType) => {
            projectsContainer.innerHTML = '';
            let filtered = sortedProjects;
            
            if (filterType !== 'all') {
                if (filterType === 'Completed') {
                    filtered = sortedProjects.filter(p => p.status.includes('Completed'));
                } else if (filterType === 'Ongoing') {
                    filtered = sortedProjects.filter(p => !p.status.includes('100%') && !p.status.includes('Completed'));
                }
            }

            filtered.forEach((project) => {
                const isCompleted = project.status.includes('Completed');
                
                let projectImg = 'https://images.unsplash.com/photo-1541888040600-4b3f17215f60?w=600&q=80';
                if(project.name.toLowerCase().includes('solar')) {
                    projectImg = 'https://images.unsplash.com/photo-1508514177221-188b1cf16e9d?w=600&q=80';
                } else if(project.name.toLowerCase().includes('meter')) {
                    projectImg = 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&q=80';
                }

                const valueCr = (project.valueLakh / 100).toFixed(2);

                const cardHtml = `
                    <div class="project-card animate-on-scroll">
                        <div class="project-img" style="background-image: url('${projectImg}')"></div>
                        <div class="project-content">
                            <h3 style="font-size: 1rem; color: var(--accent-color);">${project.client}</h3>
                            <p style="font-weight: 600; font-size: 1.1rem; margin-bottom: 0.5rem; color: var(--text-dark);">${project.name}</p>
                            <div style="font-size: 0.9rem; color: var(--text-muted); display:flex; justify-content:space-between; margin-top:1rem; border-top:1px solid #eee; padding-top:0.5rem;">
                                <span><i class="fa-solid fa-indian-rupee-sign"></i> ${valueCr} Cr</span>
                                <span style="color: ${isCompleted ? '#10b981' : 'var(--accent-color)'}; font-weight:600;">${project.status}</span>
                            </div>
                        </div>
                    </div>
                `;
                projectsContainer.insertAdjacentHTML('beforeend', cardHtml);
            });

            projectsContainer.querySelectorAll('.animate-on-scroll').forEach(el => observer.observe(el));
        };

        renderProjects('all');

        if(filterBtns.length > 0) {
            filterBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                    filterBtns.forEach(b => b.classList.remove('active', 'btn-primary'));
                    filterBtns.forEach(b => b.classList.add('btn-outline'));
                    
                    btn.classList.add('active', 'btn-primary');
                    btn.classList.remove('btn-outline');
                    
                    renderProjects(btn.getAttribute('data-filter'));
                });
            });
        }
    }

    // Contact Form Handling
    const contactForm = document.getElementById('contact-form');
    const formSuccess = document.getElementById('form-success');
    const formError = document.getElementById('form-error');

    if (contactForm && formSuccess) {
        contactForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            const submitButton = contactForm.querySelector('button[type="submit"]');
            if (submitButton) {
                submitButton.disabled = true;
                submitButton.setAttribute('aria-busy', 'true');
            }

            if (formError) {
                formError.style.display = 'none';
            }

            try {
                const formData = new FormData(contactForm);
                const response = await fetch(contactForm.action, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        Accept: 'application/json',
                    },
                });

                if (!response.ok) {
                    throw new Error('Form submission failed');
                }

                contactForm.style.transition = 'opacity 0.4s ease';
                contactForm.style.opacity = '0';

                setTimeout(() => {
                    contactForm.reset();
                    contactForm.style.display = 'none';
                    formSuccess.style.display = 'block';
                    formSuccess.style.opacity = '0';
                    formSuccess.style.transition = 'opacity 0.4s ease';

                    // Trigger reflow for transition
                    formSuccess.offsetHeight;
                    formSuccess.style.opacity = '1';

                    // Scroll to message
                    formSuccess.scrollIntoView({ behavior: 'smooth', block: 'center' });
                }, 400);
            } catch (error) {
                if (formError) {
                    formError.style.display = 'block';
                }
            } finally {
                if (submitButton) {
                    submitButton.disabled = false;
                    submitButton.removeAttribute('aria-busy');
                }
            }
        });
    }
});
