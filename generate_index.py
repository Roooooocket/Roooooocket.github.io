# -*- coding: utf-8 -*-

html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tengfei Cui | Environmental Chemistry Researcher</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        html { scroll-behavior: smooth; }
        body { font-family: -apple-system, BlinkMacSystemFont, sans-serif; background: #0a0a0a; color: #f5f5f7; }
        
        nav { position: fixed; top: 0; left: 0; right: 0; z-index: 1000; padding: 0 48px; height: 48px; background: rgba(0,0,0,0.4); backdrop-filter: blur(20px); display: flex; align-items: center; justify-content: space-between; }
        .nav-logo { font-size: 21px; font-weight: 600; color: #fff; text-decoration: none; }
        .nav-links { display: flex; gap: 32px; list-style: none; }
        .nav-links a { color: rgba(255,255,255,0.8); text-decoration: none; font-size: 14px; transition: color 0.3s; }
        .nav-links a:hover { color: #fff; }
        
        /* Hero - Full Screen Image */
        .hero {
            min-height: 100vh;
            background: url('assets/hero-bg.jpg') center/cover no-repeat;
            position: relative;
            display: flex;
            align-items: flex-end;
            justify-content: space-between;
            padding: 80px 80px 100px;
        }
        
        .hero::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background: linear-gradient(135deg, rgba(0,0,0,0.3) 0%, rgba(0,0,0,0.1) 50%, rgba(0,0,0,0.4) 100%);
            z-index: 1;
        }
        
        .hero-left {
            position: relative;
            z-index: 2;
            display: flex;
            flex-direction: column;
            gap: 16px;
        }
        
        .hero-label {
            font-size: 13px;
            color: rgba(255,255,255,0.9);
            letter-spacing: 0.15em;
            text-transform: uppercase;
            font-weight: 500;
        }
        
        .research-item {
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 15px;
            color: rgba(255,255,255,0.95);
            opacity: 0;
            animation: fadeInLeft 0.8s ease forwards;
        }
        
        .research-item:nth-child(2) { animation-delay: 0.2s; }
        .research-item:nth-child(3) { animation-delay: 0.4s; }
        .research-item:nth-child(4) { animation-delay: 0.6s; }
        
        .research-icon {
            width: 40px;
            height: 40px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            background: rgba(255,255,255,0.15);
            backdrop-filter: blur(10px);
        }
        
        .hero-right {
            position: relative;
            z-index: 2;
            text-align: right;
            display: flex;
            flex-direction: column;
            align-items: flex-end;
            gap: 20px;
        }
        
        .hero-title {
            font-family: 'Playfair Display', serif;
            font-size: clamp(56px, 8vw, 120px);
            font-weight: 700;
            color: #ffffff;
            text-shadow: 0 8px 40px rgba(0,0,0,0.6), 0 2px 10px rgba(0,0,0,0.4);
            letter-spacing: -0.02em;
            line-height: 1;
            opacity: 0;
            animation: floatUp 1.2s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
            animation-delay: 0.3s;
        }
        
        .hero-subtitle {
            font-size: 18px;
            color: rgba(255,255,255,0.95);
            font-weight: 300;
            letter-spacing: 0.05em;
            opacity: 0;
            animation: fadeInUp 0.8s ease forwards;
            animation-delay: 0.8s;
        }
        
        .tibetan-label {
            display: flex;
            align-items: center;
            gap: 8px;
            cursor: help;
            position: relative;
        }
        
        .tibetan-label span {
            font-size: 14px;
            color: rgba(255,255,255,0.85);
            border-bottom: 1px dashed rgba(255,255,255,0.5);
            padding-bottom: 2px;
            opacity: 0;
            animation: fadeInUp 0.8s ease forwards;
            animation-delay: 1.1s;
        }
        
        .tibetan-tooltip {
            position: absolute;
            bottom: 100%;
            right: 0;
            margin-bottom: 12px;
            background: rgba(0,0,0,0.85);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.2);
            border-radius: 12px;
            padding: 12px 16px;
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s ease;
            white-space: nowrap;
            z-index: 100;
        }
        
        .tibetan-label:hover .tibetan-tooltip {
            opacity: 1;
            visibility: visible;
            transform: translateY(-5px);
        }
        
        .tibetan-tooltip p {
            font-size: 13px;
            color: rgba(255,255,255,0.9);
            margin: 0;
            line-height: 1.4;
        }
        
        @keyframes fadeInLeft {
            from { opacity: 0; transform: translateX(-20px); }
            to { opacity: 1; transform: translateX(0); }
        }
        
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        @keyframes floatUp {
            from { opacity: 0; transform: translateY(40px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        /* Sections */
        section { padding: 100px 48px; max-width: 1200px; margin: 0 auto; }
        .section-header { text-align: center; margin-bottom: 80px; }
        .section-label { font-size: 14px; font-weight: 500; color: #2997ff; letter-spacing: 0.04em; text-transform: uppercase; margin-bottom: 12px; }
        .section-title { font-size: clamp(32px, 5vw, 48px); font-weight: 700; letter-spacing: -0.02em; }
        
        /* TIMELINE */
        .timeline-wrapper { position: relative; max-width: 800px; margin: 0 auto; padding: 60px 0; }
        .timeline-center-line { position: absolute; left: 50%; top: 0; bottom: 0; width: 2px; background: linear-gradient(to bottom, #2997ff, rgba(255,255,255,0.1)); transform: translateX(-50%); }
        .timeline-arrow { position: absolute; left: 50%; bottom: -20px; transform: translateX(-50%); width: 0; height: 0; border-left: 10px solid transparent; border-right: 10px solid transparent; border-bottom: 14px solid #2997ff; }
        .timeline-node { position: absolute; left: 50%; transform: translateX(-50%); display: flex; flex-direction: column; align-items: center; z-index: 10; }
        .timeline-node-dot { width: 16px; height: 16px; border-radius: 50%; background: #2997ff; box-shadow: 0 0 20px rgba(41,151,255,0.5); margin-bottom: 10px; }
        .timeline-node-label { padding: 6px 16px; background: #0a0a0a; border: 1px solid #2997ff; border-radius: 20px; font-size: 14px; font-weight: 600; color: #2997ff; }
        .timeline-row { display: grid; grid-template-columns: 1fr 1fr; gap: 60px; margin-bottom: 50px; position: relative; }
        .timeline-row::before { content: ''; position: absolute; left: 50%; top: 20px; width: 30px; height: 2px; background: rgba(255,255,255,0.2); transform: translateX(-50%); }
        .timeline-left, .timeline-right { padding: 20px; }
        .timeline-right { text-align: left; }
        .timeline-left { text-align: right; }
        .timeline-card { background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; padding: 24px; transition: all 0.3s; }
        .timeline-left .timeline-card:hover { border-color: #34c759; }
        .timeline-right .timeline-card:hover { border-color: #ff9500; }
        .timeline-card-label { font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 8px; }
        .timeline-left .timeline-card-label { color: #34c759; }
        .timeline-right .timeline-card-label { color: #ff9500; }
        .timeline-card-title { font-size: 18px; font-weight: 600; margin-bottom: 8px; }
        .timeline-card-org { font-size: 14px; color: rgba(255,255,255,0.6); margin-bottom: 12px; }
        .timeline-card-desc { font-size: 14px; color: rgba(255,255,255,0.5); line-height: 1.6; }
        .skill-tags { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 12px; }
        .timeline-left .skill-tags { justify-content: flex-end; }
        .skill-tag { padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 500; }
        .timeline-left .skill-tag { background: rgba(52,199,89,0.15); color: #34c759; border: 1px solid rgba(52,199,89,0.3); }
        .timeline-right .skill-tag { background: rgba(255,149,0,0.15); color: #ff9500; border: 1px solid rgba(255,149,0,0.3); }
        
        .research-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: 24px; }
        .research-card { background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); border-radius: 20px; padding: 32px; transition: all 0.4s; text-decoration: none; display: block; }
        .research-card:hover { transform: translateY(-8px); border-color: #2997ff; }
        .research-image { width: 100%; height: 180px; background: #1a1a1a; border-radius: 12px; margin-bottom: 20px; display: flex; align-items: center; justify-content: center; overflow: hidden; }
        .research-image img { width: 100%; height: 100%; object-fit: cover; }
        .research-badge { display: inline-block; padding: 4px 12px; border-radius: 6px; font-size: 12px; font-weight: 600; margin-bottom: 12px; }
        .research-badge.published { background: rgba(52,199,89,0.15); color: #34c759; }
        .research-badge.in-progress { background: rgba(41,151,255,0.15); color: #2997ff; }
        .research-card-title { font-size: 18px; font-weight: 600; margin-bottom: 8px; color: #fff; line-height: 1.4; }
        .research-card-authors { font-size: 13px; color: rgba(255,255,255,0.5); margin-bottom: 12px; }
        .research-card-link { font-size: 14px; color: #2997ff; font-weight: 500; display: flex; align-items: center; gap: 6px; }
        .research-card-link::after { content: '→'; }
        
        .publication-item { padding: 32px 0; border-bottom: 1px solid rgba(255,255,255,0.1); }
        .publication-header { display: flex; justify-content: space-between; gap: 20px; margin-bottom: 12px; }
        .publication-title { font-size: 19px; font-weight: 600; flex: 1; }
        .publication-year { font-size: 15px; color: rgba(255,255,255,0.6); }
        .publication-journal { font-size: 15px; color: #2997ff; font-style: italic; margin-bottom: 8px; }
        .publication-authors { font-size: 14px; color: rgba(255,255,255,0.5); margin-bottom: 12px; }
        .publication-actions { display: flex; gap: 12px; }
        .pub-link { padding: 8px 16px; border-radius: 8px; font-size: 14px; font-weight: 500; text-decoration: none; }
        .pub-link-doi { background: #2997ff; color: white; }
        .pub-link-pdf { background: transparent; color: #2997ff; border: 1px solid rgba(41,151,255,0.3); }
        
        .interests-container { position: relative; width: 100%; height: 500px; margin: 40px 0; background: radial-gradient(ellipse at center, rgba(41,151,255,0.05) 0%, transparent 70%); border-radius: 24px; }
        .interests-center { position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%); width: 50px; height: 50px; border-radius: 50%; background: radial-gradient(circle, #2997ff 0%, rgba(41,151,255,0.5) 50%, transparent 70%); box-shadow: 0 0 60px rgba(41,151,255,0.4); z-index: 10; }
        .interest-node { position: absolute; font-size: 36px; cursor: pointer; transition: all 0.3s; z-index: 5; animation: float 3s ease-in-out infinite; }
        .interest-node:hover { transform: scale(1.4); z-index: 20; }
        .interest-tooltip { position: absolute; bottom: 100%; left: 50%; transform: translateX(-50%) translateY(-10px); background: #1a1a1a; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 12px; opacity: 0; visibility: hidden; transition: all 0.3s; z-index: 100; min-width: 140px; text-align: center; }
        .interest-node:hover .interest-tooltip { opacity: 1; visibility: visible; }
        .interest-tooltip img { width: 120px; height: 80px; object-fit: cover; border-radius: 8px; margin-bottom: 8px; }
        .interest-tooltip p { font-size: 12px; color: rgba(255,255,255,0.7); margin: 0; }
        
        .contact-content { text-align: center; max-width: 700px; margin: 0 auto; }
        .contact-emails { display: flex; flex-direction: column; gap: 16px; margin-bottom: 32px; }
        .contact-email-item { padding: 16px 24px; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; display: flex; align-items: center; justify-content: center; gap: 12px; }
        .contact-email-item svg { color: #2997ff; }
        .contact-email-item a { color: #fff; text-decoration: none; font-size: 17px; }
        .contact-email-item .email-label { font-size: 12px; color: rgba(255,255,255,0.5); background: rgba(41,151,255,0.1); padding: 4px 10px; border-radius: 6px; }
        .contact-xiaohongshu { margin-top: 24px; }
        .contact-xiaohongshu p { color: rgba(255,255,255,0.5); font-size: 15px; margin-bottom: 16px; }
        .contact-link { display: inline-flex; align-items: center; gap: 8px; padding: 14px 28px; background: rgba(255,45,85,0.1); border: 1px solid rgba(255,45,85,0.3); border-radius: 12px; color: #fff; text-decoration: none; font-size: 15px; }
        footer { padding: 48px; text-align: center; border-top: 1px solid rgba(255,255,255,0.1); }
        footer p { font-size: 14px; color: rgba(255,255,255,0.5); }
        
        @keyframes float { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-8px); } }
        
        @media (max-width: 900px) {
            .hero { flex-direction: column; align-items: flex-end; justify-content: flex-end; padding: 60px 40px 80px; }
            .hero-left { margin-bottom: 40px; }
            .hero-title { font-size: clamp(40px, 6vw, 80px); }
            .timeline-row { grid-template-columns: 1fr; }
            .timeline-center-line { left: 20px; }
            .timeline-node { left: 20px; transform: none; }
            .timeline-row::before { left: 20px; }
            .timeline-left, .timeline-right { text-align: left; padding-left: 50px; }
            .timeline-left .skill-tags { justify-content: flex-start; }
        }
        @media (max-width: 768px) {
            nav { padding: 0 24px; }
            .nav-links { display: none; }
            .hero { padding: 60px 24px 60px; }
            .hero-left { gap: 12px; }
            .research-item { font-size: 14px; }
            .hero-title { font-size: clamp(32px, 5vw, 60px); }
            .interests-container { height: 500px; }
            .interest-node { font-size: 28px; }
        }
    </style>
</head>
<body>
    <nav>
        <a href="#" class="nav-logo">Tengfei Cui</a>
        <ul class="nav-links">
            <li><a href="#about">About</a></li>
            <li><a href="#research">Research</a></li>
            <li><a href="#interests">Interests</a></li>
            <li><a href="#publications">Publications</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>

    <section class="hero">
        <div class="hero-left">
            <p class="hero-label">Research Focus</p>
            <div class="research-item"><div class="research-icon">🏔️</div><span>PFAS in Tibetan Plateau</span></div>
            <div class="research-item"><div class="research-icon">🧊</div><span>PHCZs in Permafrost</span></div>
            <div class="research-item"><div class="research-icon">🔬</div><span>Carbon Dots Detection</span></div>
        </div>
        <div class="hero-right">
            <h1 class="hero-title">Tengfei Cui</h1>
            <p class="hero-subtitle">Environmental Chemistry Researcher</p>
            <div class="tibetan-label">
                <span>Tibetan Plateau</span>
                <div class="tibetan-tooltip"><p>Researching organic pollutants in high-altitude ecosystems</p></div>
            </div>
        </div>
    </section>

    <section id="about">
        <div class="section-header"><p class="section-label">Journey</p><h2 class="section-title">Education & Research Timeline</h2></div>
        <div class="timeline-wrapper">
            <div class="timeline-center-line"><div class="timeline-arrow"></div></div>
            <div class="timeline-node" style="top: 20px;"><div class="timeline-node-dot"></div><span class="timeline-node-label">Present</span></div>
            <div class="timeline-node" style="top: 50%;"><div class="timeline-node-dot"></div><span class="timeline-node-label">2023</span></div>
            <div class="timeline-node" style="bottom: 20px; top: auto;"><div class="timeline-node-dot"></div><span class="timeline-node-label">2019</span></div>
            <div class="timeline-row" style="margin-top: 100px;">
                <div class="timeline-left">
                    <div class="timeline-card">
                        <p class="timeline-card-label">Master's Program</p>
                        <h3 class="timeline-card-title">UCAS Master's</h3>
                        <p class="timeline-card-org">University of Chinese Academy of Sciences | GPA: 3.42/4.00</p>
                        <p class="timeline-card-desc">POPs Analysis and Environmental Behavior Research Group at RCEES, CAS.</p>
                        <div class="skill-tags"><span class="skill-tag">LC-MS/MS</span><span class="skill-tag">Instrumental Analysis</span></div>
                    </div>
                </div>
                <div class="timeline-right">
                    <div class="timeline-card">
                        <p class="timeline-card-label">Research Project</p>
                        <h3 class="timeline-card-title">PFAS Temporal Trends</h3>
                        <p class="timeline-card-org">First Author | ES&T 2026</p>
                        <p class="timeline-card-desc">Tracked 70 years of PFAS emission history in Tibetan Plateau sediments.</p>
                        <div class="skill-tags"><span class="skill-tag">LC-MS/MS</span><span class="skill-tag">Sediment Dating</span></div>
                    </div>
                </div>
            </div>
            <div class="timeline-row" style="margin-top: 80px;">
                <div class="timeline-left">
                    <div class="timeline-card">
                        <p class="timeline-card-label">Bachelor's Degree</p>
                        <h3 class="timeline-card-title">Southwest Minzu University</h3>
                        <p class="timeline-card-org">Outstanding Graduate (Rank 1/39)</p>
                        <p class="timeline-card-desc">Provincial Excellent Award in Innovation & Entrepreneurship Training.</p>
                        <div class="skill-tags"><span class="skill-tag">Environmental Engineering</span><span class="skill-tag">Research</span></div>
                    </div>
                </div>
                <div class="timeline-right">
                    <div class="timeline-card">
                        <p class="timeline-card-label">Undergraduate Research</p>
                        <h3 class="timeline-card-title">Carbon Dots</h3>
                        <p class="timeline-card-org">3rd Author | Microchem. J. 2022</p>
                        <p class="timeline-card-desc">Microwave-assisted synthesis of carbon dots for selenite detection.</p>
                        <div class="skill-tags"><span class="skill-tag">Synthesis</span><span class="skill-tag">Fluorescence</span></div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="research">
        <div class="section-header"><p class="section-label">Research</p><h2 class="section-title">Selected Publications</h2></div>
        <div class="research-grid">
            <a href="research/pfas-sediment.html" class="research-card">
                <div class="research-image"><img src="assets/images/pfas/fig_1_1.png" alt="PFAS" onerror="this.style.display='none'; this.parentElement.innerHTML='<span style=font-size:48px;opacity:0.3>🏔️</span>'"></div>
                <span class="research-badge published">Published | ES&T 2026</span>
                <h3 class="research-card-title">Temporal Trends of PFASs in Tibetan Plateau Sediment Cores (1952-2020)</h3>
                <p class="research-card-authors">Cui T., Chen Y., Fu Q., et al.</p>
                <span class="research-card-link">View Details</span>
            </a>
            <a href="research/phczs-permafrost.html" class="research-card">
                <div class="research-image"><span style="font-size:48px;opacity:0.3">🧊</span></div>
                <span class="research-badge in-progress">In Progress</span>
                <h3 class="research-card-title">Cold Trapping and Frost Filter Effects on PHCZs</h3>
                <p class="research-card-authors">Cui T., et al.</p>
                <span class="research-card-link">View Details</span>
            </a>
            <a href="research/carbon-dots.html" class="research-card">
                <div class="research-image"><img src="assets/images/carbon-dots/fig_1_1.jpeg" alt="Carbon Dots" onerror="this.style.display='none'; this.parentElement.innerHTML='<span style=font-size:48px;opacity:0.3>🔬</span>'"></div>
                <span class="research-badge published">Published | Microchem. J. 2022</span>
                <h3 class="research-card-title">Carbon-dots for Detection of Selenite</h3>
                <p class="research-card-authors">Liao G., Cui T., Xu M., et al.</p>
                <span class="research-card-link">View Details</span>
            </a>
        </div>
    </section>

    <section id="interests">
        <div class="section-header"><p class="section-label">Beyond Research</p><h2 class="section-title">Interests & Hobbies</h2></div>
        <div class="interests-container">
            <div class="interests-center"></div>
            <div class="interest-node" style="left: 12%; top: 15%;">📸<div class="interest-tooltip"><img src="assets/avatar.png" alt=""><p>Photography</p></div></div>
            <div class="interest-node" style="left: 78%; top: 12%;">🎵<div class="interest-tooltip"><img src="assets/avatar.png" alt=""><p>Music</p></div></div>
            <div class="interest-node" style="left: 88%; top: 40%;">🎮<div class="interest-tooltip"><img src="assets/avatar.png" alt=""><p>Gaming</p></div></div>
            <div class="interest-node" style="left: 82%; top: 70%;">🏔️<div class="interest-tooltip"><img src="assets/avatar.png" alt=""><p>Hiking</p></div></div>
            <div class="interest-node" style="left: 55%; top: 88%;">🛠️<div class="interest-tooltip"><img src="assets/avatar.png" alt=""><p>3D Printing</p></div></div>
            <div class="interest-node" style="left: 30%; top: 85%;">🎬<div class="interest-tooltip"><img src="assets/avatar.png" alt=""><p>Filmmaking</p></div></div>
            <div class="interest-node" style="left: 8%; top: 50%;">🧗<div class="interest-tooltip"><img src="assets/avatar.png" alt=""><p>Rock Climbing</p></div></div>
            <div class="interest-node" style="left: 20%; top: 25%;">🎨<div class="interest-tooltip"><img src="assets/avatar.png" alt=""><p>Design</p></div></div>
            <div class="interest-node" style="left: 68%; top: 22%;">🧪<div class="interest-tooltip"><img src="assets/avatar.png" alt=""><p>DIY Science</p></div></div>
            <div class="interest-node" style="left: 42%; top: 10%;">✈️<div class="interest-tooltip"><img src="assets/avatar.png" alt=""><p>Travel</p></div></div>
            <div class="interest-node" style="left: 25%; top: 55%;">📚<div class="interest-tooltip"><img src="assets/avatar.png" alt=""><p>Reading</p></div></div>
            <div class="interest-node" style="left: 75%; top: 55%;">☕<div class="interest-tooltip"><img src="assets/avatar.png" alt=""><p>Coffee</p></div></div>
        </div>
    </section>

    <section id="publications">
        <div class="section-header"><p class="section-label">Publications</p><h2 class="section-title">Academic Publications</h2></div>
        <div class="publication-item">
            <div class="publication-header">
                <h3 class="publication-title">Temporal Trends of PFASs in Tibetan Plateau Sediment Cores (1952-2020)</h3>
                <span class="publication-year">2026</span>
            </div>
            <p class="publication-journal">Environmental Science & Technology</p>
            <p class="publication-authors">Cui T., Chen Y., Fu Q., et al.</p>
            <div class="publication-actions">
                <a href="https://doi.org/10.1021/acs.est.5c11161" class="pub-link pub-link-doi" target="_blank">DOI</a>
                <a href="assets/papers/pfas-sediment.pdf" class="pub-link pub-link-pdf" download>PDF</a>
            </div>
        </div>
        <div class="publication-item">
            <div class="publication-header">
                <h3 class="publication-title">Microwave-assisted One-pot Synthesis of Carbon-dots for Detection of Selenite</h3>
                <span class="publication-year">2022</span>
            </div>
            <p class="publication-journal">Microchemical Journal</p>
            <p class="publication-authors">Liao G., Cui T., Xu M., et al.</p>
            <div class="publication-actions">
                <a href="https://doi.org/10.1016/j.microc.2022.107440" class="pub-link pub-link-doi" target="_blank">DOI</a>
                <a href="assets/papers/carbon-dots.pdf" class="pub-link pub-link-pdf" download>PDF</a>
            </div>
        </div>
    </section>

    <section id="contact">
        <div class="section-header"><p class="section-label">Contact</p><h2 class="section-title">Get in Touch</h2></div>
        <div class="contact-content">
            <div class="contact-emails">
                <div class="contact-email-item">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                    <a href="mailto:cuitengfei23@mails.ucas.ac.cn">cuitengfei23@mails.ucas.ac.cn</a>
                    <span class="email-label">UCAS</span>
                </div>
                <div class="contact-email-item">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                    <a href="mailto:cuitf6@gmail.com">cuitf6@gmail.com</a>
                    <span class="email-label">Personal</span>
                </div>
            </div>
            <div class="contact-xiaohongshu">
                <p>For my life & photography, check out Xiaohongshu:</p>
                <a href="https://xhslink.com/m/29SRzkWFRtY" class="contact-link" target="_blank">Follow me on 小红书</a>
            </div>
        </div>
    </section>

    <footer><p>&copy; 2024 Tengfei Cui. Built with passion for environmental science.</p></footer>
</body>
</html>'''

with open(r'C:\Users\Rocket\.qclaw\workspace\tengfei-cui-website\index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print('✓ index.html generated successfully')
