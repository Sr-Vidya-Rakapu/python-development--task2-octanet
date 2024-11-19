import os

class Item:
    """Class to represent an individual item."""
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        """Calculate total price for the item."""
        return self.price * self.quantity


class ReceiptCalculator:
    """Class to manage the receipt calculator functionalities."""
    def __init__(self):
        self.items = []
        self.tax_rate = 0.1  # Example: 10% tax
        self.discount_rate = 0.05  # Example: 5% discount

    def add_item(self, name, price, quantity):
        """Add an item to the receipt."""
        self.items.append(Item(name, price, quantity))

    def calculate_subtotal(self):
        """Calculate subtotal of all items."""
        return sum(item.get_total_price() for item in self.items)

    def calculate_tax(self, subtotal):
        """Calculate tax on the subtotal."""
        return subtotal * self.tax_rate

    def calculate_discount(self, subtotal):
        """Calculate discount on the subtotal."""
        return subtotal * self.discount_rate

    def calculate_final_total(self, subtotal, tax, discount):
        """Calculate the final total after tax and discount."""
        return subtotal + tax - discount

    def generate_receipt(self):
        """Generate a receipt string."""
        receipt_lines = []
        receipt_lines.append("------- Receipt -------")
        receipt_lines.append("Item\tQty\tPrice\tTotal")
        
        for item in self.items:
            receipt_lines.append(f"{item.name}\t{item.quantity}\t{item.price:.2f}\t{item.get_total_price():.2f}")
        
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax(subtotal)
        discount = self.calculate_discount(subtotal)
        final_total = self.calculate_final_total(subtotal, tax, discount)
        
        receipt_lines.append("-----------------------")
        receipt_lines.append(f"Subtotal:\t{subtotal:.2f}")
        receipt_lines.append(f"Tax:\t{tax:.2f}")
        receipt_lines.append(f"Discount:\t-{discount:.2f}")
        receipt_lines.append(f"Total:\t{final_total:.2f}")
        receipt_lines.append("-----------------------")

        return "\n".join(receipt_lines)

    def save_receipt(self, filename="receipt.txt"):
        """Save the receipt to a file."""
        receipt_content = self.generate_receipt()
        with open(filename, "w") as file:
            file.write(receipt_content)
        print(f"Receipt saved to {filename}")


# Main Functionality
if __name__ == "__main__":
    calculator = ReceiptCalculator()

    while True:
        print("\nAdd a new item to the receipt:")
        name = input("Enter item name (or 'done' to finish): ").strip()
        if name.lower() == "done":
            break
        try:
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            calculator.add_item(name, price, quantity)
        except ValueError:
            print("Invalid input. Please try again.")

    print("\nGenerating receipt...")
    print(calculator.generate_receipt())
    
    save_choice = input("Would you like to save the receipt? (yes/no): ").strip().lower()
    if save_choice == "yes":
        filename = input("Enter filename (default 'receipt.txt'): ").strip()
        filename = filename if filename else "receipt.txt"
        calculator.save_receipt(filename)
