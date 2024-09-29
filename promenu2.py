class Merchandise:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Sale:
    def __init__(self, merchandise, quantity, region):
        self.merchandise = merchandise
        self.quantity = quantity
        self.total_price = merchandise.price * quantity
        self.region = region

class TeamMerchandisingRevenueSystem:
    def __init__(self):
        self.merchandise_list = []
        self.sales_records = []

    # CRUD operations for merchandise
    def add_merchandise(self, merchandise):
        self.merchandise_list.append(merchandise)

    def delete_merchandise(self, merchandise_name):
        self.merchandise_list = [item for item in self.merchandise_list if item.name != merchandise_name]

    def get_merchandise(self):
        return self.merchandise_list

    # Add a sales record
    def record_sale(self, sale):
        self.sales_records.append(sale)

    # Track and display total revenue
    def total_revenue(self):
        return sum(sale.total_price for sale in self.sales_records)

    # Unified analysis by product, store, and region
    def analyze_sales(self):
        product_sales = {}
        region_sales = {}

        for sale in self.sales_records:
            # Track sales by product
            product = sale.merchandise.name
            if product not in product_sales:
                product_sales[product] = 0
            product_sales[product] += sale.total_price

            # Track sales by region
            region = sale.region
            if region not in region_sales:
                region_sales[region] = 0
            region_sales[region] += sale.total_price

        return product_sales, region_sales

# Function to display the menu
def display_menu():
    print("\n1. Add Merchandise")
    print("2. Delete Merchandise")
    print("3. Record Sale")
    print("4. Display Total Revenue")
    print("5. Analyze Sales")
    print("6. View Merchandise List")
    print("7. Exit")

# Main interactive function
if __name__ == "__main__":
    system = TeamMerchandisingRevenueSystem()
    
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            # Add Merchandise
            name = input("Enter merchandise name: ")
            price = float(input("Enter merchandise price: "))
            merchandise = Merchandise(name, price)
            system.add_merchandise(merchandise)
            print(f"Merchandise '{name}' added.")
        
        elif choice == 2:
            # Delete Merchandise
            name = input("Enter merchandise name to delete: ")
            system.delete_merchandise(name)
            print(f"Merchandise '{name}' deleted.")
        
        elif choice == 3:
            # Record Sale
            merchandise_name = input("Enter merchandise name: ")
            merchandise = next((m for m in system.get_merchandise() if m.name == merchandise_name), None)
            if merchandise:
                quantity = int(input("Enter quantity sold: "))
                region = input("Enter region name: ")
                sale = Sale(merchandise, quantity, region)
                system.record_sale(sale)
                print(f"Sale recorded for {merchandise_name}.")
            else:
                print(f"Merchandise '{merchandise_name}' not found.")
        
        elif choice == 4:
            # Display Total Revenue
            print(f"Total Revenue: ₹{system.total_revenue()}")
        
        elif choice == 5:
            # Unified Sales Analysis
            product_sales, region_sales = system.analyze_sales()
            
            print("\nSales by Product:")
            for product, revenue in product_sales.items():
                print(f"{product}: ₹{revenue}")
            
            print("\nSales by Region:")
            for region, revenue in region_sales.items():
                print(f"{region}: ₹{revenue}")
        
        elif choice == 6:
            # View Merchandise List
            print("\nMerchandise List:")
            for item in system.get_merchandise():
                print(f"{item.name} - ₹{item.price}")
        
        elif choice == 7:
            # Exit
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please try again.")
