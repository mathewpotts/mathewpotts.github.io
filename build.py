from pathlib import Path
from html import escape


SITE_ROOT = Path(__file__).parent
HEADER = SITE_ROOT / "templates" / "header.html"
FOOTER = SITE_ROOT / "templates" / "footer.html"
PROJECT_CARD = SITE_ROOT / "templates" / "project.html"
GALLERY = SITE_ROOT / "templates" / "gallery.html"
HOME_GALLERY = SITE_ROOT / "templates" / "home-gallery.html"
HOME_GALLERY_ITEM = SITE_ROOT / "templates" / "home-gallery-item.html"
ABOUT_ME = SITE_ROOT / "templates" / "about-me.html"
RESEARCH_EXPERIENCE_TEMPLATE = SITE_ROOT / "templates" / "research-experience.html"
RESEARCH_LIST_ITEM = SITE_ROOT / "templates" / "research-list-item.html"

PAGES = {
    "pages/education.html": ("Education", "Education"),
    "pages/research.html": ("Research", "Research"),
    "pages/projects.html": ("Projects", "Projects"),
    "pages/SDmonitoring.html": ("SD Monitoring", "Projects"),
    "pages/sFLASH.html": ("sFLASH", "Projects"),
    "pages/TALEML.html": ("TALEML", "Projects"),
    "pages/trinity.html": ("Trinity", "Projects"),
    "pages/UHECR_energy_spec.html": ("UHECR Energy Spectrum w/ TAx4", "Projects"),
}

HOME_PHOTOS = [
    {
        "src": "assets/images/SLAC/20160730_000754.jpg",
        "alt": "sFLASH people watching data in the End Station A control room",
        "caption": "Watching data arrive during the first sFLASH experiment in 2018.",
    },
    {
        "src": "assets/images/potts_defense.jpg",
        "alt": "Mathew Potts at his Ph.D. defense",
        "caption": "Ph.D. defense on April 15, 2022.",
    },
    {
        "src": "assets/images/MD_Mirrors.jpg",
        "alt": "Mathew standing in front of Middle Drum mirrors",
        "caption": "Middle Drum fluorescence detector mirrors.",
    },
    {
        "src": "assets/images/apsApril2022.jpg",
        "alt": "End Station A control room during the APS April 2022 meeting",
        "caption": "APS April 2022 meeting.",
    },
    {
        "src": "assets/images/SLAC/slac_research_logo.jpg",
        "alt": "Researchers working in the SLAC End Station A",
        "caption": "Working in End Station A at SLAC.",
    },
    {
        "src": "assets/images/TA-All-meeting-2021.png",
        "alt": "Telescope Array collaboration meeting held over Zoom",
        "caption": "Telescope Array meeting, December 2021.",
    },
]

ABOUT_ME_PARAGRAPHS = [
    '''
My name is Mathew Potts, and I am an experimental physicist and computational researcher with a Ph.D. in Physics from the University of Utah. My background combines particle and astroparticle physics, scientific computing, Monte Carlo simulation, detector development, data analysis, high-performance computing, and software development. My doctoral research focused on ultra-high-energy cosmic rays with the Telescope Array (TA) observatory. In particular, I developed a measurement of the cosmic-ray energy spectrum using TAx4, the observatory's expanded detector array. My work used hybrid events observed by both surface detectors and fluorescence telescopes, combining complementary measurements of extensive air showers to reconstruct the properties of the primary cosmic rays. This research involved large-scale data analysis, detector characterization, Monte Carlo simulation, statistical analysis, and comparison of experimental data with simulated events.

    ''',
    '''
Following my Ph.D., I worked as a postdoctoral researcher at the Georgia Institute of Technology, where I contributed to the Trinity PeV Neutrino Observatory. Trinity is designed to search for very-high-energy, Earth-skimming neutrinos through the upward-going extensive air showers produced following tau-neutrino interactions in the Earth. My work included simulation and analysis supporting the Trinity demonstrator and its detection of Cherenkov light from these air showers.

    ''',
    '''
I subsequently worked as a Postdoctoral Research Assistant at Pacific Northwest National Laboratory (PNNL), where my research expanded into detector physics, low-background experiments, scientific computing, and national-security applications. My work included Geant4 and CORSIKA Monte Carlo simulations, detector calibration and analysis, and experimental work involving germanium and cryogenic detector systems. I contributed to projects associated with experiments including SuperCDMS and BeEST and worked in dilution-refrigerator and clean-laboratory environments.

    ''',
    '''
Throughout my research career, I have developed scientific software primarily in C++, Python, and C, with extensive experience working in Linux and high-performance computing environments. I have built and maintained simulation and analysis workflows using technologies including Geant4, ROOT, CORSIKA, CUDA, SLURM, CMake, NumPy, SciPy, pandas, and PyTorch. My work has included running and analyzing tens of thousands of computational jobs, developing custom simulation and analysis software, debugging complex scientific codebases, and translating physical models into computational implementations.

    ''',
    '''
More recently, I have been expanding my GPU-computing experience by developing a CUDA-based N-body simulator from scratch. This project includes GPU kernel development, memory tiling, investigation of thread and warp configurations, performance benchmarking using CUDA events, visualization, and comparisons of different approaches to GPU memory and computation.

    ''',
    '''
I also have experience applying modern AI tools to software and scientific workflows. I have worked with large language models, the OpenAI API, AI agents, and agentic frameworks, including developing automated tools that process job descriptions and generate tailored professional documents. I am interested in using AI and machine learning as practical tools for scientific computing, software engineering, data analysis, and automation while maintaining appropriate validation and human oversight.

    ''',
    '''
My broader research and technical interests center on using computation, instrumentation, and data to solve difficult scientific and engineering problems. I am particularly interested in high-performance and GPU computing, scientific software engineering, detector and simulation development, AI/ML-assisted computing, and applying my physics background to problems beyond traditional academic research.
    ''',
]

