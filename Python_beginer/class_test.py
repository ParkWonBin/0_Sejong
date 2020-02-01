class Bicycle():
    def move(self,speed):
        print(f"자전거 시속 {speed}킬로미터로 전진")

    def rotation(self, speed):
        print(f"자전거  {speed}으로 회전")

    def stop(self):
        print(f"자전거 정지")

    pass

mybicycle = Bicycle()
mybicycle.wheel_size = 20
mybicycle.color = 'red'

print(f" 자전거의 바퀴 크기는 {mybicycle.wheel_size}이고, 색깔은 {mybicycle.color}이다.")

