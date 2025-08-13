to_do_list=[] 
while True:
    print('TO DO LIST APP')
    print(" 1 to add task ")
    print(" 2 to display ")
    print(" 3 to delete task ")
    print(" 4 to finish ")   
    operation=int(input("enter the number of the opertion: "))
    
    if operation==1:
        task=input("ENTER THE TASK YOU WANT TO ADD : ")
        to_do_list.append(task)
        print("the task was added succesfully..")
    elif operation==2:
        if not to_do_list:
            print("there is not tasks yet..")
        else :
            print("the tasks are : ")
            for i, task in enumerate(to_do_list, 1):
                print(f'{i} : {task}.')
    elif operation==3:
        if not to_do_list:
            print("there is no tasks to be deleted.")
        else:
            for i,task in enumerate(to_do_list,1):
                print(f'{i} : {task}.')
            try:
                index=int(input("enter the number of the task. ")) -1
                if 0<=index<len(to_do_list):
                    removed=to_do_list.pop()
                    print("the task is deleted succesfully..")
                else:
                    print("the number of the index is incorrect")
            except ValueError:
                print("enter a valid number..")
                
    elif operation==4:
        print("the app is closed")
        break
    
    else:
        print("invalid operator ")
        