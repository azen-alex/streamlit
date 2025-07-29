#!/usr/bin/env python3
"""
Grocery Store Data Generator

This script generates a comprehensive 4-level hierarchical dataset for a grocery store:
1. Departments (Level 1)
2. Categories (Level 2) 
3. Subcategories (Level 3)
4. Products (Level 4)

The data is designed to stress-test UI/UX components with realistic variety and volume.
"""

import pandas as pd
import random
from faker import Faker
from pathlib import Path
import json

# Initialize Faker for generating realistic data
fake = Faker()
Faker.seed(42)  # For reproducible data
random.seed(42)

def create_departments():
    """Create the top-level departments (Level 1)"""
    departments = [
        {"id": 1, "name": "Fresh Foods", "description": "Fresh fruits, vegetables, and perishables"},
        {"id": 2, "name": "Packaged Goods", "description": "Shelf-stable packaged items and snacks"},
        {"id": 3, "name": "Frozen Foods", "description": "Frozen meals, ice cream, and frozen ingredients"},
        {"id": 4, "name": "Dairy & Eggs", "description": "Milk, cheese, yogurt, and egg products"},
        {"id": 5, "name": "Meat & Seafood", "description": "Fresh and processed meats and seafood"},
        {"id": 6, "name": "Bakery", "description": "Fresh baked goods and bread products"},
        {"id": 7, "name": "Beverages", "description": "Drinks, juices, and liquid refreshments"},
        {"id": 8, "name": "Health & Personal Care", "description": "Vitamins, supplements, and personal care items"}
    ]
    return pd.DataFrame(departments)

def create_categories():
    """Create categories within each department (Level 2)"""
    categories_data = [
        # Fresh Foods (dept_id: 1)
        {"id": 1, "department_id": 1, "name": "Fruits", "description": "Fresh seasonal fruits"},
        {"id": 2, "department_id": 1, "name": "Vegetables", "description": "Fresh vegetables and herbs"},
        {"id": 3, "department_id": 1, "name": "Salads & Prepared", "description": "Ready-to-eat salads and prepared foods"},
        
        # Packaged Goods (dept_id: 2)
        {"id": 4, "department_id": 2, "name": "Snacks", "description": "Chips, crackers, and snack foods"},
        {"id": 5, "department_id": 2, "name": "Pantry Staples", "description": "Canned goods, grains, and cooking essentials"},
        {"id": 6, "department_id": 2, "name": "Condiments & Sauces", "description": "Dressings, sauces, and flavor enhancers"},
        {"id": 7, "department_id": 2, "name": "Breakfast Items", "description": "Cereals, oatmeal, and breakfast foods"},
        
        # Frozen Foods (dept_id: 3)
        {"id": 8, "department_id": 3, "name": "Frozen Meals", "description": "Complete frozen dinner options"},
        {"id": 9, "department_id": 3, "name": "Ice Cream & Desserts", "description": "Frozen treats and desserts"},
        {"id": 10, "department_id": 3, "name": "Frozen Vegetables", "description": "Flash-frozen vegetable products"},
        {"id": 11, "department_id": 3, "name": "Frozen Proteins", "description": "Frozen meat and seafood products"},
        
        # Dairy & Eggs (dept_id: 4)
        {"id": 12, "department_id": 4, "name": "Milk & Cream", "description": "Various milk types and cream products"},
        {"id": 13, "department_id": 4, "name": "Cheese", "description": "Natural and processed cheese varieties"},
        {"id": 14, "department_id": 4, "name": "Yogurt & Probiotics", "description": "Yogurt and fermented dairy products"},
        {"id": 15, "department_id": 4, "name": "Eggs", "description": "Fresh eggs and egg products"},
        
        # Meat & Seafood (dept_id: 5)
        {"id": 16, "department_id": 5, "name": "Fresh Meat", "description": "Fresh cuts of beef, pork, and poultry"},
        {"id": 17, "department_id": 5, "name": "Seafood", "description": "Fresh and frozen fish and shellfish"},
        {"id": 18, "department_id": 5, "name": "Deli & Prepared Meats", "description": "Sliced meats and prepared options"},
        
        # Bakery (dept_id: 6)
        {"id": 19, "department_id": 6, "name": "Bread & Rolls", "description": "Fresh baked breads and dinner rolls"},
        {"id": 20, "department_id": 6, "name": "Pastries & Desserts", "description": "Cakes, cookies, and sweet treats"},
        {"id": 21, "department_id": 6, "name": "Specialty Baked Goods", "description": "Artisan and specialty baked items"},
        
        # Beverages (dept_id: 7)
        {"id": 22, "department_id": 7, "name": "Soft Drinks", "description": "Carbonated and flavored beverages"},
        {"id": 23, "department_id": 7, "name": "Juices", "description": "Fruit and vegetable juices"},
        {"id": 24, "department_id": 7, "name": "Coffee & Tea", "description": "Hot beverage products and accessories"},
        
        # Health & Personal Care (dept_id: 8)
        {"id": 25, "department_id": 8, "name": "Vitamins & Supplements", "description": "Health supplements and vitamins"},
        {"id": 26, "department_id": 8, "name": "Personal Care", "description": "Basic personal hygiene products"}
    ]
    return pd.DataFrame(categories_data)