RESEARCH_EXPERIENCE = [
    {
        "title": "Pacific Northwest National Lab",
        "dates": "Summer 2024 - Fall 2026",
        "logo": "../assets/images/pnnl-logo.png",
        "alt": "Pacific Northwest National Lab Logo",
        "details": "Pacific Northwest National Lab<br>Richland, Washington<br>Manager: Bryan Fulsom",
        "bullets": [
            "Developed and analyzed Geant4 and CORSIKA Monte Carlo simulations for experimental physics and national-security research projects.",
            "Conducted detector research in dilution-refrigerator and clean-laboratory environments supporting the SuperCDMS and BeEST experiments.",
            "Applied computational modeling, detector analysis, and experimental techniques to characterize and support particle-physics research.",
            "Performed national-security research under Department of Energy Q clearance.",
        ],
    },
    {
        "title": "High Energy Neutrino Research",
        "dates": "Summer 2022 - Fall 2023",
        "logo": "../assets/images/trinity-logo.png",
        "alt": "Trinity Neutrino Experiment Logo",
        "details": "Trinity Demonstrator Telescope<br>Georgia Institute of Technology, School of Physics<br>PI: Otte Nepomuk",
        "bullets": [
            "Led development, integration, and testing of the Trinity Demonstrator telescope across electronics, optics, data acquisition (DAQ), cooling, and camera systems.",
            "Designed and implemented remote-observation procedures, software, and hardware to enable remote operation of the Trinity Demonstrator.",
            "Built, integrated, and tested telescope subsystems from individual components through system-level operation, troubleshooting hardware and software issues during development and testing.",
            "Designed and tested the cooling system for the EUSO-SPB2 Cherenkov telescope, integrating thermal-control requirements with detector and optical systems.",
            "Developed and ran CORSIKA, GrOptics, and C++ simulations to characterize the performance of the Trinity Observatory and Demonstrator telescope.",
            "Managed and provided technical direction to a team of approximately five graduate and undergraduate researchers, assigning research tasks, coordinating priorities, reviewing results, and troubleshooting technical issues.",
            "Mentored graduate and undergraduate researchers in experimental design, electronics, optics, DAQ, software development, simulation, data analysis, and scientific communication.",
            "Coordinated hardware development, software, simulation, and experimental activities across multiple research projects to meet project milestones.",
        ],
    },
    {
        "title": "Ultra High Energy Cosmic Ray Research",
        "dates": "Fall 2015 - Fall 2024",
        "logo": "../assets/images/TALogo.png",
        "alt": "Telescope Array Logo",
        "details": "Telescope Array Cosmic Ray Observatory<br>University of Utah, Department of Physics and Astronomy<br>Research Advisor: <a href=\"https://faculty.utah.edu/u0035487-CHARLES_JUI/hm/index.hml\" target=\"_blank\">Charles Jui</a><br>Thesis: <a href=\"UHECR_energy_spec.html\">Ultra High Energy Cosmic Ray Energy Spectrum using Hybrid Analysis with TAx4</a><br>Thesis Defense Slides: <a href=\"https://docs.google.com/presentation/d/1XjKTnhM_FJhsQyar7xkNWjNmCF2YZYyiSXctHDwY0oM/edit?usp=sharing\">pptx</a>, <a href=\"../assets/docs/Ph.D. Defense.pdf\">pdf</a>",
        "bullets": [
            "Analyzed two years of TAx4 hybrid-detection data to calculate the ultra-high-energy cosmic-ray energy spectrum from above 1 EeV through the Greisen-Zatsepin-Kuzmin (GZK) cutoff.",
            "Maintained and operated surface and fluorescence detectors used for cosmic-ray data collection.",
            "Administered the Telescope Array Linux data server and computational cluster, supporting scientific computing and data-analysis workflows.",
            "Developed Monte Carlo simulations to characterize fluorescence-detector energy sensitivity and cosmic-ray interactions in the atmosphere.",
            "Processed reconstructed detector data using histogram-based analysis and CERN ROOT fitting workflows.",
        ],
    },
    {
        "title": "Accelerator Research",
        "dates": "Fall 2015 - Fall 2022",
        "logo": "../assets/images/slac_logo.png",
        "alt": "SLAC Logo",
        "details": "sFLASH Collaboration<br>Stanford Linear Accelerator Center, National Accelerator Laboratory<br>Proceedings/Publications: <a href=\"../assets/docs/sFLASH_instruments_PoS(INSCC2017)407.pdf\" target=\"_blank\">Instruments of sFLASH</a>",
        "bullets": [
            "Performed two experiments in 2016 and 2018 aimed at measuring the air fluorescence yield at Stanford Linear Accelerator Center.",
            "Performed photomultiplier tube calibration with a UV LED diode.",
            "Assisted in taking data when the beam was running and kept an experimental log of each data run.",
            "Analyzed beam run data to find golden runs where the beam energy was stable.",
        ],
    },
    {
        "title": "Astronomy Research",
        "dates": "Fall 2014 - Spring 2015",
        "logo": "../assets/images/kepler_logo.png",
        "alt": "Kepler Logo",
        "details": "Salt Lake Community College, Salt Lake City, Utah<br>Research Advisor: <a href=\"https://www.slcc.edu/geomatics/contact.aspx\" target=\"_blank\">Jonathan Barnes</a><br>Senior Project: <a href=\"https://docs.google.com/presentation/d/14i3i0Zl2fZQMNm-Fr-Jk-oxOaoD44S1b/edit?usp=sharing&ouid=115602461398853445865&rtpof=true&sd=true\" target=\"_blank\">A Closer Look at the KOI-22 Light Curve</a>",
        "bullets": [
            "Examined Kepler exoplanet data for evidence of precession in the light curves of Hot Jupiter systems that could hint at additional exoplanets.",
            "Found a trend in the difference of the orbital times of KOI-22 that repeated every sixty-two orbits, which may suggest a perturbing body.",
        ],
    },
]

