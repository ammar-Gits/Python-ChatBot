## Advanced Mobile Product Analysis and Interactive Chatbot System
# Project Overview
This project involves web scraping mobile product data from daraz.pk, developing an interactive chatbot, and presenting insights through a Flask-based dashboard. The system extracts detailed mobile phone information, stores it using SQLAlchemy, and enables user interaction via an intelligent chatbot.

## Features

# Web Scraping
Extracts mobile phone data (name, price, brand, reviews) from the first five pages of daraz.pk.
Uses Selenium or BeautifulSoup to navigate and parse product details.
Filters out irrelevant products (e.g., cases, covers, chargers).
Stores data in CSV or a database using SQLAlchemy.

## Database Integration
Uses SQLAlchemy as the ORM for structured data storage.
Enables efficient queries (e.g., retrieving products in a price range).

# Chatbot Development
Answers user queries using scraped data.
Handles questions like “Best phone under $300?” using Natural Language Processing (NLP).

# Dashboard Development
Provides key insights, including:
Total number of listings
Average product price & ratings
Top 5 mobile phones based on ratings/reviews
Interactive, with clickable product links to daraz.pk.
Built using Flask for the backend and a responsive frontend.

# Technologies Used
Python (for achatbot)
Selenium / BeautifulSoup (for web scraping)
Pandas (for data processing)
Flask (for the web framework)
SQLAlchemy (for database management)

# Evaluation Criteria
Successful product & review extraction.
Effective data storage & retrieval using SQLAlchemy.
Functional chatbot capable of understanding user queries.
Well-designed, interactive dashboard.

# Developer
This project was developed by Muhammad Ammar.

Let me know if you need any modifications! 🚀
