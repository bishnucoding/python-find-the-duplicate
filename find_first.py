class FindDuplicate:
    def __init__(self) -> None:
        pass

    def find_duplicate(self, input) -> int:
        tortoise = input[0]
        rabbit = input[input[0]]

        while tortoise != rabbit:
            tortoise = input[tortoise]
            rabbit = input[input[rabbit]]
        
        tortoise = 0   
        while tortoise != rabbit:
            tortoise = input[tortoise] 
            rabbit = input[rabbit]
        return tortoise    
   
