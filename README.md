# 🕷️ AI Web Scraper with Gemini

An intelligent web scraping application powered by Google's Gemini AI that extracts and analyzes website content. Simply enter a URL and let AI extract structured information including titles, headings, links, and contact details.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.24.1-red.svg)
![Selenium](https://img.shields.io/badge/Selenium-4.15.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🎯 Features

- **🤖 AI-Powered Analysis** - Uses Google Gemini to intelligently parse and summarize content
- **🔍 Smart Extraction** - Automatically identifies titles, headings, links, and contact information
- **⚡ Real-Time Processing** - Instant results with live scraping
- **🎨 Clean Interface** - User-friendly Streamlit web application
- **🔧 Customizable** - Easy to modify extraction templates



# 🌐 Live Demo
Check out the live app here: (https://advancedaiwebscraper-3g2nodxwpgakprbadbjc3w.streamlit.app/)

## 📸 Screenshots

<!-- Add screenshots here after deploying -->
```
[Screenshot of main interface]
[Screenshot of extraction results]
```

## 🏗️ Technology Stack

| Component | Technology |
|-----------|-----------|
| **Frontend** | Streamlit |
| **Web Scraping** | Selenium + ChromeDriver |
| **AI/LLM** | Google Gemini (gemini-1.5-flash) |
| **LLM Framework** | LangChain |
| **HTML Parsing** | BeautifulSoup4 |
| **Language** | Python 3.8+ |

## 📁 Project Structure

```
WebScraping1/
├── main.py                 # Streamlit application
├── scrape.py              # Web scraping logic
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not in repo)
├── .env.example          # Environment template
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key
- Chrome browser (latest version)
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Hasssaan514/Web-Scraping.git
cd Web-Scraping
```

2. **Create virtual environment**
```bash
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

Create a `.env` file in the project root:
```bash
GOOGLE_API_KEY=your_gemini_api_key_here
```

**Get your Gemini API key:**
- Visit https://makersuite.google.com/app/apikey
- Click "Create API Key"
- Copy and paste into `.env` file

5. **Setup ChromeDriver**

**Option A: Auto-download (Recommended)**

Update `scrape.py` to use `webdriver-manager`:
```python
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)
```

**Option B: Manual download**
- Download from https://chromedriver.chromium.org/
- Match your Chrome version
- Place in project folder
- Update path in `scrape.py`


## Setup ChromeDriver

1. Download ChromeDriver: https://chromedriver.chromium.org/
2. Extract to project folder
3. Update path in `scrape.py`


### Running the Application

```bash
streamlit run main.py
```

The application will open in your browser at `http://localhost:8501`

## 📖 Usage

### Basic Usage

1. **Enter URL** - Type or paste any website URL
2. **Click "Scrape site"** - Start the scraping process
3. **View Results** - AI extracts and displays structured information

### Example URLs to Try

```
https://python.org
https://github.com
https://news.ycombinator.com
https://stackoverflow.com
```

### What Gets Extracted

- 📄 **Website Title** - Main page title
- 📋 **Main Headings** - H1, H2, H3 headings
- 🔗 **Links** - First 5 important links with descriptions
- 📞 **Contact Info** - Email addresses and phone numbers
- 📝 **Summary** - AI-generated content summary

## ⚙️ Configuration

### Customize Extraction Template

Edit the prompt in `main.py` to extract different information:

```python
prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant. Extract from this website:

- Website Title
- Main Headings
- Product Names (if e-commerce)
- Pricing Information
- Social Media Links
- Custom fields you need

HTML:
{html}
""")
```

### Adjust HTML Character Limit

In `main.py`, modify the HTML length:
```python
response = chain.invoke({"html": html[:6000]})  # Change 6000 to desired length
```

### Modify Scraping Delay

In `scrape.py`, adjust wait time:
```python
time.sleep(5)  # Increase for slow-loading sites
```

## 🔒 Security & Privacy

- ✅ API keys stored in `.env` (not committed to Git)
- ✅ Environment variables for sensitive data
- ✅ `.gitignore` prevents accidental key exposure
- ⚠️ Only scrape publicly available content
- ⚠️ Respect website `robots.txt`
- ⚠️ Follow terms of service

## 🐛 Troubleshooting

### Common Issues

**"GOOGLE_API_KEY not set"**
```bash
# Solution: Create .env file with your API key
echo GOOGLE_API_KEY=your_key_here > .env
```

**"ChromeDriver not found"**
```bash
# Solution 1: Use webdriver-manager (auto-downloads)
pip install webdriver-manager

# Solution 2: Download manually and update path in scrape.py
```

**"Session not created: version mismatch"**
```bash
# Solution: Update Chrome browser to latest version
# Or download matching ChromeDriver version
```

**"Connection timeout"**
```python
# Solution: Increase timeout in scrape.py
time.sleep(10)  # Increase from 5 to 10 seconds
```

**"Module not found"**
```bash
# Solution: Ensure virtual environment is activated
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

## 🚀 Deployment

### Important Note

Selenium requires Chrome browser. Standard cloud platforms (Streamlit Cloud, Vercel) don't support browsers by default.

### Deployment Options

**Option 1: Streamlit Cloud (Simplified Version)**

Replace Selenium with `requests` for cloud compatibility:

```python
# scrape.py (cloud-friendly)
import requests

def scrape_website(website):
    if not website.startswith("http"):
        website = "https://" + website
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    response = requests.get(website, headers=headers, timeout=10)
    return response.text
```

Update `requirements.txt`:
```txt
streamlit==1.24.1
requests==2.31.0
python-dotenv==1.0.0
langchain-google-genai==1.0.0
langchain-core==0.1.0
```

Then deploy to Streamlit Cloud:
1. Push to GitHub
2. Go to https://streamlit.io/cloud
3. Connect repository
4. Add secret: `GOOGLE_API_KEY`

**Option 2: Docker Deployment**

For Render, Railway, or DigitalOcean with Docker support.

**Option 3: Heroku with Buildpacks**

Use Chrome and ChromeDriver buildpacks for Selenium support.

## 📊 Performance Optimization

- **Limit HTML size** - Only process first 6000 characters
- **Add delays** - Prevent overwhelming target servers
- **Use headless mode** - Faster scraping without GUI
- **Cache results** - Avoid re-scraping same URLs

```python
# Enable headless mode in scrape.py
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
```

## 🔮 Future Enhancements

- [ ] Support for JavaScript-rendered SPAs
- [ ] Batch URL processing
- [ ] Export to CSV/JSON/Excel
- [ ] Custom extraction templates via UI
- [ ] Screenshot capture
- [ ] Historical data tracking
- [ ] Proxy support
- [ ] Rate limiting
- [ ] API endpoint for programmatic access

## 📝 Requirements

```txt
streamlit==1.24.1
selenium==4.15.0
beautifulsoup4==4.12.2
python-dotenv==1.0.0
langchain-google-genai==1.0.0
langchain-core==0.1.0
```

For auto-downloading ChromeDriver, add:
```txt
webdriver-manager==4.0.1
```

## ⚠️ Limitations

- Cannot scrape sites requiring authentication
- JavaScript-heavy SPAs may need additional handling
- Some websites block automated scraping
- Gemini API has token limits
- Rate limiting on frequent requests
- Chrome browser required for Selenium

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create feature branch: `git checkout -b feature/AmazingFeature`
3. Commit changes: `git commit -m 'Add AmazingFeature'`
4. Push to branch: `git push origin feature/AmazingFeature`
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Hassan Iqbal**
- GitHub: [@Hasssaan514](https://github.com/Hasssaan514)
- Project Link: [https://github.com/Hasssaan514/Web-Scraping](https://github.com/Hasssaan514/Web-Scraping)

## 🙏 Acknowledgments

- [Google Gemini AI](https://ai.google.dev/) - Natural language processing
- [Streamlit](https://streamlit.io/) - Web application framework
- [Selenium](https://www.selenium.dev/) - Web browser automation
- [LangChain](https://www.langchain.com/) - LLM framework
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) - HTML parsing

## 📬 Support

For issues and questions:
- Open an [Issue](https://github.com/Hasssaan514/Web-Scraping/issues)
- Check existing issues for solutions
- Star ⭐ the repo if you find it helpful!

## 🎓 Use Cases

- **Research** - Gather data from multiple sources
- **Content Analysis** - Analyze competitor websites
- **Lead Generation** - Extract contact information
- **Price Monitoring** - Track product prices
- **News Aggregation** - Collect articles from news sites
- **SEO Analysis** - Extract meta tags and headings

---

**⭐ If you found this project helpful, please give it a star!**

*Built with ❤️ using AI, Python, and Modern Web Technologies*
