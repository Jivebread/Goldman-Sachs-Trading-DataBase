class Matcher:
    """
     Matcher has 6 functions which are used to 
     create , ammend , cacel , match and query the data
    
    Attributes:
        buyBook: a dictionary data type, this is used to hash buy order in terms of their order ID
        sellBook:a dictionary data type, this is used to hash sell order in terms of their order ID
        
    """
    buyBook = {}
    sellBook= {}
    past_timestamp = 0
    """
    Mat function takes the action from the command list and sends it to designated functions
         Attributes: 
                    
    """
    def Mat():
        if len(s) == 0:
            try:
                raise InputValueError('','T',book["Order_ID"])
            except InputValueError('','T',book["Order_ID"]) as e:
                print(e.message)
        else:
            s = input().split(",")
            Command=s[0]
        
            if(Command=='N'):
                if input_check(s,self.past_timestamps):
                    Matcher.new(s)
            elif(Command=='A'):
                if input_check(s,self.past_timestamps):
                    Matcher.ammend(s)
            elif(Command=='X'):
                if input_check(s,self.past_timestamps):
                    Matcher.cancel(s)
            elif(Command=='M'):
                if input_check(s,self.past_timestamps):
                    s+=","
                    Matcher.match(s)
            elif(Command=='Q'):
                if input_check(s,self.past_timestamps):
                    s+=","+","
                    Matcher.Query(s)
            else:
                try:
                    raise InputValueError('','T',0)
                except InputValueError('','T',0) as e:
                    print(e.message)
                
    """
    This function creates new 
    """
    
    def new(s):
        book={}
        book["Order_ID"]=s[1]
        book["time_stamp"]=s[2]
        book["symbol"]=s[3]
        book["order-type"]=s[4]
        book["side"]=s[5]
        book["price"]=s[6]
        book["quantity"]=s[7]
        if(s[5]=='B'):
            Matcher.buyBook[s[1]]=book
            print(Matcher.buyBook)
        else:
            Matcher.sellBook[s[1]]=book
            print(Matcher.sellBook)
    
    def ammend(s):
        
        book={}
        book["Order_ID"]=s[1]
        book["time_stamp"]=s[2]
        book["symbol"]=s[3]
        book["order-type"]=s[4]
        book["side"]=s[5]
        book["price"]=s[6]
        book["quantity"]=s[7]
    
        if(s[1] in Matcher.buyBook.keys()):
            Matcher.buyBook[s[1]]=book
            print(Matcher.buyBook)
        elif(s[1] in Matcher.sellBook.keys()):
            Matcher.sellBook[s[1]]=book
            print(Matcher.sellBook)
        else:
            try:
                raise InputValueError('','A',book["Order_ID"])
            except InputValueError('','N',book["Order_ID"]) as e:
                print(e.message)
            
    def cancel(s):
        
        if(s[1] in Matcher.buyBook.keys()):
            del Matcher.buyBook[s[1]]
            print(Matcher.buyBook)
        elif(s[1] in Matcher.sellBook.keys()):
            del Matcher.sellBook[s[1]]
            print(Matcher.sellBook)
        else:
            try:
                raise InputValueError('','C',book["Order_ID"])
            except InputValueError('','C',book["Order_ID"]) as e:
                print(e.message)
    
    def match(s):
        sBook=[]
        bBook=[]
        if(not s[1].isalpha()):
            for i in Matcher.buyBook.keys():
                if(Matcher.buyBook[i]['time_stamp']<=s[1]):
                    bBook.append(i)
            for j in Matcher.sellBook.keys():
                if(Matcher.sellBook[j]['time_stamp']<=s[1]):
                    sBook.append(j)
            
                        
        else:
            for i in Matcher.buyBook.keys():
                if(Matcher.buyBook[i]['time_stamp']<=s[1] and Matcher.buyBook[i]['symbol']==s[2]):
                    bBook.append(i)
            for j in Matcher.sellBook.keys():
                if(Matcher.sellBook[j]['time_stamp']<=s[1] and Matcher.sellBook[j]['symbol']==s[2]):
                    sBook.append(j)            
            
                
            for i in bBook:
                for j in sBook:
                    if((Matcher.buyBook[i]['price']==Matcher.sellBook[j]['price']) and (Matcher.buyBook[i]['symbol']==Matcher.sellBook[j]['symbol'])):
                        quantity_matched=(min(Matcher.buyBook[i]['quantity'],Matcher.sellBook[j]['quantity']))
                        print(Matcher.buyBook[i]['symbol']+"|"+Matcher.buyBook[i]['Order_ID']+","+Matcher.buyBook[i]['order-type']+","+quantity_matched+","
                        +Matcher.buyBook[i]['price']+"|"+Matcher.sellBook[j]['price']+","+quantity_matched+","+Matcher.sellBook[j]['order-type']+","+Matcher.sellBook[j]['Order_ID'])
                        Matcher.buyBook[i]['quantity']=str(abs(int(Matcher.buyBook[i]['quantity'])-int(quantity_matched)))
                        Matcher.sellBook[j]['quantity']=str(abs(int(Matcher.sellBook[i]['quantity'])-int(quantity_matched)))
    
                
    def Query(s):
        sBook=[]
        bBook=[]
        mbBook=[]
        sbBook=[]
        timeStamp=0
        matched=True
        symbol="x"
        if(s[1].isalpha() or s[1].isdigit()):
            if(s[2].isalpha() or s[2].isdigit()):
                if(len(s[1])>3):
                    timeStamp=s[1]
                    symbol=s[2]
                else:
                    timeStamp=s[2]
                    symbol=s[1]
                for i in Matcher.buyBook.keys():
                    if(Matcher.buyBook[i]['time_stamp']<=timeStamp and Matcher.buyBook[i]['symbol']==symbol):
                        bBook.append(i)
                for j in Matcher.sellBook.keys():
                    if(Matcher.buyBook[j]['time_stamp']<=timeStamp and Matcher.buyBook[j]['symbol']==symbol):
                        sBook.append(j)
            else:
                if((len(s[1]))>3):
                    timeStamp=s[1]
                    for i in Matcher.buyBook.keys():
                        if(Matcher.buyBook[i]['time_stamp']<=timeStamp):
                            bBook.append(i)
                    for j in Matcher.sellBook.keys():
                        if(Matcher.buyBook[j]['time_stamp']<=timeStamp):
                            sBook.append(j)
                else:
                    symbol=s[1]
                    for i in Matcher.buyBook.keys():
                        if(Matcher.buyBook[i]['symbol']==symbol):
                            bBook.append(i)
                    for j in Matcher.sellBook.keys():
                        if(Matcher.buyBook[j]['symbol']==symbol):
                            sBook.append(j)
                
        else:
            for i in Matcher.buyBook.keys():
                bBook.append(i)
            for j in Matcher.sellBook.keys():
                sBook.append(j)
        if(len(bBook)==0):
            sbBook=sBook
        if(len(sBook)==0):
             mbBook=bBook
    
                
        for i in bBook:
            for j in sBook:
                if((Matcher.buyBook[i]['price']==Matcher.sellBook[j]['price']) and (Matcher.buyBook[i]['symbol']==Matcher.sellBook[j]['symbol'])):
                    quantity_matched=(min(Matcher.buyBook[i]['quantity'],Matcher.sellBook[j]['quantity']))
                    print(Matcher.buyBook[i]['symbol']+"|"+Matcher.buyBook[i]['Order_ID']+","+Matcher.buyBook[i]['order-type']+","+quantity_matched+","
                    +Matcher.buyBook[i]['price']+"|"+Matcher.sellBook[j]['price']+","+quantity_matched+","+Matcher.sellBook[j]['order-type']+","+Matcher.sellBook[j]['Order_ID'])
                    matched=True and matched
                    sbBook.append(j)
                else:
                    matched=False and matched
                    
            if(not matched):
                mbBook.append(i) 
            
        if(len(mbBook)>0):
            for i in mbBook:
                print(Matcher.buyBook[i]['symbol']+"|"+Matcher.buyBook[i]['Order_ID']+","+Matcher.buyBook[i]['order-type']+","+Matcher.buyBook[i]['quantity']+","
                        +Matcher.buyBook[i]['price'])
                
        if((len(sBook)-len(sbBook))>0):
            for j in sBook:
                if(j not in sbBook):
                    print(Matcher.sellBook[j]['symbol']+"|"+Matcher.sellBook[j]['Order_ID']+","+Matcher.sellBook[j]['order-type']+","+Matcher.sellBook[j]['quantity']+","
                        +Matcher.sellBook[j]['price'])
    #command input checks
    def input_check(s, past_time):
        
        #Check timestamp and command
        #Check if the length of the arguments are 8.
        if len(s) == 8 and s[0] == 'N': 
            #check if the price and quantity is positive and timestamp is bigger than the past.
            if s[6] > 0 and s[7] > 0  and past_time < s[2] and type(s[7]) == int:
                self.past_timestamp = s[2]
                return True
            else:
                try:
                    raise InputValueError('','N',s[1])
                except InputValueError('','N',s[1]) as e:
                    print(e.message)
                    return False
                
        elif len(s) == 8 and s[0] == 'A':
            
            #check if the price and quantity is positive and timestamp is bigger than the past.
            if s[6] > 0 and s[7] > 0  and past_time < s[2] and isinstance(s[7], float):
                self.past_timestamp = s[2]
                return True
            else:
                try:
                    raise InputValueError('','A',s[1])
                except InputValueError('','A',s[1]) as e:
                    print(e.message)
        
        elif len(s) <= 3 and s[0] == 'M':
            #check if the price and quantity is positive and timestamp is bigger than the past.
            if past_time < s[1]:
                self.past_timestamp = s[1]
                return True
            else:
                try:
                    raise InputValueError('','M',0)
                except InputValueError('','M',0) as e:
                    print(e.message)
            
        elif len(s) <= 3 and s[0] == 'Q':
            return True
            
        elif len(s) == 3 and s[0] == 'X':
            if past_time < s[1]:
                self.past_timestamp = s[1]
                return True
            else:
                try:
                    raise InputValueError('','M',0)
                except InputValueError('','M',0) as e:
                    print(e.message)
            
        else:
            #Command is not listed.
            try:
                raise InputValueError('','F',s[1])
            except InputValueError('','F',s[1]) as e:
                print(e.message)