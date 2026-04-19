const projectsData = [
    {
        id: 0, title: "Smart Metering & Infrastructure", category: "Smart Metering", location: "Malda, Bhagalpur, Sahibganj", value: "\u20B9 280 Lakh", valueNumeric: 2.80, status: "Ongoing", progress: 60, client: "Eastern Railway", loa: "N/A", date: "Ongoing", desc: "Installation of Smart Energy Meters, Infrastructure Design, and System Integration for Eastern Railway (Indian Railways)"
    },
    {
        id: 1, title: "Plastic Park Substation", category: "Substation & Civil", location: "Tinsukia", value: "\u20B9 174.79 Lakh", valueNumeric: 1.74, status: "Completed", progress: 100, client: "APDCL", loa: "N/A", date: "20.12.2016", desc: "2\u00D75 MVA, 33/11 kV substation + control room building"
    },
    {
        id: 2, title: "Barpeta\u2013Howly Line Project", category: "Power Distribution", location: "Barpeta-Howly", value: "\u20B9 124.73 Lakh", valueNumeric: 1.24, status: "Completed", progress: 100, client: "APDCL", loa: "N/A", date: "12.06.2017", desc: "11KV & LT composite line + dismantling"
    },
    {
        id: 3, title: "Nagaon Dhing Feeder R&M", category: "Power Distribution", location: "Nagaon", value: "\u20B9 270.35 Lakh", valueNumeric: 2.70, status: "Completed", progress: 100, client: "APDCL", loa: "N/A", date: "25.11.2016", desc: "33KV line renovation + bay construction"
    },
    {
        id: 4, title: "Abhayapuri Line & Substation", category: "Substation & Civil", location: "Abhayapuri", value: "\u20B9 288.73 Lakh", valueNumeric: 2.88, status: "Completed", progress: 100, client: "APDCL", loa: "N/A", date: "30.06.2019", desc: "11KV lines, substations, LT lines, reconnections"
    },
    {
        id: 5, title: "Rural Electrification (Upper Assam)", category: "Solar Power", location: "Tinsukia, Dibrugarh, Jorhat", value: "\u20B9 2153.11 Lakh", valueNumeric: 21.53, status: "Completed", progress: 100, client: "APDCL", loa: "BOMT Model", date: "28.02.2019", desc: "Solar micro-grid"
    },
    {
        id: 6, title: "Feeder Metering (Jorhat)", category: "Smart Metering", location: "Jorhat", value: "\u20B9 87.08 Lakh", valueNumeric: 0.87, status: "Completed", progress: 100, client: "APDCL", loa: "N/A", date: "28.02.2019", desc: "33KV & 11KV feeder metering"
    },
    {
        id: 7, title: "DTR Metering (Jorhat)", category: "Smart Metering", location: "Jorhat", value: "\u20B9 165.50 Lakh", valueNumeric: 1.65, status: "Completed", progress: 100, client: "APDCL", loa: "N/A", date: "20.03.2019", desc: "DTR Metering Implementation"
    },
    {
        id: 8, title: "DTR Metering (Guwahati Circle-II)", category: "Smart Metering", location: "Guwahati", value: "\u20B9 291.38 Lakh", valueNumeric: 2.91, status: "Completed", progress: 100, client: "APDCL", loa: "N/A", date: "28.02.2019", desc: "DTR Metering Implementation"
    },
    {
        id: 9, title: "SAGY Electrification", category: "Power Distribution", location: "Nagaon", value: "\u20B9 419.00 Lakh", valueNumeric: 4.19, status: "Completed", progress: 100, client: "APDCL", loa: "SAGY Scheme", date: "31.03.2019", desc: "SAGY Electrification"
    },
    {
        id: 10, title: "Urban Electrification (IPDS)", category: "Power Distribution", location: "Kampur & Doboka", value: "\u20B9 858.70 Lakh", valueNumeric: 8.58, status: "Completed", progress: 100, client: "APDCL", loa: "IPDS Scheme", date: "29.11.2019", desc: "Urban Electrification"
    },
    {
        id: 11, title: "Substation Protection", category: "Substation & Civil", location: "Assam (15 SS)", value: "\u20B9 281.04 Lakh", valueNumeric: 2.81, status: "Completed", progress: 100, client: "APDCL", loa: "N/A", date: "Completed", desc: "Feeder metering & transformer protection"
    },
    {
        id: 12, title: "Assam-wide Feeder Metering", category: "Smart Metering", location: "Assam (27 Districts)", value: "\u20B9 350.39 Lakh", valueNumeric: 3.50, status: "Completed", progress: 100, client: "APDCL", loa: "N/A", date: "31.12.2020", desc: "Feeder metering across state"
    },
    {
        id: 13, title: "DTR Metering (Upper Assam)", category: "Smart Metering", location: "Jorhat, Golaghat, Sibsagar", value: "\u20B9 2222.07 Lakh", valueNumeric: 22.22, status: "Completed", progress: 100, client: "APDCL", loa: "N/A", date: "31.12.2020", desc: "DTR Metering Package"
    },
    {
        id: 14, title: "Solar Street Lighting", category: "Solar Power", location: "Assam", value: "\u20B9 102.95 Lakh", valueNumeric: 1.02, status: "Completed", progress: 100, client: "APDCL", loa: "N/A", date: "Completed", desc: "LED Solar Lights + 5-year O&M"
    },
    {
        id: 15, title: "Feeder Metering (Guwahati)", category: "Smart Metering", location: "Guwahati, Rangia, Mangaldoi", value: "\u20B9 537.32 Lakh", valueNumeric: 5.37, status: "Completed", progress: 100, client: "APDCL", loa: "N/A", date: "28.02.2022", desc: "Feeder Metering Implementation"
    },
    {
        id: 16, title: "Feeder Metering (Upper Assam)", category: "Smart Metering", location: "Upper Assam", value: "\u20B9 376.39 Lakh", valueNumeric: 3.76, status: "Completed", progress: 100, client: "APDCL", loa: "N/A", date: "15.01.2021", desc: "Feeder Metering Implementation"
    },
    {
        id: 17, title: "NERPSIP Line Project", category: "Power Distribution", location: "Assam", value: "\u20B9 372.13 Lakh", valueNumeric: 3.72, status: "Completed", progress: 100, client: "APDCL", loa: "NERPSIP Scheme", date: "30.11.2020", desc: "11KV lines (45.67 km + 1.25 km) + panel meters"
    },
    {
        id: 18, title: "Smart Metering (AMI)", category: "Smart Metering", location: "Kokrajhar, Goalpara, Nalbari", value: "\u20B9 11390.00 Lakh", valueNumeric: 113.90, status: "Completed", progress: 100, client: "APDCL", loa: "N/A", date: "30.09.2022", desc: "AMI Smart Metering"
    },
    {
        id: 19, title: "Srikona\u2013Meherpur Line", category: "Power Distribution", location: "Srikona", value: "\u20B9 442.13 Lakh", valueNumeric: 4.42, status: "Completed", progress: 100, client: "APDCL", loa: "N/A", date: "29.03.2024", desc: "14 km 33KV Line"
    },
    {
        id: 20, title: "Smart Prepaid Metering", category: "Smart Metering", location: "Rural Assam", value: "\u20B9 10112.12 Lakh", valueNumeric: 101.12, status: "Ongoing", progress: 97, client: "APDCL", loa: "N/A", date: "05.06.2025", desc: "AMI Smart Prepaid Metering in Azara, Amingaon, etc."
    },
    {
        id: 21, title: "AIIMS Changsari Line", category: "Power Distribution", location: "Changsari", value: "\u20B9 1239.65 Lakh", valueNumeric: 12.39, status: "Completed", progress: 100, client: "APDCL", loa: "N/A", date: "22.05.2022", desc: "33KV overhead + underground cable (16.2 km total)"
    },
    {
        id: 22, title: "Rangia Substation & Line", category: "Substation & Civil", location: "Rangia", value: "\u20B9 5197.00 Lakh", valueNumeric: 51.97, status: "Ongoing", progress: 95, client: "APDCL", loa: "N/A", date: "31.03.2026", desc: "33/11KV substation + lines"
    },
    {
        id: 23, title: "RDSS Electrification", category: "Power Distribution", location: "Nagaon", value: "\u20B9 1436.01 Lakh", valueNumeric: 14.36, status: "Ongoing", progress: 75, client: "APDCL", loa: "RDSS Scheme", date: "28.02.2026", desc: "Electrification of un-electrified households"
    },
    {
        id: 24, title: "Jal Jeevan Mission (Malda)", category: "Civil & Water", location: "West Bengal", value: "\u20B9 520.40 Lakh", valueNumeric: 5.20, status: "Completed", progress: 100, client: "PHED", loa: "N/A", date: "15.08.2023", desc: "Piped water supply and distribution network installation under JJM"
    },
    {
        id: 25, title: "DTR Metering (Kokrajhar)", category: "Smart Metering", location: "Kokrajhar", value: "\u20B9 345.12 Lakh", valueNumeric: 3.45, status: "Completed", progress: 100, client: "APDCL", loa: "N/A", date: "10.11.2023", desc: "Distribution Transformer Metering in Kokrajhar Circle"
    },
    {
        id: 26, title: "Solar Power Generation (Bihar)", category: "Solar Power", location: "Bhagalpur", value: "\u20B9 890.30 Lakh", valueNumeric: 8.90, status: "Completed", progress: 100, client: "BREDA", loa: "N/A", date: "22.12.2023", desc: "Utility-scale grid-connected solar power plant installation"
    },
    {
        id: 27, title: "33/11 KV Substation (Amingaon)", category: "Substation & Civil", location: "Amingaon", value: "\u20B9 1245.00 Lakh", valueNumeric: 12.45, status: "Completed", progress: 100, client: "APDCL", loa: "N/A", date: "05.01.2024", desc: "Construction of 33/11 KV substation with modern grid controls"
    },
    {
        id: 28, title: "Urban Infrastructure (Guwahati)", category: "Civil & Water", location: "Guwahati", value: "\u20B9 312.45 Lakh", valueNumeric: 3.12, status: "Completed", progress: 100, client: "GMC", loa: "N/A", date: "20.02.2024", desc: "Development of urban roads and drainage infrastructure"
    },
    {
        id: 29, title: "Feeder Metering (Silchar)", category: "Smart Metering", location: "Silchar", value: "\u20B9 278.60 Lakh", valueNumeric: 2.78, status: "Completed", progress: 100, client: "APDCL", loa: "N/A", date: "12.03.2024", desc: "Implementation of feeder metering for energy audit"
    },
    {
        id: 30, title: "Power Infrastructure (Sikkim)", category: "Power Distribution", location: "Gangtok", value: "\u20B9 950.00 Lakh", valueNumeric: 9.50, status: "Completed", progress: 100, client: "Sikkim Power Dept", loa: "N/A", date: "30.04.2024", desc: "High altitude power distribution network expansion"
    },
    {
        id: 31, title: "Industrial Wiring Project", category: "Power Distribution", location: "Tinsukia", value: "\u20B9 410.25 Lakh", valueNumeric: 4.10, status: "Completed", progress: 100, client: "Assam Gas Co.", loa: "N/A", date: "15.05.2024", desc: "Industrial electrification and substation wiring"
    },
    {
        id: 32, title: "Substation R&M (Jorhat)", category: "Substation & Civil", location: "Jorhat", value: "\u20B9 620.00 Lakh", valueNumeric: 6.20, status: "Completed", progress: 100, client: "AEGCL", loa: "N/A", date: "01.06.2024", desc: "Renovation and Modernization of 33KV Substations"
    },
    {
        id: 33, title: "Smart Prepaid Metering Phase-II", category: "Smart Metering", location: "Bongaigaon", value: "\u20B9 835.40 Lakh", valueNumeric: 8.35, status: "Completed", progress: 100, client: "APDCL", loa: "N/A", date: "25.07.2024", desc: "Phase-II implementation of Smart Prepaid Meters"
    }
];

