# 🥗 Food Label Decoder

A web-based application that analyzes packaged food labels using **OCR and rule-based nutrition analysis**. Users can upload an image of a food label and receive extracted nutrition information, ingredient explanations, allergen detection, and nutrition classifications.

## 🚀 Features

* 📷 Upload packaged food label images
* 🔍 Extract text using **Tesseract OCR**
* 🥑 Analyze nutrition information
* 📊 Classify nutrition levels as **Low, Moderate, or High**
* 🧪 Decode food additives and ingredients
* ⚠️ Detect common allergens
* 📝 Display extracted OCR text
* 🌐 User-friendly web interface using Flask

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **Tesseract OCR**
* **HTML**
* **CSS**
* **JavaScript**

## 🔄 How It Works

```text
Food Label Image
       ↓
    OCR using
  Tesseract OCR
       ↓
 Extracted Text
       ↓
Nutrition & Ingredient
     Analysis
       ↓
Classification & Detection
       ↓
 Results Dashboard
```

## 📂 Project Structure

```text
food-label-decoder/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── services/
│   ├── food_analyzer.py
│   ├── analysis_service.py
│   └── classification_service.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── uploads/
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/food-label-decoder.git
cd food-label-decoder
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Install Tesseract OCR

Install Tesseract OCR on your system and make sure it is correctly configured in the project.

### 6. Run the application

```bash
python app.py
```

Open the local Flask URL shown in the terminal, usually:

```text
http://127.0.0.1:5000/
```

## 📊 Nutrition Classification

The application analyzes nutrition values when they are available **per 100 g**.

| Nutrient  | Classification        |
| --------- | --------------------- |
| Sugar     | Low / Moderate / High |
| Total Fat | Low / Moderate / High |
| Sodium    | Low / Moderate / High |
| Protein   | Low / Moderate / Good |

If the food label does not provide values on a per-100-g basis, the application displays the available values without applying the project's classification rules.

## 🎯 Project Objective

The main objective of this project is to make food labels easier to understand by converting complex nutritional and ingredient information into a simple and user-friendly format.

## 🔮 Future Enhancements

* 🤖 ML-based food health scoring
* 📱 Responsive mobile application
* 🗃️ Larger ingredient and additive database
* 🌍 Multi-language OCR support
* 📈 Personalized nutrition recommendations
* 🧠 AI-powered ingredient explanations

## 👩‍💻 Author

**Ashika G R**

B.Tech Artificial Intelligence & Data Science

---

⭐ If you find this project useful, consider giving the repository a star!
