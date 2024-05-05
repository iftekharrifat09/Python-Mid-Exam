class Star_Cinema:
    hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, row, col, hall_no) -> None:
        self.__seats = {}
        self.__show_list = []
        self.__row = row
        self.__col = col
        self.__hall_no = hall_no
        self.__initialize()  # Here calling the initialize method
        super().__init__()
        
        Star_Cinema.entry_hall(self)

    def __initialize(self):
        for i in range(self.__row):
            for j in range(self.__col):
                self.__seats[(i, j)] = 0

    def entry_show(self, movie_name, time):
        show_id = int(f'{self.__hall_no}{len(self.__show_list) + 1}')
        show_info = (show_id, movie_name, time,)
        self.__show_list.append(show_info)

    def view_show_list(self):
        for show in self.__show_list:
            print(f"Show ID: {show[0]}  Movie Name: {show[1]}  Time: {show[2]}")
        
    def book_seats(self, show_id, seat_list):

        found = False
        for show in self.__show_list:
            if show[0] == int(show_id):
                found = True
                break
            
        if not found:
            return found

        for row, col in seat_list:
            if row not in range(1, self.__row + 1) or col not in range(1, self.__col + 1):
                print(f"You Have entered Invalid {row}-{col} !!!")
                continue

            if self.__seats[(row-1, col-1)] == 1:
                print(f"Seat {row}-{col} is Already Booked for Show ID- {show_id}, Try another Seat")
            else:
                self.__seats[(row-1, col-1)] = 1
                print(f"Seat {row}-{col} Booked Successfully for Show ID- {show_id} :)")
                
        return found

    def show_all_seats(self, show_id):
        found = False
        for show in self.__show_list:
            if show[0] == show_id:
                found = True
                break
        if not found:
            return found
        
        print(f'\nSeat List As Direction Pair of Show ID- {show_id}:')
        cnt = 1
        for seat, value in self.__seats.items():
            print(f'Seat No-{cnt} : {seat}')
            cnt += 1

        print(f'\nSeat List As a Matrix of Show ID- {show_id}: ')
        for i in range(self.__row):
            for j in range(self.__col):
                print(self.__seats[(i, j)], end=" ")
            print()
        print()
        
        return found

def ticket_counter():              
    print('\nWelcome to Star Cinema Ticket Counter\n')
    while True:
        print('1. VIEW ALL SHOW TODAY')
        print('2. VIEW AVAILABLE SEATS FOR A SHOW')
        print('3. BOOK TICKET FOR A SHOW')
        print('4. EXIT THE PAGE')
        
        command = int(input('\nEnter your Choice: '))
        if command == 1:
            print()
            print('********* Movies Are Running into the Hall **********')
            print()
            for hall in Star_Cinema.hall_list:
                hall.view_show_list()
            print()
        elif command == 2:
            print()
            show_id = int(input('Enter the show id: '))
            track = False
            for hall in Star_Cinema.hall_list:
                if(hall.show_all_seats(show_id)):
                    track = True
                    break
            if not track:
                print('\nInvalid Show ID\n')
                
        elif command == 3:
            print()
            show_id = input('Enter the ID of the show: ')
            num_seat = int(input('Enter the Number of Seat to book: '))
            if num_seat <= 0:
                print('Number of seats should be a positive integer.')
                continue
            seat = []
            for i in range(num_seat):
                row = int(input(f'Enter the {i+1} Ticket Row Number: '))
                col = int(input(f'Enter the {i+1} Ticket Column Number: '))
                seat.append((row, col))
            print()
            track = False
            for hall in Star_Cinema.hall_list:
                if(hall.book_seats(show_id, seat)):
                    track = True
                    break
            if not track:
                print('\nInvalid Show ID\n')
            print()
                
        elif command == 4:
            print()
            print('Exiting....')
            break
        else:
            print()
            print('Invalid Choice, Try Again\n')
       


h1 = Hall(5, 7, 1)
h1.entry_show('Justice Legue', '11:30')
h2 = Hall(4, 7, 2)
h2.entry_show('Pathan', '01:50')
h3 = Hall(5, 6, 3)
h3.entry_show('Bhader Meye Joshna', '08:15')

ticket_counter()
