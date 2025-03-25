from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime

class LibraryMnagementSystem:
    def __init__(self,root): 
        self.root=root
        self.root.title("Library Management System") 
        self.root.geometry("1929x1200+0+0")


    #*****************************Varaiable************************

        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.authorname_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook_var = StringVar()
        self.latereturnfine_var = StringVar()
        self.dateoverdue_var = StringVar()
        self.actualprice_var = StringVar()

         
        lbtitle=Label(self.root, text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue" ,fg="green" ,bd=20, relief=RIDGE,font=("times new roman",50,"bold") ,padx=2, pady=6)
        lbtitle.pack(side=TOP, fill=X)


        #*************************dataframe*******************
        frame=Frame(self.root,bd=12,relief=RIDGE , bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=400)

        #*************************dataframeleft*******************

        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="powder blue" ,fg="green" ,bd=12, relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5, width=890, height=350)

        lblMemberType = Label(DataFrameLeft, bg="powder blue",text="MemType", font=("times new roman", 14, "bold"), padx=2, pady=4)
        lblMemberType.grid(row=0, column=0, sticky=W)

        comMember = ttk.Combobox(DataFrameLeft,textvariable=self.member_var, font=("times new roman",12,"bold"),state="readonly", width=34)
        comMember["values"]=("Admin Staff", "Student", "Lecturer")
        comMember.current(0)
        comMember.grid(row=0, column=1)

        lblPRN_NO = Label(DataFrameLeft, bg="powder blue", text="PRN No:", font=("times new roman", 14, "bold"), padx=2, pady=4)
        lblPRN_NO.grid(row=1, column=0, sticky=W)
        txtPRN_NO = Entry(DataFrameLeft,textvariable=self.prn_var, font=("times new roman", 14, "bold"), width=29)
        txtPRN_NO.grid(row=1, column=1)

        lblID_NO = Label(DataFrameLeft, bg="powder blue", text="ID No:", font=("times new roman", 14, "bold"), padx=2, pady=4)
        lblID_NO.grid(row=2, column=0, sticky=W)
        txtID_NO = Entry(DataFrameLeft,textvariable=self.id_var, font=("times new roman", 14, "bold"), width=29)
        txtID_NO.grid(row=2, column=1)

        lblFirstName = Label(DataFrameLeft, bg="powder blue", text="First Name:", font=("times new roman", 14, "bold"), padx=2, pady=4)
        lblFirstName.grid(row=3, column=0, sticky=W)
        txtFirstName = Entry(DataFrameLeft,textvariable=self.firstname_var, font=("times new roman", 14, "bold"), width=29)
        txtFirstName.grid(row=3, column=1)

        lblLastName = Label(DataFrameLeft, bg="powder blue", text="Last Name:", font=("times new roman", 14, "bold"), padx=2, pady=4)
        lblLastName.grid(row=4, column=0, sticky=W)
        txtLastName = Entry(DataFrameLeft,textvariable=self.lastname_var, font=("times new roman", 14, "bold"), width=29)
        txtLastName.grid(row=4, column=1)

        lblAddress1 = Label(DataFrameLeft, bg="powder blue", text="Address 1:", font=("times new roman", 14, "bold"), padx=2, pady=4)
        lblAddress1.grid(row=5, column=0, sticky=W)
        txtAddress1 = Entry(DataFrameLeft,textvariable=self.address1_var, font=("times new roman", 14, "bold"), width=29)
        txtAddress1.grid(row=5, column=1)

        lblAddress2 = Label(DataFrameLeft, bg="powder blue", text="Address 2:", font=("times new roman", 14, "bold"), padx=2, pady=4)
        lblAddress2.grid(row=6, column=0, sticky=W)
        txtAddress2 = Entry(DataFrameLeft,textvariable=self.address2_var, font=("times new roman", 14, "bold"), width=29)
        txtAddress2.grid(row=6, column=1)

        lblPostCode = Label(DataFrameLeft, bg="powder blue", text="Post Code:", font=("times new roman", 14, "bold"), padx=2, pady=4)
        lblPostCode.grid(row=7, column=0, sticky=W)
        txtPostCode = Entry(DataFrameLeft,textvariable=self.postcode_var, font=("times new roman", 14, "bold"), width=29)
        txtPostCode.grid(row=7, column=1)

        lblMobile = Label(DataFrameLeft, bg="powder blue", text="Mobile:", font=("times new roman", 14, "bold"), padx=2, pady=3)
        lblMobile.grid(row=8, column=0, sticky=W)
        txtMobile = Entry(DataFrameLeft, textvariable=self.mobile_var,font=("times new roman", 14, "bold"),width=29)
        txtMobile.grid(row=8, column=1)

        # ================= Second Column (Starting at row=0, column=2) =================
        lblBookId = Label(DataFrameLeft, bg="powder blue", text="Book ID:", font=("times new roman", 14, "bold"), padx=2, pady=4)
        lblBookId.grid(row=0, column=2, sticky=W)
        txtBookId = Entry(DataFrameLeft,textvariable=self.bookid_var, font=("times new roman", 14, "bold"), width=29)
        txtBookId.grid(row=0, column=3)

        lblBookTitle = Label(DataFrameLeft, bg="powder blue", text="Book Title:", font=("times new roman", 14, "bold"), padx=2, pady=4)
        lblBookTitle.grid(row=1, column=2, sticky=W)
        txtBookTitle = Entry(DataFrameLeft,textvariable=self.booktitle_var, font=("times new roman", 14, "bold"), width=29)
        txtBookTitle.grid(row=1, column=3)

        lblAuthorName = Label(DataFrameLeft, bg="powder blue", text="Author Name:", font=("times new roman", 14, "bold"), padx=2, pady=4)
        lblAuthorName.grid(row=2, column=2, sticky=W)
        txtAuthorName = Entry(DataFrameLeft,textvariable=self.authorname_var, font=("times new roman", 14, "bold"), width=29)
        txtAuthorName.grid(row=2, column=3)

        lblDateBorrowed = Label(DataFrameLeft, bg="powder blue", text="Date Borrowed:", font=("times new roman", 14, "bold"), padx=2, pady=4)
        lblDateBorrowed.grid(row=3, column=2, sticky=W)
        txtDateBorrowed = Entry(DataFrameLeft,textvariable=self.dateborrowed_var, font=("times new roman", 14, "bold"), width=29)
        txtDateBorrowed.grid(row=3, column=3)

        lblDateDue = Label(DataFrameLeft, bg="powder blue", text="Date Due:", font=("times new roman", 14, "bold"), padx=2, pady=4)
        lblDateDue.grid(row=4, column=2, sticky=W)
        txtDateDue = Entry(DataFrameLeft,textvariable=self.datedue_var, font=("times new roman", 14, "bold"), width=29)
        txtDateDue.grid(row=4, column=3)

        lblDaysOnBook = Label(DataFrameLeft, bg="powder blue", text="Days On Book:", font=("times new roman", 14, "bold"), padx=2, pady=4)
        lblDaysOnBook.grid(row=5, column=2, sticky=W)
        txtDaysOnBook = Entry(DataFrameLeft,textvariable=self.daysonbook_var, font=("times new roman", 14, "bold"), width=29)
        txtDaysOnBook.grid(row=5, column=3)

        lblLateReturnFine = Label(DataFrameLeft, bg="powder blue", text="Late Return Fine:", font=("times new roman", 14, "bold"), padx=2, pady=4)
        lblLateReturnFine.grid(row=6, column=2, sticky=W)
        txtLateReturnFine = Entry(DataFrameLeft,textvariable=self.latereturnfine_var, font=("times new roman", 14, "bold"), width=29)
        txtLateReturnFine.grid(row=6, column=3)

        lblDateOverDue = Label(DataFrameLeft, bg="powder blue", text="Date Over Due:", font=("times new roman", 15, "bold"), padx=2, pady=4)
        lblDateOverDue.grid(row=7, column=2, sticky=W)
        txtDateOverDue = Entry(DataFrameLeft,textvariable=self.dateoverdue_var, font=("times new roman",14, "bold"), width=29)
        txtDateOverDue.grid(row=7, column=3)

        lblActualPrice = Label(DataFrameLeft, bg="powder blue", text="Actual Price:", font=("times new roman", 14, "bold"), padx=2, pady=4)
        lblActualPrice.grid(row=8, column=2, sticky=W)
        txtActualPrice = Entry(DataFrameLeft, textvariable=self.actualprice_var,font=("times new roman", 14, "bold"), width=29)
        txtActualPrice.grid(row=8, column=3)

        #****************data frame right**********************

        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue" ,fg="green" ,bd=12, relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameRight.place(x=870,y=5, width=580, height=350)
        self.txtBox=Text(DataFrameRight, font=("times new roman",12,"bold"), width=32 , height=16 ,padx=2, pady=6)
        self.txtBox.grid(row=0,column=2)

        listSrollbar= Scrollbar(DataFrameRight) 
        listSrollbar.grid(row=0, column=1, sticky="ns")

        listBooks=["Introduction to the Theory of Computation",
        "Structure and Interpretation of Computer Programs",
        "Computer Networking: A Top-Down Approach",
        "Artificial Intelligence: A Modern Approach",
        "The Pragmatic Programmer",
        "Design Patterns: Elements of Reusable Object-Oriented Software",
        "Operating System Concepts",
        "Clean Code",
        "Algorithms",
        "Introduction to Algorithms",
        "Computer Organization and Design",
        "Database System Concepts",
        "The Art of Computer Programming",
        "You Don't Know JS",
        "Python Crash Course",
        "Deep Learning",
        "Code: The Hidden Language of Computer Hardware and Software",
        "Compilers: Principles, Techniques, and Tools",
        "Computer Science Distilled",
        "Grokking Algorithms"]
        def SelectBook(event=""):
            Value = str(listbox.get(listbox.curselection()[0]))

            x= Value
            if (x=="Introduction to the Theory of Computation"):
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("Automata manual")
                self.authorname_var.set("John Hopcroft and Jeffery Ullman")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2 
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("788")

            elif (x=="Structure and Interpretation of Computer Programs"):
                self.bookid_var.set("BKID5455")
                self.booktitle_var.set("Computer manual")
                self.authorname_var.set("Kyle MacRae")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2 
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("765")

            elif (x=="Computer Networking: A Top-Down Approach"):
                self.bookid_var.set("BKID5456")
                self.booktitle_var.set("Networking manual")
                self.authorname_var.set("David j.Wetherall")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2 
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("987")

            elif (x == "Artificial Intelligence: A Modern Approach"):
                self.bookid_var.set("BKID1001")
                self.booktitle_var.set("AI Guide")
                self.authorname_var.set("Stuart Russell, Peter Norvig")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("1200")

            elif (x == "The Pragmatic Programmer"):
                self.bookid_var.set("BKID1002")
                self.booktitle_var.set("Pragmatic Dev")
                self.authorname_var.set("Andrew Hunt, David Thomas")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("850")

            elif (x == "Design Patterns: Elements of Reusable Object-Oriented Software"):
                self.bookid_var.set("BKID1003")
                self.booktitle_var.set("Design Patterns")
                self.authorname_var.set("Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("950")

            elif (x == "Operating System Concepts"):
                self.bookid_var.set("BKID1004")
                self.booktitle_var.set("OS Principles")
                self.authorname_var.set("Abraham Silberschatz, Peter Baer Galvin, Greg Gagne")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("1100")

            elif (x == "Clean Code"):
                self.bookid_var.set("BKID1005")
                self.booktitle_var.set("Code Cleanliness")
                self.authorname_var.set("Robert C. Martin")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("750")

            elif (x == "Algorithms"):
                self.bookid_var.set("BKID1006")
                self.booktitle_var.set("Algorithm Basics")
                self.authorname_var.set("Robert Sedgewick, Kevin Wayne")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("900")

            elif (x == "Introduction to Algorithms"):
                self.bookid_var.set("BKID1007")
                self.booktitle_var.set("CLRS")
                self.authorname_var.set("Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("1250")

            elif (x == "Computer Organization and Design"):
                self.bookid_var.set("BKID1008")
                self.booktitle_var.set("Comp Org & Arch")
                self.authorname_var.set("David A. Patterson, John L. Hennessy")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("980")

            elif (x == "Database System Concepts"):
                self.bookid_var.set("BKID1009")
                self.booktitle_var.set("DBMS Concepts")
                self.authorname_var.set("Abraham Silbe")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("1025")

            elif (x == "The Art of Computer Programming"):
                self.bookid_var.set("BKID1010")
                self.booktitle_var.set("Comp Prog Art")
                self.authorname_var.set("Donald Knuth")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("50")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("1400")

 
 


        
        listbox=Listbox(DataFrameRight,font=("times new roman",12,"bold"), width=20 , height=16 )
        listbox.bind("<<ListboxSelect>>",SelectBook)
        listbox.grid(row=0, column=0,padx=4)
        listSrollbar.config(command=listbox.yview)

        for item in listBooks:
            listbox.insert(END,item)

        

        #*****************BUTTONS FRAME************************* 

        framebutton=Frame(self.root,bd=12,relief=RIDGE ,padx=70, bg="powder blue")
        framebutton.place(x=0, y=530, width=1530, height=60)

        btnAddData=Button(framebutton,command=self.add_data,text="Add Data",font=("times new roman",12,"bold"), width=23, bg="blue", fg="white")
        btnAddData.grid(row=0, column=0)

        btnAddData=Button(framebutton,command=self.show_data,text="Show Data",font=("times new roman",12,"bold"), width=23, bg="blue", fg="white")
        btnAddData.grid(row=0, column=1)

        btnAddData=Button(framebutton, command=self.update,text="Update",font=("times new roman",12,"bold"), width=23, bg="blue", fg="white")
        btnAddData.grid(row=0, column=2)

        btnAddData=Button(framebutton , command=self.delete,text="Delete",font=("times new roman",12,"bold"), width=23, bg="blue", fg="white")
        btnAddData.grid(row=0, column=3)

        btnAddData=Button(framebutton,command=self.reset,text="Reset",font=("times new roman",12,"bold"), width=23, bg="blue", fg="white")
        btnAddData.grid(row=0, column=4)

        btnAddData=Button(framebutton,command=self.exit, text="Exit",font=("times new roman",12,"bold"), width=23, bg="blue", fg="white")
        btnAddData.grid(row=0, column=5)


        #*****************INFORMATION FRAME*************************

        FrameDetails=Frame(self.root,bd=12,relief=RIDGE ,padx=20, bg="powder blue")
        FrameDetails.place(x=0, y=600, width=1530, height=195)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE ,bg="powder blue")
        Table_frame.place(x=0, y=2, width=1475, height=175)

        xscroll=ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame,column=("membertype", "prnno", "idno", "firstname", "lastname", "address1",
                                 "address2", "postcode", "mobile", "bookid", "booktitle", "authorname",
                                 "dateborrowed", "datedue", "daysonbook", "latereturnfine",
                                 "dateoverdue", "actualprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM ,fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype", text="Member Type")
        self.library_table.heading("prnno", text="PRN No")
        self.library_table.heading("idno", text="ID No")
        self.library_table.heading("firstname", text="First Name")
        self.library_table.heading("lastname", text="Last Name")
        self.library_table.heading("address1", text="Address 1")
        self.library_table.heading("address2", text="Address 2")
        self.library_table.heading("postcode", text="Post Code")
        self.library_table.heading("mobile", text="Mobile")
        self.library_table.heading("bookid", text="Book ID")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("authorname", text="Author Name")
        self.library_table.heading("dateborrowed", text="Date Borrowed")
        self.library_table.heading("datedue", text="Date Due")
        self.library_table.heading("daysonbook", text="Days On Book")
        self.library_table.heading("latereturnfine", text="Late Return Fine")
        self.library_table.heading("dateoverdue", text="Date Over Due")
        self.library_table.heading("actualprice", text="Actual Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH, expand=1)

        self.library_table.column("membertype", width=100)
        self.library_table.column("prnno", width=100)
        self.library_table.column("idno", width=100)
        self.library_table.column("firstname", width=100)
        self.library_table.column("lastname", width=100)
        self.library_table.column("address1", width=100)
        self.library_table.column("address2", width=100)
        self.library_table.column("postcode", width=100)
        self.library_table.column("mobile", width=100)
        self.library_table.column("bookid", width=100)
        self.library_table.column("booktitle", width=100)
        self.library_table.column("authorname", width=100)
        self.library_table.column("dateborrowed", width=100)
        self.library_table.column("datedue", width=100)
        self.library_table.column("daysonbook", width=100)
        self.library_table.column("latereturnfine", width=100)
        self.library_table.column("dateoverdue", width=100)
        self.library_table.column("actualprice", width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    def  add_data(self):
        conn= mysql.connector.connect(host="localhost", username="root", password="Hitman@45", database="LibraryDB")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library_members values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            self.member_var.get(),
            self.prn_var.get(),
            self.id_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address1_var.get(),
            self.address2_var.get(),
            self.postcode_var.get(),
            self.mobile_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.authorname_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.daysonbook_var.get(),
            self.latereturnfine_var.get(),
            self.dateoverdue_var.get(),
            self.actualprice_var.get()

            ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success","Member has been inserted succesfully")

    def fetch_data(self):
        conn= mysql.connector.connect(host="localhost", username="root", password="Hitman@45", database="LibraryDB")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library_members")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content["values"]

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.authorname_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.actualprice_var.set(row[17])

    def show_data(self):
        self.txtBox.insert(END,"MemType:\t\t"+ self.member_var.get()+"\n")
        self.txtBox.insert(END, "PRN No:\t\t" + self.prn_var.get() + "\n")
        self.txtBox.insert(END, "ID No:\t\t" + self.id_var.get() + "\n")
        self.txtBox.insert(END, "First Name:\t\t" + self.firstname_var.get() + "\n")
        self.txtBox.insert(END, "Last Name:\t\t" + self.lastname_var.get() + "\n")
        self.txtBox.insert(END, "Address1:\t\t" + self.address1_var.get() + "\n")
        self.txtBox.insert(END, "Address2:\t\t" + self.address2_var.get() + "\n")
        self.txtBox.insert(END, "Postcode:\t\t" + self.postcode_var.get() + "\n")
        self.txtBox.insert(END, "Mobile:\t\t" + self.mobile_var.get() + "\n")
        self.txtBox.insert(END, "Book ID:\t\t" + self.bookid_var.get() + "\n")
        self.txtBox.insert(END, "Book Title:\t\t" + self.booktitle_var.get() + "\n")
        self.txtBox.insert(END, "Author Name:\t\t" + self.authorname_var.get() + "\n")
        self.txtBox.insert(END, "Date Borrowed:\t\t" + self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END, "Date Due:\t\t" + self.datedue_var.get() + "\n")
        self.txtBox.insert(END, "Days on Book:\t\t" + str(self.daysonbook_var.get()) + "\n")
        self.txtBox.insert(END, "Late Return Fine:\t\t" + str(self.latereturnfine_var.get()) + "\n")
        self.txtBox.insert(END, "Date Overdue:\t\t" + self.dateoverdue_var.get() + "\n")
        self.txtBox.insert(END, "Actual Price:\t\t" + str(self.actualprice_var.get()) + "\n")

    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.authorname_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue_var.set(""),
        self.actualprice_var.set("")
        self.txtBox.delete("1.0",END)

    def exit(self):
        exit= tkinter.messagebox.askyesno("Library Management Sytem","Do you want to exit")
        if exit>0:
            self.root.destroy()
            return
        

    def update(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Hitman@45", database="LibraryDB")
        my_cursor=conn.cursor()
        my_cursor.execute("update library_members set  membertype=%s, idno=%s, firstname=%s, lastname=%s, address1=%s, address2=%s, postcode=%s, mobile=%s, bookid=%s, booktitle=%s, authorname=%s, dateborrowed=%s, datedue=%s, daysonbook=%s, latereturnfine=%s, dateoverdue=%s, actualprice=%s where prnno=%s ",(
            self.member_var.get(),
            self.id_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address1_var.get(),
            self.address2_var.get(),
            self.postcode_var.get(),
            self.mobile_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.authorname_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.daysonbook_var.get(),
            self.latereturnfine_var.get(),
            self.dateoverdue_var.get(),
            self.actualprice_var.get(),
            self.prn_var.get()

        ))
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success","Member has been updated")

    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First select the number")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Hitman@45", database="LibraryDB")
            my_cursor=conn.cursor()
            query="delete from library_members where prnno=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","Member has been deleted")


           
            







if __name__ =="__main__":
    root=Tk()
    obj=LibraryMnagementSystem(root)
    root.mainloop()
        