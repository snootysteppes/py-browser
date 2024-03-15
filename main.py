from tkinter import *
import tkinterweb
import webbrowser

class Browser(Tk):
    def __init__(self):
        super(Browser, self).__init__()
        self.title("Tk Browser")
        self.browser = self.create_browser()
        self.create_search_bar()
        self.create_new_tab_button()

    def create_browser(self):
        try:
            browser = tkinterweb.HtmlFrame(self)
            browser.pack(fill="both", expand=True)
            return browser
        except Exception as e:
            print(f"An error occurred: {e}")
            sys.exit()

    def create_search_bar(self):
        search_bar = Entry(self)
        search_bar.bind('<Return>', self.load_website_from_search_bar)
        search_bar.pack()

    def create_new_tab_button(self):
        new_tab_button = Button(self, text="New Tab", command=self.open_new_tab)
        new_tab_button.pack()

    def open_new_tab(self):
        webbrowser.open_new_tab("https://google.com")

    def load_website_from_search_bar(self, event):
        search_bar = event.widget
        url = search_bar.get()
        if self.browser:
            self.browser.load_website(url)

def main():
    browser = Browser()
    browser.mainloop()

if __name__ == "__main__":
    main()
