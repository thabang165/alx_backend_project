# alx_backend_project
# Product Price Comparer API

## Overview

The **Product Price Comparer API** is a web-based application that allows users to search for products and compare their prices across multiple stores. It provides detailed information about each product, including store, price, currency, and the date the price was last checked. The API is built using **Django** and **Django REST Framework** and includes an administrative interface for managing products, stores, and prices.

---

## Features

- Search products by name (case-insensitive, partial matches allowed).  
- View prices for a product across all stores.  
- Admin interface to manage:
  - Products
  - Stores
  - Prices  
- JWT-based authentication for secure access to protected endpoints.  
- Dynamic RESTful API endpoints for easy integration with frontend applications.

---

## Tech Stack

- **Backend:** Python, Django, Django REST Framework  
- **Database:** SQLite (default for development; can be replaced with PostgreSQL for production)  
- **Frontend:** HTML, JavaScript, and simple AJAX calls to the API  
- **Authentication:** JWT (JSON Web Tokens)

---

## Installation

1. Clone the repository
