user_input="{()}"
symbol_dictionary={
    "{":"}",
    "[":"]",
    "(":")"
}
symbol_stack=[]
top=-1
for symbol in user_input:
    if symbol in symbol_dictionary:
        top+=1
        symbol_stack.insert(top,symbol)
    else:
        if(top==-1):
            print(symbol_stack,"invalid")
            break
        current_element=symbol_stack[top]
        if symbol==symbol_dictionary.get(current_element):
            symbol_stack.pop()
            top-=1
        else:
            print(symbol_stack,"invalid paranthesis")
            break
else:
    print(symbol_stack,"valid paranthesis")
        
