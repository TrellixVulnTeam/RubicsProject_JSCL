#this is meant to be just a general template for a state and the set of moves
#for the rubics cube. Changes may be made as neccessary

#colors
R = 'R'  # red
B = 'B'  # blue
G = 'G'  # green
Y = 'Y'  # yellow
O = 'O'  # orange
W = 'W'  # white

COLORS = [R,B,G,Y,O,W]
NOT_COLORS = [1,2,3,4,5,6]

class State:
    def __init__(self, front, back, left, right, top, under):
        self.front = front
        self.back = back
        self.left = left
        self.right = right
        self.top = top
        self.under = under
    
    def __str__(self):
        toReturn = ''
        toReturn += '      + - - +\n' 
        toReturn += '      | ' + self.top[0][0] + ' ' + self.top[0][1] + ' |\n'
        toReturn += '      | ' + self.top[1][0] + ' ' + self.top[1][1] + ' |\n'
        toReturn += '+ - - + - - + - - + - - +\n'
        toReturn += '| ' + self.left[0][0] + ' ' + self.left[0][1] + ' | ' + self.front[0][0] + ' ' + self.front[0][1] + ' | ' + self.right[0][0] + ' ' + self.right[0][1] + ' | ' + self.back[0][0] + ' ' + self.back[0][1] + ' |\n'
        toReturn += '| ' + self.left[1][0] + ' ' + self.left[1][1] + ' | ' + self.front[1][0] + ' ' + self.front[1][1] + ' | ' + self.right[1][0] + ' ' + self.right[1][1] + ' | ' + self.back[1][0] + ' ' + self.back[1][1] + ' |\n'
        toReturn += '+ - - + - - + - - + - - +\n'
        toReturn += '      | ' + self.under[0][0] + ' ' + self.under[0][1] + ' |\n'
        toReturn += '      | ' + self.under[1][0] + ' ' + self.under[1][1] + ' |\n'
        toReturn += '      + - - +\n' 
        return toReturn

    def __eq__(self, other):
        global COLORS
        colors = list(COLORS)
        
        #front
        selfRep.append(self.front[0][0])
        otherRep.append(other.front[0][0])
        selfRep.append(self.front[0][1])
        otherRep.append(other.front[0][1])
        selfRep.append(self.front[1][0])
        otherRep.append(other.front[1][0])
        selfRep.append(self.front[1][1])
        otherRep.append(other.front[1][1])
        #left
        selfRep.append(self.left[0][0])
        otherRep.append(other.left[0][0])
        selfRep.append(self.left[0][1])
        otherRep.append(other.left[0][1])
        selfRep.append(self.left[1][0])
        otherRep.append(other.left[1][0])
        selfRep.append(self.left[1][1])
        otherRep.append(other.left[1][1])
        #back
        selfRep.append(self.back[0][0])
        otherRep.append(other.back[0][0])
        selfRep.append(self.back[0][1])
        otherRep.append(other.back[0][1])
        selfRep.append(self.back[1][0])
        otherRep.append(other.back[1][0])
        selfRep.append(self.back[1][1])
        otherRep.append(other.back[1][1])
        #right
        selfRep.append(self.right[0][0])
        otherRep.append(other.right[0][0])
        selfRep.append(self.right[0][1])
        otherRep.append(other.right[0][1])
        selfRep.append(self.right[1][0])
        otherRep.append(other.right[1][0])
        selfRep.append(self.right[1][1])
        otherRep.append(other.right[1][1])
        #top
        selfRep.append(self.top[0][0])
        otherRep.append(other.top[0][0])
        selfRep.append(self.top[0][1])
        otherRep.append(other.top[0][1])
        selfRep.append(self.top[1][0])
        otherRep.append(other.top[1][0])
        selfRep.append(self.top[1][1])
        otherRep.append(other.top[1][1])
        #under
        selfRep.append(self.under[0][0])
        otherRep.append(other.under[0][0])
        selfRep.append(self.under[0][1])
        otherRep.append(other.under[0][1])
        selfRep.append(self.under[1][0])
        otherRep.append(other.under[1][0])
        selfRep.append(self.under[1][1])
        otherRep.append(other.under[1][1])
        
        selfDict = {}
        otherDict = {}
        remainingColorsSelf = list(NOT_COLORS)
        remainingColorsOther = list(NOT_COLORS)
        for j in range(len(selfRep)):
            currentColorSelf = selfRep[j]
            currentColorOther = otherRep[j]
            
            if currentColorSelf in selfDict:
                selfRep[j] = selfDict[currentColorSelf]
            else:
                nextColorSelf = remainingColorsSelf.pop()
                selfDict[currentColorSelf] = nextColorSelf
                selfRep[j] = nextColorSelf
            
            if currentColorOther in otherDict:
                otherRep[j] = otherDict[currentColorOther]
            else:
                nextColorOther = remainingColorsOther.pop()
                otherDict[currentColorOther] = nextColorOther
                otherRep[j] = nextColorOther
        
        for k in range(len(selfRep)):
            if selfRep[k] != otherRep[k]:
                return False
        
        return True

    def __hash__(self):
        return (self.__str__()).__hash__()
