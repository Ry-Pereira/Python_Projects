import random
import server






def main():
    server.random_number = random.randint(0,9)
    server.app.run()
    



if __name__ == "__main__":
    main()