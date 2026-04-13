# data_analyzer.py
"""
Data Analysis Tool
Demonstrates: file I/O, data processing, statistics, list comprehensions
"""

import csv
import json
from statistics import mean, median, stdev

class DataAnalyzer:
    def __init__(self):
        self.data = []
        self.headers = []
    
    def load_csv(self, filename):
        """Load data from CSV file"""
        try:
            with open(filename, 'r') as file:
                reader = csv.DictReader(file)
                self.headers = reader.fieldnames
                self.data = list(reader)
                
                # Convert numeric columns
                for row in self.data:
                    for key in row:
                        try:
                            row[key] = float(row[key])
                        except ValueError:
                            pass  # Keep as string if not numeric
            
            print(f"Loaded {len(self.data)} records from {filename}")
            return True
        except FileNotFoundError:
            print(f"File {filename} not found!")
            return False
        except Exception as e:
            print(f"Error loading file: {e}")
            return False
    
    def load_json(self, filename):
        """Load data from JSON file"""
        try:
            with open(filename, 'r') as file:
                self.data = json.load(file)
                if self.data and isinstance(self.data[0], dict):
                    self.headers = list(self.data[0].keys())
            
            print(f"Loaded {len(self.data)} records from {filename}")
            return True
        except FileNotFoundError:
            print(f"File {filename} not found!")
            return False
        except Exception as e:
            print(f"Error loading file: {e}")
            return False
    
    def generate_sample_data(self):
        """Generate sample data for demonstration"""
        self.data = [
            {'name': 'Product A', 'sales': 150, 'price': 25.99, 'rating': 4.5},
            {'name': 'Product B', 'sales': 230, 'price': 19.99, 'rating': 4.2},
            {'name': 'Product C', 'sales': 98, 'price': 49.99, 'rating': 4.8},
            {'name': 'Product D', 'sales': 310, 'price': 15.99, 'rating': 3.9},
            {'name': 'Product E', 'sales': 175, 'price': 32.50, 'rating': 4.1},
            {'name': 'Product F', 'sales': 45, 'price': 89.99, 'rating': 4.7},
            {'name': 'Product G', 'sales': 267, 'price': 12.99, 'rating': 4.3},
            {'name': 'Product H', 'sales': 189, 'price': 27.99, 'rating': 4.0},
        ]
        self.headers = list(self.data[0].keys())
        print(f"Generated {len(self.data)} sample records")
    
    def analyze_column(self, column_name):
        """Perform statistical analysis on a numeric column"""
        values = [row[column_name] for row in self.data 
                 if isinstance(row.get(column_name), (int, float))]
        
        if not values:
            print(f"Column '{column_name}' has no numeric data!")
            return None
        
        print(f"\nAnalysis of '{column_name}':")
        print(f"{'='*40}")
        print(f"Count:     {len(values)}")
        print(f"Sum:       {sum(values):.2f}")
        print(f"Mean:      {mean(values):.2f}")
        print(f"Median:    {median(values):.2f}")
        print(f"Min:       {min(values):.2f}")
        print(f"Max:       {max(values):.2f}")
        
        if len(values) > 1:
            print(f"Std Dev:   {stdev(values):.2f}")
        
        return {
            'count': len(values),
            'sum': sum(values),
            'mean': mean(values),
            'median': median(values),
            'min': min(values),
            'max': max(values)
        }
    
    def filter_data(self, column, operator, value):
        """Filter data based on condition"""
        filtered = []
        
        for row in self.data:
            if column not in row:
                continue
            
            row_value = row[column]
            
            if operator == '>':
                if row_value > value:
                    filtered.append(row)
            elif operator == '<':
                if row_value < value:
                    filtered.append(row)
            elif operator == '==':
                if row_value == value:
                    filtered.append(row)
            elif operator == '>=':
                if row_value >= value:
                    filtered.append(row)
            elif operator == '<=':
                if row_value <= value:
                    filtered.append(row)
        
        print(f"\nFiltered: {len(filtered)} records where {column} {operator} {value}")
        return filtered
    
    def sort_data(self, column, ascending=True):
        """Sort data by a column"""
        sorted_data = sorted(self.data, 
                           key=lambda x: x.get(column, 0) if isinstance(x.get(column), (int, float)) else str(x.get(column, '')),
                           reverse=not ascending)
        return sorted_data
    
    def display_data(self, limit=10):
        """Display data in table format"""
        if not self.data:
            print("No data to display!")
            return
        
        print(f"\n{'='*80}")
        print(f"DATA DISPLAY (Showing {min(limit, len(self.data))} of {len(self.data)} records)")
        print(f"{'='*80}")
        
        # Display headers
        header_row = " | ".join([f"{h:<15}" for h in self.headers])
        print(header_row)
        print("-" * len(header_row))
        
        # Display rows
        for row in self.data[:limit]:
            values = []
            for h in self.headers:
                val = row.get(h, '')
                if isinstance(val, float):
                    values.append(f"{val:<15.2f}")
                else:
                    values.append(f"{str(val):<15}")
            print(" | ".join(values))
    
    def export_report(self, filename):
        """Export analysis report to file"""
        report = {
            'data_summary': {
                'total_records': len(self.data),
                'columns': self.headers
            },
            'analyses': {}
        }
        
        # Analyze each numeric column
        for col in self.headers:
            try:
                analysis = self.analyze_column(col)
                if analysis:
                    report['analyses'][col] = analysis
            except:
                pass
        
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"Report exported to {filename}")

def run_data_analyzer():
    analyzer = DataAnalyzer()
    
    # Start with sample data
    analyzer.generate_sample_data()
    
    while True:
        print("\n" + "="*40)
        print("DATA ANALYSIS TOOL")
        print("="*40)
        print("1. Load CSV File")
        print("2. Load JSON File")
        print("3. Analyze Column")
        print("4. Filter Data")
        print("5. Sort Data")
        print("6. Display Data")
        print("7. Export Report")
        print("8. Exit")
        
        choice = input("\nEnter your choice (1-8): ")
        
        if choice == '1':
            filename = input("Enter CSV filename: ")
            analyzer.load_csv(filename)
        
        elif choice == '2':
            filename = input("Enter JSON filename: ")
            analyzer.load_json(filename)
        
        elif choice == '3':
            print(f"Available columns: {analyzer.headers}")
            col = input("Enter column name to analyze: ")
            analyzer.analyze_column(col)
        
        elif choice == '4':
            print(f"Available columns: {analyzer.headers}")
            col = input("Enter column name: ")
            op = input("Enter operator (>, <, ==, >=, <=): ")
            try:
                val = float(input("Enter value: "))
                filtered = analyzer.filter_data(col, op, val)
                if filtered:
                    print("\nFiltered Results:")
                    for item in filtered[:10]:
                        print(f"  {item}")
            except ValueError:
                print("Invalid value!")
        
        elif choice == '5':
            col = input("Enter column to sort by: ")
            order = input("Ascending? (y/n): ").lower() == 'y'
            sorted_data = analyzer.sort_data(col, order)
            analyzer.data = sorted_data
            print("Data sorted!")
        
        elif choice == '6':
            try:
                limit = int(input("Number of records to display (default 10): ") or "10")
                analyzer.display_data(limit)
            except ValueError:
                analyzer.display_data()
        
        elif choice == '7':
            filename = input("Enter report filename (e.g., report.json): ")
            analyzer.export_report(filename)
        
        elif choice == '8':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    run_data_analyzer()