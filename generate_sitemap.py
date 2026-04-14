import os
import datetime

base_url = 'https://mywintercar.com'
path = r'd:\Antigravity\MyWinterCar.com'

ignore = ['guia.html']
current_date = datetime.datetime.now().strftime('%Y-%m-%d')

priorities = {
    '/': '1.0',
    '/wiki': '0.9',
    '/guides': '0.9',
    '/car-build-guide': '0.9',
    '/about': '0.5',
    '/contact': '0.5',
    '/faq': '0.6'
}

urls = []
for file in os.listdir(path):
    if file.endswith('.html') and file not in ignore:
        name = file[:-5]
        if name == 'index':
            loc_path = '/'
            loc_full = base_url + '/'
        else:
            loc_path = '/' + name
            loc_full = base_url + loc_path
            
        priority = priorities.get(loc_path, '0.8')
        changefreq = 'weekly'
        if priority == '0.5' or priority == '0.6':
            changefreq = 'monthly'
        elif priority == '1.0':
            changefreq = 'daily'
            
        urls.append({
            'loc': loc_full,
            'lastmod': current_date,
            'changefreq': changefreq,
            'priority': priority
        })

urls.sort(key=lambda x: x['priority'], reverse=True)

with open(os.path.join(path, 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n\n')
    for u in urls:
        f.write('  <url>\n')
        f.write(f'    <loc>{u["loc"]}</loc>\n')
        f.write(f'    <lastmod>{u["lastmod"]}</lastmod>\n')
        f.write(f'    <changefreq>{u["changefreq"]}</changefreq>\n')
        f.write(f'    <priority>{u["priority"]}</priority>\n')
        f.write('  </url>\n')
    f.write('\n</urlset>\n')
    
print('sitemap.xml updated with ' + str(len(urls)) + ' urls.')