def create_subcategories():
    """Create subcategories within each category (Level 3)"""
    subcategories_data = [
        # Fruits (cat_id: 1)
        {"id": 1, "category_id": 1, "name": "Citrus Fruits", "description": "Oranges, lemons, limes, and grapefruits"},
        {"id": 2, "category_id": 1, "name": "Berries", "description": "Strawberries, blueberries, raspberries"},
        {"id": 3, "category_id": 1, "name": "Tropical Fruits", "description": "Pineapples, mangoes, papayas"},
        {"id": 4, "category_id": 1, "name": "Stone Fruits", "description": "Peaches, plums, apricots, cherries"},
        {"id": 5, "category_id": 1, "name": "Apples & Pears", "description": "Various apple and pear varieties"},
        
        # Vegetables (cat_id: 2)
        {"id": 6, "category_id": 2, "name": "Leafy Greens", "description": "Lettuce, spinach, kale, arugula"},
        {"id": 7, "category_id": 2, "name": "Root Vegetables", "description": "Carrots, potatoes, onions, turnips"},
        {"id": 8, "category_id": 2, "name": "Cruciferous Vegetables", "description": "Broccoli, cauliflower, Brussels sprouts"},
        {"id": 9, "category_id": 2, "name": "Peppers & Squash", "description": "Bell peppers, zucchini, squash varieties"},
        {"id": 10, "category_id": 2, "name": "Herbs & Aromatics", "description": "Fresh herbs and aromatic vegetables"},
        
        # Salads & Prepared (cat_id: 3)
        {"id": 11, "category_id": 3, "name": "Pre-made Salads", "description": "Ready-to-eat salad combinations"},
        {"id": 12, "category_id": 3, "name": "Cut Vegetables", "description": "Pre-cut and prepared vegetables"},
        
        # Snacks (cat_id: 4)
        {"id": 13, "category_id": 4, "name": "Chips & Crisps", "description": "Potato chips and similar snacks"},
        {"id": 14, "category_id": 4, "name": "Crackers", "description": "Various cracker types and brands"},
        {"id": 15, "category_id": 4, "name": "Nuts & Seeds", "description": "Roasted nuts and seed mixes"},
        {"id": 16, "category_id": 4, "name": "Candy & Sweets", "description": "Chocolates, gummies, and confections"},
        
        # Pantry Staples (cat_id: 5)
        {"id": 17, "category_id": 5, "name": "Canned Goods", "description": "Canned vegetables, fruits, and soups"},
        {"id": 18, "category_id": 5, "name": "Rice & Grains", "description": "Rice, quinoa, and grain products"},
        {"id": 19, "category_id": 5, "name": "Pasta & Noodles", "description": "Dried pasta and noodle varieties"},
        {"id": 20, "category_id": 5, "name": "Cooking Oils", "description": "Olive oil, vegetable oils, and specialty oils"},
        
        # Condiments & Sauces (cat_id: 6)
        {"id": 21, "category_id": 6, "name": "Salad Dressings", "description": "Bottled and homemade-style dressings"},
        {"id": 22, "category_id": 6, "name": "Hot Sauces", "description": "Spicy condiments and pepper sauces"},
        {"id": 23, "category_id": 6, "name": "Marinades", "description": "Meat and vegetable marinades"},
        
        # Breakfast Items (cat_id: 7)
        {"id": 24, "category_id": 7, "name": "Cereals", "description": "Cold breakfast cereals"},
        {"id": 25, "category_id": 7, "name": "Oatmeal & Hot Cereals", "description": "Hot breakfast options"},
        {"id": 26, "category_id": 7, "name": "Pancake & Waffle Mix", "description": "Breakfast baking mixes"},
        
        # Continue with remaining categories...
        # Frozen Meals (cat_id: 8)
        {"id": 27, "category_id": 8, "name": "Pizza", "description": "Frozen pizza varieties"},
        {"id": 28, "category_id": 8, "name": "TV Dinners", "description": "Complete frozen meal trays"},
        {"id": 29, "category_id": 8, "name": "International Cuisine", "description": "Ethnic frozen food options"},
        
        # Ice Cream & Desserts (cat_id: 9)
        {"id": 30, "category_id": 9, "name": "Ice Cream", "description": "Premium and regular ice cream"},
        {"id": 31, "category_id": 9, "name": "Frozen Yogurt", "description": "Healthier frozen dessert options"},
        {"id": 32, "category_id": 9, "name": "Popsicles & Bars", "description": "Frozen treats on sticks"},
        
        # Frozen Vegetables (cat_id: 10)
        {"id": 33, "category_id": 10, "name": "Mixed Vegetables", "description": "Frozen vegetable medleys"},
        {"id": 34, "category_id": 10, "name": "Single Vegetables", "description": "Individual frozen vegetables"},
        
        # Frozen Proteins (cat_id: 11)
        {"id": 35, "category_id": 11, "name": "Frozen Chicken", "description": "Frozen chicken products"},
        {"id": 36, "category_id": 11, "name": "Frozen Seafood", "description": "Frozen fish and shellfish"},
        
        # Milk & Cream (cat_id: 12)
        {"id": 37, "category_id": 12, "name": "Regular Milk", "description": "Whole, 2%, 1%, and skim milk"},
        {"id": 38, "category_id": 12, "name": "Alternative Milks", "description": "Almond, soy, oat, and other plant milks"},
        {"id": 39, "category_id": 12, "name": "Cream Products", "description": "Heavy cream, half-and-half, whipped cream"},
        
        # Cheese (cat_id: 13)
        {"id": 40, "category_id": 13, "name": "Hard Cheeses", "description": "Cheddar, Swiss, parmesan varieties"},
        {"id": 41, "category_id": 13, "name": "Soft Cheeses", "description": "Brie, camembert, cream cheese"},
        {"id": 42, "category_id": 13, "name": "Shredded Cheese", "description": "Pre-shredded cheese blends"},
        
        # Yogurt & Probiotics (cat_id: 14)
        {"id": 43, "category_id": 14, "name": "Greek Yogurt", "description": "High-protein Greek-style yogurt"},
        {"id": 44, "category_id": 14, "name": "Regular Yogurt", "description": "Traditional yogurt varieties"},
        {"id": 45, "category_id": 14, "name": "Probiotic Drinks", "description": "Kefir and other probiotic beverages"},
        
        # Eggs (cat_id: 15)
        {"id": 46, "category_id": 15, "name": "Chicken Eggs", "description": "Regular and free-range chicken eggs"},
        {"id": 47, "category_id": 15, "name": "Specialty Eggs", "description": "Duck, quail, and other specialty eggs"},
        
        # Fresh Meat (cat_id: 16)
        {"id": 48, "category_id": 16, "name": "Beef", "description": "Fresh beef cuts and ground beef"},
        {"id": 49, "category_id": 16, "name": "Pork", "description": "Pork chops, bacon, and pork products"},
        {"id": 50, "category_id": 16, "name": "Poultry", "description": "Chicken, turkey, and other poultry"},
        
        # Seafood (cat_id: 17)
        {"id": 51, "category_id": 17, "name": "Fresh Fish", "description": "Daily fresh fish selection"},
        {"id": 52, "category_id": 17, "name": "Shellfish", "description": "Shrimp, crab, lobster, and mollusks"},
        
        # Deli & Prepared Meats (cat_id: 18)
        {"id": 53, "category_id": 18, "name": "Sliced Meats", "description": "Deli-sliced lunch meats"},
        {"id": 54, "category_id": 18, "name": "Prepared Sausages", "description": "Ready-to-cook sausage varieties"},
        
        # Bread & Rolls (cat_id: 19)
        {"id": 55, "category_id": 19, "name": "Sandwich Bread", "description": "Sliced bread for sandwiches"},
        {"id": 56, "category_id": 19, "name": "Artisan Breads", "description": "Specialty and artisan bread varieties"},
        {"id": 57, "category_id": 19, "name": "Dinner Rolls", "description": "Small rolls and buns"},
        
        # Pastries & Desserts (cat_id: 20)
        {"id": 58, "category_id": 20, "name": "Cakes", "description": "Fresh baked cakes and cupcakes"},
        {"id": 59, "category_id": 20, "name": "Cookies", "description": "Fresh baked cookies and biscuits"},
        {"id": 60, "category_id": 20, "name": "Donuts & Pastries", "description": "Donuts, croissants, and pastries"},
        
        # Specialty Baked Goods (cat_id: 21)
        {"id": 61, "category_id": 21, "name": "Gluten-Free Options", "description": "Gluten-free baked goods"},
        {"id": 62, "category_id": 21, "name": "Seasonal Items", "description": "Holiday and seasonal baked goods"},
        
        # Soft Drinks (cat_id: 22)
        {"id": 63, "category_id": 22, "name": "Cola Drinks", "description": "Cola and cola-flavored beverages"},
        {"id": 64, "category_id": 22, "name": "Flavored Sodas", "description": "Fruit and specialty flavored sodas"},
        {"id": 65, "category_id": 22, "name": "Sparkling Water", "description": "Carbonated water varieties"},
        
        # Juices (cat_id: 23)
        {"id": 66, "category_id": 23, "name": "Orange Juice", "description": "Fresh and from-concentrate orange juice"},
        {"id": 67, "category_id": 23, "name": "Mixed Fruit Juices", "description": "Blended fruit juice varieties"},
        {"id": 68, "category_id": 23, "name": "Vegetable Juices", "description": "V8 and other vegetable-based juices"},
        
        # Coffee & Tea (cat_id: 24)
        {"id": 69, "category_id": 24, "name": "Ground Coffee", "description": "Pre-ground coffee varieties"},
        {"id": 70, "category_id": 24, "name": "Coffee Beans", "description": "Whole bean coffee options"},
        {"id": 71, "category_id": 24, "name": "Tea Bags", "description": "Bagged tea varieties"},
        {"id": 72, "category_id": 24, "name": "Loose Leaf Tea", "description": "Bulk loose leaf tea options"},
        
        # Vitamins & Supplements (cat_id: 25)
        {"id": 73, "category_id": 25, "name": "Daily Vitamins", "description": "Multivitamins and daily supplements"},
        {"id": 74, "category_id": 25, "name": "Specialty Supplements", "description": "Targeted health supplements"},
        
        # Personal Care (cat_id: 26)
        {"id": 75, "category_id": 26, "name": "Oral Care", "description": "Toothpaste, mouthwash, dental care"},
        {"id": 76, "category_id": 26, "name": "Hair Care", "description": "Shampoo, conditioner, styling products"}
    ]
    return pd.DataFrame(subcategories_data)

