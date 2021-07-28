from package import parking_module, vechile_module, parking_records

parking_space = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
if __name__ == "__main__":
    print("*"*100)
    print("Welcome!")
    print("*"*100)

    park = parking_module.Parking()
    while True:
        park.display_board(parking_space)
        if park.check_parking_full():
            print("Parking is full")
            break
        else:
            ticket = park.get_ticket(parking_space)
            print("")
            print("\n1.Park\n2.Return\n3.Update\n4.Query\n".upper())
            try:
                choice = int(input("Enter your choice"))
            except ValueError:
                print("Please use integer.")
                continue
            else:
                if choice == 1:
                    print("\nA: Bike\nB: Car")
                    vechile_catagoery = input("Your vechile(A/B): ")
                    if vechile_catagoery.upper() == "A":
                        print("Please fill the following.\n\n")
                        model = input("Enter bike name: ")
                        try:
                            registration_num = int(input("Enter your registration number: "))
                        except ValueError:
                            print("Use integer!")
                            continue
                        colour = input("Enter bike colour: ")
                        bike = vechile_module.Vechile("A", model, registration_num, colour)
                        print("\n")
                        print(f"Please park your bike at parking slot {ticket}")
                        slot, date_time = park.bike_park(ticket,parking_space)
                        parking_records.add_record(vechile_catagoery.upper(),model,registration_num,colour,ticket,date_time)
                    elif vechile_catagoery.upper() == "B":
                        model = input("Enter car name: ")
                        try:
                            registration_num = int(input("Enter your registration number: "))
                        except ValueError:
                            print("Use integer!")
                            continue
                        colour = input("Enter car colour: ")
                        car = vechile_module.Vechile("B", model, registration_num, colour)
                        print(f"Please park your car at parking slot {ticket}")
                        slot, date_time= park.car_park(ticket,parking_space)
                        parking_records.add_record(vechile_catagoery.upper(),model,registration_num,colour,ticket,date_time)
                        print("\n")
                    else:
                        print("Invalid Input!")
                        continue
                elif choice == 2:
                    vechile_catagoery = input("Your vechile(A/B): ")
                    try:
                        registration_num = int(input("Enter your registration number: "))
                    except ValueError:
                        print("Use integer!")
                        continue
                    my_result = parking_records.get_record(vechile_catagoery.upper(),registration_num)
                    print("*"*100)
                    print(f'id: {my_result[0]}')
                    print(f'catagoery: {my_result[1]}')
                    print(f'model: {my_result[2]}')
                    print(f'registration_num: {my_result[3]}')
                    print(f'colour: {my_result[4]}')
                    print(f'slot : {my_result[5]}')
                    print(f'date_time: {my_result[6]}')
                    print("*"*100)
                    slot = my_result[5]
                    catagoery =  my_result[1]
                    date_time = my_result[6]
                    if vechile_catagoery.lower() == "a":
                        park.remove_bike(slot,parking_space)
                    elif vechile_catagoery.lower() == "b":
                        park.remove_car(slot,parking_space)

                    bill = park.cost(catagoery,date_time)
                    print(f"Total bill is {bill}")
                    print('ok')
                elif choice == 3:
                    category = input("Enter category: ")
                    carid = int(input("Enter parking id you want to update: "))
                    # model = input("Enter model name you want to update: ")
                    reg_num = int(input("Enter registration number you want to update: "))
                    my_result = parking_records.get_record(category.upper(),reg_num)
                    if my_result:
                        # new_category = input("Enter new category: ")
                        new_model = input("Enter new model name: ")
                        # new_model = input("Enter new registration name: ")
                        try:
                            new_reg_num = int(input("Enter new registration number: "))
                        except ValueError:
                            print("Please use integer!")
                            continue
                        # new_colour = input("Enter colour: ")
                        parking_records.update_record(carid,new_model,new_reg_num)
                        # parking_records.update_record(new_category.upper(),reg_num,new_category.upper(),new_model,new_reg_num,new_colour)
                    else:
                        print("xaoma")
                    

                else:
                    break
                    
        #test