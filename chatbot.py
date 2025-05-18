# chatbot 
import time
def chatbot():
    print("🤖 ChAtBoT")
    print()
    def ask():
        name = input("Enter Your name : ")
        print(f"Hello {name} ! Welcome to chatbot." ) 
        print()
        answer = str(input(f"can i ask you a Question {name} ? (y/n): ")).lower()

        if answer == "y":
            location = input(f"Where are you from ?")
            print()
            print(f"Wow {location} sounds awsome {name}.")
    
        
            def describe():
                print()    
                dest = str(input(f"Can you describe {location} in one word {name}."))
                if dest  not in {"shitty", "worst", "bad","worst","sick"}:
                    print(f" cool dude. sounds you are living in peace.")
                else:
                    print("preety sad dude.")
            describe()       
            
            def next():
                print()   
                print("lets move into next topic")
                print()
                it = str(input(f"is it ok {name} (y/n) :")).lower()
                print()
                if it == "y":
                    age = int(input(f"can you tell me your age {name}"))
                    if age <= 18:
                        print(f"lol {name} you are smaller than me !")
                    else:
                        print(f"you are bigger than me. isn't it concerinng {name}")
                else:
                    print(f"Thankyou {name}")
            next()
            
            def height():
                print()
                heit= float(input("what's your height dude ?"))
                if heit > 6.0 :
                    print(f"nice heignt bro. I think you should try some sports.")
                else:
                    print("grow up baby! feeling sorry for you.")

            height()       

        else:
            print("Sorry for distrubance 😢")
        
    ask()

chatbot()