import codecs

try:
    with codecs.open('e:/project/index.html', 'r', 'utf-8') as f:
        idx = f.read()

    # Rhino Moulders updates
    idx = idx.replace("<div class=\"sustainabilityBox1\">Manufacturing<br>Excellence</div>", 
                    "<div class=\"sustainabilityBox1\">Top Manufacturer<br>>10Cr Turnover | 1000 KVA</div>")
    idx = idx.replace("<h4>Distribution Transformers & Plastic Utilities</h4>", 
                    "<h4>Distribution Transformers & Injection Moulding</h4>")
    
    # Rhino Electricals (replacing Shremad Industries)
    idx = idx.replace("<div class=\"card-2 subcard\" style=\"background-image: url('logo/shreemad_industries.jpeg');\">", 
                    "<div class=\"card-2 subcard\" style=\"background-image: url('https://images.unsplash.com/photo-1558449028-b53a39d100fc?w=800&q=80');\">")
    idx = idx.replace("<div class=\"card-heading\">Shremad Industries</div>", 
                    "<div class=\"card-heading\">Rhino Electricals</div>")
    idx = idx.replace("<div class=\"sustainabilityBox1\">Food & Beverage<br>Processing</div>", 
                    "<div class=\"sustainabilityBox1\">Est. Aug 1988<br>Largest Stockist</div>")
    idx = idx.replace("<h4>Premium Fruit Pulp Exports</h4>", 
                    "<h4>NE Region's First Experience Center</h4>")
    
    # Replace the FIRST 'View Company' with Rhino Moulders capacity, and SECOND with Rhino Electricals
    idx = idx.replace("<a href=\"#\" class=\"sustainabilityBtn\">View Company</a>", 
                    "<span class=\"sustainabilityBtn\">60+ Tons Capacity</span>", 1)
    
    idx = idx.replace("<a href=\"#\" class=\"sustainabilityBtn\">View Company</a>", 
                    "<a href=\"https://www.rhinoelectricals.com\" target=\"_blank\" class=\"sustainabilityBtn\">Visit Store</a>", 1)

    with codecs.open('e:/project/index.html', 'w', 'utf-8') as f:
        f.write(idx)
    print("SUCCESS")
except Exception as e:
    print(e)
