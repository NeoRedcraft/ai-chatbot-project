import socket
import threading
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog

class ChatClient:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(('127.0.0.1', 55555))

        # Create login window
        msg = tkinter.Tk()
        msg.withdraw()
        
        self.nickname = simpledialog.askstring("Nickname", "Please choose a nickname", parent=msg)

        self.gui_done = False
        self.running = True

        # Start GUI and receive threads
        gui_thread = threading.Thread(target=self.gui_loop)
        receive_thread = threading.Thread(target=self.receive)
        
        gui_thread.start()
        receive_thread.start()

    def gui_loop(self):
        # Chat window
        self.win = tkinter.Tk()
        self.win.configure(bg="lightgray")
        self.win.title(f"Chat - {self.nickname}")

        # Chat text area
        self.chat_area = tkinter.scrolledtext.ScrolledText(self.win)
        self.chat_area.pack(padx=20, pady=5)
        self.chat_area.config(state='disabled')

        # Message input area
        self.msg_label = tkinter.Label(self.win, text="Message:", bg="lightgray")
        self.msg_label.pack(padx=20, pady=5)
        
        self.input_area = tkinter.Text(self.win, height=3)
        self.input_area.pack(padx=20, pady=5)

        # Send button
        self.send_button = tkinter.Button(self.win, text="Send", command=self.write)
        self.send_button.pack(padx=20, pady=5)

        self.gui_done = True

        self.win.protocol("WM_DELETE_WINDOW", self.stop)
        self.win.mainloop()

    def write(self):
        message = f"{self.nickname}: {self.input_area.get('1.0', 'end')}"
        self.client.send(message.encode('utf-8'))
        self.input_area.delete('1.0', 'end')

    def stop(self):
        self.running = False
        self.win.destroy()
        self.client.close()
        exit(0)

    def receive(self):
        while self.running:
            try:
                message = self.client.recv(1024).decode('utf-8')
                if message == 'NICK':
                    self.client.send(self.nickname.encode('utf-8'))
                else:
                    if self.gui_done:
                        self.chat_area.config(state='normal')
                        self.chat_area.insert('end', message + '\n')
                        self.chat_area.yview('end')
                        self.chat_area.config(state='disabled')
            except ConnectionAbortedError:
                break
            except:
                print("Error")
                self.client.close()
                break

client = ChatClient()