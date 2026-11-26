"""Build a dependency-free academic website. Run: python build.py"""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parent
DIST = ROOT
ORIGIN = 'https://rezart1427.github.io'

PUBLICATIONS = [
    {
        'year': '2026',
        'title': 'A threshold-sensitive framework for tracking hypoxia recurrence across coastal ecosystems',
        'authors': 'Reza Badpa, Sultan Hameed, and Kamazima M. M. Lwiza',
        'journal': 'Ecological Indicators, 193, 115859',
        'doi': '10.1016/j.ecolind.2026.115859',
    },
    {
        'year': '2026',
        'title': 'Application of causal discovery of factors driving dissolved oxygen in estuarine environments',
        'authors': 'Reza Badpa and Kamazima M. M. Lwiza',
        'journal': 'Journal of Environmental Sciences, 168, 479–493',
        'doi': '10.1016/j.jes.2025.11.024',
    },
    {
        'year': '2024',
        'title': 'Geospatial investigation on self-purification capacity of river estuaries in the Caspian region: reducing heavy metals pollution',
        'authors': 'Ali Marefat, Soheil Asgari, Reza Badpa, Mina Jahanirad, Masoud Sagheb Molaei, and Abdolreza Karbassi',
        'journal': 'npj Clean Water, 7, 32',
        'doi': '10.1038/s41545-024-00327-4',
    },
    {
        'year': '2023',
        'title': 'Enhancement of flocculation processes of metals during estuarine mixing by electrodes',
        'authors': 'S. Asgari, Reza Badpa, R. Jokar, A. Lombar, and A. Karbassi',
        'journal': 'Journal of Water Process Engineering, 56, 104496',
        'doi': '10.1016/j.jwpe.2023.104496',
    },
    {
        'year': '2021',
        'title': 'A review on the various beds used for immobilization of nanoparticles: Overcoming the barrier to nanoparticle applications in water and wastewater treatment',
        'authors': 'P. Alipour, Reza Badpa, V. Aghabalaee, and M. Baghdadi',
        'journal': 'Journal of Environmental Chemical Engineering, 9(6), 106514',
        'doi': '10.1016/j.jece.2021.106514',
    },
    {
        'year': '2016',
        'title': 'Hydrostatic and hydrodynamic behavior of floating dock',
        'authors': 'Reza Badpa and A. Ghasemi',
        'journal': 'Studies Geography, Civil Engineering, and Urban Management, 2(1)',
    },
]

MANUSCRIPTS = [
    ('Under review', 'Transition-aware forecasting improves early-warning diagnostics for coastal hypoxia', 'Reza Badpa, Hendrik F. Hamann, and Kamazima M. M. Lwiza'),
    ('In preparation', 'Stratification-dependent daily evolution of bulk shear in Long Island Sound', 'Reza Badpa and Kamazima M. M. Lwiza'),
    ('In preparation', 'Climatic prediction of dissolved oxygen in Long Island Sound', 'Kamazima M. M. Lwiza and Reza Badpa'),
]

PRESENTATIONS = [
    ('2026', 'Beyond Potential Energy Anomaly: Learning the Stratification State Space of Western Long Island Sound with a Physics-Guided Autoencoder', 'Reza Badpa and Kamazima Lwiza', 'Physics of Estuaries and Coastal Seas (PECS), Portland, Maine, USA', 'Talk'),
    ('2025', 'Forecasting Bottom Dissolved Oxygen in Long Island Sound', '', 'Science and Technical Advisory Committee (STAC), Stony Brook, New York, USA', 'Talk'),
    ('December 2025', 'Hypoxia Risk Mapping in Eastern US Estuaries Using Extreme Value', 'Reza Badpa and Kamazima Lwiza', 'AGU Ocean Science Meeting, New Orleans, Louisiana, USA', 'Poster'),
    ('December 2025', 'Causal Relationships Between Water-Column Dynamics and Bottom Dissolved Oxygen', 'Reza Badpa and Kamazima Lwiza', 'AGU Ocean Science Meeting, New Orleans, Louisiana, USA', 'Poster'),
    ('2025', 'Comparison of AI classification methods in identifying factors influencing hypoxia in Long Island Sound', 'A. Palomino, D. Nelson, D. Lewis, Reza Badpa, and Kamazima Lwiza', 'URECA, Stony Brook, New York, USA', 'Poster'),
    ('2024', 'Causal Discovery of Water-column Properties with Bottom Dissolved Oxygen', 'Reza Badpa and Kamazima Lwiza', 'Annual National Estuary Program meeting, Stony Brook University', ''),
    ('2019', 'Global marine climate change and its main indicators', 'A. Gohari and Reza Badpa', '3rd International Conference on Architecture, Civil Engineering, Agriculture and the Environment, Sofia, Bulgaria', 'Poster'),
    ('2019', 'A Review of Tidal Power Resource Evaluation for Tidal Barrage', 'Reza Badpa, A. Gohari, and A. Ghasemi', '5th International Conference on Environmental Engineering and Natural Resource, Tehran, Iran', 'Talk'),
]

