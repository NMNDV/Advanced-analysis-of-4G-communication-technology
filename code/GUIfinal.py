from tkinter import *
import tkinter.messagebox
import channel, matrix_generator, encoder, decoder
import math



class Choice:
    def __init__(self, var1, var2, var3, rows, cols, H_matrix):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3
        self.rows = rows
        self.cols = cols
        self.H_matrix = H_matrix
choices = Choice(0, 0, 0, 0, 0, [])
choices_global = choices
def setvar1(i):
    choices.var1 = i

def setvar2(i):
    choices.var2 = i

def setvar3(i):
    choices.var3 = i

class SimpleTableInput(Frame):
    def __init__(self, parent, rows, columns):
        Frame.__init__(self, parent)

        self._entry = {}
        self.rows = rows
        self.columns = columns

        # register a command to use for validation
        vcmd = (self.register(self._validate), "%P")

        # create the table of widgets
        for row in range(self.rows):
            for column in range(self.columns):
                index = (row, column)
                e = Entry(parent, validate="key", validatecommand=vcmd)
                e.grid(row=row, column=column, stick="nsew")
                self._entry[index] = e
        # adjust column weights so they all expand equally
        for column in range(self.columns):
            self.grid_columnconfigure(column, weight=1)
        # designate a final, empty row to fill up any extra space
        self.grid_rowconfigure(rows, weight=1)

    def get(self):
        '''Return a list of lists, containing the data in the table'''
        result = []
        for row in range(self.rows):
            current_row = []
            for column in range(self.columns):
                index = (row, column)
                current_row.append(self._entry[index].get())
            result.append(current_row)
        return result

    def _validate(self, P):
        '''Perform input validation. 

        Allow only an empty value, or a value that can be converted to a float
        '''
        if P.strip() == "":
            return True

        try:
            f = float(P)
        except ValueError:
            self.bell()
            return False
        return True
def savmat(mat):
    choices.H_matrix = []
    for temp in mat:
        choices.H_matrix.append(list(map(int, temp)))
    print(choices_global.H_matrix, choices_global.var1, choices_global.var2, choices_global.var3)

def set_to_glob(frame_setting2, rows, columns):
    choices_global = choices
    choices_global.rows = rows
    choices_global.cols = columns
    frame_setting2.quit()
    if choices_global.var3 == 1:
        root2 = Tk()
        matrix_input = SimpleTableInput(root2, rows, columns)
        matrix_input.grid(row=11, column=1)
        button_LDPC = Button(root2, text="submit", command= lambda: savmat(matrix_input.get()))
        button_LDPC.grid(rows = rows + 1)
        root2.mainloop()
    else:
        choices.H_matrix = []

def is_valid(length, k):
    if choices_global.var3 == 0:
        '''if choices_global.var2 == 0:
            return  length == k
        else:
            return length == k + 1 + 2 * int(math.sqrt(k))'''
        return length == k
    else:
        return length == len(choices_global.H_matrix[0])
    



def setting_configure():
    setting_window = Tk()
    frame_setting2 = Frame(setting_window, height=800, width=900)
    var = IntVar()
    setting_of_channel_label = Label(frame_setting2, text="Channel Type : ")
    C1 = Radiobutton(frame_setting2, text="BSC channel", variable=var, value=0, command=lambda :setvar1(0))
    C2 = Radiobutton(frame_setting2, text="BEC channel", variable=var, value=1, command=lambda :setvar1(1))
    setting_of_channel_label.grid(row=0, column=0)
    C1.grid(row=0, column=1, sticky=W)
    C2.grid(row=1, column=1, sticky=W)
    var2 = IntVar()
    setting_of_channel_label2 = Label(frame_setting2, text="Message Type : ")
    T1 = Radiobutton(frame_setting2, text="Only Message of k bits", variable=var2, value=0, command=lambda :setvar2(0))
    T2 = Radiobutton(frame_setting2, text="Noisy Encoded Message", variable=var2, value=1, command=lambda :setvar2(1))
    var3 = IntVar()
    setting_of_channel_label2.grid(row=4, column=0)
    T1.grid(row=4, column=1, sticky=W)
    T2.grid(row=5, column=1, sticky=W)
    setting_of_channel_label3 = Label(frame_setting2, text="Type of Decoder : ")
    H1 = Radiobutton(frame_setting2, text="Product Code", variable=var3, value=0, command=lambda :setvar3(0))
    H2 = Radiobutton(frame_setting2, text="LDPC", variable=var3, value=1, command=lambda :setvar3(1))
    setting_of_channel_label3.grid(row=6, column=0)
    H1.grid(row=6, column=1, sticky=W)
    H2.grid(row=7, column=1, sticky=W)
    rows = Entry(frame_setting2)
    columns = Entry(frame_setting2)
    row_label = Label(frame_setting2, text="rows:")
    column_label = Label(frame_setting2, text="columns:")
    row_label.grid(row=8, column=0, sticky=E)
    column_label.grid(row=9, column=0, sticky=E)
    rows.grid(row=8, column=1)
    columns.grid(row=9, column=1)

    submit_button = Button(frame_setting2, text="Apply", command=lambda : set_to_glob(frame_setting2, int(rows.get()), int(columns.get())))
    submit_button.grid(row=15, column=1)
    frame_setting2.pack()
    setting_window.mainloop()
