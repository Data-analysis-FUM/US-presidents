class presidents:
    def __init__(data, dataset):
        data.df = dataset
        data.ordinal = data.df[0]
        data.name = data.df[1]
        data.height = data.df[2]
        
    def header(data):
        return(data.df.head())
    
    def Uper180(data):#It counts the number of presidents whose height was more than 180 cm
        counter = 0
        h = data.height
        i = 0
        while i < len(h):
            if(h[i]<180):
                counter = counter + 1
            i = i + 1
            
        return(counter)
    
    def find_Roosevelt(data):#Finds the height of people named Roosevelt
        target = "Roosevelt";
        name_list = data.name
        height_list = data.height
        counter = 0
        while counter < len(name_list):
            if target in name_list[counter]:
                print("height of ", name_list[counter], " is: ", height_list[counter], "cm", sep="")
            
            counter = counter + 1
            
    def maximum_height(data):
        name_list = data.name
        height_list = data.height
        
        maximum_height = height_list.max()
        print("Maximum height is: ", maximum_height, "cm", sep="")
        
        counter = 0
        print("The tallest presidents are:")
        while counter < len(name_list):
            if height_list[counter] == maximum_height:
                print(name_list[counter])
                
            
            counter = counter + 1
        
        
