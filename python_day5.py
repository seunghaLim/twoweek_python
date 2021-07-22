# #클래스의 메소드 - 클래스에 묶여서 클래스의 인스턴스와 관계되는 일을 하는 함수

# class AttackUnit:
#     def __init__(self, name, hp, damage):     
#         self.name = name     
#         self.hp = hp
#         self.damage = damage

#     #메소드 2개 - attack와 damaged
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))      #앞에 self가 붙으면 - 유닛 내부 변수 / 없으면 전달받은 인자값
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))


# firebat = AttackUnit("파이어뱃", 50, 16)
# firebat.attack("5시")
# firebat.damaged(25)
# firebat.damaged(25)

# #상속 - Unit이라는 클래스의 멤버 변수를 상속받아서 attackUnit 제작 

# class Unit: 
#     def __init__(self, name, hp):       #__init__ 생성자. 
#         self.name = name        #멤버 변수 - class 안에서 정의된 변수. self.mame, self.damage, self.hp 등등...
#         self.hp = hp


# class AttackUnit(Unit):     #Unit이라는 클래스를 상속받아서 AttackUnit을 만듦 Unit - 부모 클래스, AttackUnit - 자식 클래스
#     def __init__(self, name, hp, damage):     
#         Unit.__init__(self, name, hp)
#         self.damage = damage

#     #메소드 2개 - attack와 damaged
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))      #앞에 self가 붙으면 - 유닛 내부 변수 / 없으면 전달받은 인자값
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# firebat = AttackUnit("파이어뱃", 50, 16)
# firebat.attack("5시")
# firebat.damaged(25)
# firebat.damaged(25)

# #다중상속 - 여러개의 클래스를 받아서 상속받는 것

# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))

# #공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):       #클래스 두 개를 받아서 클래스를 만듦
#     def __init__(self, name, hp, damage, flying_speed): 
#         AttackUnit.__init__(self, name, hp, damage)
#         Flyable.__init__(self, flying_speed)

# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")      #이름. 으로 부모 클래스에 접근해서 변수를 쓰거나 메소드 사용 가능
# valkyrie.attack("3시")
# valkyrie.damaged(200)

# #메소드 오버라이딩 


# class Unit: 
#     def __init__(self, name, hp, speed):      
#         self.name = name        
#         self.hp = hp
#         self.speed = speed

#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# class AttackUnit(Unit):     
#     def __init__(self, name, hp, speed, damage):     
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     #메소드 2개 - attack와 damaged
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))      #앞에 self가 붙으면 - 유닛 내부 변수 / 없으면 전달받은 인자값
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))


# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# #공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):       #클래스 두 개를 받아서 클래스를 만듦
#     def __init__(self, name, hp, damage, flying_speed): 
#         AttackUnit.__init__(self, name, hp, 0, damage)
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)     #Flyable 클래스에 있는 메소드. self 없이 보내도 됨
#         #Flyable이라는 부모 클래스가 이제 내 것이 되었으니 self.를 써주고 flyable 클래스에 있는 fly 함수를 사용

    

# vulture = AttackUnit("벌쳐", 80, 10, 20)
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("5시")
# battlecruiser.move("5시")

# #패스
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass       #pass 하고 그냥 넘어감

# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     pass

# game_start()
# game_over()

# #supper
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         #Unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0)       #위에 Unit을 불러오는 것 대신 super을 써서 만들 수 있음. super을 쓸 경우 ()를 붙이고 self는 안써줌
#         self.location = location

# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# # 주의!! 다중상속을 받을 때 super을 사용하면 맨 처음에 넣어준 매개변수 클래스만 작동됨. 다중상속 시 클래스를 일일이 다 정의해주는 걸로

# #퀴즈
# class House:
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year
    
#     def show_detail(self):
#         print("{0} {1} {2} {3} {4}".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))
#         #print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

# h1 = House("강남", "아파트", "매매", "10억", "2010년")
# h2 = House("마포", "오피스텔", "전세", "5억", "2007년")
# h3 = House("송파", "빌라", "월세", "500/50", "2000년")

# print("총 3대의 매물이 있습니다.")
# h1.show_detail()
# h2.show_detail()
# h3.show_detail()

# '''
# house = []
# house1 = House("강남", "아파트", "매매", "10억", "2010년")
# house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
# house3 = House("송파", "빌라", "월세", "500/50", "2000년")
# house.append(house1)
# house.append(house2)
# house.append(house3)

# print("총 {0}대의 매물이 있습니다.".format(len(house)))
# for i in house:
#     i.show_detail()

# '''

#try 내부 명령을 실행하다가 오류 발생 -> except로 이동. except에 해당하는 오류가 있으면 해당 명령을 실행 
#예외처리 - 에러가 발생했을 때 처리해주는 기능

try:    
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫번째 숫자를 입력하세요: ")))
    nums.append(int(input("두번째 숫자를 입력하세요: ")))
    #nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:                  #잘못된 자료형의 값을 입력했을 때 (삼)
    print("에러! 잘못된 값을 입력하셨습니다.")
except ZeroDivisionError as err:     #0으로 나눴을 때 에러
    print(err)                       #division by zero
except Exception as err:
    print(err)
    print("알 수 없는 에러가 발생했습니다.")

'''
except:
    print("알 수 없는 에러가 발생했습니다.")
위에 오류에 해당되지 않는 에러는 전부 위의 명령으로 처리 
'''