from server import app





def main():
    flask_app_instance = app
    flask_app_instance.run()


if __name__ == "__main__":
    main()