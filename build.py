from pathlib import Path
from html import escape


SITE_ROOT = Path(__file__).parent
HEADER = SITE_ROOT / "templates" / "header.html"
FOOTER = SITE_ROOT / "templates" / "footer.html"
PROJECT_CARD = SITE_ROOT / "templates" / "project.html"
GALLERY = SITE_ROOT / "templates" / "gallery.html"

PAGES = {
    "index.html": ("About Me", "Homepage"),
    "pages/education.html": ("Education", "Education"),
    "pages/research.html": ("Research", "Research"),
    "pages/projects.html": ("Projects", "Projects"),
    "pages/SDmonitoring.html": ("SD Monitoring", "Projects"),
    "pages/sFLASH.html": ("sFLASH", "Projects"),
    "pages/TALEML.html": ("TALEML", "Projects"),
    "pages/trinity.html": ("Trinity", "Projects"),
    "pages/UHECR_energy_spec.html": ("UHECR Energy Spectrum w/ TAx4", "Projects"),
}

PROJECTS = [
    {
        "title": "Comic Ray Species Identification with Machine Learning",
        "url": "TALEML.html",
        "dates": "November, 2023 - Present",
        "description": "TALE extends cosmic ray detection down to energies of 10 PeV. I am studying whether reconstructed shower parameters can identify the primary cosmic ray in Monte Carlo data.",
    },
    {
        "title": "Trinity: High Energy Neutrino Detector",
        "url": "trinity.html",
        "dates": "May, 2022 - October, 2023",
        "description": "The Trinity demonstrator searches for upward-going air showers created by earth-skimming ultra-high-energy neutrinos.",
    },
    {
        "title": "Ultra-High Energy Cosmic Ray Energy Spectrum using Hybrid Analysis with TAx4",
        "url": "UHECR_energy_spec.html",
        "dates": "August, 2017 - May, 2022",
        "description": "My thesis research used Telescope Array surface and fluorescence detector data to calculate the first TAx4 hybrid cosmic ray energy spectrum.",
    },
    {
        "title": "Surface Detector Monitoring",
        "url": "SDmonitoring.html",
        "dates": "August, 2016 - May, 2022",
        "description": "I developed tools to compare daily surface detector errors with the access list and supported detector maintenance in the field.",
    },
    {
        "title": "sFLASH Measurement of Fluorescence Yield at SLAC",
        "url": "sFLASH.html",
        "dates": "August, 2016 - May, 2018",
        "description": "The sFLASH experiment measured air fluorescence yield and its dependence on shower development at SLAC National Accelerator Laboratory.",
    },
]