PUBLICATIONS = [
    "M.F. Albakry et al. (SuperCDMS Collaboration). Calibration and Performance of Germanium High Voltage Detectors for SuperCDMS SNOLAB. 2026.",
    "A. Armatol et al. (TESSERACT Collaboration). Low Energy Phonon Bursts Created By Fast Neutron Damage. 2026.",
    "M. Bagheri et al. (Trinity Collaboration). The Camera and Readout for the Trinity Demonstrator and the EUSO-SPB2 Cherenkov Telescope. Nuclear Instruments and Methods in Physics Research, 2024.",
    "M. Potts. Ultra-High Energy Cosmic Ray Energy Spectrum Using Hybrid Analysis with TAx4. Dissertation, 2022.",
    "R.U. Abbasi et al. (TA Collaboration). Indications of a Cosmic Ray Source in the Perseus-Pices Supercluster. 2021.",
    "M. Potts and C. Jui (TA Collaboration). <a href=\"../assets/docs/ICRC2021_343.pdf\" target=\"_blank\">Monocular Energy Spectrum using the TAx4 Fluorescence Detector.</a> Proceedings of Science (ICRC2021), 343.",
    "R.U. Abbasi et al. (TA Collaboration). <a href=\"../assets/docs/TAX4SD_paper.pdf\" target=\"_blank\">Surface detectors of the TAx4 experiment.</a> Nuclear Instruments and Methods in Physics Research, 2021.",
    "S. Atwood et al. (sFLASH Collaboration). <a href=\"../assets/docs/sFLASH_instruments_PoS(INSCC2017)407.pdf\" target=\"_blank\">The Instruments of sFLASH experiment.</a> Proceedings of Science (ICRC2017), 407.",
]

