#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: April 25, 2025
# Program that displays a sequence of rgb color codes
# from [0,0,0] to [255,255,255]


def main():
    # RED
    for r in range(0, 256, 15):
        # GREEN
        for g in range(0, 256, 15):
            # BLUE
            for b in range(0, 256, 15):
                # COLOR
                print(f"\033[38;2;{r};{g};{b}m", end="")
                # RGB(RED, GREEN, BLUE)
                print(f"RGB({r:03d},{g:03d},{b:03d})")
    # Program completion message
    print("Thanks for Playing!")


if __name__ == "__main__":
    main()
