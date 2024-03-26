import requests
import os

# function to test connection with webex server
def test_connection(token):
    try:
        url = 'https://webexapis.com/v1/people/me'
        headers = {
            'Authorization' : 'Bearer {}'.format(token)
        }

        response = requests.get(url, headers = headers)
        
        if(response.status_code == 200):
            print("Connection test successful.")
        else:
            print("Connection test failed.")

    except:
        print("An error occurred")

# function to display user information
def disp_user_info(token):
    try:
        url = 'https://webexapis.com/v1/people/me'
        headers = {
            'Authorization' : 'Bearer {}'.format(token)
        }

        response = requests.get(url, headers = headers)
        
        if(response.status_code == 200):
            user_info = response.json()
            print("User Information")
            print("Displayed Name : " + user_info["displayName"])
            print("Nickname : " + user_info["nickName"])
            print("Email : " + user_info["emails"] [0])
        else:
            print("Failed to retrieve information. Please try again.") 

    except:
        print("An error occurred")

# function to display room list
def disp_room_list(token):
    try:
        url = 'https://webexapis.com/v1/rooms'
        headers = {
            'Authorization' : 'Bearer {}'.format(token)
        }

        response = requests.get(url, headers = headers)
        
        if(response.status_code == 200):
            rooms = response.json()
            for room in rooms["items"]:
                print("\n")
                print("Room ID : " + room["id"])
                print("Room Title : " + room["title"])
                print("Date Created : " + room["created"])
                print("Last Activity : " + room["lastActivity"])
        else:
            print("Failed to retrieve room list. Please try again")

    except:
        print("An error occurred")

# function to create a room
def create_room(token):
    try:
        url = 'https://webexapis.com/v1/rooms'
        headers = {
            'Authorization' : 'Bearer {}'.format(token),
            'Content-Type': 'application/json'
        }

        room_title = input("Enter the room title: ")

        params = { 'title' : room_title }
        response = requests.post(url, headers = headers, json=params)
        
        if(response.status_code == 200):
            print("Room has been successfully created.")
        else:
            print("Room cannot be created. Please try again.")
    except:
        print("An error occurred")

# function to send message to a room
def message_to_room(token):
    try:
        url = 'https://webexapis.com/v1/rooms'
        headers ={
            'Authorization' : 'Bearer {}'.format(token)
        }

        response = requests.get(url, headers = headers)
        
        if(response.status_code == 200):
            rooms = response.json()
            room_number = 0
            for room in rooms["items"]:
                room_number = room_number + 1

                print("")
                print(room_number)
                print("Room ID : " + room["id"])
                print("Room Title : " + room["title"])
                print("Date Created : " + room["created"])
                print("Last Activity : " + room["lastActivity"])

            room_number = int(input("Choose a room by number to send message: "))
            room_id = rooms["items"][room_number - 1]["id"]
            
            message = input("Enter the message: ")

            url2 = 'https://webexapis.com/v1/messages'

            headers2 ={
            'Authorization': 'Bearer {}'.format(token),
             'Content-Type': 'application/json'
            }

            params = {'roomId': room_id, 'markdown': message}
            response2 = requests.post(url2, headers=headers2, json=params)

            if(response2.status_code == 200):
                print("Successfully send message")
            else:
                print("Message cannot be sent. Please try again.")
                print(response2.json())
    except:
        print("An error occurred")

# main function
print("\t\tWEBEX ")
print("\n")
try:
    # prompt the user to provide their authentication token and validate it.
    token = input("Please enter your Webex token : ")
    
    while True:

        # URL for token validation
        url = 'https://webexapis.com/v1/people/me'
        headers = {
            'Authorization' : 'Bearer {}'.format(token)
        }

        response = requests.get(url, headers = headers)

        if(response.status_code == 200):
            break
        else:
            print("An invalid token or error occurred. please try again")
            print("")
    
    while True:
        print("\n")

        # display the menu options and handle user's choice.
        print("You are required to choose one:")
        print("0. Test connection to webex ")
        print("1. User information ")
        print("2. List room ")
        print("3. Create room ")
        print("4. Send message ")
        print("5. Exit ")
        
        chooseoption = int(input("Enter your choice: "))

        # test connection
        if(chooseoption == 0):
            test_connection(token)

        # user information
        elif(chooseoption == 1):
            disp_user_info(token)

        # room list
        elif(chooseoption == 2):
            disp_room_list(token)

        # create a room
        elif(chooseoption == 3):
            create_room(token)

        # message to room
        elif(chooseoption == 4):
            message_to_room(token)

        # exit
        elif(chooseoption == 5):
            os._exit(0)

except:
    print("Error occurred")
