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
        ordinal = data.ordinal
        name_list = data.name
        height_list = data.height
        
        height_list = height_list.tolist()
        
        return [list(group) for key, group in groupby(height_list)]
    
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
        
