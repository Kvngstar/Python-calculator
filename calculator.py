import tkinter as tk

root = tk.Tk()
root.title("Calculator")

# to set navbar display icon
calc_icon = tk.PhotoImage(file="./calc-icon.png")
root.iconphoto(False,calc_icon)
root.geometry("420x600") 


# Building a container frame
wrapper_frame = tk.Frame(root)
wrapper_frame.grid(column=0,row=0,sticky='nsew')

# Creating header row
header_frame = tk.Frame(wrapper_frame,bg="white")
header_frame.grid(column=0,row=0,sticky="nsew")


# Creating Menu icon
menu_label = tk.Label(header_frame,anchor=tk.W,bg="white")
menu_icon = tk.PhotoImage(file='./hamburger.png')
menu_label['image'] = menu_icon
menu_label.grid(column=0,row=0,sticky="nw")

# Writing the "Standard" text
standard_text = tk.Label(header_frame,text="Standard",fg="black",anchor=tk.W,background="white")
standard_text.grid(column=1,row=0,columnspan=2,sticky="nwe")

  # Changing font style
Font_tuple = ("Verdana",15,"normal")
standard_text.configure(font=Font_tuple)

# colored calculation_icon
action = tk.Label(header_frame,anchor="e")
action_image = tk.PhotoImage(file='./action.png')
action['image'] = action_image
action.grid(column=3,row=0,sticky="ne")

# Display Area
displayFrame = tk.Frame(wrapper_frame)
displayFrame.grid(column=0,row=1,sticky="nswe")

displayLabel = tk.Label(displayFrame ,text="0.",anchor="s")
displayLabel.grid(column=0,row=0, sticky="se",pady=6)
Display_Font_tuple = ("Tahoma",24,"bold")
displayLabel.configure(font=Display_Font_tuple)


# Clickable Buttons

# overall container frame for all the button
buttons_frame = tk.Frame(wrapper_frame,bg='')
buttons_frame.grid(column=0,row=2,sticky="nswe",pady=0)

# button first row frame (1)
frame1 = tk.Frame(buttons_frame)
frame1.grid(column=0,row=0,pady=1,sticky="nswe")

#  frame items
percent_button = tk.Button(frame1,bg="white", width=4,text="%",borderwidth=0,relief=tk.FLAT)
percent_button.grid(column=0,row=0,sticky="nswe",padx=1)

on_button = tk.Button(frame1,width=4,bg="white", text="CE",borderwidth=0,relief=tk.FLAT)
on_button.grid(column=1,row=0,sticky="nswe",padx=1)

store_button = tk.Button(frame1,width=4,bg="white", text="Str",borderwidth=0,relief=tk.FLAT)
store_button.grid(column=2,row=0,sticky="nswe",padx=1)

clear_button = tk.Button(frame1,width=4,bg="white", text="Del",borderwidth=0,relief=tk.FLAT)
clear_button.grid(column=3,row=0,sticky="nswe",padx=1)

# button second row frame (2)
frame2 = tk.Frame(buttons_frame)
frame2.grid(column=0,row=1,pady=1,sticky="nswe")


inverse_button = tk.Button(frame2,width=4,bg="white", text="1/x",borderwidth=0,relief=tk.FLAT)
inverse_button.grid(column=0,row=0,sticky="nswe",padx=1)

squared_button = tk.Button(frame2,width=4,bg="white", text="x^2",borderwidth=0,relief=tk.FLAT)
squared_button.grid(column=1,row=0,sticky="nswe",padx=1)

sq_rt_button = tk.Button(frame2,width=4,bg="white", text="root",borderwidth=0,relief=tk.FLAT)
sq_rt_button.grid(column=2,row=0,sticky="nswe",padx=1)

divide_button = tk.Button(frame2,width=4,bg="white", text="div",borderwidth=0,relief=tk.FLAT)
divide_button.grid(column=3,row=0,sticky="nswe",padx=1)

# button third row frame (3)
frame3 = tk.Frame(buttons_frame)
frame3.grid(column=0,row=2,pady=1,sticky="nswe",)
seven = tk.Button(frame3,width=4,bg="white", text="7",borderwidth=0,relief=tk.FLAT)
seven.grid(column=0,row=0,sticky="nswe",padx=1)

eight = tk.Button(frame3,width=4,bg="white", text="8",borderwidth=0,relief=tk.FLAT)
eight.grid(column=1,row=0,sticky="nswe",padx=1)

nine = tk.Button(frame3,width=4,bg="white", text="9",borderwidth=0,relief=tk.FLAT)
nine.grid(column=2,row=0,sticky="nswe",padx=1)

multiply = tk.Button(frame3,width=4,bg="white", text="div",borderwidth=0,relief=tk.FLAT)
multiply.grid(column=3,row=0,sticky="nswe",padx=1)

# button fourth row frame (4)
frame4 = tk.Frame(buttons_frame)
frame4.grid(column=0,row=3,pady=1,sticky="nswe",)
four = tk.Button(frame4,width=4,bg="white", text="4",borderwidth=0,relief=tk.FLAT)
four.grid(column=0,row=0,sticky="nswe",padx=1)