def generate_products():
    """Generate individual products (Level 4) with realistic variety and details"""
    products = []
    product_id = 1
    
    # Product templates for different subcategories
    product_templates = {
        # Citrus Fruits
        1: [
            "Navel Oranges", "Valencia Oranges", "Blood Oranges", "Mandarin Oranges",
            "Meyer Lemons", "Eureka Lemons", "Persian Limes", "Key Limes",
            "Ruby Red Grapefruit", "White Grapefruit", "Pink Grapefruit"
        ],
        # Berries
        2: [
            "Strawberries", "Blueberries", "Raspberries", "Blackberries",
            "Cranberries", "Gooseberries", "Elderberries", "Mulberries",
            "Organic Strawberries", "Wild Blueberries", "Golden Raspberries"
        ],
        # Tropical Fruits
        3: [
            "Pineapples", "Mangoes", "Papayas", "Passion Fruit", "Dragon Fruit",
            "Kiwi", "Star Fruit", "Coconuts", "Plantains", "Guava"
        ],
        # Stone Fruits
        4: [
            "Peaches", "Nectarines", "Plums", "Apricots", "Cherries",
            "Sweet Cherries", "Sour Cherries", "White Peaches", "Donut Peaches"
        ],
        # Apples & Pears
        5: [
            "Gala Apples", "Fuji Apples", "Granny Smith Apples", "Red Delicious Apples",
            "Honeycrisp Apples", "Bartlett Pears", "Anjou Pears", "Bosc Pears",
            "Asian Pears", "Seckel Pears"
        ]
    }
    
    # Generate comprehensive product list for all subcategories
    for subcategory_id in range(1, 77):  # 76 subcategories total
        
        # Use predefined templates where available, otherwise generate generic products
        if subcategory_id in product_templates:
            product_names = product_templates[subcategory_id]
        else:
            # Generate generic product names for subcategories without templates
            subcategory_name = f"Category_{subcategory_id}"
            product_names = [
                f"{subcategory_name} Item {i}" for i in range(1, random.randint(5, 12))
            ]
        
        # Add more realistic products for major categories
        if subcategory_id <= 76:  # All our defined subcategories
            additional_products = []
            
            # Add brand variations and sizes
            for base_name in product_names[:3]:  # Take first 3 products
                additional_products.extend([
                    f"Organic {base_name}",
                    f"Premium {base_name}",
                    f"{base_name} - Family Size",
                    f"{base_name} - Single Serve"
                ])
            
            product_names.extend(additional_products)
        
        # Create products with realistic details
        for product_name in product_names:
            # Generate realistic pricing based on product type
            base_price = random.uniform(0.99, 15.99)
            if "organic" in product_name.lower() or "premium" in product_name.lower():
                base_price *= random.uniform(1.2, 1.8)
            if "family size" in product_name.lower():
                base_price *= random.uniform(1.5, 2.2)
            
            # Generate realistic stock quantities
            stock_quantity = random.randint(0, 150)
            
            # Determine appropriate units
            unit_options = ["lb", "each", "oz", "bag", "box", "bottle", "pack"]
            unit = random.choice(unit_options)
            
            # Add some seasonal availability (some items out of stock)
            if random.random() < 0.05:  # 5% chance of being out of stock
                stock_quantity = 0
            
            # Add quality field with weighted distribution
            quality_choices = ["good", "neutral", "poor"]
            quality_weights = [50, 35, 15]  # 50% good, 35% neutral, 15% poor
            quality = random.choices(quality_choices, weights=quality_weights)[0]
            
            products.append({
                "id": product_id,
                "subcategory_id": subcategory_id,
                "name": product_name,
                "price": round(base_price, 2),
                "stock_quantity": stock_quantity,
                "unit": unit,
                "sku": f"SKU-{product_id:06d}",
                "barcode": fake.ean13(),
                "description": f"High quality {product_name.lower()} available in our store",
                "quality": quality
            })
            product_id += 1
    
    return pd.DataFrame(products)

