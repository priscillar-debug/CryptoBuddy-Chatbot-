# 🚀 CryptoBuddy: Rule-Based Chatbot for Crypto Advice

# Introduction
print("🤖 Hello! I'm CryptoBuddy – your friendly guide to profitable & sustainable crypto investing!")
print("Ask me things like:")
print("• Which crypto is trending up?")
print("• What’s the most sustainable coin?")
print("• Which crypto should I buy for long-term growth?")
print("Type 'exit' or 'quit' to end the chat.\n")

# Sample cryptocurrency database
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

# Response logic
def respond_to_query(user_query):
    user_query = user_query.lower()

    if "sustainable" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"🌱 Invest in {recommend}! It’s eco-friendly and has long-term potential!")

    elif "trending" in user_query or "rising" in user_query:
        trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        print("📈 These coins are trending up:", ", ".join(trending))

    elif "long-term" in user_query or "growth" in user_query:
        options = [coin for coin in crypto_db if
                   crypto_db[coin]["price_trend"] == "rising" and
                   crypto_db[coin]["sustainability_score"] > 0.7]
        if options:
            print(f"🚀 {options[0]} is trending up and has a top-tier sustainability score!")
        else:
            print("🤔 No coins found with strong growth and sustainability right now.")

    elif "energy" in user_query:
        print("⚡ Crypto energy usage:")
        for coin, data in crypto_db.items():
            print(f"- {coin}: Energy Use = {data['energy_use']}")

    elif "market cap" in user_query:
        print("💰 Market cap of coins:")
        for coin, data in crypto_db.items():
            print(f"- {coin}: Market Cap = {data['market_cap']}")

    else:
        print("❓ Sorry, I didn't understand. Try asking about trending coins, sustainability, or energy use.")

# Chat loop
while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ["exit", "quit"]:
        print("CryptoBuddy: 👋 Stay smart and do your own research. Bye!")
        break
    respond_to_query(user_input)

# Disclaimer
print("\n⚠️ Disclaimer: This is not financial advice. Crypto is risky—always DYOR (Do Your Own Research)!")
