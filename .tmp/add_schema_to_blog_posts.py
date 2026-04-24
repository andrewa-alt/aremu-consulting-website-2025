#!/usr/bin/env python3
"""
Add GA4, BreadcrumbList, and BlogPosting schema to all blog posts in lab/
"""
import os
import re
from pathlib import Path

BASE_DIR = Path("/root/website/lab")

# Blog post data extracted from file headers
# Format: filename -> {title, published_time, og_image}
BLOG_POSTS = {
    "agile-support-hidden-backlog-costs-smbs-25k-yearly.html": {
        "title": "Your \"Agile\" Customer Support Is a £25K Ticket Backlog Disaster",
        "published_time": "March 06, 2026",
        "og_image": "https://www.aremuconsulting.com/lab/images/agile-support-hidden-backlog-costs-smbs-25k-yearly.png"
    },
    "automated-invoices-vendor-relationship-disaster.html": {
        "title": "Your \"Automated\" Invoices Are a £40K Vendor Relationship Wrecking Ball",
        "published_time": "March 09, 2026",
        "og_image": "https://www.aremuconsulting.com/lab/images/automated-invoices-vendor-relationship-disaster.jpg"
    },
    "customer-onboarding-emails-churn-costs.html": {
        "title": "Your \"Quick\" Customer Onboarding Emails Are Triggering £30K Churn Bombs",
        "published_time": "March 04, 2026",
        "og_image": "https://www.aremuconsulting.com/lab/images/customer-onboarding-emails-churn-costs.png"
    },
    "email-inbox-automation-smb-liability.html": {
        "title": "The Silent Killer: Why Your Team's Email Inbox Is Your Biggest Business Liability",
        "published_time": "March 02, 2026",
        "og_image": "https://www.aremuconsulting.com/lab/images/email-inbox-automation-smb-liability.png"
    },
    "google-sheets-collaboration-sabotaging-agency.html": {
        "title": "How to Fix Google Sheets Collaboration (Without Switching Tools)",
        "published_time": "2026-02-20T10:00:00Z",
        "og_image": "https://www.aremuconsulting.com/lab/images/image4.png"
    },
    "google-sheets-free-trap.html": {
        "title": "How to Make Google Sheets Work Like a £50k System (For Free)",
        "published_time": "March 1, 2026",
        "og_image": "https://www.aremuconsulting.com/lab/images/image3.png"
    },
    "infallible-inventory-gut-revenue-black-hole.html": {
        "title": "Your \"Infallible\" Inventory Gut Is a £40K+ Revenue Black Hole",
        "published_time": "2026-03-16",
        "og_image": "https://aremuconsulting.com/lab/images/infallible-inventory-gut-revenue-black-hole.png"
    },
    "inventory-sync-failures.html": {
        "title": "Inventory Sync Failures Are Quietly Stealing £8,000/Month From Your Warehouse",
        "published_time": "February 25, 2026",
        "og_image": "https://www.aremuconsulting.com/lab/images/image1.png"
    },
    "lead-qualification-manual-sales-waste-smb.html": {
        "title": "Your \"Smart\" Lead Qualification Is a £25K Sales Time Black Hole",
        "published_time": "March 06, 2026",
        "og_image": "https://www.aremuconsulting.com/lab/images/lead-qualification-manual-sales-waste-smb.png"
    },
    "manual-inventory-cost.html": {
        "title": "The $120,000 Annual Drain: Why Your 'Efficient' Manual Inventory is Actually Costing You",
        "published_time": "February 25, 2026",
        "og_image": "https://www.aremuconsulting.com/lab/images/image3.png"
    },
    "manual-onboarding-turnover-cost-smb.html": {
        "title": "Your \"Streamlined\" Manual Onboarding Is a £30K Turnover Trap for New Hires",
        "published_time": "March 06, 2026",
        "og_image": "https://www.aremuconsulting.com/lab/images/manual-onboarding-turnover-cost-smb.png"
    },
    "multi-user-sheets-team-chaos-costs-smbs-30k-yearly.html": {
        "title": "Your \"Trustworthy\" Multi-User Sheets Are a Gold-Plated Lie Fueling Team Chaos",
        "published_time": "March 04, 2026",
        "og_image": "https://www.aremuconsulting.com/lab/images/multi-user-sheets-team-chaos-costs-smbs-30k-yearly.png"
    },
    "plug-and-play-integrations-silent-assassins.html": {
        "title": "Your \"Plug-and-Play\" Integrations Are Silent Assassins",
        "published_time": "2026-03-23",
        "og_image": "https://aremuconsulting.com/lab/images/plug-and-play-integrations-silent-assassins.png"
    },
    "post-template.html": {
        "title": "{{POST_TITLE}}",
        "published_time": "{{PUBLISH_DATE}}",
        "og_image": "{{POST_IMAGE}}"
    },
    "shopify-inventory-sync-oversell-nightmare.html": {
        "title": "Your \"Reliable\" Shopify Inventory Sync Is a £40K Oversell Nightmare",
        "published_time": "2026-03-18",
        "og_image": "https://aremuconsulting.com/lab/images/shopify-inventory-sync-oversell-nightmare.png"
    },
    "support-team-ticket-avalanche-trap.html": {
        "title": "Your \"Helpful\" Support Team Is a £35K Ticket Avalanche Trap",
        "published_time": "March 11, 2026",
        "og_image": "https://www.aremuconsulting.com/lab/images/support-team-ticket-avalanche-trap.png"
    },
    "why-we-build-on-google-sheets.html": {
        "title": "Why We Build On Google Sheets (Not Replace It)",
        "published_time": "March 1, 2026",
        "og_image": "https://www.aremuconsulting.com/lab/images/image1.png"
    }
}