document.addEventListener("DOMContentLoaded", () => {
    // Initial sort by value (Highest to Lowest)
    projectsData.sort((a, b) => b.valueNumeric - a.valueNumeric);
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

    function populateCategories() {
        const categories = [...new Set(projectsData.map(p => p.category))];
        catSelect.innerHTML = '<option value="all">All Categories</option>';
        categories.forEach(cat => {
            const opt = document.createElement('option');
            opt.value = cat;
            opt.textContent = cat;
            catSelect.appendChild(opt);
        });
    }
    populateCategories();

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
        const sorted = filtered.sort((a, b) => b.valueNumeric - a.valueNumeric);
        renderProjects(sorted);
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
    
    // Sort keys by value numeric to make bar charts look cooler
    const sortedCats = Object.keys(catMap).sort((a,b) => catMap[b] - catMap[a]);
    const sortedVals = sortedCats.map(c => catMap[c]);

    new Chart(ctxValue, {
        type: 'bar',
        data: {
            labels: sortedCats,
            datasets: [{
                label: 'Project Value (\u20B9 Cr)', data: sortedVals, backgroundColor: 'rgba(255, 102, 0, 0.1)', borderColor: neon, borderWidth: 2, borderRadius: 4
            }]
        },
        options: {
            responsive: true, maintainAspectRatio: false,
            scales: { y: { beginAtZero: true, grid: { color: 'rgba(0,0,0,0.05)' } }, x: { grid: { display: false } } },
            plugins: { legend: { display: false }, title: { display: true, text: 'Portfolio Value by Category', color: '#051424', font: {size: 16, family: 'Orbitron'} } }
        }
    });
}


