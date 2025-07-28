# Diplom_3
## 1. Install requirements
- Python 3.8+
- Allure
- WebDriver for Firefox
- WebDriver for Chorme
## 2. Activate venv
```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```
## 3. Install dependecies
```bash
pip install -r requirements.txt
```

## 4. Run test
```bash
pytest
```

## 5. Run tests with Allure
```bash
pytest --alluredir=allure_results
```

## 6. Generate Allure report
```bash
allure serve allure_results  
```