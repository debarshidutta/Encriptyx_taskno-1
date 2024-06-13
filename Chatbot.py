from tkinter import *  # Importing everything from the tkinter module

# Creating the main window
root = Tk()
root.title("Simple Chatbot")  # Sets the title of the window

# Defining the function to handle sending of messages
def send():
    # Gets the user input from the entry widget
    send = "You -> " + e.get()
    # Inserting user's message into the text widget
    txt.insert(END, "\n" + send)
    # Converting user's message into lowercase for easier comparison
    user = e.get().lower()
    
    # Determining bot's response to user input
    if user == 'hello':
        txt.insert(END, "\n" + "Bot -> Hi!")
    elif user in ['hi', 'hii', 'hiii']:
        txt.insert(END, "\n" + "Bot -> Hello!")
    elif user == 'how are you?':
        txt.insert(END, '\n' + "Bot -> I'm fine. How are you?")
    elif user in ["fine", "i am good", "i am doing good"]:
        txt.insert(END, '\n' + "Bot -> Great to hear that! How can I help you?")
    else:
        txt.insert(END, '\n' + "Bot -> Sorry, I couldn't get you.")
    
    # Clear the entry widget after sending the message
    e.delete(0, END)

# Create a text widget to display the chat's history
txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)  # Place the text widget in the window

# Create an entry widget for the user input
e = Entry(root, width=88)
e.grid(row=1, column=0)  # Place the entry widget in the window

# Create the button for sending the messages
send_btn = Button(root, 
                  text="Send", 
                  font=("Bookman Old Style", 15),
                  foreground="white",  # Foreground color of the button
                  background="#007bff",  # Bright blue color background of the button
                  highlightbackground="#007bff",  # Highlighting the background
                  cursor="hand2", 
                  borderwidth=0.5, 
                  relief='raised', 
                  bd=2.5, 
                  highlightcolor='green', 
                  command=send)  # Command to call the send function
# Place the send button in the window
send_btn.grid(row=1, column=1, padx=5, pady=15)

# Run the tkinter event loop
root.mainloop()
