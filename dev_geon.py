import argparse

def parsing_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("-lr","--learning rate", default=0.001, type=float, help='learning rate')
    return parser.parse_args()

def main():
    args = parsing_argument()
    print("Trainging model Start")
    print(f"Learning rate: {args.lr}")
    print("------->")
    print("Finsihed!")

if __name__=="__main__":
    main()
