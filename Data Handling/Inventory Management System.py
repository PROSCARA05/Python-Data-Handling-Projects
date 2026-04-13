# inventory_manager.py
"""
Inventory Management System
Demonstrates: dictionaries, list comprehension, sorting, filtering
"""

class InventoryManager:
    def __init__(self):
        self.inventory = {}
        self.transactions = []
    
    def add_product(self, product_id, name, price, quantity):
        """Add a new product to inventory"""
        if product_id in self.inventory:
            print(f"Product {product_id} already exists! Use update instead.")
            return
        
        self.inventory[product_id] = {
            'name': name,
            'price': price,
            'quantity': quantity
        }
        self._log_transaction('ADD', product_id, quantity)
        print(f"Added {name} (ID: {product_id})")
    
    def update_stock(self, product_id, quantity_change):
        """Update product quantity (positive for restock, negative for sale)"""
        if product_id not in self.inventory:
            print(f"Product {product_id} not found!")
            return
        
        old_qty = self.inventory[product_id]['quantity']
        new_qty = old_qty + quantity_change
        
        if new_qty < 0:
            print(f"Insufficient stock! Only {old_qty} available.")
            return
        
        self.inventory[product_id]['quantity'] = new_qty
        transaction_type = 'RESTOCK' if quantity_change > 0 else 'SALE'
        self._log_transaction(transaction_type, product_id, abs(quantity_change))
        
        print(f"Updated {self.inventory[product_id]['name']}: {old_qty} → {new_qty}")
    
    def _log_transaction(self, trans_type, product_id, quantity):
        """Internal method to log transactions"""
        from datetime import datetime
        self.transactions.append({
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'type': trans_type,
            'product_id': product_id,
            'quantity': quantity
        })
    
    def search_product(self, search_term):
        """Search products by name or ID"""
        results = []
        search_term = search_term.lower()
        
        for pid, info in self.inventory.items():
            if search_term in pid.lower() or search_term in info['name'].lower():
                results.append((pid, info))
        
        return results
    
    def display_inventory(self):
        """Display all products in inventory"""
        if not self.inventory:
            print("Inventory is empty!")
            return
        
        print(f"\n{'='*60}")
        print("CURRENT INVENTORY")
        print(f"{'='*60}")
        print(f"{'ID':<10} {'Name':<20} {'Price':<10} {'Quantity':<10}")
        print("-"*60)
        
        total_value = 0
        for pid, info in self.inventory.items():
            value = info['price'] * info['quantity']
            total_value += value
            print(f"{pid:<10} {info['name']:<20} ${info['price']:<9.2f} {info['quantity']:<10}")
        
        print("-"*60)
        print(f"Total Inventory Value: ${total_value:.2f}")
    
    def low_stock_alert(self, threshold=5):
        """Show products with quantity below threshold"""
        low_stock = {pid: info for pid, info in self.inventory.items() 
                    if info['quantity'] < threshold}
        
        if low_stock:
            print(f"\nLOW STOCK ALERT (Below {threshold}):")
            for pid, info in low_stock.items():
                print(f"{info['name']} (ID: {pid}) - Only {info['quantity']} left!")
        else:
            print(f"\nNo low stock items (threshold: {threshold})")
    
    def transaction_history(self, limit=10):
        """Show recent transactions"""
        if not self.transactions:
            print("No transactions recorded!")
            return
        
        print(f"\n{'='*60}")
        print("RECENT TRANSACTIONS")
        print(f"{'='*60}")
        
        for trans in self.transactions[-limit:]:
            print(f"{trans['timestamp']} | {trans['type']:<7} | "
                  f"Product: {trans['product_id']} | Qty: {trans['quantity']}")

def run_inventory_system():
    manager = InventoryManager()
    
    # Sample data
    manager.add_product("P001", "Laptop", 999.99, 10)
    manager.add_product("P002", "Mouse", 24.99, 50)
    manager.add_product("P003", "Keyboard", 79.99, 25)
    
    while True:
        print("\n" + "="*40)
        print("INVENTORY MANAGEMENT SYSTEM")
        print("="*40)
        print("1. Add Product")
        print("2. Update Stock")
        print("3. Search Product")
        print("4. View Inventory")
        print("5. Low Stock Alert")
        print("6. Transaction History")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == '1':
            pid = input("Product ID: ")
            name = input("Product Name: ")
            try:
                price = float(input("Price: R"))
                quantity = int(input("Quantity: "))
                manager.add_product(pid, name, price, quantity)
            except ValueError:
                print("Invalid input!")
        
        elif choice == '2':
            pid = input("Product ID: ")
            try:
                change = int(input("Quantity change (+ for restock, - for sale): "))
                manager.update_stock(pid, change)
            except ValueError:
                print("Invalid input!")
        
        elif choice == '3':
            term = input("Enter search term: ")
            results = manager.search_product(term)
            if results:
                print(f"\nFound {len(results)} product(s):")
                for pid, info in results:
                    print(f"{info['name']} (ID: {pid}) - R{info['price']} - Stock: {info['quantity']}")
            else:
                print("No products found!")
        
        elif choice == '4':
            manager.display_inventory()
        
        elif choice == '5':
            try:
                threshold = int(input("Enter threshold (default 5): ") or "5")
                manager.low_stock_alert(threshold)
            except ValueError:
                manager.low_stock_alert()
        
        elif choice == '6':
            manager.transaction_history()
        
        elif choice == '7':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    run_inventory_system()