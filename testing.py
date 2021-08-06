import unittest
from unittest import result
from package.vechile_module import Vechile
from package.parking_module import Parking
from datetime import datetime

class VechileTest(unittest.TestCase):
    def test_display_correct_stock(self):
        vechile1 = Vechile(0,0,0,0)
        vechile2 = Vechile("A",0,1,2)
        self.assertEqual(vechile1.display_info(),(0,0,0,0))
        self.assertEqual(vechile2.display_info(),("A",0,1,2))

class ParkingTest(unittest.TestCase):
    parking_space = [1,2,3,4,5,6,7,8,9]

    def invalid_space_check(self,parking_space):
        parking1 = Parking()
        self.assertEqual(parking1.space_check(9,parking_space),None)
        self.assertEqual(parking1.space_check(10,parking_space), None)
        self.assertIsNone(parking1.space_check(None,parking_space))

    def valid_space_check(self):
        parking_space = [1,2,3,4,"R",6,7,8,"R"]
        parking = Parking()
        self.assertEqual(parking.space_check(8,parking_space),"R")

    def test_check_parking_full(self):
        parking_space = ["R","R","R","R","R","R"]
        parking_space1 = ["R","R",2,"R"]
        parking = Parking()
        self.assertEqual(parking.check_parking_full(parking_space),True)
        self.assertEqual(parking.check_parking_full(parking_space1),False)

    def test_get_ticket(self):
        parking_space = ["R","R","R","R","R","R"]
        parking_space1 = ["R","R",2,"R"]
        parking = Parking()
        self.assertEqual(parking.get_ticket(parking_space), None)
        self.assertEqual(parking.get_ticket(parking_space1),2)
        
    def test_car_park(self):
        parking_space = ["R",1,2,"R"]
        now = datetime.now()
        str_now = datetime.strftime(now,"%Y-%m-%d %H:%M:%S.%f")
        parking = Parking()
        self.assertEqual(parking.car_park(1,parking_space),(1,str_now) )

    def test_return_car_park(self):
        parking_space = ["R",1,2,"R"]
        park = Parking()
        self.assertEqual(park.remove_car(1,parking_space),1)

    def test_cost(self):
        time_str = "2021-08-06 6:48:22.12345"
        time_str1 = "2021-08-06 19:55:12.12345"
        park = Parking()
        # bill = park.cost("a",time_str)
        self.assertEqual(park.cost("a",time_str1),10)
        self.assertEqual(park.cost("a",time_str),130)
        self.assertEqual(park.cost("b",time_str1),20)
        self.assertEqual(park.cost("b",time_str),260)

        




if __name__ == "__main__":
    unittest.main()