def author_text(text):
    return escape(text).replace('Reza Badpa', '<strong>Reza Badpa</strong>')

def publication(p, compact=False):
    title = escape(p['title'])
    if p.get('doi'):
        title = f'<a href="https://doi.org/{p["doi"]}">{title}</a>'
    authors = '' if compact else f'<p class="authors">{author_text(p["authors"])}</p>'
    doi = f'<a class="doi" href="https://doi.org/{p["doi"]}">DOI: {p["doi"]}</a>' if p.get('doi') and not compact else ''
    return f'<li class="publication"><span class="entry-date">{p["year"]}</span><div><h3>{title}</h3>{authors}<p class="journal">{escape(p["journal"])}</p>{doi}</div></li>'

def record(date, title, body):
    return f'<li class="record"><span class="entry-date">{date}</span><div><h3>{title}</h3>{body}</div></li>'

def presentation(date, title, authors, venue, kind):
    byline = f'<p class="authors">{author_text(authors)}</p>' if authors else ''
    label = f'{escape(kind)} · ' if kind else ''
    return record(escape(date), escape(title), f'{byline}<p class="journal">{label}{escape(venue)}</p>')

HOME = '''
<div class="intro">
  <p class="eyebrow">Physical oceanography · Coastal science · Machine Learning</p>
  <h1>Hi, I’m Reza Badpa.</h1>
  <p>I am a Ph.D. candidate in Physical Oceanography at <a href="https://www.stonybrook.edu/">Stony Brook University</a>’s <a href="https://www.stonybrook.edu/somas/">School of Marine and Atmospheric Sciences</a> in Stony Brook, NY.</p>
  <p>My research examines how coastal circulation, stratification, and mixing shape dissolved oxygen and hypoxia in estuaries. I combine physical oceanography, hydrodynamic modeling, and machine learning to understand these processes and improve coastal oxygen predictions. We also developed the Hypoxia Recurrence Risk Indicator (HRRI) to track how often low-oxygen conditions recur across coastal ecosystems, accounting for sensitivity to oxygen thresholds and uncertainty in risk classification.</p>
  <p>Much of my current work focuses on Long Island Sound, from identifying the physical and biogeochemical drivers of bottom-water oxygen to developing forecasts that capture the onset and recovery of hypoxia. I also study how low-oxygen conditions recur across U.S. coastal ecosystems.</p>
  <p>Feel free to shoot me an email at <a href="mailto:reza.badpa@stonybrook.edu">reza.badpa@stonybrook.edu</a>.</p>
</div>
<section aria-labelledby="research-heading">
  <h2 id="research-heading">Research interests</h2>
  <div class="research-item"><h3>Coastal dynamics and mixing</h3><p>Stratification, bulk shear, and circulation in estuaries, using hydrodynamic simulations and observations to examine changes in the water column.</p></div>
  <div class="research-item"><h3>Dissolved oxygen and hypoxia</h3><p>Causal discovery, extreme-value analysis, and recurrence indicators to understand the drivers and spatial patterns of low-oxygen conditions.</p></div>
  <div class="research-item"><h3>Physics-guided machine learning</h3><p>Neural networks, autoencoders, and forecasting models that connect coastal physical processes with predictions of oxygen and state transitions.</p></div>
</section>
<section aria-labelledby="selected-heading">
  <div class="section-top"><h2 id="selected-heading">Selected publications</h2><a href="publications/">All publications</a></div>
  <ul class="entries">''' + ''.join(publication(p, True) for p in PUBLICATIONS[:2]) + '''</ul>
</section>
'''

