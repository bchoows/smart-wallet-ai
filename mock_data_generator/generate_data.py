import pandas as pd
import random
from faker import Faker
import datetime

# Initialize Faker for generating random data
fake = Faker()

# Define categories with a greatly expanded and more distinct list of merchants and descriptions
CATEGORIES = {
    "Food & Drink": {
        "merchants": [
            "McDonald's", "Starbucks", "KFC", "Subway", "Pizza Hut", "Domino's Pizza",
            "The Alley", "Tealive", "Gong Cha", "Zus Coffee", "FamilyMart", "Mamak ABC",
            "Burger King", "Secret Recipe", "Boost Juice", "OldTown White Coffee", "Coffee Bean",
            "Marrybrown", "Sushi King", "Kyochon", "Haidilao", "The Coffee House"
        ],
        "descriptions": [
            "Lunch with colleagues", "Morning coffee", "Dinner takeout", "Boba tea",
            "Coffee meeting", "Supper", "Team lunch", "Quick bite", "Weekend brunch",
            "Dessert", "Business dinner", "Ice cream treat", "Healthy smoothie",
            "Birthday celebration dinner", "Breakfast set", "Takeaway sushi"
        ]
    },
    "Transport": {
        "merchants": [
            "Grab", "AirAsia Ride", "Touch 'n Go eWallet", "LRT Kelana Jaya", "MRT",
            "KTM Komuter", "KLIA Ekspres", "KLIA Transit", "Petronas", "Shell", "Caltex",
            "Setel", "SOCAR", "Moovit", "Easybook", "RapidKL Bus", "Firefly Airlines"
        ],
        "descriptions": [
            "Ride to work", "Toll payment", "Train ticket", "Fuel top-up", "Parking fee",
            "Airport transfer", "Bus fare", "Car rental", "Public transport pass",
            "E-hailing service", "Road trip fuel", "Airport commute", "Flight ticket booking",
            "Bus ticket to Penang", "Commuter train pass", "Expressway toll"
        ]
    },
    "Shopping": {
        "merchants": [
            "Lazada", "Shopee", "Zalora", "Amazon", "Uniqlo", "H&M", "Zara", "Sephora",
            "IKEA", "Mr. D.I.Y.", "Apple Store", "Machines (Apple)", "All IT Hypermarket",
            "Decathlon", "Nike Store", "Adidas", "Cotton On", "Typo", "Harvey Norman",
            "Courts Mammoth", "Popular Bookstore", "BookXcess", "Kinokuniya", "Times Bookstore",
            "Sunway Pyramid", "Mid Valley Megamall", "Padini"
        ],
        "descriptions": [
            "Online order", "New clothes", "Fashion accessories", "Gadget purchase",
            "Sporting goods", "Electronics purchase", "Home decor", "Skincare haul",
            "Gift for friend", "Book purchase", "Furniture purchase", "Appliance upgrade",
            "New shoes", "Running shoes", "Handbag purchase", "Sneakers", "Laptop purchase",
            "Phone case", "Office attire", "Formal dress", "Birthday gift"
        ]
    },
    "Groceries": {
        "merchants": [
            "Jaya Grocer", "AEON", "Lotus's", "Village Grocer", "99 Speedmart", "Giant",
            "NSK Trade City", "Cold Storage", "myNEWS", "Econsave", "Checkers Hypermarket",
            "BMS Organics", "B.I.G.", "Ben's Independent Grocer", "KK Super Mart"
        ],
        "descriptions": [
            "Weekly groceries", "Buying snacks", "Dairy and eggs", "Fresh produce",
            "Household items", "Restocking pantry", "Beverages and snacks", "Toiletries",
            "Baking supplies", "Organic food purchase", "Bulk buying", "Weekly grocery run",
            "Buying fresh milk and bread", "Canned goods", "Frozen food restock"
        ]
    },
    "Bills & Utilities": {
        "merchants": [
            "Tenaga Nasional", "Air Selangor", "SYABAS", "Unifi", "TIME Internet", "Maxis",
            "Celcom", "Digi", "Astro", "Netflix", "Spotify", "Disney+ Hotstar",
            "YouTube Premium", "Indah Water Konsortium", "Google Workspace", "Adobe Creative Cloud"
        ],
        "descriptions": [
            "Electricity bill", "Internet bill", "Phone bill", "Monthly subscription",
            "Music streaming", "Water bill", "Mobile postpaid", "Streaming service",
            "Cloud storage fee", "Cable TV subscription", "Sewerage bill", "Gas bill",
            "Domain name renewal", "Software subscription"
        ]
    },
    "Health": {
        "merchants": [
            "Watsons", "Guardian", "Caring Pharmacy", "BIG Pharmacy", "Alpro Pharmacy",
            "Klinik Mediviron", "Klinik Kesihatan", "Sunway Medical Centre", "Pantai Hospital",
            "Columbia Asia Hospital", "iCare Dental", "Fitness First", "Anytime Fitness",
            "GNC Live Well", "Optical 88"
        ],
        "descriptions": [
            "Vitamins purchase", "Skincare products", "Prescription medicine", "Doctor's visit",
            "Dental check-up", "Health screening", "First aid supplies", "Over-the-counter meds",
            "Gym membership", "Specialist consultation", "Annual health check", "Eye check-up",
            "New glasses", "Fitness supplements", "Physiotherapy session", "Dental scaling"
        ]
    },
    "Entertainment": {
        "merchants": [
            "TGV Cinemas", "GSC Cinemas", "Steam Games", "PlayStation Store", "Ticketmaster",
            "Redbox Karaoke", "Loud Speaker Karaoke", "KidZania", "Sunway Lagoon",
            "Genting SkyWorlds", "Breakout Escape Room", "District 21", "Aquaria KLCC"
        ],
        "descriptions": [
            "Movie tickets", "Weekend movie", "Online game purchase", "Concert tickets",
            "In-game purchase", "Magazine subscription", "Live event", "Karaoke session",
            "Theme park tickets", "Family outing", "Video game subscription", "Escape room game",
            "Adventure park tickets", "Aquarium visit", "Stand-up comedy show"
        ]
    }
}

# --- SCRIPT CONFIGURATION ---
NUM_TRANSACTIONS = 2000
OUTPUT_FILE = "mock_transactions.csv"

# --- GENERATION LOGIC ---
transactions = []
for _ in range(NUM_TRANSACTIONS):
    category_name = random.choice(list(CATEGORIES.keys()))
    category_data = CATEGORIES[category_name]
    merchant = random.choice(category_data["merchants"])
    description = random.choice(category_data["descriptions"])

    if category_name in ["Food & Drink", "Transport"]:
        amount = round(random.uniform(5, 60), 2)
    elif category_name in ["Bills & Utilities", "Groceries"]:
        amount = round(random.uniform(20, 350), 2)
    elif category_name == "Shopping":
        amount = round(random.uniform(30, 800), 2)
    else:
        amount = round(random.uniform(15, 250), 2)

    timestamp = fake.date_time_between(start_date="-1y", end_date="now")
    transactions.append({
        "timestamp": timestamp, "amount": amount, "merchant": merchant,
        "description": description, "category": category_name
    })

df = pd.DataFrame(transactions)
df.to_csv(OUTPUT_FILE, index=False, encoding='utf-8')
print(
    f"✅ Successfully generated {len(df)} transactions with expanded variety.")
print(f"✅ Data saved to '{OUTPUT_FILE}'.")
