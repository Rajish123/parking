import random
from datetime import datetime, date
from parking import parking_space


class Parking:
    def display_board(self,parking_space):
        print(f" {parking_space[12]} | {parking_space[13]} | {parking_space[14]} ")
        print("-----------")
        print("\n")
        print("-----------")
        print(f" {parking_space[9]}  | {parking_space[10]} | {parking_space[11]} ")
        print("-----------")
        print("\n")
        print("-----------")
        print(f" {parking_space[6]}  | {parking_space[7]}  | {parking_space[8]} ")
        print("-----------")
        print("\n")
        print("-----------")
        print(f" {parking_space[3]}  | {parking_space[4]}  | {parking_space[5]} ")
        print("-----------")
        print("\n")
        print("-----------")
        print(f" {parking_space[0]}  | {parking_space[1]}  | {parking_space[2]} ")
        print("-----------")
        print("\n")
        print("-----------")

    def space_check(self,position,parking_space):
        return parking_space[position] == position

    def check_parking_full(self):
        for i in range(15):
            check = self.space_check(i,parking_space)
            if check == "R":
                # return true if parking is full
                return True
            return False

    def get_ticket(self,parking_space):
        empty_space = []
        if not self.check_parking_full():
            for i in parking_space:
                if i != "R":
                    empty_space.append(i)
            ticket = random.choice(empty_space)
            return ticket
        else:
            print("Parking is full.No tickets available!")
            return None

    def car_park(self, parking_slot,parking_space):
        now = datetime.now()
        current_time_str = now.strftime("%Y-%m-%d %H:%M:%S.%f")
        # current_time = datetime.strptime(current_time_str,"%H:%M:%S").time()
        parking_space[parking_slot] = "R"
        print(f"list of space = {parking_space}")
        print(f"\nTime:{current_time_str}\n")
        return parking_slot,current_time_str

    def remove_car(self,parking_slot,parking_space):
        parking_space[parking_slot] = parking_slot

    def bike_park(self,parking_slot):
        now = datetime.now()
        current_time_str = now.strftime("%Y-%m-%d %H:%M:%S.%f")
        # current_time = datetime.strptime(current_time_str,"%H:%M:%S").time()
        parking_space[parking_slot] = "R"
        print(parking_space)
        print(f"\nTime:{current_time_str}\n")
        return parking_slot,current_time_str

    def remove_bike(self, parking_slot,parking_space):
        parking_space[parking_slot] = parking_slot

    def cost(self, category, date_time_str):
        now = datetime.now()
        date_time = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S.%f")
        bill = 0
        parking_period = now - date_time
        # get hour
        total_hour = parking_period.days * 24 + parking_period.seconds//3600
        if category == "a" and total_hour < 1:
            bill = 10
        elif category == "a" and total_hour > 1:
            bill = total_hour * 10
        elif category == "b" and total_hour < 1:
            bill = 20
        else:
            bill = total_hour * 20
        return bill


        
