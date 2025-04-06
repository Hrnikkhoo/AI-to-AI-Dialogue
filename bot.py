import requests
import json
import google.generativeai as genai
import time
from bidi.algorithm import get_display
import arabic_reshaper


# توکن مدل اولی رو اینجا بزار========================👇👇👇 google API Key ===============================================
api_key = "" 
genai.configure(api_key=api_key)
#=========================================================👇👇👇API Key 2  =================================================
API_KEY = ""
#=============================================================================================================================
def reshape_text(text):
    return get_display(arabic_reshaper.reshape(text))

# تابع ارسال درخواست به OpenRouter
def get_openrouter_response(user_message):
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        data=json.dumps({
            "model": "meta-llama/llama-4-maverick:free",
            "messages": [
                {
                    "role": "user",
                    "content": user_message
                }
            ]
        })
    )

    if response.status_code == 200:
        data = response.json()
        result = data["choices"][0]["message"]["content"]
        return result
    else:
        reshape_text(f"❌ خطا:{response.status_code}")
        reshape_text(response.text)
        return None

# تابع ارسال درخواست به Gemini
def send_to_gemini(prompt):
    try:
        # استفاده از مدل Gemini برای تولید محتوا
        gemini_model = genai.GenerativeModel("gemini-2.0-flash")#----->>>>>>>gemini-1.5-pro
        start_time = time.time()

        # ارسال درخواست به مدل
        response = gemini_model.generate_content(prompt)

        # محاسبه زمان پردازش
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Time taken for processing: {execution_time:.3f} seconds")

        return response.text, execution_time
    except Exception as e:
        print(f"Error from Gemini API: {e}")
        return None, None

# حلقه برای 100 بار ارسال پیام
def chat():
    user_input = "سلام! حالت چطوره؟"  # ورودی اولیه از کاربر
    chat_history = []

    for i in range(100):
        reshape_text(f"\n📝 پیام {i + 1} از کاربر: {user_input}")

        # ارسال ورودی به OpenRouter
        openrouter_response = get_openrouter_response(user_input)

        if openrouter_response:
            reshape_text(f"🔍 پاسخ از OpenRouter:, {openrouter_response}")
            chat_history.append({"role": "system", "content": openrouter_response})

            # ارسال پاسخ OpenRouter به Gemini
            gemini_answer, gemini_execution_time = send_to_gemini(openrouter_response)

            if gemini_answer:
                reshape_text(f"💬 پاسخ از Gemini: {gemini_answer}")
                chat_history.append({"role": "assistant", "content": gemini_answer})

                # پاسخ Gemini به عنوان ورودی برای پیام بعدی
                user_input = gemini_answer
            else:
                reshape_text("❌ مشکلی در دریافت پاسخ از Gemini پیش آمد.")
                break
        else:
            reshape_text("❌ مشکلی در دریافت پاسخ از OpenRouter پیش آمد.")
            break

        # ذخیره تاریخچه چت در فایل JSON
        with open("chat_history.json", "w", encoding="utf-8") as json_file:
            json.dump(chat_history, json_file, ensure_ascii=False, indent=4)

    reshape_text("✅ چت به پایان رسید. 100 پیام رد و بدل شد.")


# اجرای چت
chat()

