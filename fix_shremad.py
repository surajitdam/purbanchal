import codecs
import re

with codecs.open('e:/project/index.html', 'r', 'utf-8') as f:
    idx = f.read()

bad_injection = """                            </div>
                        </div>
                    </div>
                    <div class="card-4 subcard" style="background-image: url('logo/shreemad_industries.jpeg');">
                        <div class="card-heading">Shremad Industries</div>
                        <div class="sustainabilityBoxWrap">
                            <div class="sustainabilityBox1">Food & Beverage<br>Processing</div>
                            <div class="sustainabilityBox2">
                                <h4>Premium Fruit Pulp Exports</h4>
                                <a href="#" class="sustainabilityBtn">View Company</a>
                            </div>
                        </div>
                    </div>
                </div>
            </section>"""

fixed_original = """                            </div>
                        </div>
                    </div>
                </div>
            </section>"""

idx = idx.replace(bad_injection, fixed_original)

# 2. Add Shremad properly AFTER Sach The Reality
pattern = re.compile(r'(<div class="card-3 subcard".*?Sach The Reality.*?</div>\s*</div>\s*</div>)', re.DOTALL)

shremad_html = """
                    <div class="card-4 subcard" style="background-image: url('logo/shreemad_industries.jpeg');">
                        <div class="card-heading">Shremad Industries</div>
                        <div class="sustainabilityBoxWrap">
                            <div class="sustainabilityBox1">Food & Beverage<br>Processing</div>
                            <div class="sustainabilityBox2">
                                <h4>Premium Fruit Pulp Exports</h4>
                                <a href="#" class="sustainabilityBtn">View Company</a>
                            </div>
                        </div>
                    </div>"""

idx = pattern.sub(r'\g<1>' + shremad_html, idx)

with codecs.open('e:/project/index.html', 'w', 'utf-8') as f:
    f.write(idx)

print("SUCCESS")
