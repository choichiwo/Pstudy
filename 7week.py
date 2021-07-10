# __main__: 현재 main module로서 실행되는 모듈명

# __name__: 현재 module의 모듈명
# 
# 객체(object) -> 유형/무형 이름 사물 
# 클래스 class 안에 속성(property,attribute)과 동작(action, method)
# instance: 변수
# __init__(): 생성자   -> 특징은 자동호출하여 변수생성
# 
# IDE: 통합개발환경
# private: 사적인  

# def set_name(self, x):   #x는 setter
#     self.m = x  # setting 

# def get_name(self): #b는getter
#     return self.m #getting
# 
#  class Parent:
#       def __init__(self):
#           self.value = "테스트"
#           print("parent클래스의 __init__호출")
#       def test(self):
#           print("Parent클래스의 test 메소드")            
#  class Child(Parent):
#       def __init__(self):
#           Parent.__init__(self)
#           print("child클래스의 __init__호출")
#   c = Child() -> "parent클래스의 __init__호출","child클래스의 __init__호출"
#   c.test() -> "Parent클래스의 test 메소드"
#   print(c.value) -> "테스트"