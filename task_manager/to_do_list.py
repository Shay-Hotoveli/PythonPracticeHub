#list created to store all tasks
task_list = []

#adding task to the list
def add_task():
    while True:
        task_name = input("Name of the task: ")
        task_input = input("what is your task?: ")
        task = {
            "name" : task_name,
            "description" : task_input,
            "completed" : False
        }
        task_list.append(task)
        print("Task added successfully")
        again_option = input("Do yo want to create another task? y/n: ")
        if again_option.lower() == "n" or again_option == "no":
            print("Alright, farewell")
            break
        elif again_option.lower() != "y":
            print(f"'{again_option}' is not a valid input, please enter 'y' or 'n'")
    
#deleting task from list
def delete_task():
    if not task_list:
        print("No tasks available to delete.")
        return
    printing_tasks()
    task_input = input("Enter the task number you want to delete: ")
    if task_input.isdigit():
        task_index = int(task_input) - 1
        if 0 <= task_index < len(task_list):
            removed_task = task_list.pop(task_index)
            print(f"Task '{removed_task['name']}' deleted successfully.")
        else:
            print("Invalid task number. Please choose a valid number from the list")
    else:
        print("Invalid input. Please choose a valid number from the list.")

def mark_task_completed():
    if not task_list:
        print("No tasks available to mark as completed or revert.")
        return
    printing_tasks()
    task_input = input("Enter the task number to toggle completion status: ")
    if task_input.isdigit():
        task_index = int(task_input) - 1  # Convert to zero-based index
        if 0 <= task_index < len(task_list):
            current_status = task_list[task_index]["completed"]
            if current_status:
                task_list[task_index]["completed"] = False
                print("Task marked as not completed.")
            else:
                task_list[task_index]["completed"] = True
                print("Task marked as completed.")
        else:
            print("Invalid task number.")
    else:
        print("Invalid input. Please enter a valid task number.")       

#printing task list with a human-readable form
def printing_tasks():
    if not task_list:
        print("No tasks in the list.")
    else:
        for i, task in enumerate(task_list, start=1):
            status = "Completed" if task.get("completed") == True  else "Not Completed"
            print(f"{i}: {task.get('name')} - {task.get('description')} - {status}")

#adding option for the user to modify anything of the task content
def modifying_task():
    if not task_list:
        print("\nNo tasks available to modify.")
        return
    print("\nThese are your tasks")
    printing_tasks()
    task_input = input("Choose a task to modify (choose by number): ")
    if task_input.isdigit():
        int_task_input = int(task_input) - 1
        if 0 <= int_task_input < len(task_list):
            print("you can change the following details:")
            print("1: Name")
            print("2: Description")
            user_input = input("choose a number for any changes (1/2): ")
            if user_input == "1":
                name_change = input("Enter new task name: ")
                task_list[int_task_input]['name'] = name_change
                print("Task name updated successfully.")
            elif user_input == "2":
                description_change = input("Write new description for your task: ")
                task_list[int_task_input]['description'] = description_change
                print("Task description updated successfully.")
            else:
                print("Invalid option. No changes made.")
        else:
            print("Invalid task number. Please choose a valid number from the list")
    else:
        print("Wrong input, Please enter a valid task number.")


# Main menu function
def main_menu():
    while True:
        print("\nMain Menu:")
        print("1: Add a New Task")
        print("2: View All Tasks")
        print("3: Modify an Existing Task")
        print("4: Delete a Task")
        print("5: Mark Task as Completed")
        print("6: Exit")
        choice = input("Choose an option: ")
        print("\n")
        match choice:
            case "1":
                add_task()
            case "2":
                printing_tasks()
            case "3":
                modifying_task()
            case "4":
                delete_task()
            case "5":
                mark_task_completed()
            case "6":
                print("Exiting the application. Goodbye!")
                break
            case _:
                print("Invalid option. Please choose a valid menu option.")
# Run the application
main_menu()
