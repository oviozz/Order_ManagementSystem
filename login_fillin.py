
class RegisterCheck:

    def signup_checking(self, name, email, password, error_handle, switch):
        if len(name.text()) > 3 and len(email.text()) > 3 and len(password.text()) > 3:
            return switch.setCurrentIndex(switch.currentIndex() + 1)
        return error_handle.setText('Please fill out the info')

    def login_checking(self, name, password, error_handle, switch):
        if len(name.text()) > 3 and len(password.text()) > 3:
            return switch.setCurrentIndex(switch.currentIndex() + 1)
        return error_handle.setText('Please fill out the info')


class PasswordCheck:
    def sign_up_info(self, name, password):
        with open("sign_up_form.txt", "a+") as store:
            store.write(f'{name.lower()}:{password.lower()}\n')

    def login_check(self, name, password,error_handle):
        with open('sign_up_form.txt', 'r') as store:
            for user in store.readlines():
                if name.lower() == user.split(':')[0] and password.lower() == user.replace('\n','').split(':')[1]:
                    return True
        error_handle.setText('Incorrect User ID')
        return False

class ChangeButtonColor:
    def log_in_click(self, button2):
        return button2.setStyleSheet("background-color: rgb(24, 160, 123);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "font: 14pt \"MS Shell Dlg 2\";\n"
                                          "gridline-color: rgb(24, 160, 123);")
    def sign_up_click(self, button1):
        return button1.setStyleSheet("background-color: rgb(67, 82, 89);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "font: 14pt \"MS Shell Dlg 2\";\n"
                                          "gridline-color: rgb(24, 160, 123);")
