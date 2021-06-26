try:
    ......
except ValueError:
    print("값 오류")     
except IndexError:
    print("OutOfBoundIndexError")   
except Exception as e: 
    print("기타 일반오류")      
else:
    print("No error")    
finally:
    print("프로그램 종료")  