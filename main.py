from bot import chat,reshape_text

def main():
    try:
        print(reshape_text("برنامه در حال شروع ..."))
        chat()
    except KeyboardInterrupt:
        print(reshape_text("\nبرنامه توسط کاربر متوقف شد."))
    except Exception as e:
        print(reshape_text(f"خطا در اجرای برنامه: {e}"))

if __name__ == "__main__":
    main()