TALKS = [
    "M. Potts. Simulation of BeEST Photopeak Calibration. American Physical Society Meeting, 2026.",
    "M. Potts. The SuperCDMS Experiment at SNOLAB. American Physical Society Meeting, 2026.",
    "M. Potts. Searching for Dark Matter using SuperCDMS at SNOLAB. PoGo Symposium, 2024.",
    "M. Potts. Progress on Trinity, an IACT Searching for UHE Neutrinos. American Physical Society April Meeting, 2023.",
    "M. Potts. Trinity: UHE Earth-Skimming Neutrino Detector. P5 Town Hall at Fermilab and Argonne, 2023.",
    "M. Potts. Ultra-High Energy Cosmic Ray Energy Spectrum Using Hybrid Analysis with TAx4. American Physical Society April Meeting, 2022.",
    "M. Potts. <a href=\"../assets/docs/TAx4 Energy Spectrum.pdf\" target=\"_blank\">Ultra-High Energy Spectrum Using Hybrid Analysis with TAx4</a>. Los Alamos National Laboratory / Stanford Linear Accelerator Center, 2021.",
    "M. Potts. <a href=\"../assets/docs/TAx4 Energy Spectrum.pdf\" target=\"_blank\">Ultra-High Energy Spectrum Using Hybrid Analysis with TAx4</a>. Georgia Institute of Technology, 2021.",
    "M. Potts, on behalf of TA. <a href=\"https://docs.google.com/presentation/d/1H_zGOqbjo2MiBdsdOZY25oFQGV-H_MDziW16CddsWj0/edit?usp=sharing\" target=\"_blank\">Monocular Energy Spectrum Using the TAx4 Fluorescence Detector.</a> ICRC, 2021.",
    "M. Potts, on behalf of TA. <a href=\"../assets/docs/ResearchSympPoster.pdf\" target=\"_blank\">TAx4 Cosmic Ray Energy Spectrum.</a> University of Utah Research Symposium, 2020.",
    "M. Potts and Jonathan Barnes. <a href=\"https://docs.google.com/presentation/d/14i3i0Zl2fZQMNm-Fr-Jk-oxOaoD44S1b/edit?usp=sharing&ouid=115602461398853445865&rtpof=true&sd=true\" target=\"_blank\">A Closer Look at the KOI-22 Light Curve.</a> Research Symposium, Salt Lake Community College, 2015.",
    "M. Potts and Jonathan Barnes. <a href=\"https://docs.google.com/presentation/d/14i3i0Zl2fZQMNm-Fr-Jk-oxOaoD44S1b/edit?usp=sharing&ouid=115602461398853445865&rtpof=true&sd=true\" target=\"_blank\">A Closer Look at the KOI-22 Light Curve.</a> Salt Lake Astronomical Society Meeting, 2015.",
]