CV = '''
<p class="eyebrow">Background & experience</p>
<h1>Curriculum Vitae</h1>
<p class="page-lead">Physical oceanography, coastal dynamics, and data-driven approaches to estuarine water quality.</p>
<div class="page-actions"><a class="button" href="../assets/Reza-Badpa-CV.pdf" download>Download full CV <span>(PDF)</span></a><button class="text-button" type="button" data-print>Print this page</button></div>
<section aria-labelledby="education"><h2 id="education">Education</h2><ul class="entries">
''' + record('2023–present', 'Ph.D. candidate in Physical Oceanography', '<p>Stony Brook University · School of Marine and Atmospheric Sciences</p><p class="detail">Advisor: Dr. Kamazima Lwiza<br>Thesis: <em>Integrating Coastal Dynamics with Physics-guided Neural Networks for Dissolved Oxygen Prediction</em><br>Expected defense: Spring 2027 · Expected conferral: May 2027</p>') + record('2020', 'M.Sc. in Environmental Engineering — Coastal', '<p>University of Tehran, College of Engineering, Iran</p><p class="detail">Advisor: Dr. Masoud Sadrinasab</p>') + record('2011', 'B.Sc. in Civil Engineering', '<p>Shahrood University of Technology, College of Engineering, Iran</p>') + '''</ul></section>
<section aria-labelledby="experience"><h2 id="experience">Research experience</h2><ul class="entries">
''' + record('2026', 'Stratification and shear in Long Island Sound', '<p>Analyzed potential energy anomaly, stratification, and bulk shear from a multidecadal 3-D hindcast. Developed a block-balanced autoencoder and recurrent-state identification to examine physical-state transitions and their seasonal dependence.</p>') + record('2026', 'Hydrodynamics of Oyster Bay', '<p>Developed a 3-D Delft3D-FM model of circulation, salinity, temperature, and bottom shear and examined their relationship with sediment and shellfish distributions.</p>') + record('2025–2026', 'Dissolved oxygen and hypoxia forecasting', '<p>Developed and benchmarked tree-based and transformer-based models, Ridge autoregression, and persistence baselines for multi-horizon forecasts, evaluated using oxygen thresholds and state transitions.</p>') + record('2025', 'Coastal hypoxia recurrence', '<p>Applied non-stationary generalized extreme-value models and return-period analysis across four U.S. coastal systems. Developed the Hypoxia Recurrence Risk Indicator (HRRI) to quantify recurrence, threshold sensitivity, and classification uncertainty.</p>') + record('2024–2025', 'Causal drivers of bottom-water oxygen', '<p>Used PCMCI+ causal discovery, lagged conditional-independence testing, nonlinear forcing transformations, feature selection, OLS, and LASSO to identify physical and biogeochemical controls in Long Island Sound.</p>') + record('2023–2024', 'Lake Turkana circulation', '<p>Used a 3-D ROMS model to investigate circulation and water-column dynamics.</p>') + record('2018–2020', 'Coastal modeling and marine energy', '<p>Modeled tides and currents in Musa Bay to evaluate tidal-lagoon energy; used SWAN to examine wave-energy resources under climate scenarios; and simulated the 2018 Arvand River flood and its plume in the northern Persian Gulf.</p>') + '''</ul></section>
<section aria-labelledby="field"><h2 id="field">Field experience</h2><ul class="entries">
''' + record('July 2024', 'R/V Connecticut · Mid-Atlantic Bight', '<p>Three-day cruise deploying moorings and water-column profilers.</p>') + record('October 2023', 'R/V Connecticut · MABIWs', '<p>Recovery of moorings and instrumentation across the Mid-Atlantic Bight shelf.</p>') + record('July 2023', 'R/V Connecticut · MABIWs', '<p>Four-day cruise deploying T-string moorings, bottom landers, and profilers, and supporting adaptive internal-wave surveys.</p>') + record('November 2019', 'Musa Bay · Persian Gulf', '<p>Two-day survey conducting CTD profiles of temperature, salinity, and pressure.</p>') + '''</ul></section>
<section aria-labelledby="teaching"><h2 id="teaching">Teaching and mentoring</h2>
<h3 class="subheading">Teaching assistant</h3>
<ul class="plain-list"><li><strong>Physics (PHY 119)</strong>, Stony Brook University, Spring 2023 and Spring 2024. Instructor: Erlend Graf.</li><li><strong>Marine Environmental Modeling</strong>, University of Tehran, Spring 2019. Instructor: Masoud Sadrinasab.</li><li><strong>Numerical Computations</strong>, Shahrood University of Technology, Spring 2010. Instructor: Hojjat Ahsani Tehrani.</li></ul>
<h3 class="subheading">Research mentoring</h3>
<p>Mentored undergraduate and graduate research on AI classification of hypoxia drivers, dissolved oxygen prediction using satellite and ship-survey data, CNN and RNN forecasting, and metal flocculation during estuarine mixing. Student projects have been presented through URECA and EarthBUS, with the flocculation research published as a journal article.</p>
</section>
<section aria-labelledby="skills"><h2 id="skills">Technical skills</h2>
<dl class="skills"><dt>Programming</dt><dd>Python, MATLAB, Linux, MPI parallel computing</dd><dt>Ocean and coastal models</dt><dd>Delft3D-FM, ROMS, SWAN</dd><dt>Machine learning</dt><dd>Tree-based models, convolutional neural networks, transformers, autoencoders</dd><dt>Data and workflows</dt><dd>Large geospatial datasets, automated analysis, remote computing, conda, pip, Jupyter, Spyder</dd></dl>
</section>
<section><h2>Publications and presentations</h2><p>See the <a href="../publications/">publications page</a> for journal articles, manuscripts, and conference presentations.</p></section>
'''