five = tk.Button(frame4,width=4,bg="white", text="5",borderwidth=0,relief=tk.FLAT)
five.grid(column=1,row=0,sticky="nswe",padx=1)

six = tk.Button(frame4,width=4,bg="white", text="6",borderwidth=0,relief=tk.FLAT)
six.grid(column=2,row=0,sticky="nswe",padx=1)

minus = tk.Button(frame4,width=4,bg="white", text="div",borderwidth=0,relief=tk.FLAT)
minus.grid(column=3,row=0,sticky="nswe",padx=1)

# button fifth row frame (5)
frame5 = tk.Frame(buttons_frame)
frame5.grid(column=0,row=4,pady=1,sticky="nswe",)
one = tk.Button(frame5,width=4,bg="white", text="1",borderwidth=0,relief=tk.FLAT)
one.grid(column=0,row=0,sticky="nswe",padx=1)

two = tk.Button(frame5,width=4,bg="white", text="2",borderwidth=0,relief=tk.FLAT)
two.grid(column=1,row=0,sticky="nswe",padx=1)

three = tk.Button(frame5,width=4,bg="white", text="3",borderwidth=0,relief=tk.FLAT)
three.grid(column=2,row=0,sticky="nswe",padx=1)

plus = tk.Button(frame5,width=4,bg="white", text="+",borderwidth=0,relief=tk.FLAT)
plus.grid(column=3,row=0,sticky="nswe",padx=1)

# button sixth row frame (6)
frame6 = tk.Frame(buttons_frame)
frame6.grid(column=0,row=5,pady=1,sticky="nswe",)
calc1 = tk.Button(frame6,width=4,bg="white", text="00",borderwidth=0,relief=tk.FLAT)
calc1.grid(column=0,row=0,sticky="nswe",padx=1)

zero = tk.Button(frame6,width=4,bg="white", text="0",borderwidth=0,relief=tk.FLAT)
zero.grid(column=1,row=0,sticky="nswe",padx=1)

dot = tk.Button(frame6,width=4, text=".",borderwidth=0,relief=tk.FLAT)
dot.grid(column=2,row=0,sticky="nswe",padx=1)

equal = tk.Button(frame6,width=4,bg="#05478A",fg="white", text="=",borderwidth=0,relief=tk.FLAT)
equal.grid(column=3,row=0,sticky="nswe")





# to Handle calculator responsiveness

root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)
wrapper_frame.columnconfigure(0,weight=1)
wrapper_frame.rowconfigure(0,weight=1)
wrapper_frame.rowconfigure(1,weight=1)
wrapper_frame.rowconfigure(2,weight=2)


header_frame.columnconfigure(0,weight=1)
header_frame.columnconfigure(1,weight=2)
header_frame.columnconfigure(3,weight=1)
header_frame.rowconfigure(0,weight=1)


displayFrame.columnconfigure(0,weight=1)
displayFrame.rowconfigure(0,weight=1)



buttons_frame.columnconfigure(0,weight=1)
buttons_frame.rowconfigure(0,weight=1)
buttons_frame.rowconfigure(1,weight=1)
buttons_frame.rowconfigure(2,weight=1)
buttons_frame.rowconfigure(3,weight=1)
buttons_frame.rowconfigure(4,weight=1)
buttons_frame.rowconfigure(5,weight=1)


frame1.rowconfigure(0,weight=1)
frame2.rowconfigure(0,weight=1)
frame3.rowconfigure(0,weight=1)
frame4.rowconfigure(0,weight=1)
frame5.rowconfigure(0,weight=1)
frame6.rowconfigure(0,weight=1)


frame1.columnconfigure(0,weight=1)
frame1.columnconfigure(1,weight=1)
frame1.columnconfigure(2,weight=1)
frame1.columnconfigure(3,weight=1)

frame2.columnconfigure(0,weight=1)
frame2.columnconfigure(1,weight=1)
frame2.columnconfigure(2,weight=1)
frame2.columnconfigure(3,weight=1)

frame3.columnconfigure(0,weight=1)
frame3.columnconfigure(1,weight=1)
frame3.columnconfigure(2,weight=1)
frame3.columnconfigure(3,weight=1)

frame4.columnconfigure(0,weight=1)
frame4.columnconfigure(1,weight=1)
frame4.columnconfigure(2,weight=1)
frame4.columnconfigure(3,weight=1)

frame5.columnconfigure(0,weight=1)
frame5.columnconfigure(1,weight=1)
frame5.columnconfigure(2,weight=1)
frame5.columnconfigure(3,weight=1)

frame6.columnconfigure(0,weight=1)
frame6.columnconfigure(1,weight=1)
frame6.columnconfigure(2,weight=1)
frame6.columnconfigure(3,weight=1)
 
root.maxsize(900,600)
root.minsize(100,600)
root.mainloop()