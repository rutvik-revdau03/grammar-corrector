import argparse
import sys
import os
from app.services.grammar_service import correct_text
from app.core.validator import validate_text

def run_prompt():
    """Interactive mode using input()"""
    print("\n--- Interactive Grammar Correction (Type 'exit' to quit) ---")
    while True:
        text = input("\nEnter sentence: ").strip()
        if text.lower() in ['exit', 'quit']:
            break
        if not text:
            continue
        try:
            # Re-use existing validation logic
            validate_text(text)
            corrected = correct_text(text)
            print(f"Original:  {text}")
            print(f"Corrected: {corrected}")
        except Exception as e:
            print(f"Error: {str(e)}")

def run_file(file_path):
    """File processing mode"""
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return

    print(f"\n--- Correcting sentences from file: {file_path} ---")
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            sentence = line.strip()
            # Skip empty lines or header comments
            if not sentence or sentence.startswith('='):
                continue
            
            try:
                # We skip validation for file batching if needed, or apply it
                corrected = correct_text(sentence)
                print(f"Original:  {sentence}")
                print(f"Corrected: {corrected}\n")
            except Exception as e:
                print(f"Error in line: {sentence} -> {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Grammar Correction CLI Utility")
    
    # Define flags
    parser.add_argument("--text", type=str, help="Single sentence to correct directly from CLI")
    parser.add_argument("--file", type=str, help="Path to a .txt file containing sentences")
    parser.add_argument("--interactive", action="store_true", help="Start interactive prompt mode")

    args = parser.parse_args()

    # Priority logic: 
    # 1. Single text flag
    # 2. File flag
    # 3. Interactive mode (default if no args provided)
    
    if args.text:
        try:
            validate_text(args.text)
            corrected = correct_text(args.text)
            print(f"Original:  {args.text}")
            print(f"Corrected: {corrected}")
        except Exception as e:
            print(f"Error: {str(e)}")
    
    elif args.file:
        run_file(args.file)
    
    else:
        # Default to interactive mode if no arguments or specifically requested
        run_prompt()

if __name__ == "__main__":
    main()
