shut=str(input("Enter if you want to shut down or not: "))

def shutdown():
    if shut=="yes":
        print("Shutting down...")
    elif shut=="no":
        print("Abort shutdown")
    else:
        print("Sorry")

shutdown()