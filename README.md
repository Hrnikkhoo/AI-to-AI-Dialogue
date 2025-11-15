# AI-to-AI Dialogue 🤖

یک پروژه برای ایجاد گفتگو بین دو مدل هوش مصنوعی: Google Gemini و Meta Llama (از طریق OpenRouter).

## 📋 ویژگی‌ها

- گفتگوی خودکار بین دو مدل AI
- پشتیبانی از متن فارسی و عربی
- ذخیره خودکار تاریخچه گفتگو در فایل JSON
- نمایش پیشرفت گفتگو

## 🚀 نصب

1. کلون کردن ریپازیتوری:
```bash
git clone https://github.com/your-username/AI-to-AI-Dialogue.git
cd AI-to-AI-Dialogue
```

2. نصب پکیج‌های مورد نیاز:
```bash
pip install -r requirements.txt
```

## ⚙️ تنظیمات

قبل از اجرا، باید API Key های خود را در فایل `bot.py` تنظیم کنید:

1. **Google Gemini API Key**: در خط 12 فایل `bot.py`
2. **OpenRouter API Key**: در خط 15 فایل `bot.py`

```python
api_key = "YOUR_GOOGLE_API_KEY"
API_KEY = "YOUR_OPENROUTER_API_KEY"
```

## 🎯 استفاده

اجرای برنامه:
```bash
python main.py
```

برنامه به صورت خودکار 100 پیام بین دو مدل AI رد و بدل می‌کند و هر 10 پیام، تاریخچه را در فایل `chat_history.json` ذخیره می‌کند.

## 📊 تحلیل تاریخچه گفتگو

برای مشاهده آمار پیام‌ها:
```bash
python Counter_JSON.py
```

## 📁 ساختار پروژه

```
AI-to-AI-Dialogue/
├── main.py              # نقطه ورود برنامه
├── bot.py               # منطق اصلی گفتگو
├── Counter_JSON.py      # تحلیل تاریخچه گفتگو
├── requirements.txt     # پکیج‌های مورد نیاز
├── chat_history.json    # تاریخچه گفتگو (تولید می‌شود)
└── README.md           # این فایل
```

## 📝 نیازمندی‌ها

- Python 3.7+
- Google Gemini API Key
- OpenRouter API Key

## 📄 لایسنس

این پروژه برای استفاده آموزشی و شخصی است.
