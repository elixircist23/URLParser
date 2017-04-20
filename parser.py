import string
 
#defining different alphabet sets
#these will help when we create a transition table
alphabet = string.ascii_lowercase
alphabet_no_w = alphabet[:22] + alphabet[23:]
alphabet_no_c = alphabet[:2] + alphabet[3:]
alphabet_no_a_o = alphabet[1:14] + alphabet[15:]
alphabet_no_m = alphabet[:12] + alphabet[13:]
alphabet_no_a = alphabet[1:]
 
#defining a transition table as a dictionary with tuple keys
#the key as a 2-tuple will have the state as its first index
#and the transition character as its second index
#the result of the transition character from the state gives the next state it will be in
#in the actual dictionary definition, only the 1 character transition states are defined e.g '.' or 'w'
transition_table = {
    ('q1', '.'):'q19', ('q1', 'w'):'q2', 
    ('q2', '.'):'q12', ('q2', 'w'):'q3', 
    ('q3', '.'):'q12', ('q3', 'w'):'q4', 
    ('q4', '.'):'q6',
    ('q5', '.'):'q12',
    ('q6', '.'):'q19', ('q6', 'c'):'q7',
    ('q7', '.'):'q12', ('q7', 'a'):'q11', ('q7', 'o'):'q8',
    ('q8', '.'):'q12', ('q8', 'm'):'q9',
    ('q9', '.'):'q12',
    ('q10', '.'):'q12',
    ('q11', '.'):'q12',
    ('q12', '.'):'q19', ('q12', 'c'):'q13',
    ('q13', '.'):'q19', ('q13', 'a'):'q17', ('q13', 'o'):'q14',
    ('q14', '.'):'q15', ('q14', 'm'):'q18',
    ('q15', '.'):'q19', ('q15', 'c'):'q16',
    ('q16', '.'):'q19', ('q16', 'a'):'q17',
    ('q17', '.'):'q19',
    ('q18', '.'):'q19',
    ('q19', '.'):'q19',
}
 
#all other transition states are added in these for loops
for i in alphabet:
    transition_table[('q4', i)] = 'q5'
    transition_table[('q5', i)] = 'q5'
    transition_table[('q9', i)] = 'q10'
    transition_table[('q10', i)] = 'q10'
    transition_table[('q11', i)] = 'q10'
    transition_table[('q17', i)] = 'q19'
    transition_table[('q18', i)] = 'q19'
    transition_table[('q19', i)] = 'q19'
 
for i in alphabet_no_w:
    transition_table[('q1', i)] = 'q5'
    transition_table[('q2', i)] = 'q5'
    transition_table[('q3', i)] = 'q5'
 
for i in alphabet_no_c:
    transition_table[('q6', i)] = 'q10'
    transition_table[('q12', i)] = 'q19'
    transition_table[('q15', i)] = 'q19'
 
for i in alphabet_no_a_o:
    transition_table[('q7', i)] = 'q10'
    transition_table[('q13', i)] = 'q19'
 
for i in alphabet_no_m:
    transition_table[('q8', i)] = 'q10'
    transition_table[('q14', i)] = 'q19'
 
for i in alphabet_no_a:
    transition_table[('q16', i)] = 'q19'
 
#defining accept states to be used when we parse a full string and want to check if it lands
#on an accepting state
accept_states = ('q9', 'q11', 'q17', 'q18')
 
#main program loop
while(True):
    #asks user if they want to input a string, if so continue the program, if not break
    decision = str(input("Do you want to enter a string? (y/n): "))
    if(decision == 'n'):
        break
     
    input_string = str(input("Enter a string: "))
    print(input_string)
 
    #define the current_state, which at first will always be the start state of q1
    current_state = 'q1'
    print("Current and start state: %s" % current_state)
 
    #for loop that will iterate through each character of the input string
    for i in input_string:
        if(i=='\r'):
            break
             
        print("Character processed: %s" % i)
        #here we set current_state to the result of the dictionaries defined transition states
        current_state=transition_table[(current_state, i)]
        print("Current state: %s" % current_state)
 
    #after the for loop finishes, it will finish on a state in the DFA
    #if said state is in the accept states, then the string was accepted
    #in not then the string was not accepted
    if current_state in accept_states:
        print("The string was accepted.")
 
    else:
        print("The string was not accepted")