def save_data():
    """Generate all data and save to CSV files"""
    print("🏗️  Generating grocery store data...")
    
    # Create data directory if it doesn't exist
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    
    # Generate all levels of data
    print("📊 Creating departments...")
    departments_df = create_departments()
    
    print("📊 Creating categories...")
    categories_df = create_categories()
    
    print("📊 Creating subcategories...")
    subcategories_df = create_subcategories()
    
    print("📊 Generating products (this may take a moment)...")
    products_df = generate_products()
    
    # Save to CSV files
    print("💾 Saving data to CSV files...")
    departments_df.to_csv(data_dir / "departments.csv", index=False)
    categories_df.to_csv(data_dir / "categories.csv", index=False)
    subcategories_df.to_csv(data_dir / "subcategories.csv", index=False)
    products_df.to_csv(data_dir / "products.csv", index=False)
    
    # Print summary statistics
    print("\n✅ Data generation complete!")
    print("📈 Summary Statistics:")
    print(f"   • Departments: {len(departments_df)}")
    print(f"   • Categories: {len(categories_df)}")
    print(f"   • Subcategories: {len(subcategories_df)}")
    print(f"   • Products: {len(products_df)}")
    print(f"   • Total data points: {len(departments_df) + len(categories_df) + len(subcategories_df) + len(products_df)}")
    
    # Show sample data
    print("\n📋 Sample Products:")
    sample_products = products_df.sample(min(5, len(products_df)))
    for _, product in sample_products.iterrows():
        print(f"   • {product['name']} - ${product['price']} ({product['stock_quantity']} {product['unit']})")
    
    print(f"\n📁 Data saved to: {data_dir.absolute()}")
    print("🚀 Ready to run: streamlit run app.py")

if __name__ == "__main__":
    save_data() 