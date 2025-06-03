By Qurratulain Rubab 
- LinkedIn
- GitHub Portfolio: github.com/qurrat2

# 🛒 AliExpress Product Listing Scraper

This project scrapes product listing data from AliExpress, including:

- Product Title
- Current Price
- Original Price
- Discount Percentage
- Shipping Information

## 🔧 Features

- ✅ Extracts essential product listing information
- ✅ Two scraping approaches implemented:
  - **Approach 1**: Using `BeautifulSoup` with class-based selectors
  - **Approach 2**: Using `lxml` and `XPath` to reduce dependency on class names (more robust to frontend changes)
  - ✅ Outputs scraped data to a structured CSV file

## 🧰 Technologies Used

- Python 3.x
- [Requests](https://pypi.org/project/requests/)
- [BeautifulSoup (bs4)](https://pypi.org/project/beautifulsoup4/)
- [lxml](https://pypi.org/project/lxml/)

🧠 Why Two Approaches?
- The BeautifulSoup version uses class names and is quick to implement.
- The lxml + XPath version is more robust to frontend changes, minimizing reliance on CSS class names.
- This dual-approach ensures higher reliability and maintainability across future UI updates.

⚠️ Disclaimer
This scraper is intended for educational and personal use. Make sure to comply with AliExpress's terms of service before using the scraper on a large scale or for commercial purposes.