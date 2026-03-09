from microbit import *

# 시리얼 통신 초기화
uart.init(baudrate=115200)
display.show(Image.HAPPY)

while True:
    if uart.any():
        msg = uart.read()
        if msg:
            try:
                data = str(msg, 'utf-8').strip()
                
                # [1일 때: 전진]
                if data == '1':
                    display.show(Image.ARROW_N) # 북쪽 화살표 표시
                    # 이족보행 키트의 서보모터를 움직여 걷기 동작 수행
                    # 예시: pin0과 pin1에 연결된 서보모터를 특정 각도로 반복 이동
                    pin0.write_analog(150) 
                    pin1.write_analog(150)
                    sleep(500)
                    pin0.write_analog(50)
                    pin1.write_analog(50)
                    sleep(500)
                
                # [0일 때: 정지]
                elif data == '0':
                    display.show(Image.ASLEEP) # 자는 표정 표시
                    # 서보모터에 신호를 주지 않거나 중립 위치(90도 등)로 설정
                    pin0.write_analog(0)
                    pin1.write_analog(0)
                    
            except:
                pass
