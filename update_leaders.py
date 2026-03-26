import codecs
import re

with codecs.open('e:/project/about.html', 'r', 'utf-8') as f:
    about = f.read()

# 1. Remove "Our Story"
story_pattern = re.compile(r'<!-- 3\. OUR STORY -->.*?<!-- 4\. CORE VALUES -->', re.DOTALL)
about = story_pattern.sub('<!-- 4. CORE VALUES -->', about)

# 2. Update Leadership Section
leader_pattern = re.compile(r'<div class="leadership-left">.*?<!-- 6\. OUR TEAM -->', re.DOTALL)

new_leadership = """<div class="leadership-left">
                    <div class="leader-info-box active" id="info-leader-1">
                        <h2>Ravi Pasari</h2>
                        <h4>Managing Director</h4>
                        <p>With visionary leadership, Mr. Ravi Pasari has been the driving force behind our strategic expansion. His unwavering commitment to operational excellence has firmly established Purbanchal Synergies as a premier name in the electrical sector.</p>
                    </div>
                    <div class="leader-info-box" id="info-leader-2">
                        <h2>Amit Kumar Agarwal</h2>
                        <h4>Director</h4>
                        <p>Bringing immense field expertise and technical acumen, Mr. Amit Kumar Agarwal leads execution strategies. His focus on seamless deployment and stringent quality control ensures every project is delivered flawlessly.</p>
                    </div>
                    <div class="leader-info-box" id="info-leader-3">
                        <h2>Aditya Todi</h2>
                        <h4>Board Member</h4>
                        <p>Providing strategic oversight and deep industry insights, Aditya Todi helps shape our future trajectory. His financial and operational guidance ensures stable growth across all our infrastructure portfolios.</p>
                    </div>
                    <div class="leader-info-box" id="info-leader-4">
                        <h2>Sunil Dubey</h2>
                        <h4>Project Head</h4>
                        <p>Leading our extensive on-ground operations, Sunil Dubey manages our large-scale smart metering and EPC deployments. Under his guidance, complex field executions are delivered safely and efficiently.</p>
                    </div>
                </div>
                <!-- Right: Scrolling Photos -->
                <div class="leadership-right">
                    <div class="leader-photo-card" id="card-leader-1" data-id="1">
                        <img src="logo/Ravi_Sir.jpeg" alt="Ravi Pasari">
                    </div>
                    <div class="leader-photo-card" id="card-leader-2" data-id="2">
                        <img src="https://images.unsplash.com/photo-1556157382-97eda2d62296?w=800&q=80" alt="Amit Kumar Agarwal">
                    </div>
                    <div class="leader-photo-card" id="card-leader-3" data-id="3">
                        <img src="https://images.unsplash.com/photo-1560250097-0b93528c311a?w=800&q=80" alt="Aditya Todi">
                    </div>
                    <div class="leader-photo-card" id="card-leader-4" data-id="4">
                        <img src="logo/Sunil_Dubey_sir.jpeg" alt="Sunil Dubey">
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 6. OUR TEAM -->"""

about = leader_pattern.sub(new_leadership, about)

with codecs.open('e:/project/about.html', 'w', 'utf-8') as f:
    f.write(about)

print("SUCCESS")
