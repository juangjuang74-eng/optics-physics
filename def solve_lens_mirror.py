def solve_lens_mirror():
    print("\n--- Advanced Lens & Mirror Solver ---")
    print("Instructions: Enter known values. Press 'Enter' for the unknown value.")
    print("Sign Convention Reminder:")
    print("  - Focal Length (f): (+) Converging, (-) Diverging")
    print("  - Object Distance (do): (+) Real Object")
    print("  - Image Distance (di): (+) Real Image, (-) Virtual Image")
    
    # Get inputs (leave one blank)
    f_in = input("Focal Length (f): ").strip()
    do_in = input("Object Distance (do): ").strip()
    di_in = input("Image Distance (di): ").strip()
    
    f, do, di = None, None, None

    try:
        # LOGIC: 1/f = 1/do + 1/di
        
        # Case 1: Solve for Focal Length (f)
        if f_in == "":
            do = float(do_in)
            di = float(di_in)
            if do == 0 or di == 0: raise ValueError("Distances cannot be zero.")
            val = (1/do) + (1/di)
            f = 1 / val
            print(f"\n-> Calculated Focal Length (f): {f:.2f} cm")

        # Case 2: Solve for Object Distance (do)
        elif do_in == "":
            f = float(f_in)
            di = float(di_in)
            val = (1/f) - (1/di)
            if val == 0:
                print("\n-> Object is at infinity.")
                return
            do = 1 / val
            print(f"\n-> Calculated Object Distance (do): {do:.2f} cm")

        # Case 3: Solve for Image Distance (di)
        elif di_in == "":
            f = float(f_in)
            do = float(do_in)
            if do == f:
                print("\n-> No Image Formed (Image is at infinity).")
                return
            val = (1/f) - (1/do)
            di = 1 / val
            print(f"\n-> Calculated Image Distance (di): {di:.2f} cm")
            
        else:
            print("Error: You must leave exactly one field blank.")
            return

        # ANALYSIS AND MAGNIFICATION
        # Magnification formula: m = -di / do
        m = -di / do
        print(f"-> Magnification (m): {m:.2f}x")
        
        # Determine Image Properties
        print("\n--- Image Analysis ---")
        
        # 1. Type (Real vs Virtual)
        # For single lens/mirror: Positive di = Real, Negative di = Virtual
        if di > 0:
            print(f"Type:        REAL image (forms on a screen)")
        else:
            print(f"Type:        VIRTUAL image (forms 'inside' the optic)")

        # 2. Orientation (Upright vs Inverted)
        # Negative Magnification = Inverted, Positive = Upright
        if m < 0:
            print("Orientation: INVERTED (Upside down)")
        else:
            print("Orientation: UPRIGHT (Right side up)")

        # 3. Size (Magnified vs Diminished)
        if abs(m) > 1:
            print("Size:        LARGER than object")
        elif abs(m) < 1:
            print("Size:        SMALLER than object")
        else:
            print("Size:        SAME SIZE as object")

    except ValueError:
        print("\nError: Please enter valid numbers. Ensure you aren't dividing by zero.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    while True:
        solve_lens_mirror()
        again = input("\nSolve another? (y/n): ")
        if again.lower() != 'y':
            break