PROJECTS = [
    {
        "title": "CUDA N-body Simulation of Gravitational Systems",
        "url": "CUDA_Nbody.html",
        "dates": "Fall, 2026 - Present",
        "description": "A fun personal project to learn CUDA programming, simulating, and displaying gravitational systems.",
    },
    {
        "title": "OpenAI Resume Tailoring",
        "url": "OpenAI_Resume_Tailoring.html",
        "dates": "Fall, 2026 - Present",
        "description": "A fun personal project to learn OpenAI programming, simulating, and displaying resume tailoring capabilities.",
    },
    {
        "title": "SuperCDMS CUTE Germainium Detector Calibration",
        "url": "SuperCDMS.html",
        "dates": "Fall, 2024 - Present",
        "description": "Pulished research on the calibration of the SuperCDMS CUTE germanium detector using various sources. My contributions were mainly in data analysis and validation of the low energy neutron activation using 252Cf.",
    },
    {
        "title": "cdmsproctools: SuperCDMS's Offline Data Validation (ODV)",
        "url": "cdmsproctools.html",
        "dates": "Spring, 2025 - Fall, 2026",
        "description": "A fun personal project to learn OpenAI programming, simulating, and displaying resume tailoring capabilities.",
    },
    {
        "title": "SuperCDMS Global Mappings",
        "url": "globalmappings.html",
        "dates": "Spring, 2025 - Fall, 2026",
        "description": "A fun personal project to learn OpenAI programming, simulating, and displaying resume tailoring capabilities.",
    },
    {
        "title": "Comic Ray Species Identification with Machine Learning",
        "url": "TALEML.html",
        "dates": "November, 2023 - May, 2024",
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


def render_home_gallery(photos):
    template = read(HOME_GALLERY_ITEM)
    indicators = []
    slides = []
    for index, photo in enumerate(photos):
        item = template
        active = "active" if index == 0 else ""
        indicators.append(f'        <li data-target="#myCarousel" data-slide-to="{index}" class="{active}"></li>')
        values = {
            "{{ACTIVE}}": f" {active}" if active else "",
            "{{SRC}}": escape(photo["src"], quote=True),
            "{{ALT}}": escape(photo["alt"], quote=True),
            "{{CAPTION}}": escape(photo["caption"]),
        }
        for placeholder, value in values.items():
            item = item.replace(placeholder, value)
        slides.append(item)
    return "\n".join(indicators), "\n".join(slides)


def render_about_me(paragraphs):
    template = read(ABOUT_ME)
    rendered = "".join(f"\t\t\t\t\t<p>{escape(paragraph)}</p>\n" for paragraph in paragraphs)
    return template.replace("{{PARAGRAPHS}}", rendered)


def render_research_experience(experience):
    template = read(RESEARCH_EXPERIENCE_TEMPLATE)
    bullets = "".join(
        read(RESEARCH_LIST_ITEM).replace("{{TEXT}}", escape(bullet))
        for bullet in experience["bullets"]
    )
    values = {
        "{{TITLE}}": escape(experience["title"]),
        "{{DATES}}": escape(experience["dates"]),
        "{{LOGO}}": escape(experience["logo"], quote=True),
        "{{ALT}}": escape(experience["alt"], quote=True),
        "{{DETAILS}}": experience["details"],
        "{{BULLETS}}": bullets,
    }
    for placeholder, value in values.items():
        template = template.replace(placeholder, value)
    return template


def render_research_list(items):
    template = read(RESEARCH_LIST_ITEM)
    rendered = []
    for item in items:
        rendered.append(template.replace("{{TEXT}}", item))
    return "".join(rendered)


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


def build_homepage():
    output = SITE_ROOT / "index.html"
    gallery_template = read(HOME_GALLERY)
    indicators, slides = render_home_gallery(HOME_PHOTOS)
    gallery = gallery_template.replace("{{INDICATORS}}", indicators).replace("{{SLIDES}}", slides)
    main = f'''<main>
        <div class="container">
            <div class="row homepage-row" id="row-tile-overlay-last">
                <div class="overlay-header"><h1>Introduction</h1></div>
                <div class="portrait" id="portrait-main">
                    {gallery}
                </div>
                {render_about_me(ABOUT_ME_PARAGRAPHS)}
            </div>
        </div>
    </main>'''
    output.write_text(render_header("About Me", "Homepage", ".") + main + "\n" + read(FOOTER), encoding="utf-8")


def build_research_page():
    output = SITE_ROOT / "pages/research.html"
    experience = "".join(render_research_experience(item) for item in RESEARCH_EXPERIENCE)
    main = f'''<main>
        <div class="container">
            <div class="row" id="row-tile-overlay-last">
                <div class="overlay-header"><h1>Research</h1></div>
                <div class="info-box" id="info-re">
                    <br>
                    <h2>Resume, Curriculum Vitae, etc.</h2>
                    <ul>
                        <li><a href="../assets/docs/CV.pdf" target="_blank">Resume/CV</a></li>
                        <li><a href="../assets/docs/Research_Statement.pdf" target="_blank">Research Statement</a></li>
                        <li><a href="../assets/docs/PUBLICATIONS.pdf" target="_blank">Publication List</a></li>
                    </ul>
                    <h2>Research Experience</h2>
                    {experience}
                    <h2>Publications</h2>
                    <ul>
                        {render_research_list(PUBLICATIONS)}
                    </ul>
                    <h2>Conferences/Talks</h2>
                    <ul>
                        {render_research_list(TALKS)}
                    </ul>
                </div>
            </div>
        </div>
    </main>'''
    output.write_text(render_header("Research", "Research", "..") + main + "\n" + read(FOOTER), encoding="utf-8")


def build_projects_page():
    output = SITE_ROOT / "pages/projects.html"
    content = "".join(render_project(project) for project in PROJECTS)
    main = f'''<main>
        <div class="container">
            <div class="row" id="row-tile-overlay-last">
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


build_homepage()
print("Built index.html")
build_research_page()
print("Built pages/research.html")

for relative_path, (title, active) in PAGES.items():
    if relative_path not in ("pages/projects.html", "pages/research.html"):
        build_page(relative_path, title, active)
        print(f"Built {relative_path}")

build_projects_page()
build_gallery_page()
print("Built pages/projects.html")
print("Built pages/gallery.html")