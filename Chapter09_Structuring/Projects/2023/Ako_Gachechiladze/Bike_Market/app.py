from market import create_app

market_app = create_app()

if __name__ == "__main__":
    market_app.run(debug=True)
