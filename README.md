# Personal Website

A minimalistic personal website with a clean design featuring white background and black text. The website supports both English and Chinese languages.

## Features

- **Bilingual Content**: Switch between English and Chinese with the language selector
- **Responsive Design**: Works well on all device sizes
- **Font Selection**: Uses Georgia for English text and Songti for Chinese text
- **Navigation**: Clean navigation with tabs for Main, Research, Thoughts, Art, and "Don't Click"
- **Profile Section**: Includes circular avatar, name with pronunciation guide, and subtitle
- **About Me**: Lists three personal objectives
- **Content Pages**:
  - Research page with PDF viewing/download capabilities
  - Thoughts page with essay previews and detailed views
  - Art page with interactive image gallery
  - "Don't Click" link to an external article

## Project Structure

```
├── app.py                 # Main Flask application
├── babel.cfg              # Babel configuration for translations
├── start.sh               # Script to start the application
├── static/
│   ├── css/
│   │   └── style.css      # Main stylesheet
│   ├── images/
│   │   ├── artwork/       # Gallery images
│   │   └── profile/       # Profile images
│   ├── js/
│   │   └── main.js        # JavaScript for interactivity
│   └── pdfs/              # PDF documents for research
├── templates/
│   ├── base.html          # Base template with common structure
│   ├── index.html         # Home page
│   ├── research.html      # Research page
│   ├── art.html           # Art gallery page
│   ├── thoughts.html      # Thoughts listing page
│   └── thoughts/          # Individual thought articles
└── translations/          # Language translations
    └── zh/                # Chinese translations
```

## Setup and Running

### Prerequisites

- Python 3.7+
- Flask and dependencies

### Installation

1. Clone this repository
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Install the dependencies:
   ```
   pip install flask flask-babel
   ```

### Running the Website

1. Use the start script:
   ```
   chmod +x start.sh
   ./start.sh
   ```
   
   Or manually:
   ```
   python app.py
   ```

2. Open a browser and navigate to http://127.0.0.1:5003/

## Adding Content

### Adding Research Papers
Place PDFs in the `static/pdfs/` directory and update the research.html template.

### Adding Art
Add images to the `static/images/artwork/` directory and update the art.html template.

### Adding Thoughts
Create a new HTML file in the `templates/thoughts/` directory and add the thought to the list in thoughts.html.

## License

All rights reserved. © 2023 

## Cursor Rules

- If an essay is written in Chinese, the English version should state that it is a generative AI translation of the original Chinese text. If an essay is written in English, the Chinese version should state that it is a generative AI translation of the original English text. 