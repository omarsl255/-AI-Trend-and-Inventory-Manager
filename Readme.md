# 🤖 AI Trend & Inventory Manager (ATIM)

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black.svg)](https://github.com/omarsl255/-AI-Trend-and-Inventory-Manager)

> **An intelligent inventory management system that leverages Google Trends and Google Gemini AI to optimize retail inventory decisions through predictive analytics and real-time trend analysis.**

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Configuration](#-configuration)
- [Example Use Cases](#-example-use-cases)
- [Documentation](#-documentation)
- [Troubleshooting](#-troubleshooting)
- [Limitations & Future Enhancements](#-limitations--future-enhancements)
- [Contributing](#-contributing)
- [License](#-license)

## 🎯 Overview

The **AI Trend & Inventory Manager (ATIM)** is a proof-of-concept software tool designed to optimize retail inventory decisions by:

- 🔍 **Analyzing Real-Time Trends**: Automatically fetches and analyzes Google Trends data for product keywords
- 🧠 **AI-Powered Recommendations**: Uses Google Gemini AI to generate actionable inventory management recommendations
- 📊 **Inventory Optimization**: Correlates trend data with current stock levels to suggest reorders, markdowns, and warehousing strategies
- 📈 **Predictive Analytics**: Identifies rising, peaking, and declining trends before they impact sales

### Problem Statement

Traditional inventory management often relies on historical data and manual intuition, leading to:

- ❌ **Missed Opportunities**: Slow to capitalize on emerging trends, resulting in understocking popular items
- ❌ **Waste and Markdowns**: Overstocking items with declining popularity, leading to excessive holding costs
- ❌ **Operational Friction**: Gap between market intelligence and actionable inventory adjustments

### Solution

ATIM bridges this gap by automatically:
1. Analyzing real-time search interest (Google Trends)
2. Processing trend data with AI (Google Gemini)
3. Generating actionable recommendations based on inventory levels, trends, and contextual factors

## ✨ Features

### Component A: Trend Analysis & Prediction
- ✅ Real-time Google Trends data fetching
- ✅ Trend velocity and strength analysis
- ✅ Automatic trend classification (Rising, Peaking, Declining, Stable)
- ✅ Confidence scoring and ranking
- ✅ Rate limit handling with exponential backoff
- ✅ Automatic keyword generation from inventory CSV

### Component B: Inventory & Warehouse Management
- ✅ AI-powered recommendation engine (Google Gemini)
- ✅ CSV-based inventory management
- ✅ Automatic category inference
- ✅ Reorder point calculations
- ✅ Warehousing strategy suggestions
- ✅ Risk assessment and markdown recommendations
- ✅ Contextual awareness (season, holidays, trends)

### Additional Features
- ✅ **59 Product Inventory**: Pre-loaded with comprehensive shoe inventory
- ✅ **Flexible CSV Format**: Supports minimal (2 columns) or expanded (9 columns) formats
- ✅ **Auto-save**: Changes automatically saved to CSV
- ✅ **Error Handling**: Robust error handling with fallback mechanisms
- ✅ **Rate Limit Protection**: Built-in rate limiting for Google Trends API

## 🏗️ Architecture

ATIM consists of two integrated AI-driven components:

```
┌─────────────────────────────────────────────────────────────┐
│                    ATIM System Architecture                  │
└─────────────────────────────────────────────────────────────┘

┌──────────────────────┐         ┌──────────────────────┐
│  Component A:        │         │  Component B:        │
│  Trend Analysis      │────────▶│  LLM Inventory Agent │
│                      │         │                      │
│  • Google Trends API │         │  • Google Gemini AI  │
│  • Trend Velocity    │         │  • Recommendations   │
│  • Classification    │         │  • Risk Assessment   │
└──────────────────────┘         └──────────────────────┘
         │                                 │
         │                                 │
         ▼                                 ▼
┌─────────────────────────────────────────────────────────────┐
│              Inventory CSV (store_inventory.csv)             │
│  • 59 Products  • Stock Levels  • Categories  • Pricing     │
└─────────────────────────────────────────────────────────────┘
```

### Component A: Trend Analysis
- **Input**: Product keywords from inventory
- **Process**: Fetches Google Trends data, analyzes velocity and strength
- **Output**: Ranked list of trending products with confidence scores

### Component B: LLM Inventory Agent
- **Input**: Trend data + Inventory data + Contextual factors
- **Process**: AI analyzes data and generates recommendations
- **Output**: Actionable recommendations for reordering, warehousing, and risk management

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key ([Get one here](https://aistudio.google.com/app/apikey))
- Internet connection

### 1. Clone the Repository
```bash
git clone https://github.com/omarsl255/-AI-Trend-and-Inventory-Manager.git
cd -AI-Trend-and-Inventory-Manager
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API Key
Create a `.env` file in the project root:
```env
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-2.0-flash
```

### 4. Run the Application
```bash
python main.py
```

That's it! The system will:
1. Load inventory from `store_inventory.csv`
2. Analyze trends for your products
3. Generate AI-powered recommendations
4. Display inventory status and alerts

## 📦 Installation

### Step-by-Step Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/omarsl255/-AI-Trend-and-Inventory-Manager.git
cd -AI-Trend-and-Inventory-Manager
```

#### 2. Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Set Up Environment Variables
Create a `.env` file in the project root:
```env
# Google Gemini API Configuration
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-2.0-flash
```

**Getting a Gemini API Key:**
1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key" or "Get API Key"
4. Copy the key and paste it in your `.env` file

#### 5. Verify Installation
```bash
python -c "from inventory_data import InventoryManager; im = InventoryManager(); print(f'Loaded {len(im.get_all_inventory())} items')"
```

## 💻 Usage

### Running the Complete System

Execute the main application to run both components:

```bash
python main.py
```

**Output includes:**
- Trend analysis for inventory products
- AI-generated inventory recommendations
- Low stock alerts
- Inventory summary and statistics

### Running Individual Components

#### Component A: Trend Analysis Only
```bash
python trend_analysis.py
```
Analyzes trends for predefined keywords and displays trending products.

#### Component B: Inventory Agent Only
```bash
python llm_inventory_agent.py
```
Generates recommendations using sample trend data (requires Gemini API key).

### Programmatic Usage

```python
from inventory_data import InventoryManager
from trend_analysis import TrendAnalyzer
from llm_inventory_agent import InventoryAgent

# Initialize components
inventory_manager = InventoryManager()
trend_analyzer = TrendAnalyzer()
inventory_agent = InventoryAgent()

# Get keywords from inventory
keywords = [item.product_name.lower() for item in inventory_manager.get_all_inventory()]

# Analyze trends
trends = trend_analyzer.get_high_confidence_trends(keywords[:15], min_confidence=20.0)

# Generate recommendations
recommendations = inventory_agent.generate_recommendations(
    trends,
    current_season="Late Summer",
    upcoming_holidays=["Labor Day", "Back to School"]
)

print(recommendations)
```

## 📁 Project Structure

```
-AI-Trend-and-Inventory-Manager/
│
├── main.py                      # Main application (integrates both components)
├── trend_analysis.py            # Component A: Google Trends analysis
├── llm_inventory_agent.py       # Component B: LLM-based inventory recommendations
├── inventory_data.py            # Inventory data management (CSV-based)
├── config.py                    # Configuration settings
│
├── store_inventory.csv          # Inventory data (59 products, 9 columns)
│
├── requirements.txt             # Python dependencies
├── .env                         # Environment variables (not in git)
├── .gitignore                   # Git ignore rules
│
├── Readme.md                    # This file
├── SETUP_GUIDE.md              # Detailed setup instructions
├── CSV_FORMAT.md               # CSV file format documentation
└── KEYWORDS_INFO.md            # Keywords management documentation
```

### Key Files Description

| File | Description |
|------|-------------|
| `main.py` | Main application that orchestrates both components |
| `trend_analysis.py` | Google Trends API integration and trend analysis |
| `llm_inventory_agent.py` | Gemini AI integration for recommendation generation |
| `inventory_data.py` | CSV-based inventory management with auto-inference |
| `config.py` | Centralized configuration (API keys, settings) |
| `store_inventory.csv` | Inventory data file (59 products) |

## ⚙️ Configuration

### Google Trends Settings
Edit `config.py`:
```python
TRENDS_GEO = "US"              # Geographic region
TRENDS_TIMEFRAME = "today 3-m" # Time range (last 3 months)
```

### Inventory Settings
Edit `config.py`:
```python
DEFAULT_REORDER_POINT = 100      # Minimum stock level
DEFAULT_LEAD_TIME_DAYS = 14      # Average lead time
CURRENT_SEASON = "Late Summer"   # Current season
```

### Google Gemini Settings
Edit `.env`:
```env
GEMINI_API_KEY=your_key_here
GEMINI_MODEL=gemini-2.0-flash    # Options: gemini-2.0-flash, gemini-2.5-flash, gemini-2.5-pro
```

### Rate Limiting
To avoid Google Trends API rate limits, the system:
- Processes keywords one at a time
- Adds 3-6 second delays between requests
- Limits to 15 keywords by default
- Implements exponential backoff on errors

To adjust, edit `main.py`:
```python
max_keywords_to_analyze = 15  # Change this value
```

## 📊 Example Use Cases

### Use Case 1: Late Summer Trend Analysis
**Scenario**: Late Summer, trending "Ankle Boots" and "Suede"

**ATIM Analysis**:
- Trend Analysis: Sharp spike in "Ankle Boot" and "Suede" searches
- Inventory Status: 120 units in stock, reorder point: 80

**AI Recommendation**:
> "Increase orders for suede ankle boots by 30% immediately. Current stock of 120 units may be insufficient given the sharp rise in search interest. Move lightweight canvas shoes to a low-priority warehouse location to make room for trending items."

### Use Case 2: Sustained Trend Management
**Scenario**: High interest in '90s-style "Retro Runners"

**ATIM Analysis**:
- Trend Analysis: Sustained, high interest with confidence score of 52.1
- Inventory Status: 90 units in stock, reorder point: 60

**AI Recommendation**:
> "Establish a minimum reorder point of 500 units for top 3 'Retro Runner' styles across all sizes to prevent stockouts. The trend shows sustained high interest, indicating this is not a short-term fad."

### Use Case 3: Risk Assessment & Markdowns
**Scenario**: "Platform Sandals" trend sharply falling after peak

**ATIM Analysis**:
- Trend Analysis: Declining trend with negative velocity (-15.2)
- Inventory Status: 250 units in stock, well above reorder point

**AI Recommendation**:
> "Initiate a final clearance promotion on all 'Platform Sandals' within 7 days to clear Q3 stock and free up capital. The trend signal is rapidly decreasing, indicating declining consumer interest. Consider 30-40% markdown to accelerate clearance."

## 📚 Documentation

### Additional Documentation Files
- **[SETUP_GUIDE.md](SETUP_GUIDE.md)**: Detailed setup and installation instructions
- **[CSV_FORMAT.md](CSV_FORMAT.md)**: Complete CSV file format documentation
- **[KEYWORDS_INFO.md](KEYWORDS_INFO.md)**: Keywords management and customization guide

### CSV Inventory Format

The system supports two CSV formats:

**Minimal Format (2 columns):**
```csv
Shoe Description,Number of Items Left
Chunky Sneakers,150
Waterproof Boots,80
```

**Expanded Format (9 columns):**
```csv
Shoe Description,Number of Items Left,Category,Reorder Point,Reorder Quantity,Lead Time (days),Warehouse Location,Cost Per Unit,Selling Price
Chunky Sneakers,150,Casual,100,200,10,Zone A,45.00,89.99
```

See [CSV_FORMAT.md](CSV_FORMAT.md) for complete documentation.

## 🔧 Troubleshooting

### Common Issues and Solutions

#### Issue: "Google Gemini API key is required"
**Solution**: 
- Create a `.env` file in the project root
- Add: `GEMINI_API_KEY=your_key_here`
- Ensure the file is in the same directory as `main.py`

#### Issue: "Error fetching trends" or "Rate limit reached"
**Solution**: 
- Google Trends API has strict rate limits
- The system automatically handles this with delays and retries
- Reduce `max_keywords_to_analyze` in `main.py` (default: 15)
- Wait a few minutes and try again
- Consider running during off-peak hours

#### Issue: "No trends found"
**Solution**: 
- Lower the `min_confidence` threshold in `main.py`
- Check that keywords match actual product names
- Verify internet connection
- Check if Google Trends API is accessible

#### Issue: Import errors or "ModuleNotFoundError"
**Solution**: 
```bash
# Reinstall dependencies
pip install -r requirements.txt

# Or install individually
pip install pytrends google-generativeai pandas python-dotenv numpy
```

#### Issue: CSV file not found
**Solution**: 
- Ensure `store_inventory.csv` is in the project root directory
- Check file name spelling (case-sensitive)
- Verify file permissions

#### Issue: Inventory not loading from CSV
**Solution**: 
- Check CSV file format (see [CSV_FORMAT.md](CSV_FORMAT.md))
- Ensure required columns exist: "Shoe Description", "Number of Items Left"
- Verify CSV encoding is UTF-8
- Check for empty rows or invalid data

### Getting Help

1. Check the [Troubleshooting](#-troubleshooting) section above
2. Review the documentation files:
   - [SETUP_GUIDE.md](SETUP_GUIDE.md)
   - [CSV_FORMAT.md](CSV_FORMAT.md)
   - [KEYWORDS_INFO.md](KEYWORDS_INFO.md)
3. Create an issue on [GitHub](https://github.com/omarsl255/-AI-Trend-and-Inventory-Manager/issues)

## 🎯 Limitations & Future Enhancements

### Current Limitations
- ⚠️ Google Trends API has rate limits (handled automatically)
- ⚠️ Uses CSV-based inventory (not connected to real inventory systems)
- ⚠️ Requires Google Gemini API key (free tier available)
- ⚠️ Trend analysis based on search interest, not actual sales data
- ⚠️ Limited to single geographic region (configurable)

### Planned Future Enhancements
- 🔄 Integration with real inventory management systems (ERP, WMS)
- 🔄 Historical sales data analysis and demand forecasting
- 🔄 Multi-region trend analysis
- 🔄 Automated reordering system integration
- 🔄 Real-time alerts and notifications
- 🔄 Web dashboard interface
- 🔄 Machine learning models for demand forecasting
- 🔄 Integration with e-commerce platforms (Shopify, WooCommerce)
- 🔄 Support for multiple product categories
- 🔄 Advanced analytics and reporting
- 🔄 API endpoints for external integrations

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Contribution Guidelines
- Follow Python PEP 8 style guidelines
- Add comments and docstrings for new functions
- Update documentation as needed
- Test your changes before submitting

## 📄 License

This project is a proof-of-concept for educational and demonstration purposes.

## 🙏 Acknowledgments

- **Google Trends API** for trend data
- **Google Gemini AI** for intelligent recommendations
- **pytrends** library for Google Trends integration
- **pandas** for data processing

## 📞 Contact & Support

- **GitHub Repository**: [https://github.com/omarsl255/-AI-Trend-and-Inventory-Manager](https://github.com/omarsl255/-AI-Trend-and-Inventory-Manager)
- **Issues**: [Create an issue](https://github.com/omarsl255/-AI-Trend-and-Inventory-Manager/issues)
- **Documentation**: See documentation files in the repository

## 🎓 AI and Management Relevance

This project demonstrates core AI concepts applied to business management:

1. **Predictive Sourcing**: Using public data (Google Trends) as a leading indicator for demand forecasting
2. **Agile Logistics**: Enabling warehouse teams to rapidly adjust stock positioning based on real-time market shifts
3. **Decision Augmentation**: The LLM acts as an expert consultant, translating complex data into clear, human-readable business strategy
4. **Automated Intelligence**: Reducing manual analysis time while improving decision quality

---

**Made with ❤️ for intelligent inventory management**

*Last updated: 2025*