PHOTOS = [
    {
        "src": "../assets/images/SLAC/20160730_000754.jpg",
        "alt": "sFLASH collaboration watching data in the End Station A control room",
        "caption": "Watching data arrive during the first sFLASH experiment.",
    },
    {
        "src": "../assets/images/potts_defense.jpg",
        "alt": "Mathew Potts at his Ph.D. defense",
        "caption": "Ph.D. defense, April 15, 2022.",
    },
    {
        "src": "../assets/images/MD_Mirrors.jpg",
        "alt": "Mathew Potts standing in front of Middle Drum mirrors",
        "caption": "Middle Drum fluorescence detector mirrors.",
    },
    {
        "src": "../assets/images/apsApril2022.jpg",
        "alt": "End Station A control room during the APS April 2022 meeting",
        "caption": "APS April 2022 meeting.",
    },
    {
        "src": "../assets/images/SLAC/slac_research_logo.jpg",
        "alt": "Researchers working in the SLAC End Station A",
        "caption": "Working in End Station A at SLAC.",
    },
    {
        "src": "../assets/images/TA-All-meeting-2021.png",
        "alt": "Telescope Array collaboration meeting held over Zoom",
        "caption": "Telescope Array meeting, December 2021.",
    },
    {
        "src": "../assets/images/uofu_logo.jpg",
        "alt": "University of Utah logo",
        "caption": "University of Utah.",
    },
    {
        "src": "../assets/images/pnnl-logo.png",
        "alt": "Pacific Northwest National Laboratory logo",
        "caption": "Pacific Northwest National Laboratory.",
    },
    {
        "src": "../assets/images/trinity-logo.png",
        "alt": "Trinity neutrino experiment logo",
        "caption": "Trinity neutrino experiment.",
    },
    {
        "src": "../assets/images/TALogo.png",
        "alt": "Telescope Array logo",
        "caption": "Telescope Array.",
    },
    {
        "src": "../assets/images/slac_logo.png",
        "alt": "SLAC National Accelerator Laboratory logo",
        "caption": "SLAC National Accelerator Laboratory.",
    },
    {
        "src": "../assets/images/kepler_logo.png",
        "alt": "Kepler mission logo",
        "caption": "Kepler mission research.",
    },
    {
        "src": "../assets/images/20200820_092136.jpg",
        "alt": "Telescope Array surface detector in the field",
        "caption": "Surface detector after field maintenance.",
    },
    {
        "src": "../assets/images/20200816_203056.jpg",
        "alt": "Telescope Array surface detector main board",
        "caption": "Surface detector electronics.",
    },
    {
        "src": "../assets/images/20200816_135218.jpg",
        "alt": "Telescope Array surface detector in the field",
        "caption": "Surface detector field work.",
    },
    {
        "src": "../assets/images/20210513_182611.jpg",
        "alt": "Telescope Array research site",
        "caption": "Telescope Array research site.",
    },
    {
        "src": "../assets/images/MD_TAx4.png",
        "alt": "TAx4 detector site",
        "caption": "TAx4 detector site.",
    },
    {
        "src": "../assets/images/GTpostdoc/demonstrator_in_lab.jpg",
        "alt": "Trinity demonstrator telescope in the laboratory",
        "caption": "Trinity demonstrator in the lab.",
    },
    {
        "src": "../assets/images/slcc_logo.jpg",
        "alt": "Salt Lake Community College logo",
        "caption": "Salt Lake Community College.",
    },
    {
        "src": "../assets/images/SLAC/20160725_161552.jpg",
        "alt": "Photomultiplier tube calibration setup",
        "caption": "PMT calibration setup at the University of Utah.",
    },
    {
        "src": "../assets/images/sflash_diagram.png",
        "alt": "Diagram of the sFLASH experimental setup",
        "caption": "sFLASH experimental setup.",
    },
    {
        "src": "../assets/images/sflash_pmts.png",
        "alt": "Six photomultiplier tubes used in the sFLASH experiment",
        "caption": "The photomultiplier tubes used in sFLASH.",
    },
    {
        "src": "../assets/images/SLAC/run1/20160727_165955.jpg",
        "alt": "Beam dump in End Station A",
        "caption": "The beam dump in End Station A.",
    },
    {
        "src": "../assets/images/SLAC/run1/20160727_193201.jpg",
        "alt": "Radiation badge after safety training at SLAC",
        "caption": "Radiation badge after SLAC safety training.",
    },
    {
        "src": "../assets/images/SLAC/run1/20160728_085702.jpg",
        "alt": "Alumina blocks along the beamline",
        "caption": "Alumina blocks used to initiate the air shower.",
    },
    {
        "src": "../assets/images/SLAC/run1/20160728_200016.jpg",
        "alt": "Stairs outside End Station A",
        "caption": "Outside End Station A.",
    },
    {
        "src": "../assets/images/SLAC/run1/20160730_104738.jpg",
        "alt": "Hallway filled with synchrotrons at SLAC",
        "caption": "A hallway at SLAC.",
    },
    {
        "src": "../assets/images/SLAC/run1/20160730_110651.jpg",
        "alt": "sFLASH collaboration meeting in the control room",
        "caption": "sFLASH collaboration meeting.",
    },
    {
        "src": "../assets/images/SLAC/run1/20160730_140059.jpg",
        "alt": "Researchers watching data arrive",
        "caption": "Watching the data roll in.",
    },
    {
        "src": "../assets/images/SLAC/run1/20160730_193343.jpg",
        "alt": "Charlie Jui in the control room during data taking",
        "caption": "The control room during data taking.",
    },
    {
        "src": "../assets/images/SLAC/run1/20160731_223622.jpg",
        "alt": "LabVIEW data acquisition program",
        "caption": "The LabVIEW data acquisition program.",
    },
    {
        "src": "../assets/images/SLAC/run1/20160801_093538.jpg",
        "alt": "Inside the photon guide tunnel with a UV LED",
        "caption": "Inside the photon guide tunnel.",
    },
    {
        "src": "../assets/images/SLAC/imagejpeg_0.jpg",
        "alt": "SLAC experimental setup",
        "caption": "sFLASH experimental setup at SLAC.",
    },
    {
        "src": "../assets/images/SLAC/20160729_120550.jpg",
        "alt": "SLAC End Station A during the sFLASH experiment",
        "caption": "End Station A during sFLASH.",
    },
    {
        "src": "../assets/images/SLAC/20160729_213616.jpg",
        "alt": "sFLASH equipment at SLAC",
        "caption": "sFLASH equipment at SLAC.",
    },
    {
        "src": "../assets/images/SLAC/20160922_092854.jpg",
        "alt": "sFLASH setup during the second experiment",
        "caption": "The second sFLASH experiment.",
    },
    {
        "src": "../assets/images/SLAC/run2/20160921_115026.jpg",
        "alt": "Window frame for the remote shutter",
        "caption": "Setting up the remote shutter window.",
    },
    {
        "src": "../assets/images/SLAC/run2/20160921_121602.jpg",
        "alt": "Photon guide setup in End Station A",
        "caption": "Before setting up the photon guide.",
    },
    {
        "src": "../assets/images/SLAC/run2/20160921_134529.jpg",
        "alt": "Experiment measurements written in a coordinate system",
        "caption": "Notes from the second sFLASH experiment.",
    },
    {
        "src": "../assets/images/SLAC/run2/20160922_142311.jpg",
        "alt": "Inside the photon guide looking toward the PMTs",
        "caption": "Inside the photon guide.",
    },
    {
        "src": "../assets/images/SLAC/run2/20160923_155154.jpg",
        "alt": "Photomultiplier tubes behind lead shielding",
        "caption": "Photomultiplier tubes behind lead shielding.",
    },
    {
        "src": "../assets/images/TA_all_arrays.png",
        "alt": "Map of the Telescope Array, TALE, and TAx4 arrays",
        "caption": "Map of the Telescope Array, TALE, and TAx4.",
    },
    {
        "src": "../assets/images/tax4_mirror.jpg",
        "alt": "TAx4 fluorescence detector mirror",
        "caption": "TAx4 fluorescence detector mirror.",
    },
    {
        "src": "../assets/images/tax4_pmt_cluster.jpg",
        "alt": "TAx4 fluorescence detector photomultiplier tube cluster",
        "caption": "TAx4 fluorescence detector camera.",
    },
]