PUBS = '''
<p class="eyebrow">Articles & presentations</p>
<h1>Publications</h1>
<p class="page-lead">Research on coastal hypoxia, estuarine dynamics, machine learning, and water quality.</p>
<nav class="jump-links" aria-label="Publication sections"><a href="#published">Published</a><a href="#manuscripts">Manuscripts</a><a href="#presentations">Presentations</a></nav>
<section aria-labelledby="published"><h2 id="published">Published articles</h2><ul class="entries publications">''' + ''.join(publication(p) for p in PUBLICATIONS) + '''</ul></section>
<section aria-labelledby="manuscripts"><h2 id="manuscripts">Manuscripts</h2><ul class="entries">
''' + ''.join(record(escape(status), escape(title), f'<p class="authors">{author_text(authors)}</p>') for status,title,authors in MANUSCRIPTS) + '''</ul></section>
<section aria-labelledby="presentations"><h2 id="presentations">Presentations</h2><ul class="entries">''' + ''.join(presentation(*p) for p in PRESENTATIONS) + '''</ul></section>
'''

ICON = {
    'pin': '<path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 1 1 16 0Z"/><circle cx="12" cy="10" r="2.5"/>',
    'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 6 9 7 9-7"/>',
    'github': '<path d="M9 19c-4 1-4-2-6-2m12 5v-4a3.4 3.4 0 0 0-1-2.6c3.3-.4 6.8-1.6 6.8-7.2A5.6 5.6 0 0 0 19.3 4a5.1 5.1 0 0 0-.1-4S18 0 15 1.6a14 14 0 0 0-6 0C6 0 4.8 0 4.8 0a5.1 5.1 0 0 0-.1 4 5.6 5.6 0 0 0-1.5 4.2c0 5.6 3.5 6.8 6.8 7.2A3.4 3.4 0 0 0 9 18v4" transform="translate(0 1) scale(.9)"/>',
    'orcid': '<circle cx="12" cy="12" r="9"/><path d="M8 10v7m0-10h.01M12 10h2a3.5 3.5 0 0 1 0 7h-2Z"/>',
    'researchgate': '<path d="M6 19V5h5a4 4 0 0 1 0 8H6m5 0 7 6M17 4h4v4"/>',
    'scholar': '<path d="m2 9 10-5 10 5-10 5ZM6 11v6q6 4 12 0v-6m4-2v7"/>',
}

