import os
import re
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

class makeGUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.make_template(master)
        self.credit_path = ''
        self.bl_path = ''
        self.excel_path=''
        self.filename = ''
        self.program_path = ''

    def make_template(self, master):
        frame = tk.Frame(master=master, borderwidth=1, height=100)
        frame1 = tk.Frame(master=master, borderwidth=1, height=100)

        for i in range(4):
            frame.grid_columnconfigure(i, weight=1)

        for i in range(4):
            frame1.grid_columnconfigure(i, weight=1)

        credit = tk.Label(master=frame, text="신용장 경로:")
        credit.grid(row=1, column=1, sticky='W')

        credit_path1 = tk.StringVar()
        credit_path = tk.Entry(master=frame, width=20, textvariable=credit_path1)
        credit_path.grid(row=1, column=2, sticky='W', pady=5, padx=10)




        bl = tk.Label(master=frame, text="bl 경로:")
        bl.grid(row=2, column=1, sticky='WE')

        bl_path1 = tk.StringVar()
        bl_path = tk.Entry(master=frame, width=20, textvariable=bl_path1)
        bl_path.grid(row=2, column=2, sticky='WE', pady=5, padx=10)

 


        output = tk.Label(master=frame, text="출력파일 경로:")
        output.grid(row=3, column=1, sticky='WE')

        output_path1 = tk.StringVar()
        output_path = tk.Entry(master=frame, width=20, textvariable=output_path1)
        output_path.grid(row=3, column=2, sticky='WE', pady=5, padx=10)

        output_button = tk.Button(master=frame, 
                                  width=10,
                                  command=lambda:self.browse_folder(output_path, "output",
                                                os.path.join(os.environ["HOMEPATH"], "Desktop")),
                                  text='클릭')
        output_button.grid(row=3, column=3, sticky='WE', pady=5, padx=10)

        output = tk.Label(master=frame, text="출력파일 경로:")
        output.grid(row=3, column=1, sticky='WE')

        output_path1 = tk.StringVar()
        output_path = tk.Entry(master=frame, width=20, textvariable=output_path1)
        output_path.grid(row=3, column=2, sticky='WE', pady=5, padx=10)

        output_button = tk.Button(master=frame, 
                                  width=10,
                                  command=lambda:self.browse_folder(output_path, "output",
                                                os.path.join(os.environ["HOMEPATH"], "Desktop")),
                                  text='클릭')


        program = tk.Label(master=frame, text="프로그램 경로:")
        program.grid(row=5, column=1, sticky='WE')

        text = os.path.join(os.environ["HOMEPATH"], "Desktop")
        program_path1 = tk.StringVar()
        program_path = tk.Entry(master=frame, width=20, textvariable=program_path1)
        program_path.insert(0, text)
        program_path.grid(row=5, column=2, sticky='WE', pady=5, padx=10)

        program_button = tk.Button(master=frame, 
                                  width=10,
                                  command=lambda:self.browse_folder(program_path, "program",
                                                os.path.join(os.environ["HOMEPATH"], "Desktop")),
                                  text='클릭')
        program_button.grid(row=5, column=3, sticky='WE', pady=5, padx=10)


        output_filename = tk.Label(master=frame, text="출력파일 이름:")
        output_filename.grid(row=4, column=1, sticky='WE')


        output_filename1 = tk.StringVar()
        output_filename_value = tk.Entry(master=frame, width=20, textvariable=output_filename1)
        output_filename_value.insert(0, 'output')
        output_filename_value.grid(row=4, column=2, sticky='WE', pady=5, padx=10)

        
        credit_button = tk.Button(master=frame, 
                                  width=10,
                                  command=lambda:self.browse_files(credit_path, "credit",
                                                                   output_filename_value),
                                  text='클릭')
        credit_button.grid(row=1, column=3, sticky='WE', pady=5, padx=10)


        bl_button = tk.Button(master=frame, 
                                  width=10,
                                  command=lambda:self.browse_files(bl_path, "bl",
                                                                    output_filename_value),
                                  text='클릭')
        bl_button.grid(row=2, column=3, sticky='WE', pady=5, padx=10)

        output_button = tk.Button(master=frame, 
                                  width=10,
                                  command=lambda:self.browse_folder(output_path, "output",
                                                os.path.join(os.environ["HOMEPATH"], "Desktop")),
                                  text='클릭')
        output_button.grid(row=3, column=3, sticky='WE', pady=5, padx=10)



        OKBUTTON = tk.Button(master=frame1,  width =10, 
                             text='OK', 
                             command=lambda:self.start_parsing(self.credit_path, 
                                                               self.bl_path,
                                                               self.excel_path,
                                                               output_filename_value))
        OKBUTTON.grid(row=6, column=9, sticky='NE', pady=10, padx=10)

        CANCELBUTTON = tk.Button(master=frame1,  width =10, 
                                text='Cancel', command=exit)
        CANCELBUTTON.grid(row=6, column=10, sticky='NE', pady=10, padx=10)
        frame.pack(fill=tk.X, side=tk.TOP)
        frame1.pack(fill=tk.X, side=tk.BOTTOM)


    def start_parsing(self, credit, bl, excel, filename_entity):
        if credit == '' or bl == '' or excel == '':
            messagebox.showwarning("Warning","경로가 모두 채워지지 않았습니다.")
            return
        self.filename = filename_entity.get()
        self.master.quit()
        #excel위치에 csv로 저장할것

        # 다음 gui 불러올것
        #invoice.main()

    def browse_folder(self, e, path_name, init_dir):
        
        folder_name = filedialog.askdirectory(initialdir = init_dir,
                                              title="Select a Foler")
        e.insert(0, folder_name)
        self.set_path(folder_name, path_name)



    def browse_files(self, e, path_name, filename_entry):
        filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          )
        e.delete(0, tk.END)
        e.insert(0, filename)
        name = re.compile('([가-힣]+.+)').findall(filename.split("/")[-1])[0].replace('.TXT','').replace('수표','').replace('신용장','').replace('.pdf','')
        filename_entry.delete(0, tk.END)
        filename_entry.insert(0, name)
        self.set_path(filename, path_name)

    def set_path(self, filename, path_name):
        if path_name == 'bl':
            self.bl_path = filename
        elif path_name == 'credit':
            self.credit_path = filename
        elif path_name == 'output':
            self.excel_path = filename
        elif path_name == 'program':
            self.program_path = filename



def gui_main():
    root = tk.Tk()
    gui = makeGUI(root)
    gui.master.title("File Founder")
    gui.master.minsize(100, 100)
    gui.mainloop()

    return gui.credit_path, gui.bl_path, gui.excel_path, gui.filename, gui.program_path


if __name__ == "__main__":
    gui_main()