# Get slug from filename
def get_slug(filename):
    return filename.replace(".html", "")

# GA4 script block
GA4_SCRIPT = """
    <!-- Google Analytics 4 -->
    <script async src='https://www.googletagmanager.com/gtag/js?id=G-AREMUXXXXX'></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-AREMUXXXXX');
    </script>
"""

# BreadcrumbList schema
BREADCRUMB_SCHEMA = """
    <!-- BreadcrumbList Schema -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://www.aremuconsulting.com/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "The Lab",
          "item": "https://www.aremuconsulting.com/lab/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "{title}",
          "item": "https://www.aremuconsulting.com/lab/{slug}.html"
        }
      ]
    }
    </script>
"""

# BlogPosting schema
BLOGPOSTING_SCHEMA = """
    <!-- BlogPosting Schema -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "BlogPosting",
      "headline": "{title}",
      "author": { "@type": "Person", "name": "Leke" },
      "datePublished": "{published_time}",
      "image": "{og_image}",
      "publisher": { "@type": "Organization", "name": "Aremu Consulting" }
    }
    </script>
"""

def add_schema_to_blog_post(filepath, post_data):
    """Add GA4, BreadcrumbList, and BlogPosting schema to a blog post"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    slug = get_slug(filepath.name)
    title = post_data['title']
    published_time = post_data['published_time']
    og_image = post_data['og_image']
    
    # Skip post-template.html as it's a template with placeholders
    if '{{' in title:
        print(f"  Skipping template: {filepath.name}")
        return
    
    # Build the combined schema block
    combined_schema = GA4_SCRIPT + BREADCRUMB_SCHEMA + BLOGPOSTING_SCHEMA
    
    # Replace placeholders
    combined_schema = combined_schema.replace("{title}", title)
    combined_schema = combined_schema.replace("{slug}", slug)
    combined_schema = combined_schema.replace("{published_time}", published_time)
    combined_schema = combined_schema.replace("{og_image}", og_image)
    
    # Find the stylesheet link and add schema after it
    # Pattern varies - look for stylesheet link before </head>
    stylesheet_pattern = r'<link rel="stylesheet" href="../assets/styles.css">'
    
    if stylesheet_pattern in content:
        content = content.replace(stylesheet_pattern, 
            '<link rel="stylesheet" href="../assets/styles.css">' + combined_schema)
    else:
        # Try alternate patterns for different templates
        alt_patterns = [
            r'<link rel="stylesheet" href="assets/styles.css">',
        ]
        for pattern in alt_patterns:
            if pattern in content:
                content = content.replace(pattern,
                    pattern + combined_schema)
                break
        else:
            # Look for the closing </head> tag and insert before it
            if '</head>' in content:
                content = content.replace('</head>', combined_schema + '\n</head>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  Updated: {filepath.name}")

def main():
    print("Adding GA4, BreadcrumbList, and BlogPosting schema to blog posts...")
    
    for filename, post_data in BLOG_POSTS.items():
        filepath = BASE_DIR / filename
        if filepath.exists():
            add_schema_to_blog_post(filepath, post_data)
        else:
            print(f"  Warning: File not found: {filename}")

if __name__ == "__main__":
    main()