def read(path):
    return path.read_text(encoding="utf-8")


def render_project(project):
    template = read(PROJECT_CARD)
    values = {
        "{{URL}}": escape(project["url"], quote=True),
        "{{TITLE}}": escape(project["title"]),
        "{{DATES}}": escape(project["dates"]),
        "{{DESCRIPTION}}": escape(project["description"]),
    }
    for placeholder, value in values.items():
        template = template.replace(placeholder, value)
    return template


def render_gallery(photos):
    template = read(GALLERY)
    items = []
    for photo in photos:
        item = template
        values = {
            "{{SRC}}": escape(photo["src"], quote=True),
            "{{ALT}}": escape(photo["alt"], quote=True),
            "{{CAPTION}}": escape(photo["caption"]),
        }
        for placeholder, value in values.items():
            item = item.replace(placeholder, value)
        items.append(item)
    return "\n".join(items)


def render_header(title, active, root):
    template = read(HEADER)
    values = {
        "{{ROOT}}": root,
        "{{TITLE}}": escape(title),
        "{{HOME_ACTIVE}}": "active" if active == "Homepage" else "",
        "{{EDUCATION_ACTIVE}}": "active" if active == "Education" else "",
        "{{RESEARCH_ACTIVE}}": "active" if active == "Research" else "",
        "{{PROJECTS_ACTIVE}}": "active" if active == "Projects" else "",
    }
    for placeholder, value in values.items():
        template = template.replace(placeholder, value)
    return template


def extract_main(source):
    start = source.index("<main>")
    end = source.index("</main>", start) + len("</main>")
    return source[start:end]


def build_page(relative_path, title, active):
    output = SITE_ROOT / relative_path
    source = read(output)
    root = "." if output.parent == SITE_ROOT else ".."
    rendered = render_header(title, active, root)
    rendered += extract_main(source)
    rendered += "\n" + read(FOOTER)
    output.write_text(rendered, encoding="utf-8")


def build_projects_page():
    output = SITE_ROOT / "pages/projects.html"
    content = "".join(render_project(project) for project in PROJECTS)
    main = f'''<main>
        <div class="container" style="height: 1100px">
            <div class="row" id="row-tile-overlay-last" style="height: 1125px">
                <div class="overlay-header"><h1>Projects</h1></div>
                <div class="info-box" id="info-pro">
                    {content}
                </div>
            </div>
        </div>
    </main>'''
    output.write_text(render_header("Projects", "Projects", "..") + main + "\n" + read(FOOTER), encoding="utf-8")


def build_gallery_page():
    output = SITE_ROOT / "pages/gallery.html"
    main = f'''<main>
        <div class="container">
            <div class="row" id="row-tile-overlay-last">
                <div class="overlay-header"><h1>Photo Gallery</h1></div>
                <div class="info-box photo-gallery">
                    {render_gallery(PHOTOS)}
                </div>
            </div>
        </div>
    </main>'''
    output.write_text(render_header("Photo Gallery", "", "..") + main + "\n" + read(FOOTER), encoding="utf-8")


for relative_path, (title, active) in PAGES.items():
    if relative_path != "pages/projects.html":
        build_page(relative_path, title, active)
        print(f"Built {relative_path}")

build_projects_page()
build_gallery_page()
print("Built pages/projects.html")
print("Built pages/gallery.html")