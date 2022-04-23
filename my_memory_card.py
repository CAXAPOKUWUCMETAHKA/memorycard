from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
from random import shuffle, randint


class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

Question_list = []
Question_list.append(Question ('Первая буква в алфавите', 'А', 'Я', 'Ь', 'О',))
Question_list.append(Question ('зимой белый летом серый', 'заяц', 'медведь', 'олень', 'мышь'))
Question_list.append(Question ('государственный язык Англии', 'Английский', 'Русский', 'Фиолетовый', 'Мягкий'))
Question_list.append(Question ('Самое холодное время года', 'Зима', 'Осень', 'Весна', 'Лето'))
Question_list.append(Question ('Кково цвета трава', 'зеленая', 'черная', 'красная', 'синяя'))
Question_list.append(Question ('Елки зимой', 'зеленые', 'желтые', 'красные', 'оранжевые'))
Question_list.append(Question ('2+2', '4', '5', '9', '15'))

 
app = QApplication([])


btn_OK = QPushButton('Ответить')
Button = QPushButton('выход') 
lb_Question = QLabel('Самый сложный вопрос в мире!') 
 

RadioGroupBox = QGroupBox("Варианты ответов")


rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')
 

RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
 

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
 

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
 

RadioGroupBox.setLayout(layout_ans1)
 

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') 
lb_Correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
 

layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout() 
 

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide()
 

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addWidget(Button,alignment=Qt.AlignRight)
layout_line3.addStretch(1)
 

layout_card = QVBoxLayout()
 

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым
 

# ----------------------------------------------------------
# Виджеты и макеты созданы, далее - функции:


def show_res():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText("Слудующий вопрос")
 

def show_quest():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText("Ответить")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
 
 
answer = [ rbtn_1,rbtn_2,rbtn_3,rbtn_4]
 
def ask(q:Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_quest()
 

def  show_correct(res):
    lb_Result.setText(res)
    show_res()
 
 
def check_answer():
    if answer[0].isChecked():
        show_correct("Правильно!")
        print('Cтатисьтика \n - Dctuj djghjcjd', window.total,'\n - Ghfdtkmys[ jndtnjd :', window.score)
        print('Рейтинг:', (window.score / window.total * 100), '%')
        window.score += 1
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked() :
            show_correct("Неверно!")
def next_questions():
    window.total += 1
    print('Cтатисьтика \n - Dctuj djghjcjd', window.total,'\n - Ghfdtkmys[ jndtnjd :', window.score)
    cur_question = randint(0, len(Question_list)-1)
    q = Question_list[cur_question]
    ask(q)
    Question_list.remove(Question_list[cur_question])
    if len(Question_list) == -1:
        show_correct('Вопросы закончились')



def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_questions()

window = QWidget()
window.setLayout(layout_card)
Button.clicked.connect(QCoreApplication.instance().quit)
btn_OK.clicked.connect(click_OK)
window.total = 0
window.score = 0

next_questions()


window.setWindowTitle("Memo Card")
window.show()
app.exec_()