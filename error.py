# class InputValueError is derived from super class ValueError
class InputValueError(ValueError):
    """Exception raised for errors in the input.
    Attributes:
        command_type -- ordertype of the order that elicits an error
        orderid -- orderid of the order that elicits an error
        msg -- explanation of the error
    """
         # Constructor or Initializer
    def __init__(self, message, command_type, order_id, *args):
        self.command_type = command_type 
        code = 0
        super(InputValueError, self).__init__(message, command_type, orderid, *args) 
        if command_type == 'N':
            code = 303
            self.message = self.message = " - ".join([self.orderid,"Reject",code,"Invalid order details"])
        elif command_type == 'A':
            code = 101
            self.message = " - ".join([self.orderid,"AmendReject",code,"invalid amendment details"])
        elif command_type == 'M':
            code = 202
            self.message = " - ".join(["MatchReject",code,"invalid match details"])
        elif command_type == 'Q':
            code = 101
            self.message = " - ".join([self.orderid,"AmendReject",code,"invalid amendment details"])
            
        elif command_type == 'X':
            code = 404
            self.message = " - ".join([self.orderid,"CancelReject",code,"Order does not exist"])
        else:
            self.message = " - ".join([self.orderid,"","invalid Command details"])