def add_task(the_list, task_name):
    # task: task name
    # done: whether it has been finished or not
    task = {"name": task_name, "done": False }
    the_list.append(task)
    print(f"{task_name} has been added to the tasks list")
    return

def read_tasks(the_list):
    print("\nLista de tarefas:")
    for index, task in enumerate(the_list, start=1):
       status = "✔" if task["done"] else " "
       task_name = task["name"]
       print(f"{index}. [{status}] {task_name}")

def update_task_name(task_list, task_index, new_task_name):
    true_index = task_index - 1 # devemos ajustar o índice informado pelo usuário, pois o usuário
    # vê o índice acrescido de um para que na visualização o índice não comece em zero
    if true_index >=0 and true_index < len(task_list):
        task_list[true_index]["name"] = new_task_name
        print(f"Tarefa {task_index} atualizada para {new_task_name}")
    else:
        print("Índice de tarefa inválido")
    return

def complete_task(task_list, task_index):
    true_index = task_index - 1
    if 0 <= true_index < len(task_list):
        task_list[true_index]["done"] = True
        print("Tarefa %s marcada como completada" % true_index)
    else:
        print("Índice de tarefa inválido")
    return

def delete_finished_tasks(task_list):
    for t in task_list:
        if t["done"]: # == True:  não é necessário comparar true com true
            task_list.remove(t)
    print("Tarefas completadas foram deletadas.")
    return

task_list = []

while True:
    print("\nMenu do Gerenciador de Lista de Tarefas:")
    print("1. Adicionar tarefas")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")
    # Get what the user wants
    choice = input("Digite a sua escolha: ")
    if choice == "1":
        new_task = input("Qual é o nome da tarefa que deseja adicionar? ")
        add_task(task_list, new_task)
    elif choice == "2":
        read_tasks(task_list)
    elif choice == "3":
        read_tasks(task_list)
        task_index = int(input("Digite o número da tarefa que deseja atualizar: "))
        new_name = input("Digite o novo nome da tarefa: ")
        update_task_name(task_list, task_index, new_name)
    elif choice == "4":
        read_tasks(task_list)
        task_index = int(input("Digite o número da tarefa que deseja marcar como completada: "))
        complete_task(task_list, task_index)
        read_tasks(task_list)

    elif choice == "5":
        delete_finished_tasks(task_list)
        read_tasks(task_list)
    elif choice == "6":
        print("Programa finalizado")
        break