# example string representation
#          + - - +
#          | T T |
#          | T T |
#    + - - + - - + - - + - - +
#    | L L | F F | R R | B B |
#    | L L | F F | R R | B B |
#    + - - + - - + - - + - - +
#          | U U |
#          | U U |
#          + - - +
#
# slightly deformed but with indicies for the faces
#          +  -   -  +
#          | T00 T01 |
#          | T10 T11 |
#+  -   -  +  -   -  +  -   -  +  -   -  +
#| L00 L01 | F00 F01 | R00 R01 | B00 B01 |
#| L10 L11 | F10 F11 | R10 R11 | B10 B11 |
#+  -   -  +  -   -  +  -   -  +  -   -  +
#          | U00 U01 |
#          | U10 U11 |
#          +  -   -  +
    
    #below are the 12 possible moves coresponding to the moves in the image https://smhttp-ssl-62406.nexcesscdn.net/resources/images/solve-it/2x2-moves.jpg
    def rotate_right(self): #'R' in image
        #rotate the strip
        #save f
        temp1 = self.front[0][1]
        temp2 = self.front[1][1]
        #move u->f
        self.front[0][1] = self.under[0][1]
        self.front[1][1] = self.under[1][1]
        #move b->u
        self.under[0][1] = self.back[1][0]
        self.under[1][1] = self.back[0][0]
        #move t->b
        self.back[1][0] = self.top[0][1]
        self.back[0][0] = self.top[1][1]
        #move f->t
        self.top[0][1] = temp1
        self.top[1][1] = temp2
        
        #rotate the side
        temp1 = self.right[0][0]
        self.right[0][0] = self.right[1][0]
        self.right[1][0] = self.right[1][1]
        self.right[1][1] = self.right[0][1]
        self.right[0][1] = temp1
        
    def rotate_right_inverse(self): #'Ri' in image
        #rotate the strip
        #save f
        temp1 = self.front[0][1]
        temp2 = self.front[1][1]
        #move t->f
        self.front[0][1] = self.top[0][1]
        self.front[1][1] = self.top[1][1]
        #move b->t
        self.top[0][1] = self.back[1][0]
        self.top[1][1] = self.back[0][0]
        #move u->b
        self.back[1][0] = self.under[0][1]
        self.back[0][0] = self.under[1][1]
        #move f->u
        self.under[0][1] = temp1
        self.under[1][1] = temp2
        
        #rotate the side
        temp1 = self.right[0][0]
        self.right[0][0] = self.right[0][1]
        self.right[0][1] = self.right[1][1]
        self.right[1][1] = self.right[1][0]
        self.right[1][0] = temp1
        
    def rotate_left(self): #'L' in image
        #rotate the strip
        #save f
        temp1 = self.front[0][0]
        temp2 = self.front[1][0]
        #move t->f
        self.front[0][0] = self.top[0][0]
        self.front[1][0] = self.top[1][0]
        #move b->t
        self.top[0][0] = self.back[1][1]
        self.top[1][0] = self.back[0][1]
        #move u->b
        self.back[1][1] = self.under[0][0]
        self.back[0][1] = self.under[1][0]
        #move f->u
        self.under[0][0] = temp1
        self.under[1][0] = temp2
        
        #rotate the side
        temp1 = self.left[0][0]
        self.left[0][0] = self.left[1][0]
        self.left[1][0] = self.left[1][1]
        self.left[1][1] = self.left[0][1]
        self.left[0][1] = temp1
        
    def rotate_left_inverse(self): #'Li' in image
        #rotate the strip
        #save f
        temp1 = self.front[0][0]
        temp2 = self.front[1][0]
        #move u->f
        self.front[0][0] = self.under[0][0]
        self.front[1][0] = self.under[1][0]
        #move b->u
        self.under[0][0] = self.back[1][1]
        self.under[1][0] = self.back[0][1]
        #move t->b
        self.back[1][1] = self.top[0][0]
        self.back[0][1] = self.top[1][0]
        #move f->t
        self.top[0][0] = temp1
        self.top[1][0] = temp2
        
        #rotate the side
        temp1 = self.left[0][0]
        self.left[0][0] = self.left[0][1]
        self.left[0][1] = self.left[1][1]
        self.left[1][1] = self.left[1][0]
        self.left[1][0] = temp1
        
    def rotate_back(self): #'B' in image
        #rotate the strip
        #save t
        temp1 = self.top[0][0]
        temp2 = self.top[0][1]
        #move r->t
        self.top[0][0] = self.right[0][1]
        self.top[0][1] = self.right[1][1]
        #move u->r
        self.right[0][1] = self.under[1][1]
        self.right[1][1] = self.under[1][0]
        #move l->u
        self.under[1][1] = self.left[1][0]
        self.under[1][0] = self.left[0][0]
        #move t->l
        self.left[1][0] = temp1
        self.left[0][0] = temp2
        
        #rotate the side
        temp1 = self.back[0][0]
        self.back[0][0] = self.back[1][0]
        self.back[1][0] = self.back[1][1]
        self.back[1][1] = self.back[0][1]
        self.back[0][1] = temp1
        
    def rotate_back_inverse(self): #'Bi' in image
        #rotate the strip
        #save t
        temp1 = self.top[0][0]
        temp2 = self.top[0][1]
        #move l->t
        self.top[0][0] = self.left[1][0]
        self.top[0][1] = self.left[0][0]
        #move u->l
        self.left[1][0] = self.under[1][1]
        self.left[0][0] = self.under[1][0]
        #move r->u
        self.under[1][1] = self.right[0][1]
        self.under[1][0] = self.right[1][1]
        #move t->r
        self.right[0][1] = temp1
        self.right[1][1] = temp2
        
        #rotate the side
        temp1 = self.back[0][0]
        self.back[0][0] = self.back[0][1]
        self.back[0][1] = self.back[1][1]
        self.back[1][1] = self.back[1][0]
        self.back[1][0] = temp1
        
    def rotate_under(self): #'D' in image
        #rotate the strip
        #save f
        temp1 = self.front[1][0]
        temp2 = self.front[1][1]
        #move l->f
        self.front[1][0] = self.left[1][0]
        self.front[1][1] = self.left[1][1]
        #move b->l
        self.left[1][0] = self.back[1][0]
        self.left[1][1] = self.back[1][1]
        #move r->b
        self.back[1][0] = self.right[1][0]
        self.back[1][1] = self.right[1][1]
        #move f->r
        self.right[1][0] = temp1
        self.right[1][1] = temp2
        
        #rotate the side
        temp1 = self.under[0][0]
        self.under[0][0] = self.under[1][0]
        self.under[1][0] = self.under[1][1]
        self.under[1][1] = self.under[0][1]
        self.under[0][1] = temp1
        
    def rotate_under_inverse(self): #'Di' in image
        #rotate the strip
        #save f
        temp1 = self.front[1][0]
        temp2 = self.front[1][1]
        #move r->f
        self.front[1][0] = self.right[1][0]
        self.front[1][1] = self.right[1][1]
        #move b->r
        self.right[1][0] = self.back[1][0]
        self.right[1][1] = self.back[1][1]
        #move l->b
        self.back[1][0] = self.left[1][0]
        self.back[1][1] = self.left[1][1]
        #move f->l
        self.left[1][0] = temp1
        self.left[1][1] = temp2
        
        #rotate the side
        temp1 = self.under[0][0]
        self.under[0][0] = self.under[0][1]
        self.under[0][1] = self.under[1][1]
        self.under[1][1] = self.under[1][0]
        self.under[1][0] = temp1
    
    def rotate_front(self): #'F' in image
        #rotate the strip
        #save t
        temp1 = self.top[1][0]
        temp2 = self.top[1][1]
        #move l->t
        self.top[1][0] = self.left[1][1]
        self.top[1][1] = self.left[0][1]
        #move u->l
        self.left[1][1] = self.under[0][1]
        self.left[0][1] = self.under[0][0]
        #move r->u
        self.under[0][1] = self.right[0][0]
        self.under[0][0] = self.right[1][0]
        #move t->r
        self.right[0][0] = temp1
        self.right[1][0] = temp2
        
        #rotate the side
        temp1 = self.front[0][0]
        self.front[0][0] = self.front[1][0]
        self.front[1][0] = self.front[1][1]
        self.front[1][1] = self.front[0][1]
        self.front[0][1] = temp1
        
    def rotate_front_inverse(self): #'Fi' in image
        #rotate the strip
        #save t
        temp1 = self.top[1][0]
        temp2 = self.top[1][1]
        #move l->t
        self.top[1][0] = self.left[1][1]
        self.top[1][1] = self.left[0][1]
        #move u->l
        self.left[1][1] = self.under[0][1]
        self.left[0][1] = self.under[0][0]
        #move r->u
        self.under[0][1] = self.right[0][0]
        self.under[0][0] = self.right[1][0]
        #move t->r
        self.right[0][0] = temp1
        self.right[1][0] = temp2
        
        #rotate the side
        temp1 = self.front[0][0]
        self.front[0][0] = self.front[1][0]
        self.front[1][0] = self.front[1][1]
        self.front[1][1] = self.front[0][1]
        self.front[0][1] = temp1
        
    def rotate_top(self): #'U' in image
        #rotate the strip
        #save f
        temp1 = self.front[0][0]
        temp2 = self.front[0][1]
        #move r->f
        self.front[0][0] = self.right[0][0]
        self.front[0][1] = self.right[0][1]
        #move b->r
        self.right[0][0] = self.back[0][0]
        self.right[0][1] = self.back[0][1]
        #move l->b
        self.back[0][0] = self.left[0][0]
        self.back[0][1] = self.left[0][1]
        #move f->l
        self.left[0][0] = tmep1
        self.left[0][1] = temp2
        
        #rotate the side
        temp1 = self.top[0][0]
        self.top[0][0] = self.top[1][0]
        self.top[1][0] = self.top[1][1]
        self.top[1][1] = self.top[0][1]
        self.top[0][1] = temp1
        
    def rotate_top_inverse(self): #'Ui' in image
        #rotate the strip
        #save f
        temp1 = self.front[0][0]
        temp2 = self.front[0][1]
        #move l->f
        self.front[0][0] = self.left[0][0]
        self.front[0][1] = self.left[0][1]
        #move b->l
        self.left[0][0] = self.back[0][0]
        self.left[0][1] = self.back[0][1]
        #move r->b
        self.back[0][0] = self.right[0][0]
        self.back[0][1] = self.right[0][1]
        #move f->r
        self.right[0][0] = temp1
        self.right[0][1] = temp2
        
        #rotate the side
        temp1 = self.top[0][0]
        self.top[0][0] = self.top[0][1]
        self.top[0][1] = self.top[1][1]
        self.top[1][1] = self.top[1][0]
        self.top[1][0] = temp1
        
    def is_goal_state(self):
        global COLORS
        colors = list(COLORS)
        sides = [self.front, self.right, self.back, self.left, self.top, self.under] #use is read only
        
        for side in sides:
            currentColor = side[0][0]
            if currentColor in colors:
                #haven't used this color yet
                colors.remove(currentColor)
            else:
                #have found this color twice
                return False
            if not (side[0][0] == side[0][1] and side[0][1] == side[1][1] and side[1][1] == side[1][0]):
                return False
        return True
        
    def front_solved(self):
        if self.front[0][0] == self.front[0][1] and 
        self.front[0][0] == self.front[1][0] and 
        self.front[0][0] == self.front[1][1]:
            return 1
        else:
            return 0
            
    def top_solved(self):
        if self.top[0][0] == self.top[0][1] and 
        self.top[0][0] == self.top[1][0] and 
        self.top[0][0] == self.top[1][1]:
            return 1
        else:
            return 0
            
    def left_solved(self):
        if self.left[0][0] == self.left[0][1] and 
        self.left[0][0] == self.left[1][0] and 
        self.left[0][0] == self.left[1][1]:
            return 1
        else:
            return 0
            
    def right_solved(self):
        if self.right[0][0] == self.right[0][1] and 
        self.right[0][0] == self.right[1][0] and 
        self.right[0][0] == self.right[1][1]:
            return 1
        else:
            return 0
            
    def back_solved(self):
        if self.back[0][0] == self.back[0][1] and 
        self.back[0][0] == self.back[1][0] and 
        self.back[0][0] == self.back[1][1]:
            return 1
        else:
            return 0
            
    def under_solved(self):
        if self.under[0][0] == self.under[0][1] and 
        self.under[0][0] == self.under[1][0] and 
        self.under[0][0] == self.under[1][1]:
            return 1
        else:
            return 0
            
    def features(self):
        sum = front_solved(self) + top_solved(self) + back_solved(self) + under_solved(self) + left_solved(self) + right_solved(self)
        result = []
        # feat1
        for i in range(sum):
            result.append(1)
        for i in range(6 - sum):
            result.append(0)
        
