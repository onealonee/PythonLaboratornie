import tkinter as tk
from tkinter import messagebox

class Example1App:
    def __init__(self, master):
        self.master = master
        master.title("Пример1")
        master.geometry("400x300")
        master.configure(bg="lightgray")

        # Кнопка для изменения цвета формы
        self.color_button = tk.Button(master, text="Цвет формы", command=self.change_color)
        self.color_button.pack(pady=10)

        # Метка для отображения названия цвета
        self.color_label = tk.Label(master, text="", font=("Arial", 12))
        self.color_label.pack()

        # Поле для отображения количества нажатий
        self.click_count_entry = tk.Entry(master, state="readonly", font=("Arial", 12))
        self.click_count_entry.pack(pady=10)

        # Меню
        menu_bar = tk.Menu(master)
        master.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Файл", menu=file_menu)
        file_menu.add_command(label="Выход", command=self.master.destroy)

        color_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Цвет формы", menu=color_menu)

        colors = ["Красный", "Синий", "Зеленый", "Желтый", "Фиолетовый"]
        for color in colors:
            color_menu.add_command(label=color, command=lambda c=color: self.change_color_by_menu(c))

        # Переключатель
        self.checkbox_var = tk.BooleanVar()
        self.checkbox = tk.Checkbutton(master, text="Переключатель", variable=self.checkbox_var)
        self.checkbox.pack()

        # Переключатели
        self.radio_var = tk.StringVar()
        self.radio_var.set("Красный")
        self.radio1 = tk.Radiobutton(master, text="Красный", variable=self.radio_var, value="Красный", command=self.change_color_by_radio)
        self.radio2 = tk.Radiobutton(master, text="Синий", variable=self.radio_var, value="Синий", command=self.change_color_by_radio)
        self.radio1.pack()
        self.radio2.pack()

        # Список выбора
        self.listbox = tk.Listbox(master)
        for color in colors:
            self.listbox.insert(tk.END, color)
        self.listbox.pack()
        self.listbox.bind("<<ListboxSelect>>", self.change_color_by_listbox)

        # Кнопка для соединения текста из полей
        self.concat_button = tk.Button(master, text="Соединить текст", command=self.concat_text)
        self.concat_button.pack(pady=10)

        # Кнопка для суммирования чисел из полей
        self.sum_button = tk.Button(master, text="Суммировать числа", command=self.sum_numbers)
        self.sum_button.pack()

        # Поля ввода
        self.entry1 = tk.Entry(master, font=("Arial", 12))
        self.entry2 = tk.Entry(master, font=("Arial", 12))
        self.entry1.pack()
        self.entry2.pack()

    def change_color(self):
        self.master.configure(bg="red")
        self.color_label.config(text="Красный")

    def change_color_by_menu(self, color):
        colors_dict = {"Красный": "red", "Синий": "blue", "Зеленый": "green", "Желтый": "yellow", "Фиолетовый": "purple"}
        self.master.configure(bg=colors_dict[color])
        self.color_label.config(text=color)
        self.update_click_count()

    def change_color_by_radio(self):
        color = self.radio_var.get()
        self.change_color_by_menu(color)

    def change_color_by_listbox(self, event):
        index = self.listbox.curselection()[0]
        color = self.listbox.get(index)
        self.change_color_by_menu(color)

    def update_click_count(self):
        count = int(self.click_count_entry.get()) + 1 if self.click_count_entry.get() else 1
        self.click_count_entry.config(state="normal")
        self.click_count_entry.delete(0, tk.END)
        self.click_count_entry.insert(0, str(count))
        self.click_count_entry.config(state="readonly")

    def concat_text(self):
        text1 = self.entry1.get()
        text2 = self.entry2.get()
        result = text1 + " " + text2
        messagebox.showinfo("Результат", result)

    def sum_numbers(self):
        try:
            num1 = int(self.entry1.get())
            num2 = int(self.entry2.get())
            result = num1 + num2
            messagebox.showinfo("Результат", f"Сумма чисел: {result}")
        except ValueError:
            messagebox.showerror("Ошибка", "Введите целые числа.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Example1App(root)
    root.mainloop()
