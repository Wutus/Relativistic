import app
import argparse

def main():
    a = app.App()
    parser = argparse.ArgumentParser()
    parser.add_argument("x1", type=float)
    parser.add_argument("y1", type=float)
    parser.add_argument("vx1", type=float)
    parser.add_argument("vy1", type=float)
    parser.add_argument("x2", type=float)
    parser.add_argument("y2", type=float)
    parser.add_argument("vx2", type=float)
    parser.add_argument("vy2", type=float)
    args = parser.parse_args()
    a.run((args.x1, args.y1), (args.vx1, args.vy1), (args.x2, args.y2), (args.vx2, args.vy2))  

main()