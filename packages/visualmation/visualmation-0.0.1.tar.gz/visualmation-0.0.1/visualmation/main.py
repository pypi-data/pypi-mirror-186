
import argparse

def main():
    
    parser = argparse.ArgumentParser(
        description='kamilu: computer graphics animation engine'
    )
    parser.add_argument('cmd',type=str,nargs='*',help='command line parse')
    
    args = parser.parse_args()
    
    



if __name__ == '__main__':
    main()