Class Operator:
    def __init__(self, name, precond, state_transf):
        self.name = name
        self.precond = precond
        self.state_transf = state_transf
 
    def is_applicable(self, s):
        return self.precond(s)
 
    def apply(self, s):
        return self.state_transf(s)
        
#ADD THIS PART
# CREATE_INITIAL_STATE = lambda: State(init)

OPERATORS = [
    Operator("rotate front", True, lambda s: s.rotate_front()),
    Operator("rotate front inverse", True, lambda s: s.rotate_front_inverse()),
    Operator("rotate under", True, lambda s: s.rotate_under()),
    Operator("rotate under inverse", True, lambda s: s.rotate_under_inverse()),
    Operator("rotate back", True, lambda s: s.rotate_back()),
    Operator("rotate back inverse", True, lambda s: s.rotate_back_inverse()),
    Operator("rotate left", True, lambda s: s.rotate_left()),
    Operator("rotate left inverse", True, lambda s: s.rotate_left_inverse()),
    Operator("rotate right", True, lambda s: s.rotate_right()),
    Operator("rotate right inverse", True, lambda s: s.rotate_right_inverse()),
    Operator("rotate top", True, lambda s: s.rotate_top()),
    Operator("rotate top inverse", True, lambda s: s.rotate_top_inverse())]