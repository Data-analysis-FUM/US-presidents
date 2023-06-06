class presidents:
    def __init__(data, dataset):
        data.df = dataset
        data.ordinal = data.df[0]
        data.name = data.df[1]
        data.height = data.df[2]
        
        
        
    def header(data):
        return(data.df.head())
    
    
    def less180(data):#It counts the number of presidents whose height was more than 180 cm
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
        ordinal = data.ordinal
        name_list = data.name
        height_list = data.height
        
        resault = []
        
        counter = 0
        while counter < len(name_list):
            if target in name_list[counter]:
                element = [ordinal[counter], name_list[counter], height_list[counter]]
                resault.append(element)
            counter = counter + 1
            
        return(resault)
    
    
            
    def maximum_height(data):
        ordinal = data.ordinal
        name_list = data.name
        height_list = data.height
        
        resault = []
        
        maximum_height = height_list.max()
        resault.append(maximum_height)
                
        counter = 0
        while counter < len(name_list):
            if height_list[counter] == maximum_height:
                element = [ordinal[counter], name_list[counter]]
                resault.append(element)
            
            counter = counter + 1
            
        return(resault)
    
    def taller_than_Obama(data):
        target = "Barack Obama"
        ordinal = data.ordinal
        name_list = data.name
        height_list = data.height
        
        n = name_list.tolist()
        obama_index = n.index(target)
        obama_height = height_list[obama_index]
        
        
        resault = []
        
        counter = 0
        while counter < len(name_list):
            if height_list[counter] > obama_height:
                element = [ordinal[counter], name_list[counter], height_list[counter]]
                resault.append(element)
            counter = counter + 1
            
        return(resault)
    
    
    def douplicated_height(data):
        
        groups = data.df.groupby(2)
        
        for height, group in groups:
            douplicate = []
            if len(group) > 1:
                names = ", ".join(group[1].tolist())
                print(f"   Presidents with height {height} cm: {names}")      
        
    
    def plot(data):
        ordinal = data.ordinal
        name_list = data.name
        height_list = data.height
        
        height_list = height_list.tolist()
        
        c = []
        
        for height in height_list:
            curr_height = height_list[height_list.index(height)]
            
            darkness = ((curr_height - 160) / 40) + 0.1
            curr_c = (0.2, 0.4, 0.6, darkness)
            
            c.append(curr_c)
        
        plt.figure().set_figwidth(15)
        plt.grid()
        
        plt.bar(data.df[1], data.df[2], color = c)
        plt.xticks(rotation=90)
        plt.ylabel('Height (cm)')
        plt.ylim([min(height_list)-1, max(height_list)+1])
        
        plt.show()
        
        
    def monitoring(data):
        print("1)How many American presidents were less than 180 cm tall?")
        print("   ", data.less180(), " presidents were less than 180 cm.", sep="")
        
        print("2)How tall was Roosevelt?")
        rosvelts = data.find_Roosevelt()
        for counter in rosvelts:
            print("   ", rosvelts[rosvelts.index(counter)][1], " was: ", rosvelts[rosvelts.index(counter)][2], "cm", sep="")
        
        
        print("3)Who was the tallest American president?")
        mx = data.maximum_height()
        print("   Maximum height between American presidents is: ", mx[0], "cm", sep="")
        print("   Tallest presidens:")
        for counter in mx:
            if mx.index(counter) != 0:
                print("      ", mx[mx.index(counter)][1], sep="")
                
        
        print("4)The tallest president(s) of America, how many president(s) of the United States?")
        mx = data.maximum_height()
        for counter in mx:
            if mx.index(counter) != 0:
                print("   ", mx[mx.index(counter)][1], " was ", mx[mx.index(counter)][0], "th president of US.", sep="")
                
        print("5)Which presidents have been taller than Obama?")
        to = data.taller_than_Obama()
        for counter in to:
            print("   ", to[to.index(counter)][1], " was: ", to[to.index(counter)][2]-185, "cm taller than Barack Obama!", sep="")
        
        
        print("6)Which presidents have had the same height?")
        data.douplicated_height()
        
        
        print("7)Display a bar graph of their height. The vertical axis of the president's name and the length of the bar should indicate his height. The order of the vertical axis should be the same as the original order of the data.")
        data.plot()
        
        
        
