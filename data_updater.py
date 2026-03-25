import codecs
import re

# --- 1. update projects.js ---
p_js = '''const projectsData = [
    {
        id: 1, title: "Smart Metering (Uday) Pt-II", category: "Smart Metering", location: "Assam", value: "₹ 113 Cr", valueNumeric: 113, status: "Ongoing", progress: 50, client: "APDCL", loa: "APDCL/CGM(PP&D)/Smart Meter(Uday)-Pt-II/2020/25", date: "7 Year Maintenance", desc: "Scope: 1,34,000 Smart meters. Services: Installation, Commissioning, and Maintenance for 7 years."
    },
    {
        id: 2, title: "AIIB Smart Meter SM-11", category: "Smart Metering", location: "Assam", value: "₹ 101 Cr", valueNumeric: 101, status: "Ongoing", progress: 40, client: "APDCL", loa: "APDCL/CPM (PIU)/AIIB/SMART METER/SM-11/2022/09", date: "7 Year Maintenance", desc: "Scope: 1,86,255 Smart meters. Services: Installation, Commissioning, and Maintenance for 7 years."
    },
    {
        id: 3, title: "Smart Meter (Uday) Pt-II Extension", category: "Smart Metering", location: "Assam", value: "₹ 5.5 Cr", valueNumeric: 5.5, status: "Ongoing", progress: 60, client: "APDCL", loa: "APDCL/CGM(PP&D)Smart Meter (Uday)Pt-II/2022/67", date: "7 Year Maintenance", desc: "Scope: 5500 Smart meters. Services: Installation, Commissioning, and Maintenance for 7 years."
    },
    {
        id: 4, title: "Smart Meter (NSC) 2023/24", category: "Smart Metering", location: "Assam", value: "₹ 1.99 Cr", valueNumeric: 1.99, status: "Ongoing", progress: 80, client: "APDCL", loa: "APDCL/CGM (PP&D)/Smart Meter (NSC)/PE/2023/24", date: "7 Year Maintenance", desc: "Scope: 2220 Smart meters. Services: Installation, Commissioning, and Maintenance for 7 years."
    },
    {
        id: 5, title: "Smart Meter (NSC) 2023/18", category: "Smart Metering", location: "Assam", value: "₹ 1.39 Cr", valueNumeric: 1.39, status: "Completed", progress: 100, client: "APDCL", loa: "APDCL/CGM (PP&D)/Smart Meter (NSC)/PE/2023/18", date: "7 Year Maintenance", desc: "Scope: 1500 Smart meters. Services: Installation, Commissioning, and Maintenance for 7 years."
    },
    {
        id: 6, title: "Smart Meter (NSC) 2023/13", category: "Smart Metering", location: "Assam", value: "₹ 1.79 Cr", valueNumeric: 1.79, status: "Completed", progress: 100, client: "APDCL", loa: "APDCL/CGM (PP&D)/Smart Meter (NSC)/PE/2023/13", date: "7 Year Maintenance", desc: "Scope: 1950 Smart meters. Services: Installation, Commissioning, and Maintenance for 7 years."
    },
    {
        id: 7, title: "Plastic Park TSK Control Room", category: "Substation & Civil", location: "Tinsukia, Assam", value: "₹ 1.75 Cr", valueNumeric: 1.75, status: "Completed", progress: 100, client: "APDCL", loa: "CGM (D)/APDCL/UAR/Plastic Park/TSK/2014/01/35", date: "Completed", desc: "Construction of Assam type Control Room Building."
    },
    {
        id: 8, title: "Solar Home Lighting Systems", category: "Solar Power", location: "Remote Villages, Assam", value: "Undisclosed", valueNumeric: 2, status: "Completed", progress: 100, client: "Dept. of Welfare of Plain Tribes", loa: "Solar/FY21-22", date: "FY 21-22", desc: "Distributed over 6000 Nos of Solar Home Lighting Systems for individuals in backward parts of Assam."
    },
    {
        id: 9, title: "SSA Furniture Supply", category: "Logistics", location: "Assam Schools", value: "Undisclosed", valueNumeric: 3, status: "Completed", progress: 100, client: "Axom Sarba Siksha Abhiyan Mission", loa: "SSA/FY21-22", date: "FY 21-22", desc: "Supplied over 1,89,066 Pairs of Low Height Plastic Chair and Table for students across Assam."
    }
];

document.addEventListener("DOMContentLoaded", () => {
    renderProjects(projectsData);
    initCharts();
    initScrollAnimations();
    setupFilters();
    
    // Modal Close
    const closeBtn = document.getElementById('closeModal');
    if (closeBtn) closeBtn.addEventListener('click', closeModal);
    const modal = document.getElementById('projectModal');
    if (modal) modal.addEventListener('click', (e) => { if(e.target === modal) closeModal(); });
});

function renderProjects(data) {
    const grid = document.getElementById("projectGrid");
    if (!grid) return;
    grid.innerHTML = "";
    if(data.length === 0) {
        grid.innerHTML = `<p style="color:var(--proj-muted); text-align:center; grid-column: 1/-1;">No projects found matching the criteria.</p>`;
        return;
    }
    data.forEach(p => {
        const statusClass = p.status === "Completed" ? "status-completed" : "status-ongoing";
        const card = document.createElement("div");
        card.className = "p-card glass-panel";
        card.onclick = () => openModal(p);
        card.innerHTML = `
            <div class="p-status ${statusClass}">${p.status}</div>
            <h3 class="p-title">${p.title}</h3>
            <div class="p-cat"><i class="fa-solid fa-code-branch"></i> ${p.category}</div>
            <div class="p-info">
                <span><i class="fa-solid fa-location-dot"></i> ${p.location}</span>
                <span style="color:var(--proj-accent); font-weight:bold;">${p.value}</span>
            </div>
            <div class="p-progress-bg">
                <div class="p-progress-bar" style="width: 0%;" data-target="${p.progress}%"></div>
            </div>
        `;
        grid.appendChild(card);
    });
    setTimeout(() => {
        document.querySelectorAll('.p-progress-bar').forEach(bar => {
            bar.style.width = bar.getAttribute('data-target');
        });
    }, 100);
}

function setupFilters() {
    const searchInput = document.getElementById('projSearch');
    const statusSelect = document.getElementById('filterStatus');
    const catSelect = document.getElementById('filterCat');
    if (!searchInput || !statusSelect || !catSelect) return;

    function applyFilters() {
        const term = searchInput.value.toLowerCase();
        const stat = statusSelect.value;
        const cat = catSelect.value;
        const filtered = projectsData.filter(p => {
            const matchesSearch = p.title.toLowerCase().includes(term) || p.location.toLowerCase().includes(term);
            const matchesStatus = stat === 'all' || p.status === stat;
            const matchesCat = cat === 'all' || p.category === cat;
            return matchesSearch && matchesStatus && matchesCat;
        });
        renderProjects(filtered);
    }
    searchInput.addEventListener('input', applyFilters);
    statusSelect.addEventListener('change', applyFilters);
    catSelect.addEventListener('change', applyFilters);
}

function openModal(project) {
    document.getElementById('mTitle').innerText = project.title;
    document.getElementById('mDesc').innerText = project.desc;
    document.getElementById('mClient').innerText = project.client;
    document.getElementById('mValue').innerText = project.value;
    document.getElementById('mLoa').innerText = project.loa;
    document.getElementById('mDate').innerText = project.date;
    document.getElementById('mCatLoc').innerHTML = `<i class="fa-solid fa-layer-group"></i> ${project.category} &nbsp;|&nbsp; <i class="fa-solid fa-location-dot"></i> ${project.location}`;
    const sBadge = document.getElementById('mStatus');
    sBadge.innerText = project.status;
    sBadge.className = "p-status " + (project.status === "Completed" ? "status-completed" : "status-ongoing");
    document.getElementById('projectModal').classList.add('active');
}

function closeModal() { document.getElementById('projectModal').classList.remove('active'); }

function initScrollAnimations() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if(entry.isIntersecting) entry.target.classList.add('visible');
        });
    }, { threshold: 0.1 });
    document.querySelectorAll('.scroll-anim').forEach(el => observer.observe(el));
}

function initCharts() {
    const ctxStatusEl = document.getElementById('statusChart');
    const ctxValueEl = document.getElementById('valueChart');
    if (!ctxStatusEl || !ctxValueEl) return;
    const neon = '#FF6600';
    const accent = '#051424';
    const completedGreen = '#16a34a';
    const text = '#1e293b';
    Chart.defaults.color = '#94a3b8';
    Chart.defaults.font.family = "'Inter', sans-serif";

    const ctxStatus = ctxStatusEl.getContext('2d');
    const ongoingCount = projectsData.filter(p => p.status === 'Ongoing').length;
    const completedCount = projectsData.filter(p => p.status === 'Completed').length;
    new Chart(ctxStatus, {
        type: 'doughnut',
        data: {
            labels: ['Ongoing', 'Completed'],
            datasets: [{
                data: [ongoingCount, completedCount],
                backgroundColor: ['rgba(255, 102, 0, 0.2)', 'rgba(0, 255, 136, 0.2)'],
                borderColor: [neon, completedGreen], borderWidth: 2, hoverOffset: 10
            }]
        },
        options: {
            responsive: true, maintainAspectRatio: false,
            plugins: { legend: { position: 'bottom' }, title: { display: true, text: 'Project Execution Status', color: '#051424', font: {size: 16, family: 'Orbitron'} } }
        }
    });

    const ctxValue = ctxValueEl.getContext('2d');
    const catMap = {};
    projectsData.forEach(p => { catMap[p.category] = (catMap[p.category] || 0) + p.valueNumeric; });
    new Chart(ctxValue, {
        type: 'bar',
        data: {
            labels: Object.keys(catMap),
            datasets: [{
                label: 'Project Value (₹ Crores)', data: Object.values(catMap), backgroundColor: 'rgba(255, 102, 0, 0.1)', borderColor: neon, borderWidth: 2, borderRadius: 4
            }]
        },
        options: {
            responsive: true, maintainAspectRatio: false,
            scales: { y: { beginAtZero: true, grid: { color: 'rgba(0,0,0,0.05)' } }, x: { grid: { display: false } } },
            plugins: { legend: { display: false }, title: { display: true, text: 'Portfolio Value by Category', color: '#051424', font: {size: 16, family: 'Orbitron'} } }
        }
    });
}
'''
with codecs.open('e:/project/projects.js', 'w', 'utf-8') as f:
    f.write(p_js)

