import random
import pandas as pd
from faker import Faker

# Initialize Faker for generating random data
fake = Faker()

# Categories with an expanded list of plausible merchants and descriptions
# Includes more international and local brands for better variety.
CATEGORIES = {
    "Food & Drink": {
        "merchants": ["McDonald's", "Starbucks", "KFC", "Subway", "Pizza Hut", "Domino's Pizza", "The Alley", "Tealive", "Gong Cha", "Zus Coffee", "FamilyMart", "Mamak ABC", "Burger King", "Secret Recipe", "Boost Juice", "OldTown White Coffee", "Chatime", "Naiise", "Sushi King", "PappaRich", "Nando's"],
        "descriptions": ["Lunch with colleagues", "Morning coffee", "Dinner takeout", "Boba tea", "Coffee meeting", "Supper", "Team lunch", "Quick bite", "Weekend brunch", "Dessert", "Business lunch", "Ice cream treat", "Healthy smoothie"],
        "amount_range": (5, 150)
    },
    "Transport": {
        "merchants": ["Grab", "AirAsia Ride", "Touch 'n Go eWallet", "LRT Kelana Jaya", "MRT", "KLIA Ekspres", "KLIA Transit", "Petronas", "Shell", "Caltex", "Setel", "SOCAR", "Waze", "GrabCar", "MyCar", "GoCar"],
        "descriptions": ["Ride to work", "Toll payment", "Train ticket", "Fuel top-up", "Parking fee", "Airport transfer", "Bus fare", "Car rental", "Public transport pass", "E-hailing service", "Road trip fuel", "Airport commute"],
        "amount_range": (5, 120)
    },
    "Shopping": {
        "merchants": ["Lazada", "Shopee", "Zalora", "Uniqlo", "H&M", "Zara", "Sephora", "IKEA", "Mr. D.I.Y.", "Apple Store", "Decathlon", "Harvey Norman", "Courts Mammoth", "Popular Bookstore", "BookXcess", "Kinokuniya", "Sunway Pyramid", "Mid Valley Megamall", "Padini"],
        "descriptions": ["Online order", "New clothes", "Shopping at mall", "Gadget purchase", "Sporting goods", "Electronics purchase", "Home decor", "Skincare haul", "Gift for friend", "Book purchase", "Furniture purchase", "Appliance upgrade", "Fashion accessories", "Stationery supplies"],
        "amount_range": (20, 10000)
    },
    "Groceries": {
        "merchants": ["Jaya Grocer", "AEON", "Lotus's", "Village Grocer", "99 Speedmart", "Giant", "NSK Trade City", "Cold Storage", "myNEWS", "Econsave", "Checkers Hypermarket", "BMS Organics"],
        "descriptions": ["Weekly groceries", "Buying snacks", "Dairy and eggs", "Fresh produce", "Household items", "Restocking pantry", "Beverages and snacks", "Toiletries", "Baking supplies", "Organic food purchase", "Bulk buying"],
        "amount_range": (10, 400)
    },
    "Bills & Utilities": {
        "merchants": ["Tenaga Nasional", "Air Selangor", "Unifi", "TIME Internet", "Maxis", "Celcom", "Digi", "Astro", "Netflix", "Spotify", "Disney+ Hotstar", "YouTube Premium", "Indah Water Konsortium", "Audible"],
        "descriptions": ["Electricity bill", "Internet bill", "Phone bill", "Monthly subscription", "Music streaming", "Water bill", "Mobile postpaid", "Streaming service", "Cloud storage fee", "Cable TV subscription", "Sewerage bill", "Gas bill", "Audiobook credit"],
        "amount_range": (10, 500)
    },
    "Health": {
        "merchants": ["Watsons", "Guardian", "Caring Pharmacy", "BIG Pharmacy", "Alpro Pharmacy", "Klinik Mediviron", "Sunway Medical Centre", "Pantai Hospital", "iCare Dental", "Fitness First", "Anytime Fitness"],
        "descriptions": ["Vitamins purchase", "Skincare products", "Prescription medicine", "Doctor's visit", "Dental check-up", "Health screening", "First aid supplies", "Over-the-counter meds", "Gym membership", "Specialist consultation", "Annual health check"],
        "amount_range": (15, 800)
    },
    "Entertainment": {
        "merchants": ["TGV Cinemas", "GSC Cinemas", "Steam Games", "PlayStation Store", "Ticketmaster", "Redbox Karaoke", "KidZania", "Sunway Lagoon", "Genting SkyWorlds"],
        "descriptions": ["Movie tickets", "Weekend movie", "Online game purchase", "Concert tickets", "In-game purchase", "Magazine subscription", "Live event", "Karaoke session", "Theme park tickets", "Family outing", "Video game subscription"],
        "amount_range": (15, 600)
    }
}

# --- SCRIPT CONFIGURATION ---
NUM_TRANSACTIONS = 2000
OUTPUT_FILE = "mock_transactions.csv"

# --- GENERATION LOGIC ---
transactions = []

for _ in range(NUM_TRANSACTIONS):
    # 1. Randomly select a category
    category_name = random.choice(list(CATEGORIES.keys()))
    category_data = CATEGORIES[category_name]

    # 2. Randomly select a merchant and description from the chosen category
    merchant = random.choice(category_data["merchants"])
    description = random.choice(category_data["descriptions"])

    # 3. Generate a realistic random amount
    min_amount, max_amount = category_data["amount_range"]
    amount = round(random.uniform(min_amount, max_amount), 2)

    # 4. Generate a random timestamp within the last year
    timestamp = fake.date_time_between(start_date="-1y", end_date="now")

    # 5. Add the transaction to our list
    transactions.append({
        "timestamp": timestamp,
        "amount": amount,
        "merchant": merchant,
        "description": description,
        "category": category_name
    })

# Convert the list of transactions into a pandas DataFrame
df = pd.DataFrame(transactions)

# Save the DataFrame to a CSV file
df.to_csv(OUTPUT_FILE, index=False, encoding='utf-8')

print(
    f"✅ Successfully generated {len(df)} transactions with expanded variety.")
print(f"✅ Data saved to '{OUTPUT_FILE}'.")

# Display the first 5 rows of the new data
print("\n--- Sample of Generated Data ---")
print(df.head())
