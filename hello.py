# 🚀 Lab 2: Python Program
# 📝 This script demonstrates basic branching concepts with a fun program!

def greet_branch(branch_name):
    """
    Function to display a greeting message for a specific branch.
    """
    print(f"🌿 Welcome to the {branch_name} branch!")
    print("🔧 This branch is focused on learning Git and GitHub.")
    print("💡 Remember: Keep committing frequently and write meaningful commit messages!")
    print("\nHappy Coding!\n")

def main():
    print("📌 Lab 2 Python Program\n")
    
    # Prompt the user to enter a branch name
    branch_name = input("Enter the branch name you are working on: ").strip()
    
    # Call the greet_branch function with the provided branch name
    greet_branch(branch_name)
    
    # Display a closing message
    print("✅ You've successfully completed the Lab 2 Python Program!")

if __name__ == "__main__":
    main()