# --- 2. Update about.html ---
with codecs.open('e:/project/about.html', 'r', 'utf-8') as f:
    about = f.read()

about = about.replace("Purbanchal Synergies Pvt. Ltd. is a leading infrastructure enterprise committed to executing large-scale, transformative projects across the region.", "Purbanchal Synergies Pvt. Ltd. (Formerly Purbanchal Enterprise), Guwahati, is an electrical services provider and business liaison company. We work with corporates, SMEs, and individuals.")
about = about.replace("“With decades of collective leadership expertise, we specialize in delivering robust solutions that bridge critical infrastructure capability gaps.”", "“With our extensive knowledge and 20 years of experience, we have secured a strong position in the electrical market, specializing in turnkey solutions towards HT line and Substation work.”")
about = about.replace("We are proudly multi-sector, focusing on energy, utilities, manufacturing, and bringing modern execution to challenging domains. We build the foundations for a resilient tomorrow.", "Our average turnover for the last three years is over 70 crore, consistently increasing year on year. We are the largest and oldest master stockist and channel partner for Larsen & Toubro and Landis+Gyr.")

with codecs.open('e:/project/about.html', 'w', 'utf-8') as f:
    f.write(about)

# --- 3. Update services.html ---
with codecs.open('e:/project/services.html', 'r', 'utf-8') as f:
    srv = f.read()

