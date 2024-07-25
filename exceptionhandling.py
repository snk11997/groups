# while True:
#     try:
#         a=int(input("enter a 1 st no"))
#         b=int(input("enter a second number"))
#         c=a/b
#     except ValueError:
#         print("INT value only accepted ")

#     except ZeroDivisionError:
#         print(" can not divisible by zero")

#     else:
#         print("no error")
#         break

#     finally:
#         print("finally block")
            

# while True:
#     try:
#         a=(10,20,30,40,50,60,70)
#         n=int(input("enter a second number"))
#         print(a[n])
      
#         import threading
#     except IndexError:
#         print("enter the valid index ")
#     except AttributeError:
#         print(" can not divisible by zero")
#     except ImportError:
#         print("check correct spelling for import module name")
#     else:
#         #print("no error")
#         break

#     finally:
#         print("finally block")



while True:
    try:
        a=(10,20,30,40,50,60,70)
        n=int(input("enter a  number"))
        print(a[n])
      
        import threading
    except IndexError:
        print("enter the valid index ") 
    except AttributeError:
        print(" can not divisible by zero")
    except ImportError:
        print("check correct spelling for import module name")
    else:
        #print("no error")
        break

    finally:
        print("finally block")




# while True:
   
#    num=int(input("enter the number"))
#    if num>0:
#        raise Exception("enter number less than one")
#    print(num)


