# Tengfei Cui - Academic Website

A personal academic website built with pure HTML/CSS, inspired by Apple's design aesthetic.

## Structure

```
tengfei-cui-website/
├── index.html                 # Main homepage
├── research/
│   ├── pfas-sediment.html     # PFAS project details
│   ├── phczs-permafrost.html  # PHCZs project details
│   └── carbon-dots.html       # Carbon dots project details
├── assets/
│   └── papers/                # PDF files for download
│       ├── pfas-sediment.pdf
│       └── carbon-dots.pdf
└── README.md
```

## Features

- **Apple-inspired design**: Dark theme with clean typography and generous whitespace
- **Interactive timeline**: Research experience with skill tags
- **Research project pages**: Detailed descriptions with image galleries
- **Publications list**: DOI links and PDF downloads
- **Responsive design**: Works on desktop and mobile
- **Smooth animations**: Scroll-triggered timeline reveals

## Deployment to GitHub Pages

1. Create a new repository on GitHub named `yourusername.github.io` (or any name)

2. Initialize git and push:
   ```bash
   cd tengfei-cui-website
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git push -u origin main
   ```

3. Enable GitHub Pages:
   - Go to repository Settings → Pages
   - Source: Deploy from a branch
   - Branch: main / root
   - Save

4. Your site will be live at: `https://YOUR_USERNAME.github.io`

## Customization

### Adding Papers
Place PDF files in `assets/papers/` and update links in:
- `index.html` (Publications section)
- Individual research pages

### Adding Images
Create an `assets/images/` folder and update image sources in research pages.

### Updating Content
- **Timeline**: Edit the `.timeline-item` sections in `index.html`
- **Publications**: Update the `.publication-item` sections
- **Research pages**: Create new HTML files in `research/` folder

## License

© 2024 Tengfei Cui. All rights reserved.
