// Projects Data Array
const projectsData = [
    {
        id: 1,
        title: "Dhubri Smart Network Phase 1",
        category: "Smart Metering",
        location: "Dhubri, Assam",
        value: "₹500 Cr",
        valueNumeric: 500,
        status: "Ongoing",
        progress: 65,
        client: "APDCL",
        loa: "APDCL/LOA/2024/001",
        date: "Dec 2026",
        desc: "End-to-end implementation of Advanced Metering Infrastructure (AMI) including smart meter physical installation, RF mesh network setup, and HES software integration."
    },
    {
        id: 2,
        title: "Dibrugarh 33/11kV Substation",
        category: "Substation",
        location: "Dibrugarh, Assam",
        value: "₹45 Cr",
        valueNumeric: 45,
        status: "Completed",
        progress: 100,
        client: "APDCL",
        loa: "CGM/PP&D/APDCL/2021/45",
        date: "Mar 2023",
        desc: "Turnkey construction of high capacity 33/11kV electrical substation including all civil works, control room establishment, and switchgear installations."
    },
    {
        id: 3,
        title: "Kamrup Rural Electrification",
        category: "Electrification",
        location: "Kamrup (R), Assam",
        value: "₹120 Cr",
        valueNumeric: 120,
        status: "Completed",
        progress: 100,
        client: "Govt of Assam - DDUGJY",
        loa: "GOA/DDUGJY/2019/88A",
        date: "Oct 2021",
        desc: "Erection of LT/HT lines, DTR installations, and household service connections providing power access to over 50 remote un-electrified villages."
    },
    {
        id: 4,
        title: "Silchar AMI Rollout",
        category: "Smart Metering",
        location: "Cachar, Assam",
        value: "₹380 Cr",
        valueNumeric: 380,
        status: "Ongoing",
        progress: 30,
        client: "APDCL",
        loa: "APDCL/LOA/2024/005",
        date: "Jun 2027",
        desc: "Comprehensive smart meter replacement initiative targeting legacy mechanical and standard digital meters for domestic and commercial consumer bases."
    },
    {
        id: 5,
        title: "Jorhat Feeder Separation",
        category: "Electrification",
        location: "Jorhat, Assam",
        value: "₹85 Cr",
        valueNumeric: 85,
        status: "Ongoing",
        progress: 80,
        client: "APDCL",
        loa: "APDCL/IPDS/2022/11",
        date: "Aug 2025",
        desc: "Separation of agricultural and non-agricultural feeders under IPDS scheme to ensure scheduled power supply to farming sectors while avoiding urban grid stress."
    }
];

// Initialize Everything
document.addEventListener("DOMContentLoaded", () => {
    renderProjects(projectsData);
    initCharts();
    initScrollAnimations();
    setupFilters();
    
    // Modal Close
    const closeBtn = document.getElementById('closeModal');
    if (closeBtn) {
        closeBtn.addEventListener('click', closeModal);
    }
    
    const modal = document.getElementById('projectModal');
    if (modal) {
        modal.addEventListener('click', (e) => {
            if(e.target === modal) closeModal();
        });
    }
});

// Render Project Cards
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
                <span style="color:#fff; font-weight:bold;">${p.value}</span>
            </div>
            <div class="p-progress-bg">
                <div class="p-progress-bar" style="width: 0%;" data-target="${p.progress}%"></div>
            </div>
        `;
        
        grid.appendChild(card);
    });

    // Trigger progress bar animations after paint
    setTimeout(() => {
        document.querySelectorAll('.p-progress-bar').forEach(bar => {
            bar.style.width = bar.getAttribute('data-target');
        });
    }, 100);
}

// Filtering Logic
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

// Modal Logic
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

function closeModal() {
    document.getElementById('projectModal').classList.remove('active');
}

// Scroll Animations
function initScrollAnimations() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if(entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.scroll-anim').forEach(el => observer.observe(el));
}

// Chart.js Setup
function initCharts() {
    const ctxStatusEl = document.getElementById('statusChart');
    const ctxValueEl = document.getElementById('valueChart');
    
    if (!ctxStatusEl || !ctxValueEl) return;

    // Styling constants from CSS
    const neon = '#00f0ff';
    const accent = '#ff0055';
    const completedGreen = '#00ff88';
    const text = '#e2e8f0';

    Chart.defaults.color = '#94a3b8';
    Chart.defaults.font.family = "'Inter', sans-serif";

    // 1. Status Pie Chart
    const ctxStatus = ctxStatusEl.getContext('2d');
    const ongoingCount = projectsData.filter(p => p.status === 'Ongoing').length;
    const completedCount = projectsData.filter(p => p.status === 'Completed').length;

    new Chart(ctxStatus, {
        type: 'doughnut',
        data: {
            labels: ['Ongoing', 'Completed'],
            datasets: [{
                data: [ongoingCount, completedCount],
                backgroundColor: [
                    'rgba(0, 240, 255, 0.2)',
                    'rgba(0, 255, 136, 0.2)'
                ],
                borderColor: [neon, completedGreen],
                borderWidth: 2,
                hoverOffset: 10
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { position: 'bottom' },
                title: { display: true, text: 'Project Execution Status', color: '#fff', font: {size: 16, family: 'Orbitron'} }
            }
        }
    });

    // 2. Value Bar Chart by Category
    const ctxValue = ctxValueEl.getContext('2d');
    
    // Aggregate values
    const catMap = {};
    projectsData.forEach(p => {
        catMap[p.category] = (catMap[p.category] || 0) + p.valueNumeric;
    });

    new Chart(ctxValue, {
        type: 'bar',
        data: {
            labels: Object.keys(catMap),
            datasets: [{
                label: 'Project Value (₹ Crores)',
                data: Object.values(catMap),
                backgroundColor: 'rgba(0, 240, 255, 0.1)',
                borderColor: neon,
                borderWidth: 2,
                borderRadius: 4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: { beginAtZero: true, grid: { color: 'rgba(255,255,255,0.05)' } },
                x: { grid: { display: false } }
            },
            plugins: {
                legend: { display: false },
                title: { display: true, text: 'Portfolio Value by Category', color: '#fff', font: {size: 16, family: 'Orbitron'} }
            }
        }
    });
}
