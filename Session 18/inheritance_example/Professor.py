from BabsonPerson import *          # * = everything

class Professor(BabsonPerson):               #subcategory of BabsonPerson
    def __init__(self, name, course):
        BabsonPerson.__init__(self, name)
        self.course = course

    def speak(self, utterance):
        newUtterance = 'In course' +self.course + 'we say'
        return BabsonPerson.speak(self, newUtterance + utterance)

    def lecture(self, topic):
        return self.speak('it is obvious that ' + topic)

def main():
    faculty = Professor('Zhi Li', 'MIS3640')
    print(faculty.speak('Python is cool!'))
    print(faculty.lecture('Python is easy.'))

if __name__ == '__main__':
    main()
