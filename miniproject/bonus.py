import sys
from checkmate import checkmate

def solve():
    
    if len(sys.argv) < 2:
        print("Error: Please provide a board file.")
        return


    for filename in sys.argv[1:]:
        try:
            
            with open(filename, 'r') as f:
                board_content = f.read()
                
            
            print(f"--- Checking {filename} ---")
            checkmate(board_content)
            print("") 

        except FileNotFoundError:
            
            print(f"Error: File '{filename}' not found.")
        except Exception as e:
            
            print(f"Error reading '{filename}': {e}")

if __name__ == "__main__":
    solve()