srv = srv.replace("Comprehensive deployment, integration, and management of Advanced Metering Infrastructure for modern grids.", "Successfully installed and commissioned over 1.5 lakh smart meters with RF modules. Currently boast a robust pipeline exceeding 2.5 lakh meters with SLA > 99%.")
srv = srv.replace("Building robust 33/11kV substations, rural electrification lines, and enhancing grid reliability across difficult terrains.", "Executing Turnkey Solutions for high quality HT lines, Substations, DT Metering and Feeder Metering projects of APDCL.")
srv = srv.replace("Utility-scale solar farms and life-changing rural solar micro-grids designed for longevity and high efficiency.", "Distributed over 6000 nos of Solar Home Lighting Systems. We set up solar power plants and micro-grids for numerous remote un-electrified villages.")

srv = srv.replace("fa-faucet-drip", "fa-truck-fast")
srv = srv.replace("Civil & Water Infrastructure", "Logistics & Supply")
srv = srv.replace("From Jal Jeevan Mission pipelines to overhead tanks and fundamental civil projects empowering communities.", "Leading supplier to Axom Sarba Siksha Abhiyan Mission supplying over 1.8 Lakh furniture units, and master stockist for top electrical brands.")

with codecs.open('e:/project/services.html', 'w', 'utf-8') as f:
    f.write(srv)

# --- 4. Update index.html ---
with codecs.open('e:/project/index.html', 'r', 'utf-8') as f:
    idx = f.read()

idx = re.sub(r'data-target="23"([^>]*?)>23\+</div>\s*<p>Major Projects</p>', r'data-target="20"\1>20+</div>\n                        <p>Years Experience</p>', idx)
idx = re.sub(r'data-target="498"([^>]*?)>498 Cr</div>\s*<p>Evaluated Project Value</p>', r'data-target="70" data-suffix=" Cr+"\1>70 Cr+</div>\n                        <p>Average Yearly Turnover</p>', idx)
idx = re.sub(r'data-target="500000"([^>]*?)>5,00,000\+</div>\s*<p>Smart Meters Installed</p>', r'data-target="150000" data-suffix="+"\1>1,50,000+</div>\n                        <p>Smart Meters Installed</p>', idx)
idx = re.sub(r'data-target="1000000"([^>]*?)>10,00,000\+</div>\s*<p>Non Smart Meters Delivered</p>', r'data-target="250000" data-suffix="+"\1>2,50,000+</div>\n                        <p>Smart Meter Pipeline</p>', idx)

idx = idx.replace("Purbanchal Synergies Pvt. Ltd. is a <b>multi-sector</b> infrastructure", "Purbanchal Synergies Pvt. Ltd. is a <b>leading</b> infrastructure")
idx = idx.replace("delivering <b>high-quality execution</b> across energy, utilities", "with over <b>20 years of experience</b> across energy, utilities")
idx = idx.replace("We build the foundations for a <b>resilient\n                                                tomorrow</b>.", "We aspire to shift to the next orbit and be a front runner in implementing the <b>Smart Grid</b> vision in India.")
idx = idx.replace("We build the foundations for a <b>resilient tomorrow</b>.", "We aspire to shift to the next orbit and be a front runner in implementing the <b>Smart Grid</b> vision in India.")

with codecs.open('e:/project/index.html', 'w', 'utf-8') as f:
    f.write(idx)

print("SUCCESS")