def icon(name):
    return f'<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{ICON[name]}</svg>'

def shell(key, title, content, prefix, page_path=''):
    nav = ''.join(f'<a href="{prefix}{href}"'+(' aria-current="page"' if key==n else '')+f'>{label}</a>' for n,href,label in [('home','', 'Home'),('cv','cv/','CV'),('publications','publications/','Publications')])
    description = 'Reza Badpa is a Ph.D. candidate in Physical Oceanography at Stony Brook University, studying coastal dynamics, dissolved oxygen, hypoxia, and physics-guided machine learning.'
    schema = json.dumps({'@context':'https://schema.org','@type':'Person','name':'Reza Badpa','jobTitle':'Ph.D. candidate in Physical Oceanography','affiliation':{'@type':'CollegeOrUniversity','name':'Stony Brook University'},'email':'mailto:reza.badpa@stonybrook.edu','sameAs':['https://github.com/rezart1427','https://orcid.org/0000-0003-4790-7120','https://www.researchgate.net/profile/Reza-Badpa','https://scholar.google.com/citations?user=OhGCAvgAAAAJ&hl=en']})
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | Reza Badpa</title><meta name="description" content="{description}"><meta name="theme-color" content="#176575">
<link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{prefix}assets/style.css">
<meta property="og:type" content="website"><meta property="og:title" content="{title} | Reza Badpa"><meta property="og:description" content="{description}"><meta property="og:url" content="{ORIGIN}/{page_path}">
<script type="application/ld+json">{schema}</script><script defer src="{prefix}assets/site.js"></script></head>
<body><a class="skip-link" href="#main">Skip to content</a>
<header class="masthead"><div class="header-inner"><a class="site-name" href="{prefix}">Reza Badpa</a><nav aria-label="Main navigation">{nav}</nav></div></header>
<div class="layout"><aside class="profile" aria-label="About Reza Badpa">
<a class="profile-mark" href="{prefix}" aria-label="Reza Badpa home"><img src="{prefix}assets/reza-badpa-profile.png" alt="Reza Badpa" width="1536" height="1024" decoding="async"></a>
<div class="profile-copy"><h2>Reza Badpa</h2><p class="role">Ph.D. candidate<br> Physical Oceanography</p><p class="affiliation">School of Marine and<br> Atmospheric Sciences<br> Stony Brook University</p>
<ul class="profile-links"><li>{icon('pin')}<span>Stony Brook, New York</span></li><li><a href="mailto:reza.badpa@stonybrook.edu">{icon('mail')}Email</a></li><li><a href="https://github.com/rezart1427">{icon('github')}GitHub</a></li><li><a href="https://orcid.org/0000-0003-4790-7120">{icon('orcid')}ORCID</a></li><li><a href="https://www.researchgate.net/profile/Reza-Badpa">{icon('researchgate')}ResearchGate</a></li><li><a href="https://scholar.google.com/citations?user=OhGCAvgAAAAJ&amp;hl=en">{icon('scholar')}Google Scholar</a></li></ul></div>
</aside><main id="main" tabindex="-1">{content}</main></div>
<footer><div class="footer-inner"><p>© 2026 Reza Badpa</p><p>Physical oceanography · Stony Brook University</p></div></footer>
</body></html>'''

def build():
    for key,title,content,rel,prefix in [
        ('home','Home',HOME,'index.html','./'),
        ('cv','Curriculum Vitae',CV,'cv/index.html','../'),
        ('publications','Publications',PUBS,'publications/index.html','../'),
    ]:
        target = DIST / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(shell(key,title,content,prefix,rel.replace('index.html','')),encoding='utf-8')
    (DIST / '.nojekyll').touch()
    (DIST / '404.html').write_text(shell('', 'Page not found', '<h1>Page not found</h1><p>The page you’re looking for may have moved. Return to the <a href="/">home page</a>.</p>', '/'), encoding='utf-8')
    print('Built Home, CV, Publications, and 404 pages in dist/.')

if __name__ == '__main__':
    build()
