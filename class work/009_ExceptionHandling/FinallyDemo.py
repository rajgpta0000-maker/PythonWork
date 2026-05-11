def test():
    try:
        a = int(input("Enter a number: "))
        return a
    except Exception as e:
            return e
    finally:
        print("Hello..Program ended")
print(test())