def show_inputerror():
    tkinter.messagebox.showerror(title="An error has occured", message="Invalid_Input")
root = Tk()
root.title("Communication Channel Simulator")
root.iconbitmap(bitmap=r"gui_icon.ico")
def do_analysis2(k, p, input_string):
            frame_output = Frame(root)
            length = len(input_string)
            ones = input_string.count("1")
            zeroes = input_string.count("0")
            errors = input_string.count('e')
            if length != 0 and length == ones + zeroes + errors and is_valid(len(input_string), k):
                msg = []
                if choices_global.var1 == 0:
                    msg = list(map(int, list(input_string)))
                else:
                    msg_dummy = list(input_string)
                    msg = []
                    for temp in msg_dummy:
                        if temp == 'e':
                            msg.append(-1)
                        else:
                            msg.append(int(temp))
                print(msg)
                H_mat = []
                if choices_global.var3 == 1:
                    H_mat = choices.H_matrix
                else:
                    if choices_global.var2 == 0:
                        H_mat = matrix_generator.get_set_of_matrices_advanced(k)[1]
                    else:
                        H_mat = matrix_generator.get_set_of_matrices_advanced(int(math.sqrt(k) - 1) ** 2)[1]
                print(H_mat)
                encoded_message = msg
                if choices_global.var2 == 0 and choices_global.var3 != 1:
                    encoded_message = encoder.product_code_encoder(msg)
                print(encoded_message)
                dumy_encoded_message = [ x for x in encoded_message ]
                noisy_signal = dumy_encoded_message
                if choices_global.var2 == 0:
                    if choices_global.var1 == 0:
                        noisy_signal = channel.insert_noise_BSC(dumy_encoded_message, p)
                    else:
                        noisy_signal = channel.insert_noise_BEC(dumy_encoded_message, p)
                print(noisy_signal)
                dumy_noisy_message = [x for x in noisy_signal]
                decoded_signal = dumy_noisy_message
                if choices_global.var3 == 0:
                    decoded_signal = decoder.decode(H_mat, dumy_noisy_message)
                else:
                    decoded_signal = decoder.decode(choices_global.H_matrix, dumy_encoded_message)
                print(decoded_signal)
                msg_label = Label(frame_output, text=str(msg))
                encoded_message_label = Label(frame_output, text=str(encoded_message))
                noisy_message_label = Label(frame_output, text=str(noisy_signal))
                decoded_message_label = Label(frame_output, text=str(decoded_signal))
                message_label = Label(frame_output, text="input message:")
                encoded_msg_label = Label(frame_output, text="Encoded message:")
                noisy_msg_label = Label(frame_output, text="Encoded message after adding noise:")
                decoded_msg_label = Label(frame_output, text="Decoded message:")
                message_label.grid(row=6, column=4, sticky=E)
                encoded_msg_label.grid(row=7, column=4, sticky=E)
                noisy_msg_label.grid(row=8, column=4, sticky=E)
                decoded_msg_label.grid(row=9, column=4, sticky=E)
                msg_label.grid(row=6, column=5, sticky=W)
                encoded_message_label.grid(row=7, column=5, sticky=W)
                noisy_message_label.grid(row=8, column=5, sticky=W)
                decoded_message_label.grid(row=9, column=5, sticky=W)
            else:
                return show_inputerror()
            button_cancel = Button(frame_output, text="Remove", fg="white", bg="red", command=frame_output.destroy)
            button_cancel.grid(row=10, column=4)
            frame_output.pack()
frame_head = Frame(root, height=600, width=500)
def do_analysis(k, p):
    print(k, p)
    if p != "" and k != "":
        p = float(p)
        k = int(k)
        if p > 1 or p < 0 or (choices_global.var3 == 0 and int(math.sqrt(k)) ** 2 != k):
            return show_inputerror()
        else:
            print(k, p)
            frame_down = Frame(root)
            msg_entry = Entry(frame_down)
            msg_label = Label(frame_down, text="message:")
            msg_entry.grid(row=4, column=4)
            button2 = Button(frame_head, text="Run", fg="white", bg="green",command=lambda : do_analysis2(k, p, msg_entry.get()))
            msg_label.grid(row=4, column=3, sticky=E)
            button2.grid(row=5, column=2, sticky=E)
            frame_down.pack()

button_setting = Button(frame_head, text="setting", command=setting_configure)


p = Entry(frame_head)
k = Entry(frame_head)
button1 = Button(frame_head, text="Go", fg="white", bg="green",command=lambda : do_analysis(k.get(), p.get()))
p_label = Label(frame_head, text="p:")
k_label = Label(frame_head, text="length of message signal:")
p_label.grid(row=1, column=3, sticky=E)
k_label.grid(row=0, column=3, sticky=E)
p.grid(row=1, column=4)
k.grid(row=0, column=4)
button1.grid(row=3, column=0)
button_setting.grid(row=1)
frame_head.pack()

root.mainloop()