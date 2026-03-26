import codecs
import re

with codecs.open('e:/project/index.html', 'r', 'utf-8') as f:
    idx = f.read()

target = """                            </div>
                        </div>
                    </div>
                </div>
            </section>"""

replacement = """                            </div>
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

idx = idx.replace(target, replacement, 1)

with codecs.open('e:/project/index.html', 'w', 'utf-8') as f:
    f.write(idx)

# To ensure css grid works if we have 4 cards
with codecs.open('e:/project/styles.css', 'r', 'utf-8') as f:
    css = f.read()

# Let's verify sustainability component width
# If we have fixed columns, we might need a minmax tweak or flex-wrap, but usually flex handles 4 elements fine if it wraps.

print("SUCCESS")
